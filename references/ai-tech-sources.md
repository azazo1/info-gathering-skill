# AI / 科技信源池

本文件给出 AI 与科技方向可以直接订阅, 直接检索的信源清单. 数据来自对橘鸦 AI 早报 90 期 (2026-08-08 至 2026-11-05, 共 1661 条新闻) 的引用统计, 加上本地推理等垂直领域的补充. 统计方法见第九节, 信源会变, 每季度重跑一次统计.

## 一, 使用方式

信源分四层, 调研时按层取用:

| 层 | 作用 | 典型信源 | 是否可作最终引用 |
|---|---|---|---|
| L0 聚合 | 发现事件, 拿到原始链接 | 橘鸦 AI 早报 RSS, TLDR AI, HN 首页 | 否, 必须顺链接回到 L1 |
| L1 一手 | 事实出处 | 官方博客, 官方 X, 模型卡, release, 论文, 官方公众号 | 是 |
| L2 权威二手 | 报道, 内幕, 解读 | Reuters, Bloomberg, The Information, WSJ, TechCrunch | 是, 标注为报道 |
| L3 社区 | 实测, 踩坑, 反例 | HN 评论, r/LocalLLaMA, linux.do, V2EX, 个人博客 | 只作佐证, 不单独支撑结论 |

规则:

1. 时效性问题 (最新模型, 最新版本, 最近发生的事) 先查 L0, 拿事件清单与原始链接
2. 每个事件回到 L1 核实, 记录发布日期
3. 垂直领域 (本地推理, 某个框架, 某个硬件) 不能只看 L0, 综合日报会漏, 必须再查第六节的垂直信源
4. 社区实测 (L3) 用来校正厂商数字, 厂商自测与社区实测冲突时两者都写

实例: 橘鸦早报收录了 Inco AI 的 DFlash 2 (2026-08-19), 却没有收录同一家公司 2026-09-17 发布的 Mac 推理引擎 Splash. Splash 只在 HN 和 LM Studio changelog 出现. 只看聚合就会漏掉当前 Mac 上最快的引擎.

## 二, L0 聚合源

| 信源 | 获取方式 | 说明 |
|---|---|---|
| 橘鸦 AI 早报 | RSS `https://daily.juya.uk/rss.xml`, 单期 `https://daily.juya.uk/issues/YYYY-MM-DD/` | 中文, 每日, 每条带原始链接, 栏目固定, 适合按日期回溯 |
| 橘鸦 AI 早报视频版 | `bili search '橘鸦Juya' --type user` 拿 UID 285286947, 视频简介与字幕 | 与文字版同源 |
| 黑鸦Heya | bilibili UID 3706929260006322 | 中文 AI 快讯, 偏传闻, 只作线索 |
| Hacker News | `https://hn.algolia.com/api/v1/search?query=...&tags=story` | 英文技术社区, 带分数与评论数, 垂直项目常先出现在这里 |
| TLDR AI, The Rundown AI | 邮件或网页 | 英文每日简报 |
| 机器之心, 量子位, 新智元 | 微信公众号, 网页 | 中文媒体, 速度快, 需回到一手 |
| testingcatalog, btibor91 (X) | X | 产品灰度与泄露线索, 只作前瞻 |

橘鸦早报栏目 (90 期统计): 开发生态 317, 行业动态 278, 产品应用 267, 模型发布 244, 要闻 235, 技术与洞察 177, 前瞻与传闻 110. "前瞻与传闻" 栏目的条目不能当事实引用.

单期抓取:

```shell
curl -sS https://daily.juya.uk/rss.xml -o juya.xml
curl -sS -A 'Mozilla/5.0' https://daily.juya.uk/issues/2026-11-05/ -o 2026-11-05.html
```

单期 HTML 结构: `<h2>` 是栏目, `<section class="news-item"><h3><a href="主信源">` 是一条新闻, 正文里 "相关链接" 列表是补充信源.

## 三, L1 一手信源: 按域名

90 期主信源共 393 个域名. 下表是出现次数最多的一手来源, 次数是作为主信源的条目数.

### 海外实验室与公司

| 次数 | 域名 | 用途 |
|---|---|---|
| 90 | openai.com | `/index/` 公告与研究 |
| 23 | help.openai.com | 产品更新说明 (release notes) |
| 14 | developers.openai.com | API 与定价 |
| 5 | alignment.openai.com | 对齐研究 |
| 59 | anthropic.com | `/news`, `/research`, `/engineering` |
| 39 | claude.com | 产品博客 |
| 7 | claude.dev | Claude Code |
| 5 | support.claude.com | 更新说明 |
| 4 | platform.claude.com | API |
| 56 | blog.google | Google 产品与模型 |
| 7 | deepmind.google | DeepMind 研究 |
| 5 | developers.googleblog.com | 开发者 |
| 5 | antigravity.google | Antigravity |
| 13 | x.ai, docs.x.ai | xAI |
| 10 | mistral.ai | `/news` |
| 9 | microsoft.ai, blogs.microsoft.com | 微软 AI |
| 9 | blogs.nvidia.com, nvidianews.nvidia.com, developer.nvidia.com | NVIDIA |
| 6 | research.meta.ai, ai.meta.com | Meta |
| 7 | elevenlabs.io | 语音 |
| 6 | cursor.com | Cursor |
| 6 | blog.cloudflare.com | Cloudflare |
| 5 | cognition.com | Devin / SWE 模型 |
| 4 | bfl.ai | FLUX 图像 |
| 4 | liquid.ai | LFM 小模型 |
| 4 | vercel.com | v0 / AI SDK |
| 3 | perplexity.ai, cohere.com, inceptionlabs.ai, manus.im | 其他 |

### 国内实验室与公司

| 次数 | 域名 | 用途 |
|---|---|---|
| 127 | mp.weixin.qq.com | 官方公众号, 国内厂商的主发布渠道 |
| 6 | kimi.com | 月之暗面 |
| 4 | api-docs.deepseek.com | DeepSeek API 更新日志 |
| 4 | docs.bigmodel.cn, z.ai | 智谱 |
| 4 | hy.tencent.com | 腾讯混元 |
| 3 | doubao.com | 字节豆包 |
| 3 | docs.qoder.cn | 阿里 Qoder |
| - | qwen.ai/blog, qwenlm.github.io | 千问博客 |
| - | aliyun.com/notice | 阿里云百炼公告与价格 |
| - | mimo.xiaomi.com | 小米 MiMo |

国内厂商的模型发布多数只在公众号首发, 不要只查官网.

### 模型与代码托管

| 次数 | 域名 | 用途 |
|---|---|---|
| 45 | github.com | release, README, 技术报告 |
| 5 | github.blog | GitHub 官方 |
| 40 | huggingface.co | 模型卡, 博客 `/blog`, 数据集 |
| 5 | arxiv.org | 论文 |
| 12 | openrouter.ai | 新模型上线, 隐身模型, 用量榜 |
| 12 | artificialanalysis.ai | 第三方速度与质量基准 |
| 3 | epoch.ai | 算力与基准研究 |
| - | arena.ai (lmarena) | 盲测榜, 橘鸦本人认为该榜单不可靠, 只作参考 |

## 四, L1 一手信源: X 账号

X 是第一大主信源 (410 条主信源, 237 个账号). 下表按用途分组, 括号内是 90 期内被引用的次数.

官方账号:

- OpenAI 系: openai (41), openaidevs (39), chatgpt (30), openainewsroom (5)
- Anthropic 系: claudedevs (42), claudeai (22), anthropicai (21)
- Google 系: google (11), googledeepmind (4), geminiapp (4), gemini_notebook (6), googleaistudio (3), googlegemma (2), googlelabs (2), antigravity (5)
- xAI: grok (4), spacexai (4)
- 工具与平台: opencode (30), cursor_ai (7), openrouter (8), arena (9), ollama (4), vercel_dev (3), cline (2), qoder_ai_ide (3), commandcodeai (6)
- 模型公司: mistralai (3), minimax_ai (4), kimi_moonshot (3), alibaba_qwen (2), zai_org (2), cohere (3), nousresearch (6), thinkymachines (2), perplexitydevs (3), elevenlabs (5), fal (3), antlingagi (13), openbmb (2)
- 基准: artificialanlys (12)

负责人与员工:

- thsottiaux (87, OpenAI Codex 负责人, 产品更新最快的一手来源)
- sama (11), gdb (4), darioamodei (4), sundarpichai (2), satyanadella (5), jensenhuang (3), elonmusk (26), aravsrinivas (3)
- bcherny (5, Claude Code), trq212 (10), lydiahallie (5), thdxr (5, opencode), tianyi (9), _catwu, therealadamg, ajambrosino
- reach_vb (4, Hugging Face), clementdelangue (2), charliermarsh (3, uv / ruff)

线索与爆料 (只作前瞻):

- testingcatalog (10), btibor91 (3), andrewcurran_ (4), synthwavedd (3), grokinsider (2), mark_k (2)

X 获取方式: 需要 browser 并登录; 单条推文可试 `https://x.com/<user>/status/<id>` 或 Nitter 镜像. 推文是一手但容易删改, 存档时截取原文并记录抓取时间.

## 五, L1 一手信源: 组织

Hugging Face 组织 (90 期内出现次数): inclusionai (12), tencent (8), nvidia (7), perplexity-ai (7), qwen (5), liquidai (5), openbmb (5), deepseek-ai (4), ibm-granite (4), jetbrains (4), sensenova (3), cloudflare (3), meta-models (2), coherelabs (2), minimaxai (2), incoai (2), zai-org (2), google (2), mistralai (2), unsloth (1), jinaai (1), internlm (1), wan-ai (1)

GitHub 组织: anthropics (12), deepseek-ai (10), tencent-hunyuan (8), qwenlm (6), minimax-ai (6), inclusionai (5), openai (5), opensensenova (3), nousresearch (2), stepfun-ai (2), ggml-org (2), baidu (2), google-antigravity (2), unslothai (1), firecrawl (1)

查询方式:

```shell
curl -sS "https://huggingface.co/api/models?author=Qwen&sort=lastModified&direction=-1&limit=10"
gh api /orgs/deepseek-ai/repos --jq '.[].full_name'
gh api /repos/ggml-org/llama.cpp/releases/latest --jq '.tag_name,.published_at'
```

## 六, 垂直领域信源

综合日报覆盖不到的领域, 单独列出. 新增垂直领域时按同样格式补充.

### 本地推理与 Apple Silicon

| 信源 | 获取方式 | 说明 |
|---|---|---|
| HN 搜索 | `hn.algolia.com/api/v1/search?query=<模型> Mac&tags=story` | 实测帖与新引擎常在这里首发, 带评论数 |
| r/LocalLLaMA | browser (curl 403) | 本地模型最大社区, 量化与速度实测 |
| LM Studio changelog | `lmstudio.ai/changelog` | 新引擎接入 (oMLX, Splash) 与 M 系列适配 |
| Ollama 博客与库 | `ollama.com/blog`, `ollama.com/library/<model>` | MLX 引擎进展, 最低版本要求 |
| llama.cpp releases | `gh api /repos/ggml-org/llama.cpp/releases` | 新架构支持, Metal 优化 |
| MLX / mlx-lm releases | `gh api /repos/ml-explore/mlx-lm/releases` | Apple 官方栈 |
| mlx-community (HF) | `huggingface.co/api/models?author=mlx-community&sort=lastModified` | 新模型的 MLX 量化 |
| Unsloth 文档 | `unsloth.ai/docs/models/<model>` | 每个模型的内存表, 推荐参数, 量化选择 |
| Inco AI 博客 | `inco.ai/blog/`, `inco.ai/sitemap.xml` | Splash, DFlash 草稿模型 |
| 个人实测博客 | HN 搜索结果中的博客 | 例: terminalbytes.com 的 Mac Studio 实测 |

### 中文开发者社区

| 信源 | 获取方式 | 说明 |
|---|---|---|
| linux.do | browser | 橘鸦早报 10 次主信源, 国内 AI 开发者讨论, 中转与额度信息多 |
| V2EX | web_fetch | 技术讨论 |
| ithome.com | web_fetch | IT 之家, 中文快讯 (7 次) |
| zhidx.com | web_fetch | 智东西 (4 次) |
| 知乎专栏 | browser | 部分 UP 主同步文字稿 |

### 权威媒体 (L2)

reuters.com (22), bloomberg.com (16), theinformation.com (9), wsj.com (9), techcrunch.com (9), the-decoder.com (7), axios.com (5), ft.com (3), wired.com, newsletter.semianalysis.com. 付费墙文章用标题加首段, 不绕过付费墙.

### 政策与监管

whitehouse.gov (3), aisi.gov.uk (3), ec.europa.eu, sec.gov (公司披露), 中国信通院公众号.

## 七, 可信度规则

- 官方博客, 模型卡, release: 一手
- 官方 X 与员工 X: 一手, 但注意删改, 必须存原文
- 官方公众号: 一手
- 第三方基准 (Artificial Analysis, Epoch): 权威, 注明测试条件
- 厂商自测基准 (例: Splash 对比 Ollama): 一手但有利益相关, 需要社区实测佐证
- 社区实测: 普通, 注明机器型号, 量化档, 引擎版本
- 聚合日报: 不作引用, 只作索引
- 爆料账号与 "前瞻与传闻": 待验证

## 八, 推荐的每日或每周订阅组合

只想覆盖 AI 主线, 订阅这几个就够, 再多会重复 (橘鸦本人的建议是不要关注太多信源, 同一事件会在多个渠道反复出现):

1. 橘鸦 AI 早报 RSS
2. HN 首页或 HN 搜索关键词订阅
3. 关注领域的 2 到 3 个官方账号与 release 页面
4. 一个垂直社区 (本地推理选 r/LocalLLaMA)

## 九, 统计方法 (可复跑)

```shell
python3 - <<'EOF'
import datetime, subprocess, time
d = datetime.date.today()
for i in range(90):
    day = d - datetime.timedelta(days=i)
    subprocess.run(['curl', '-sS', '-m', '20', '-A', 'Mozilla/5.0', '-o', f'{day}.html',
                    f'https://daily.juya.uk/issues/{day}/'])
    time.sleep(1)
EOF
```

抓取后解析 `<section class="news-item">`: 第一个 `<a href>` 为主信源, 其余为相关链接, 按域名, X 账号, HF 组织, GitHub 组织计数. 同一域名请求间隔 1 秒.
