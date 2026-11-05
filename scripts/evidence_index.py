#!/usr/bin/env python3
"""扫描证据库 sources, 生成 index.md.

用法:
    python3 evidence_index.py <调研目录>
    python3 evidence_index.py --self-test
"""

from __future__ import annotations

import argparse
import sys
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

REQUIRED_FIELDS = ("id", "url", "title", "fetched_at", "source_type", "credibility")
KNOWN_TYPES = ("官方文档", "标准", "学术", "代码仓库", "社区", "新闻", "视频", "数据", "其他")
KNOWN_CREDIBILITY = ("一手", "权威", "普通", "待验证")


def parse_frontmatter(text: str) -> Dict[str, str]:
    """解析开头的 YAML frontmatter, 只支持 key: value 的简单形式."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end]
    data: Dict[str, str] = {}
    for line in block.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, _, value = line.partition(":")
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def id_sort_key(entry: Dict[str, str]) -> Tuple[int, str]:
    """按 S 编号自然排序, 缺 id 的排在最后."""
    raw = entry.get("id", "")
    digits = "".join(ch for ch in raw if ch.isdigit())
    if digits:
        return (int(digits), raw)
    return (10**6, raw)


def load_sources(sources_dir: Path) -> List[Tuple[Path, Dict[str, str]]]:
    entries: List[Tuple[Path, Dict[str, str]]] = []
    for path in sorted(sources_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        entries.append((path, parse_frontmatter(text)))
    entries.sort(key=lambda item: id_sort_key(item[1]))
    return entries


def cell(value: str, limit: int = 60) -> str:
    """表格单元格转义, 过长截断."""
    value = value.replace("|", "\\|").replace("\n", " ").strip()
    if len(value) > limit:
        value = value[: limit - 1] + "…"
    return value or "-"


def build_index(entries: List[Tuple[Path, Dict[str, str]]], errors: List[str]) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "# 证据索引",
        "",
        f"生成时间: {now}",
        f"来源总数: {len(entries)}",
        "",
        "| ID | 标题 | 类型 | 可信度 | 发布时间 | 抓取时间 | 链接 |",
        "|---|---|---|---|---|---|---|",
    ]
    for path, fm in entries:
        sid = fm.get("id", "-")
        title = cell(fm.get("title", "-"), 50)
        url = fm.get("url", "")
        link = f"[{title}]({url})" if url else title
        lines.append(
            "| {id} | {link} | {stype} | {cred} | {published} | {fetched} | {url} |".format(
                id=cell(sid, 12),
                link=link,
                stype=cell(fm.get("source_type", "-"), 12),
                cred=cell(fm.get("credibility", "-"), 12),
                published=cell(fm.get("published_at", "-"), 12),
                fetched=cell(fm.get("fetched_at", "-"), 12),
                url=cell(url, 80),
            )
        )

    by_cred: Dict[str, int] = {}
    by_type: Dict[str, int] = {}
    for _, fm in entries:
        by_cred[fm.get("credibility", "未知")] = by_cred.get(fm.get("credibility", "未知"), 0) + 1
        by_type[fm.get("source_type", "未知")] = by_type.get(fm.get("source_type", "未知"), 0) + 1

    lines += ["", "## 统计", ""]
    for name in KNOWN_CREDIBILITY + ("未知",):
        if name in by_cred:
            lines.append(f"- 可信度 {name}: {by_cred[name]}")
    for name in KNOWN_TYPES + ("未知",):
        if name in by_type:
            lines.append(f"- 类型 {name}: {by_type[name]}")

    lines += ["", "## 数据检查", ""]
    if errors:
        lines += [f"- {msg}" for msg in errors]
    else:
        lines.append("- 未发现缺失字段")
    return "\n".join(lines) + "\n"


def run(root: Path) -> int:
    """扫描 root/sources, 生成 root/index.md, 返回错误数."""
    sources_dir = root / "sources"
    if not sources_dir.is_dir():
        print(f"错误: 找不到 {sources_dir}", file=sys.stderr)
        return 1

    entries = load_sources(sources_dir)
    if not entries:
        print(f"警告: {sources_dir} 下没有 .md 文件", file=sys.stderr)

    errors: List[str] = []
    seen_ids: Dict[str, str] = {}
    for path, fm in entries:
        missing = [name for name in REQUIRED_FIELDS if not fm.get(name)]
        if missing:
            errors.append(f"{path.name} 缺少字段: {', '.join(missing)}")
        sid = fm.get("id")
        if sid:
            if sid in seen_ids:
                errors.append(f"{path.name} 的 id {sid} 与 {seen_ids[sid]} 重复")
            else:
                seen_ids[sid] = path.name
        if fm.get("source_type") and fm["source_type"] not in KNOWN_TYPES:
            print(f"提示: {path.name} 的 source_type 不在推荐取值内: {fm['source_type']}", file=sys.stderr)
        if fm.get("credibility") and fm["credibility"] not in KNOWN_CREDIBILITY:
            print(f"提示: {path.name} 的 credibility 不在推荐取值内: {fm['credibility']}", file=sys.stderr)
        if not fm.get("published_at"):
            errors.append(f"{path.name} 缺少字段: published_at (未知请写 unknown)")

    index_text = build_index(entries, errors)
    (root / "index.md").write_text(index_text, encoding="utf-8")
    print(f"已生成 {root / 'index.md'}, 来源 {len(entries)} 条, 问题 {len(errors)} 个")
    for msg in errors:
        print(f"  - {msg}")
    return len(errors)


def self_test() -> int:
    """造样例跑一遍, 校验生成逻辑与错误检测."""
    with tempfile.TemporaryDirectory() as td:
        root = Path(td) / "demo"
        sources = root / "sources"
        sources.mkdir(parents=True)
        (sources / "s01-ok.md").write_text(
            "---\n"
            "id: S1\n"
            "url: https://example.com/a\n"
            "title: 样例来源 A\n"
            "publisher: 示例站\n"
            "published_at: 2024-05-01\n"
            "fetched_at: 2026-11-06\n"
            "source_type: 官方文档\n"
            "credibility: 一手\n"
            "used_for: Q1\n"
            "---\n\n## 摘录\n\n> 原文内容\n",
            encoding="utf-8",
        )
        (sources / "s02-bad.md").write_text(
            "---\n"
            "id: S2\n"
            "title: 缺失字段的样例\n"
            "---\n\n## 摘录\n\n> 原文内容\n",
            encoding="utf-8",
        )
        errors = run(root)
        index = (root / "index.md").read_text(encoding="utf-8")
        assert errors > 0, "应检测到缺失字段"
        assert "| S1 |" in index, "索引应包含 S1"
        assert "缺少字段" in index, "索引应列出缺失字段"
    print("self-test OK")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="扫描证据库 sources 生成 index.md")
    parser.add_argument("dir", nargs="?", help="调研目录, 例如 .research/<slug>")
    parser.add_argument("--self-test", action="store_true", help="用临时样例自检")
    args = parser.parse_args()

    if args.self_test:
        return self_test()
    if not args.dir:
        parser.error("需要调研目录, 或使用 --self-test")
    return min(run(Path(args.dir)), 1)


if __name__ == "__main__":
    sys.exit(main())
