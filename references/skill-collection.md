# 收集与整合现成 skill

需要某类能力时, 先找现成 skill, 评估后决定复用, 抽取, 还是自建. 不要一上来就写新 skill.

## 一, 搜索渠道

### 1. 本地

- 当前会话注入的 available_skills 列表
- `~/pjs/skills/`: user 自己的技能目录
- `~/.dsh/skills/`: dsh 安装的技能
- 先查本地, 命中率高, 且已知质量

### 2. GitHub

- 搜索仓库: `gh api /search/repositories?q=<关键词>+skill&sort=stars`, 或用 web_search 加 `site:github.com`
- 搜索代码: `gh api /search/code?q=filename:SKILL.md+<关键词>` (需要登录态)
- 话题: `topic:agent-skills`, `topic:claude-skills`
- 官方与清单仓库:
  - anthropics/skills: 官方示例
  - VoltAgent/awesome-agent-skills: 社区清单
  - ComposioHQ/awesome-claude-skills: 清单与资源
  - travisvn/awesome-claude-skills
  - sickn33/agentic-awesome-skills: 带本地目录发现工具
  - BehiSecc/awesome-claude-skills
- 关键词组合: `claude code skill <领域>`, `codex skill <领域>`, `agent skill <领域>`, `SKILL.md <领域>`

### 3. skill 市场与插件生态

- agentskills.io: skill 市场, 重定向到首页, 按领域浏览
- skills.sh: skill 索引
- awesome-dsh-plugin.com/plugins.json: dsh 插件市场清单, 与 skill 同生态, 可参考命名与分发方式
- 市场条目质量参差, 仍需按第三节评估

### 4. 论文与博客

- 搜索 "agent skills" 相关文章, 了解设计模式
- 大厂工程博客常有 skill 设计经验

## 二, 关键词与查询式

- 领域词加 skill: `pdf skill`, `video transcript skill`, `reverse engineering skill`
- 结构词: `SKILL.md references scripts agent skill`
- 中文: `技能 插件 信息收集`, `调研 skill`
- 时间限定: 近一年, skill 生态变化快

## 三, 评估清单

### 结构

- 有 SKILL.md, frontmatter 含 name 与 description
- description 写清触发条件, 能被自动路由
- references 与 scripts 职责清楚, 不是大杂烩
- 有安装步骤与依赖说明

### 维护

- 最后提交时间, 半年内活跃优先
- issue 与 PR 的响应情况
- star 数只作参考, 不作为质量结论
- 许可证: MIT / Apache 等宽松许可能借鉴, GPL 类注意传染性

### 安全

- scripts 会做什么: 网络请求, 文件写删, 安装软件, 修改配置
- 是否需要密钥, 登录, 提权
- 是否要求 agent 执行任意命令, 有提示注入风险
- 是否访问不该访问的路径

### 适配

- 依赖的 CLI 与工具本机是否可用, 不可用时是否有等价路径
- 与现有 skill 是否功能重叠
- 平台差异, macOS 与 Linux 行为不同处

## 四, 整合方式

三种, 按匹配度选:

1. 直接引用: 原 skill 独立存放, 不复制. 适合功能完整, 维护活跃, 无冲突的
2. 抽取方法论: 把流程, 清单, 模板吸收进自己的 references, 保留来源与许可说明. 适合部分可借鉴的
3. 自建: 无现成或都不合适, 按七阶段写新 skill, 吸收多个来源

整合步骤:

1. 记录来源: 仓库, commit 或版本, 许可
2. 抽取流程与清单, 不整段复制原文
3. 写清与现有 skill 的边界, 避免重复
4. 用一个真实小任务跑通, 验证可用
5. 在 README 或 SKILL.md 注明来源

## 五, 选型记录模板

放在 `.research/<slug>/` 或 skill 仓库根:

| 候选 | 来源 | 最后提交 | 许可 | 可整合部分 | 结论 |
|---|---|---|---|---|---|
| Weizhena/Deep-Research-skills | GitHub | 2026 | 查 | 检索模块化 | 抽取 |
| 199-biotech/claude-deep-research-skill | GitHub | 2026 | 查 | 8 阶段, 可信度评分 | 抽取 |

## 六, 本 skill 的来源 (实际案例)

本 skill 创建时的收集与整合记录:

| 来源 | 吸收的部分 | 处理 |
|---|---|---|
| Weizhena/Deep-Research-skills | 按信息源拆检索模块, 人机协同 | 转化为 source-matrix 分领域 |
| 199-biotechnologies/claude-deep-research-skill | 8 阶段流水线, 来源可信度评分, 证据持久化 | 七阶段加四档可信度与证据库 |
| hoolulu/deep-research | 多子 agent 并行写章节, 取最新数据, 质检 | 报告模板与质量门槛 |
| lingzhi227/agent-research-skills | 学术文献综述流程 | 学术来源与检索式 |
| rohunvora/x-research-skill | 平台专项调研 | 社交平台只作线索的规则 |
| jivoi/awesome-osint | 来源目录的领域划分 | 作为分类参考, 不照搬安全条目 |
| edoardottt/awesome-hacker-search-engines | 搜索引擎清单 | 通用搜索补充 |
| lorien/awesome-web-scraping | 抓取工具与库 | channels 的在线服务与库 |
| h4ckf0r0day/awesome-ai-web-scraping | 抓取 API, MCP, 搜索 API 清单 | channels 的工具清单 |

## 七, 本 skill 未覆盖, 需要时转交

- 安全侦察与 OSINT: reverse-skill
- 插件开发: dsh-plugin-create
- 文档格式处理: office 系 skill
- 视觉与 OCR: lookit, paddleocr-ocr
