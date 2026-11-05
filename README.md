# info-gathering-skill

通用网络调研与信息收集 skill. 给定一个主题, 按七阶段流程检索, 存档证据, 产出带引用的报告.

## 内容

- `SKILL.md`: 入口, 七阶段流水线, 质量门槛
- `references/channels.md`: 获取通道与工具 (内置工具, 命令行, 专用 CLI, 在线服务, API 实测, 降级路径)
- `references/source-matrix.md`: 信息源总目录, 19 个领域
- `references/skill-collection.md`: 收集与评估现成 skill 的渠道与整合方式
- `references/evidence-spec.md`: 证据库目录与元数据格式
- `references/report-template.md`: 报告骨架与引用规范
- `scripts/evidence_index.py`: 扫描证据库生成索引, 校验缺字段
- `justfile`: 常用操作

## 使用

```shell
just index .research/<slug>
just self-test
```

## 依赖

- 会话内置: web_search, web_fetch, browser (需授权)
- 命令行: curl, python3, jq
- 信息源 CLI (按需): bili, cnki, yt-dlp, qwen3-asr, tucao

## 产物

调研产物写进当前项目的 `.research/<slug>/`, 包含 brief, plan, sources, index, report 五类文件.
