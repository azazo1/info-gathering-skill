# 信息源总目录

按领域组织, 每个来源给获取方式. 通道细节见 `channels.md`.

通用约定:

- 能直连 API 的优先 API, 不能的用 web_fetch, 再不行用 browser
- 每个子问题至少两个独立来源
- 可信度四档: 一手 / 权威 / 普通 / 待验证, 判定标准见 `evidence-spec.md`

## 1. 通用搜索与元搜索

| 来源 | 获取方式 | 备注 |
|---|---|---|
| Google | web_search, browser | 索引最全, 反爬强, 适合 browser 或搜索 API |
| Bing | web_search, browser | 中文结果可用 |
| DuckDuckGo | web_search, browser | 隐私向, 结果偏少 |
| Brave Search | web_search, API | 独立索引, 有官方 API |
| SearXNG | 自建实例, browser | 聚合多个引擎, 规避单引擎限流 |
| Kagi | web_search, API | 付费, 结果质量高 |
| Yandex | web_fetch, browser | 俄语与图片检索强 |
| Baidu | web_search, web_fetch | 中文为主 |
| 360 搜索, 搜狗 | web_fetch | 中文补充 |
| Startpage, Mojeek, Stract, Swisscows | web_fetch, browser | 隐私向补充 |
| Naver | web_fetch, browser | 韩语内容 |
| Dogpile, MetaGer | web_fetch | 元搜索, 适合查漏 |

## 2. 学术文献

英文与开放获取:

| 来源 | 获取方式 | 备注 |
|---|---|---|
| arXiv | API, web_fetch | 预印本, 一手但未评审 |
| OpenAlex | API | 元数据, 引用数, 作者机构, 覆盖全 |
| Crossref | API | DOI 元数据, 出版信息 |
| Semantic Scholar | API | 摘要, 引用关系, 无 key 易 429 |
| PubMed | E-utilities API | 医学与生物 |
| bioRxiv, medRxiv | web_fetch, API | 生物医学预印本 |
| SSRN | web_fetch | 社科预印本 |
| CORE | API, web_fetch | 开放获取全文聚合 |
| DOAJ | web_fetch, API | 开放获取期刊目录 |
| Unpaywall | API | 按 DOI 找合法全文 |
| Zenodo, Figshare | API, web_fetch | 数据与预印本存档 |
| Google Scholar | browser | 引用追踪, 反爬强 |
| ResearchGate | browser | 论文与作者主页, 需登录 |
| Papers with Code | web_fetch | 论文加代码实现 |
| DBLP | web_fetch | 计算机会议与期刊文献库, 偶尔 500 可换镜像 |
| ACL Anthology | web_fetch | NLP 论文全文 |
| CVF Open Access | web_fetch | CVPR / ICCV / ECCV 全文 |
| IEEE Xplore, ACM DL, SpringerLink, ScienceDirect | 目录页 web_fetch, 全文需机构账号 | 权威但多付费 |
| 中国临床指南网, 国家卫健委 | web_fetch | 医学指南与规范 |

中文:

| 来源 | 获取方式 | 备注 |
|---|---|---|
| CNKI 知网 | cnki CLI | 期刊, 学位论文, 会议, 专利, 标准, 年鉴 |
| 万方 | browser, web_fetch | 知网补充 |
| 维普 | browser, web_fetch | 知网补充 |
| 百度学术 | web_fetch | 中文引用与外文索引 |
| 国家哲学社会科学文献中心 | web_fetch | 开放获取中文文献 |

## 3. 代码与仓库

| 来源 | 获取方式 | 备注 |
|---|---|---|
| GitHub | gh api, git clone | 仓库, issue, release, 代码检索需登录态 |
| GitLab | API, web_fetch | 自建实例多 |
| grep.app | web_fetch | 跨仓库代码检索 |
| Sourcegraph | browser | 大型代码检索 |
| Searchcode | web_fetch | 代码检索 |
| npm | registry API | 包信息, 版本, 依赖 |
| PyPI | JSON API | 包信息 |
| crates.io | API | Rust 包 |
| Maven Central | API | Java 包 |
| pkg.go.dev | web_fetch | Go 包 |
| Hugging Face | API | 模型, 数据集, 论文卡片 |
| DeepWiki | web_fetch, browser | 把 GitHub 仓库生成文档与问答, 易 429 |
| gitingest | web_fetch | 仓库一键转文本, 便于通读 |
| repomix, uithub | 本地 CLI 或 web_fetch | 打包仓库给 LLM 阅读 |

## 4. 问答与技术社区

| 来源 | 获取方式 | 备注 |
|---|---|---|
| Stack Overflow 及各 SE 站 | Stack Exchange API | 高票答案, 注意版本时效 |
| Hacker News | Algolia API | 技术趋势与讨论 |
| Reddit | JSON 接口 (403 时用 browser) | 子版块讨论 |
| V2EX | web_fetch, API | 中文技术社区 |
| Lobsters | web_fetch | 技术讨论 |
| Quora | browser | 问答, 质量参差 |
| 知乎 | browser, site: 检索 | 深度回答与经验帖 |
| 掘金 | site: 检索, web_fetch | 中文前端后端实践 |
| 思否 SegmentFault | site: 检索 | 中文问答 |
| CSDN | site: 检索 | 量大质杂, 核对代码 |
| 博客园 | site: 检索 | 老牌中文博客 |
| Medium, dev.to, Substack, Hashnode | web_fetch, RSS | 英文博客与专栏 |
| 个人技术博客 | web_search, RSS | 一手经验, 质量看作者 |

## 5. 视频与音频

| 来源 | 获取方式 | 备注 |
|---|---|---|
| bilibili | bili CLI | search / video / subtitle / danmaku / download |
| YouTube | yt-dlp 或 browser | 字幕优先, 无字幕取音频转写 |
| Vimeo | web_fetch, yt-dlp | 独立创作者视频 |
| 慕课平台 (中国大学 MOOC, Coursera等) | browser | 课程大纲与讲义 |
| 播客 | RSS 加转写 | 小宇宙 / Apple Podcasts 等, 用 RSS 地址 |
| 会议录像 (PyCon 等) | web_fetch, yt-dlp | 常有官方字幕与幻灯片 |
| 网易公开课 | web_fetch | 中文课程 |

## 6. 新闻与媒体

| 来源 | 获取方式 | 备注 |
|---|---|---|
| Google News | web_fetch, RSS | 聚合, 适合查时间线 |
| GDELT | API, browser | 全球新闻事件数据库, 可查趋势 |
| 主流媒体 (新华社, 财新, 澎湃, Reuters, AP 等) | web_fetch, RSS | 权威, 注意通稿 |
| 行业媒体 | site: 检索, RSS | 细分领域动态 |
| 公司新闻稿与发布会 | web_fetch | 一手 |
| 财新, 华尔街见闻 等财经 | web_fetch, 付费墙注意 | 权威财经 |
| 快讯类 (36氪, 钛媒体) | web_fetch | 时效快, 细节少 |

## 7. 社交平台

| 来源 | 获取方式 | 备注 |
|---|---|---|
| X (Twitter) | browser, 需登录 | 实时讨论, 反爬严 |
| 微博 | browser | 中文舆情 |
| 小红书 | browser | 消费与经验内容, 广告多 |
| 抖音 | browser | 短视频, 信息密度低 |
| Telegram 频道 | browser, 公开频道页 | 公开频道可读 |
| LinkedIn | browser, 需登录 | 职业与公司信息 |
| Mastodon, Bluesky | web_fetch, API | 开放网络 |
| VK | web_fetch | 俄语社交 |

社交平台只作线索, 关键结论必须回到一手来源.

## 8. 百科与知识图谱

| 来源 | 获取方式 | 备注 |
|---|---|---|
| Wikipedia | API, web_fetch | 术语与背景, 看引用原文 |
| Wikidata | API / SPARQL | 实体属性与关系 |
| DBpedia | web_fetch | 结构化百科 |
| 百度百科 | web_fetch | 中文背景补充 |
| 萌娘百科等垂直百科 | web_fetch | 二次元等垂直领域 |

## 9. 数据与统计

| 来源 | 获取方式 | 备注 |
|---|---|---|
| World Bank | API | 经济社会指标 |
| IMF | API | 金融与经济 |
| OECD | API | 发达国家统计 |
| UN Data | web_fetch, API | 全球统计 |
| Our World in Data | web_fetch, 数据下载 | 可视化与原始数据 |
| 国家统计局 | web_fetch | 中国宏观数据 |
| 中国统计年鉴, 各省统计公报 | web_fetch | 中文权威数据 |
| Kaggle | API, web_fetch | 数据集 |
| Hugging Face Datasets | API | 机器学习数据集 |
| Statista | 付费 | 商业统计, 免费页有限 |
| 企业年报, 招股书 | web_fetch | 一手公司数据 |
| 天池, 和鲸 | web_fetch | 中文竞赛与开源数据集 |
| 巨潮资讯 | web_fetch | A 股公告与年报 |
| 上交所, 深交所, 北交所 | web_fetch | 上市公司公告 |
| 东方财富, 同花顺 | web_fetch | 行情与财报 |
| 国家法律法规数据库 | web_fetch | 法律法规全文 |
| 国务院政策文件库 | web_fetch | 政策文件 |
| 北大法宝, 威科先行 | 付费, browser | 法规与案例 |
| 裁判文书网 | browser, 需登录 | 判例与裁判观点 |

## 10. 公司与工商

| 来源 | 获取方式 | 备注 |
|---|---|---|
| 天眼查, 企查查, 爱企查 | browser, 需登录, 部分付费 | 工商, 股权, 司法 |
| OpenCorporates | web_fetch, API | 全球公司注册 |
| Crunchbase | browser | 融资与公司档案 |
| 公司官网, 财报, IR 页 | web_fetch | 一手 |
| 招聘 JD | web_fetch, browser | 反映技术栈与业务方向 |
| 专利与商标库 | 见第 11 类 | 技术布局线索 |

## 11. 专利与标准

| 来源 | 获取方式 | 备注 |
|---|---|---|
| Google Patents | web_fetch | 全球专利检索 |
| Espacenet | web_fetch | 欧洲专利局 |
| CNIPA 国家知识产权局 | web_fetch, browser | 中国专利 |
| WIPO PATENTSCOPE | web_fetch | 国际专利 |
| RFC | `https://www.rfc-editor.org/rfc/rfcNNNN` | 互联网标准, 一手 |
| W3C, IETF, ECMA | web_fetch | 标准与草案 |
| ISO, IEC | 付费, 目录页可读 | 国际标准 |
| 全国标准信息公共服务平台 | web_fetch | GB / GB/T 标准 |
| 各行业标准 | 按行业检索 | 注意版本与现行性 |

## 12. 档案与网络历史

| 来源 | 获取方式 | 备注 |
|---|---|---|
| Wayback Machine | availability API, web_fetch | 页面快照, 处理已消失页面 |
| Archive.today | web_fetch | 手动存档 |
| Common Crawl | API, S3 | 大规模历史网页语料 |
| Google Cache | 基本不可用 | 不作为主路径 |
| 国家图书馆, 档案馆 | browser | 古籍与档案 |
| 新闻数据库 (慧科等) | 付费, 图书馆渠道 | 历史报道 |

## 13. 域名, IP 与证书 (谨慎使用)

安全侦察转 `reverse-skill`. 通用调研只在需要确认站点归属时用:

| 来源 | 获取方式 | 备注 |
|---|---|---|
| crt.sh | web_fetch, API | 证书透明度日志, 子域名线索 |
| whois | shell 或公共接口 | 注册信息, 注意隐私脱敏 |
| DNS 查询 (dig, DoH) | shell, web_fetch | 解析现状 |
| Shodan, Censys, FOFA 等 | 需账号 | 默认不用, 属安全侦察 |

## 14. 事实核查

| 来源 | 获取方式 | 备注 |
|---|---|---|
| Snopes | web_fetch | 英文事实核查 |
| PolitiFact | web_fetch | 美国政治事实核查 |
| FactCheck.org | web_fetch | 英文事实核查 |
| 腾讯较真 | web_fetch | 中文事实核查 |
| 澎湃明查 | web_fetch | 中文事实核查 |
| 各媒体更正声明 | 站内检索 | 已更正内容要引用更正版 |

## 15. 图片与视觉

| 来源 | 获取方式 | 备注 |
|---|---|---|
| Google Images | web_fetch, browser | 图片检索 |
| TinEye | web_fetch | 反向图片检索 |
| Yandex Images | web_fetch | 反向图片检索强 |
| Bing Visual Search | browser | 图片检索 |
| OCR | paddleocr-ocr skill | 截图与扫描件取文字 |
| 本地视觉分析 | lookit skill | 描述, 定位, 对比图片 |
| 图片元数据 (EXIF) | exiftool 或 python | 拍摄时间, 设备, GPS (注意隐私) |

## 16. 本地与内部资料

| 来源 | 获取方式 | 备注 |
|---|---|---|
| 当前仓库 README, docs | grep, read | 一手但可能过时 |
| `.references/` 参考项目 | grep, read | 项目内参考资料 |
| git 历史与 issue | git log, gh | 决策背景 |
| user 提供的文档 | read | 以 user 说明为准 |
| 本地缓存与抓取存档 | 文件系统 | 调研过程本身产生的证据 |

## 17. 检索式模板

- 通用: `"精确短语" site:domain.com filetype:pdf 2025`
- 找原始出处: `"关键词" original source`, `"关键词" 官方`
- 找对比: `A vs B benchmark`, `A 与 B 区别 实测`
- 找问题: `关键词 报错`, `关键词 不工作 原因`
- 找时间线: `关键词 2023 2024 2025 变化`
- 找批评: `关键词 缺点 局限 争议`
- 中文补英文: 同一概念中英文各查一次
- 知网: `cnki search '神经网络*自然语言' --group subject --json`

## 18. 选择原则

1. 结论性事实优先一手: 官方文档, 标准, 原始数据, 论文原文
2. 二手只作线索, 追到原始出处再引用
3. 冲突时看发布时间与口径, 不简单多寡对比
4. 时效敏感主题 (价格, 版本, 政策) 必须标抓取日期
5. 找不到可靠来源时写 "未找到", 不拿常识补
