# 证据库规范

所有调研产物放在当前项目 `.research/<slug>/`, `<slug>` 用主题的英文短名, kebab-case.

```
.research/<slug>/
- brief.md      # 需求澄清, 子问题树
- plan.md       # 检索计划与执行记录
- sources/      # 每个来源一份, 编号连续
- index.md      # 由 scripts/evidence_index.py 生成, 不要手写
- report.md     # 最终报告
```

## brief.md

记录四类信息:

- 主题与目的: 结论要回答哪个问题
- 范围: 时间窗, 地域, 语言, 版本
- 交付要求: 长度, 是否要对比表, 是否要行动建议
- 禁忌: 不采信哪些来源

## plan.md

用表格记录检索计划与执行结果:

| 子问题 | 信息源 | 查询式 | 状态 |
|---|---|---|---|
| Q1 | 官方文档 | site:docs.x.com async | 已取 3 条 |
| Q2 | 学术 | arXiv query=... | 抓取失败, 见备注 |

抓取失败的行保留, 备注写状态码与原因.

## sources/<id>.md

文件命名 `s01-<short>.md`, 编号与 ID 对应, 也被报告引用为 `[S1]`.

每个文件由 frontmatter 加正文组成. frontmatter 必填字段:

```yaml
---
id: S1
url: https://example.com/post
title: 页面标题
publisher: 站点或作者
published_at: 2024-05-01
fetched_at: 2026-11-06
source_type: 官方文档
credibility: 一手
used_for: Q1, Q3
---
```

字段取值:

- `id`: `S` 加两位编号, 与文件名一致
- `published_at`: 未知写 `unknown`, 不要猜
- `fetched_at`: 抓取日期, 必填
- `source_type`: 官方文档 / 标准 / 学术 / 代码仓库 / 社区 / 新闻 / 视频 / 数据 / 其他
- `credibility`: 一手 / 权威 / 普通 / 待验证
- `used_for`: 关联的子问题编号, 逗号分隔

正文只写两节:

```markdown
## 摘录

> 原文关键段落, 保留原貌, 只做必要的截断并标 [...]

## 备注

- 需要说明的上下文, 例如页面已改版, 内容与另一来源冲突
```

不要转述后冒充原文. 需要写解读时放 `## 备注`, 明确标为解读.

## index.md

由脚本生成, 内容是来源表格加统计:

- 每个来源一行: id, 标题, 类型, 可信度, 发布时间, 抓取时间, URL
- 统计: 总数, 各可信度计数, 缺失字段清单

脚本发现缺失字段时, 在 index.md 末尾列出, 并返回非零退出码.

## 引用规则

- 报告里每条事实后挂 `[S1]`, 多个来源写 `[S1][S3]`
- 只引用 sources 中存在的 id
- 同一来源支撑多个断言时重复标注
- 推断与观点不挂引用, 单独标注为推断

## 证据保留时限

调研任务结束后保留整个 `.research/<slug>/`, 便于复查. 用户要求清理时才删除.
