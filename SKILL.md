---
name: info-gathering-skill
description: 通用网络调研与信息收集技能. 当用户要求调研, 收集, 对比, 汇总某个主题的资料, 需要多源检索, 证据留存和带引用的调研报告时使用. 触发词: 调研 / 信息收集 / 查资料 / 深挖 / 综述 / 对比分析 / research / deep research.
---

# 信息收集 (Info Gathering)

把一个模糊的调研需求, 变成有来源, 可复查, 带引用的结论. 本 skill 只管收集与整合, 不碰安全侦察, 也不做代码修改.

## 何时使用

- 用户要求围绕一个主题收集资料, 做综述, 对比, 趋势判断, 选型建议
- 用户要做调研报告, 且需要可追溯的来源
- 需要核实某个说法在多个来源中的一致性与冲突
- 需要找现成 skill, 或评估别人的 skill 是否可用

## 何时不用

- 目标侦察, 资产枚举, OSINT 情报: 转交 `reverse-skill`
- 单一事实的简单查询: 直接 1 到 2 次检索回答
- 纯代码调试: 走正常开发流程

## 产物

调研产物统一放在当前项目的 `.research/<slug>/` 下, `<slug>` 由主题生成, kebab-case. 结构见 `references/evidence-spec.md`:

```
.research/<slug>/
- brief.md      # 需求澄清与子问题树
- plan.md       # 检索计划
- sources/      # 每个来源一份, 元数据加原文摘录
- index.md      # 证据索引, 由 scripts/evidence_index.py 生成
- report.md     # 最终报告
```

## 七阶段流水线

### 1. 需求澄清

检索前把不确定项问清, 一次问完, 不要边搜边问:

- 主题与目的: 结论要回答哪个问题
- 适用范围: 时间窗, 地域, 语言, 版本
- 交付物: 报告长度, 是否需要对比表, 是否需要行动建议
- 禁忌: 不采信哪些来源, 是否排除营销内容

把答案写进 `brief.md`.

### 2. 问题拆解

把主题拆成子问题树, 每个子问题满足:

- 可以用一两个查询式检索到材料
- 有明确的判定标准, 是 / 否, 哪个更好, 何时发生

子问题超过 8 个时先合并, 避免检索发散.

### 3. 检索规划

先看 `references/channels.md` 选获取通道, 再按 `references/source-matrix.md` 给每个子问题分配来源和查询式, 写进 `plan.md`. 原则:

- 先一手与官方, 再权威二手, 最后社区讨论
- 每个子问题至少两个独立来源
- 查询式区分中英文, 关键词和站点限定两种写法
- 通道从直接可用的开始, 不通再降级

### 4. 多源检索与抓取

- 找入口用 web_search, 抓正文用 web_fetch, 动态页面用 browser
- 结构化数据优先走 API 或专用 CLI, 见 `references/channels.md`
- 每条材料记录 URL, 标题, 抓取时间, 发布者
- 抓取失败的来源记入 `plan.md`, 不要静默丢弃
- 遵守目标站点的 robots 与使用条款

### 5. 证据存档

每个来源存一份 `sources/<id>.md`, 元数据格式严格按 `references/evidence-spec.md`. 只摘录与子问题相关的原文, 保留关键段落原貌, 不要转述后冒充原文.

### 6. 核验与分级

- 交叉验证: 同一条事实至少两个独立来源
- 冲突处理: 显式记录分歧, 给出可能原因, 时间差, 口径差异, 利益相关
- 可信度四档: 一手 (官方文档 / 标准 / 原始数据), 权威 (同行评审 / 主流媒体 / 官方转述), 普通 (社区 / 博客), 待验证 (匿名 / 无出处)
- 过期材料标注发布时间, 并判断是否仍适用

### 7. 整合产出

- 用 `scripts/evidence_index.py` 生成 `index.md`
- 按 `references/report-template.md` 写 `report.md`
- 每条事实挂 `[S1]` 形式的来源编号, 编号对应 sources 文件
- 无证据的推断单独标注为推断, 并说明依据

## 质量门槛

交付前逐条自检:

- [ ] 每个结论都能追到至少一个 sources 文件
- [ ] 冲突和不确定性已显式写出, 没有只挑顺手的证据
- [ ] 时效性: 关键来源标了发布时间, 报告标了调研日期
- [ ] 无编造: 找不到就写未找到可靠来源, 不用常识补
- [ ] 报告与证据一致, 摘要里的数字和正文对得上

## 参考文件

- `references/channels.md`: 获取通道与工具, 内置工具, 命令行, 专用 CLI, 在线服务, API 实测, 降级路径
- `references/source-matrix.md`: 信息源总目录, 按领域列出可查站点与获取方式
- `references/skill-collection.md`: 收集与评估现成 skill 的渠道, 评估清单, 整合方式与选型记录
- `references/evidence-spec.md`: 证据目录与元数据格式
- `references/report-template.md`: 报告骨架与引用规范
- `scripts/evidence_index.py`: 扫描 sources 生成索引并检查缺字段
- `justfile`: `just index <dir>` 等常用操作
