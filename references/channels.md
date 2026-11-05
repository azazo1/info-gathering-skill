# 获取通道与工具

通道清单按 "直接可用程度" 排列, 先用靠前的, 不够再往下换. 缺工具时先找等价路径, 不要由 agent 自行安装软件, 需要新工具时交给 user 决定.

## 1. 内置工具

- web_search: 关键词检索, 返回摘要与入口列表. 用于冷启动和找入口, 结果需再用 web_fetch 核实
- web_fetch: 抓取单页并解码为文本. 适合静态页面与文档页, 一次一页
- browser use: 真实浏览器, 可执行 JS, 登录, 点击, 滚动. 适合动态渲染站, 反爬站, 需登录的页面. 需 user 授权 (kw: br) 后使用. macOS 上不要在沙箱内直接开 Chrome, 会崩溃且看不到报错

## 2. 命令行直连

- curl: 拉 API, RSS, JSON, 静态 HTML. 习惯参数 `-sS -m 20`, 需要代理时加 `-x http://localhost:7890`
- python3: curl 报 TLS 错误时改用 python, 复杂 JSON / XML / PDF 解析, 并发下载. 优先只用标准库, 避免临时装包
- jq: 解析 JSON 输出, 例如 `curl -s URL | jq -r '.items[].title'`
- gh: GitHub API, 例如 `gh api /search/repositories?q=...`, 代码检索 `gh api /search/code?q=...`
- git: `git clone --depth 1` 深读仓库源码与文档
- sqlite3: 本地数据整理

## 3. 专用 CLI (信息源直连)

### bili (bilibili)

```
bili search '关键词' --type video --json --max 10    # 综合/视频/专栏/用户/番剧/直播
bili search 'UP名' --type user --max 10              # 找 UP 主 UID, 再进空间或合集找视频
bili video BV... --json                              # 详情, 加 -c 看评论, --ai 看 AI 总结
bili video subtitle BV...                            # 列出并导出字幕
bili video danmaku BV...                             # 导出弹幕
bili video download BV...                            # 下载视频或音频
bili user <uid>                                      # UP 主资料
```

### cnki (知网)

首次使用需 `cnki auth login`, 打开受控浏览器完成验证, 之后复用会话.

```
cnki search '深度学习' --sort cited --limit 20 --json
cnki adv  / cnki expr  / cnki sentence               # 高级, 专业, 句子检索
cnki author <作者>                                    # 作者发文检索
cnki group <查询> --group subject,source             # 分组聚合
cnki refine                                          # 上一轮结果内收窄
cnki detail <id>                                     # 文献详情
cnki download <id>                                   # 下载全文 PDF 或 CAJ
cnki export <查询> --format markdown                 # 题录导出
```

运算符: `*` 与, `+` 或, `-` 非, `""` 短语, `()` 分组, 含运算符的词用半角单引号包住.

### 其他 (按需, 未安装时由 user 决定)

- yt-dlp: `yt-dlp --write-auto-subs --skip-download <url>`, 或 `yt-dlp -x --audio-format mp3 <url>` 取音频
- ffmpeg: 音视频抽轨, 格式转换, 截取片段
- qwen3-asr: 音频转 txt / srt, 配合 bili 或 yt-dlp 下载的音频
- tucao: 吐槽弹幕网番剧信息与下载
- newsboat: 终端 RSS 阅读, 批量跟进订阅源
- RSSHub: 把没有 RSS 的站点转成 RSS, 公共实例可用, 也可本地部署

## 4. 在线转化与抓取服务

网页转 LLM 友好文本:

- r.jina.ai: `curl https://r.jina.ai/https://example.com`, 免 key, 免费额度, 对简单反爬有效
- Firecrawl: scrape / crawl / map / search 接口, 需 API key, 免费额度
- Apify: 现成 actor 市场, 需 API key
- ScrapingBee, ZenRows, Oxylabs, Bright Data: 付费抓取 API, 处理强反爬与代理池

自建或库:

- Crawl4AI, Scrapling, trafilatura, newspaper3k: Python 抓取与正文抽取库, 需安装
- SearXNG: 自建元搜索, 规避单引擎限流

搜索 API (需 key, 适合批量检索):

- Exa (神经搜索), Tavily (面向 LLM 的检索), Serper / SerpAPI (Google 结果), Brave Search API, Kagi Search API, Linkup, You.com

MCP 服务 (会话接入 MCP 时可用):

- firecrawl-mcp, fetch MCP, browserbase MCP, apify MCP, brightness data MCP

## 5. 视频与音频管线

- bilibili 有字幕: `bili video subtitle BV...`
- bilibili 无字幕: `bili video download BV...` 取音频, 再 qwen3-asr 转写
- YouTube: yt-dlp 取字幕或音频, 再转写
- 播客: RSS 拉音频地址, curl 下载, 转写
- 转写结果照样进 sources, 标注为转录稿并记录视频发布时间

## 6. 公开 API 一览 (实测 2026-11-06)

| 服务 | 接口 | 状态 |
|---|---|---|
| OpenAlex | `https://api.openalex.org/works?search=...` | 200 |
| Crossref | `https://api.crossref.org/works?query=...` | 200 |
| Semantic Scholar | `https://api.semanticscholar.org/graph/v1/paper/search?query=...` | 无 key 易 429 |
| arXiv | `https://export.arxiv.org/api/query?search_query=...` | 301 跟随 |
| Unpaywall | `https://api.unpaywall.org/v2/<doi>?email=<email>` | 需邮箱 |
| HN Algolia | `https://hn.algolia.com/api/v1/search?query=...` | 200 |
| Stack Exchange | `https://api.stackexchange.com/2.3/search/advanced?site=stackoverflow&q=...` | 200 |
| Wayback | `https://archive.org/wayback/available?url=...` | 200 |
| devdocs | `https://devdocs.io/docs.json` | 302 跟随 |
| GitHub | `gh api /search/repositories?q=...` | 200 |
| npm | `https://registry.npmjs.org/<pkg>/latest` | 200 |
| PyPI | `https://pypi.org/pypi/<pkg>/json` | 200 |
| Hugging Face | `https://huggingface.co/api/models?limit=5` | 200 |
| Wikipedia | `https://zh.wikipedia.org/w/api.php?action=query&list=search&srsearch=...` | 200 |
| r.jina.ai | `https://r.jina.ai/<url>` | 200 |
| Reddit | `https://www.reddit.com/search.json?q=...` | 403, 需 browser |

## 7. 降级与升级规则

抓取结果先判断状态, 再决定通道, 不要在一个通道上反复重试:

| 现象 | 判定 | 动作 |
|---|---|---|
| 200 且正文完整 | 正常 | 直接存档 |
| 200 但正文为空壳, 只有导航与脚本 | JS 渲染 | 立刻换 browser, 或先试 r.jina.ai |
| 403 / 429 / 验证码 / Cloudflare 挑战 | 反爬拦截 | 立刻换 browser, 不要连续 curl 重试 |
| 302 跳转到登录页 | 需登录 | browser 中登录后取页 |
| TLS 握手失败 | 证书或代理 | 换 python3, 或加代理 localhost:7890 |
| 结构化 API 429 | 限流 | 加延时退避, 换同类 API |
| 搜索结果被反爬或区域污染 | 搜索通道受限 | browser 搜索, 或换引擎 / SearXNG / 代理 |
| 404 | 路径失效 | 查 Wayback, 或换入口 |

关键原则:

- 反爬, 验证码, 登录墙是 browser 通道的明确触发条件, 不是最后一招. 同一站连续两次 curl 失败就升级到 browser
- 浏览器使用需要 user 授权 (kw: br / browser), 使用前先检查 browser 工具是否可用
- 视频无字幕: 音频加转写, 或退化为文字摘要加时间点
- 所有通道都不通: 记录在 plan.md, 在报告 "未覆盖" 里写清

## 8. 浏览器通道

user 说 br / browser, 表示允许并要求在抓取任务中使用浏览器. 这时浏览器是主通道, 不是兜底:

- 关键页面用 browser 打开确认, 不只依赖 curl 返回的文本
- 搜索结果页, 动态渲染页, 登录页, 需要点击展开的页面, 优先用 browser
- 结构化 API 与静态文档仍可直接用 curl 或 web_fetch
- 前置检查: 先确认浏览器扩展已连上. 未连上时把配置步骤告诉 user 并等待, 不要反复重试
- 使用后把关键内容与 URL 存进 sources, 不要只凭记忆写结论

## 9. 合规与礼貌

- 遵守 robots.txt 与站点条款
- 同一域名请求间隔至少 1 秒, 并发不超过 3
- 不绕过付费墙, 需要全文时走合法渠道
- 不采集未公开的个人信息, 不保存隐私数据
