# 社区高评价金融 AI Skill 深度分析（第 2 批）

> 本文件分析第 2 批下载的社区金融 AI skills。与第 1 批 Anthropic 官方 skill 相比，本批更偏实时市场数据、中文财经资讯、行情工具、社交读取、估值计算和 agent 工具连接。

## 0. 本批去重说明

| 来源 | 已收录内容 | 不重复边界 |
| --- | --- | --- |
| `RKiding/Awesome-finance-skills` | 10 个 skill，偏实时财经新闻、多市场数据、情绪、预测、逻辑链路和报告生成 | 不重复 Anthropic 官方的投研写作流程；本批重点记录“数据/资讯/链路可视化能力” |
| `himself65/finance-skills` | 24 个 skill，偏市场分析、估值、期权、社交读取、数据源和 TradingView | 不重复 Anthropic 官方的财务建模与投研模板；本批重点记录“可执行工具与外部数据连接” |

## 1. 总体判断

第 1 批 Anthropic 官方 skill 更像金融知识工作的“标准作业程序”：投行材料怎么写、KYC 怎么路由、对账如何分类、财富管理报告如何准备。本批社区 skill 则更像金融 agent 的“感知层和工具层”：哪里取行情，哪里取新闻，怎么读社交媒体，怎么做情绪分析，怎么画传导链路，怎么跑估值或期权 payoff。

这两类资源组合起来，才比较接近一个完整金融 AI 系统：官方 skill 提供专业流程和输出质量标准，社区 skill 提供实时数据、工具接口和市场感知能力。对个人学习来说，可以先把社区 skill 当作“可借鉴的工具目录”，再把它们映射到银行场景：经营快报、同业动态、市场风险监测、客户经理资讯助手、投研摘要、财富产品市场解读等。

## 2. 每个 skill 的深度分析

## 实时财经资讯、市场情绪与逻辑链路

### FSK-064 `alphaear-deepear-lite`

- **来源与路径**：来自 `community-awesome-finance-skills`，上游路径 `skills/alphaear-deepear-lite/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-awesome-finance-skills/skills/alphaear-deepear-lite/SKILL.md`。
- **原始定位**：官方/上游描述：Fetch the latest financial signals and transmission-chain analyses from DeepEar Lite. Use when the user needs immediate insights into financial market trends, stock performance factors, and reasoning from the DeepEar Lite dashboard.
- **金融业务理解**：这个项目更偏“市场感知层”：把新闻、热榜、财经信源、情绪、预测市场、股票数据、逻辑链路图和报告生成组合起来。它比 Anthropic 官方投研 skill 更接近每日市场跟踪和中文市场资讯流，适合学习如何把外部信息源变成结构化投研输入。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于本项目后续构建“每日金融 AI 信息雷达”：自动抓取公开财经热点，生成中文摘要、影响链路、涉及行业/银行业务模块、需要人工复核的问题清单。
- **风险与治理边界**：治理重点是时效性和来源可靠性。实时新闻、社交舆情和预测市场信息容易噪声很高，必须保留来源、时间、抓取口径，不能把热度、情绪或预测概率直接当成投资结论。

### FSK-065 `alphaear-logic-visualizer`

- **来源与路径**：来自 `community-awesome-finance-skills`，上游路径 `skills/alphaear-logic-visualizer/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-awesome-finance-skills/skills/alphaear-logic-visualizer/SKILL.md`。
- **原始定位**：官方/上游描述：Create visualize finance logic diagrams (e.g., Draw.io XML) to explain complex finance transmission chains or finance logic flows.
- **金融业务理解**：这个项目更偏“市场感知层”：把新闻、热榜、财经信源、情绪、预测市场、股票数据、逻辑链路图和报告生成组合起来。它比 Anthropic 官方投研 skill 更接近每日市场跟踪和中文市场资讯流，适合学习如何把外部信息源变成结构化投研输入。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于本项目后续构建“每日金融 AI 信息雷达”：自动抓取公开财经热点，生成中文摘要、影响链路、涉及行业/银行业务模块、需要人工复核的问题清单。
- **风险与治理边界**：治理重点是时效性和来源可靠性。实时新闻、社交舆情和预测市场信息容易噪声很高，必须保留来源、时间、抓取口径，不能把热度、情绪或预测概率直接当成投资结论。

### FSK-066 `alphaear-news`

- **来源与路径**：来自 `community-awesome-finance-skills`，上游路径 `skills/alphaear-news/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-awesome-finance-skills/skills/alphaear-news/SKILL.md`。
- **原始定位**：官方/上游描述：Fetch hot finance news, unified trends, and prediction financial market data. Use when the user needs real-time financial news, trend reports from multiple finance sources (Weibo, Zhihu, WallstreetCN, etc.), or Polymarket finance market prediction data.
- **金融业务理解**：这个项目更偏“市场感知层”：把新闻、热榜、财经信源、情绪、预测市场、股票数据、逻辑链路图和报告生成组合起来。它比 Anthropic 官方投研 skill 更接近每日市场跟踪和中文市场资讯流，适合学习如何把外部信息源变成结构化投研输入。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于本项目后续构建“每日金融 AI 信息雷达”：自动抓取公开财经热点，生成中文摘要、影响链路、涉及行业/银行业务模块、需要人工复核的问题清单。
- **风险与治理边界**：治理重点是时效性和来源可靠性。实时新闻、社交舆情和预测市场信息容易噪声很高，必须保留来源、时间、抓取口径，不能把热度、情绪或预测概率直接当成投资结论。

### FSK-067 `alphaear-predictor`

- **来源与路径**：来自 `community-awesome-finance-skills`，上游路径 `skills/alphaear-predictor/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-awesome-finance-skills/skills/alphaear-predictor/SKILL.md`。
- **原始定位**：官方/上游描述：Market prediction skill using Kronos. Use when user needs finance market time-series forecasting or news-aware finance market adjustments.
- **金融业务理解**：这个项目更偏“市场感知层”：把新闻、热榜、财经信源、情绪、预测市场、股票数据、逻辑链路图和报告生成组合起来。它比 Anthropic 官方投研 skill 更接近每日市场跟踪和中文市场资讯流，适合学习如何把外部信息源变成结构化投研输入。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于本项目后续构建“每日金融 AI 信息雷达”：自动抓取公开财经热点，生成中文摘要、影响链路、涉及行业/银行业务模块、需要人工复核的问题清单。
- **风险与治理边界**：治理重点是时效性和来源可靠性。实时新闻、社交舆情和预测市场信息容易噪声很高，必须保留来源、时间、抓取口径，不能把热度、情绪或预测概率直接当成投资结论。

### FSK-068 `alphaear-reporter`

- **来源与路径**：来自 `community-awesome-finance-skills`，上游路径 `skills/alphaear-reporter/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-awesome-finance-skills/skills/alphaear-reporter/SKILL.md`。
- **原始定位**：官方/上游描述：Plan, write, and edit professional financial reports; generate finance chart configurations. Use when condensing finance analysis into a structured output.
- **金融业务理解**：这个项目更偏“市场感知层”：把新闻、热榜、财经信源、情绪、预测市场、股票数据、逻辑链路图和报告生成组合起来。它比 Anthropic 官方投研 skill 更接近每日市场跟踪和中文市场资讯流，适合学习如何把外部信息源变成结构化投研输入。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于本项目后续构建“每日金融 AI 信息雷达”：自动抓取公开财经热点，生成中文摘要、影响链路、涉及行业/银行业务模块、需要人工复核的问题清单。
- **风险与治理边界**：治理重点是时效性和来源可靠性。实时新闻、社交舆情和预测市场信息容易噪声很高，必须保留来源、时间、抓取口径，不能把热度、情绪或预测概率直接当成投资结论。

### FSK-069 `alphaear-search`

- **来源与路径**：来自 `community-awesome-finance-skills`，上游路径 `skills/alphaear-search/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-awesome-finance-skills/skills/alphaear-search/SKILL.md`。
- **原始定位**：官方/上游描述：Perform finance web searches and local context searches. Use when the user needs general finance info from the web (Jina/DDG/Baidu) or needs to retrieve finance information from a local document store (RAG).
- **金融业务理解**：这个项目更偏“市场感知层”：把新闻、热榜、财经信源、情绪、预测市场、股票数据、逻辑链路图和报告生成组合起来。它比 Anthropic 官方投研 skill 更接近每日市场跟踪和中文市场资讯流，适合学习如何把外部信息源变成结构化投研输入。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于本项目后续构建“每日金融 AI 信息雷达”：自动抓取公开财经热点，生成中文摘要、影响链路、涉及行业/银行业务模块、需要人工复核的问题清单。
- **风险与治理边界**：治理重点是时效性和来源可靠性。实时新闻、社交舆情和预测市场信息容易噪声很高，必须保留来源、时间、抓取口径，不能把热度、情绪或预测概率直接当成投资结论。

### FSK-070 `alphaear-sentiment`

- **来源与路径**：来自 `community-awesome-finance-skills`，上游路径 `skills/alphaear-sentiment/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-awesome-finance-skills/skills/alphaear-sentiment/SKILL.md`。
- **原始定位**：官方/上游描述：Analyze finance text sentiment using FinBERT or LLM. Use when the user needs to determine the sentiment (positive/negative/neutral) and score of financial text markets.
- **金融业务理解**：这个项目更偏“市场感知层”：把新闻、热榜、财经信源、情绪、预测市场、股票数据、逻辑链路图和报告生成组合起来。它比 Anthropic 官方投研 skill 更接近每日市场跟踪和中文市场资讯流，适合学习如何把外部信息源变成结构化投研输入。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于本项目后续构建“每日金融 AI 信息雷达”：自动抓取公开财经热点，生成中文摘要、影响链路、涉及行业/银行业务模块、需要人工复核的问题清单。
- **风险与治理边界**：治理重点是时效性和来源可靠性。实时新闻、社交舆情和预测市场信息容易噪声很高，必须保留来源、时间、抓取口径，不能把热度、情绪或预测概率直接当成投资结论。

### FSK-071 `alphaear-signal-tracker`

- **来源与路径**：来自 `community-awesome-finance-skills`，上游路径 `skills/alphaear-signal-tracker/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-awesome-finance-skills/skills/alphaear-signal-tracker/SKILL.md`。
- **原始定位**：官方/上游描述：Track finance investment signal evolution and update logic based on new finance market information. Use when monitoring finance signals and determining if they are strengthened, weakened, or falsified.
- **金融业务理解**：这个项目更偏“市场感知层”：把新闻、热榜、财经信源、情绪、预测市场、股票数据、逻辑链路图和报告生成组合起来。它比 Anthropic 官方投研 skill 更接近每日市场跟踪和中文市场资讯流，适合学习如何把外部信息源变成结构化投研输入。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于本项目后续构建“每日金融 AI 信息雷达”：自动抓取公开财经热点，生成中文摘要、影响链路、涉及行业/银行业务模块、需要人工复核的问题清单。
- **风险与治理边界**：治理重点是时效性和来源可靠性。实时新闻、社交舆情和预测市场信息容易噪声很高，必须保留来源、时间、抓取口径，不能把热度、情绪或预测概率直接当成投资结论。

### FSK-072 `alphaear-stock`

- **来源与路径**：来自 `community-awesome-finance-skills`，上游路径 `skills/alphaear-stock/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-awesome-finance-skills/skills/alphaear-stock/SKILL.md`。
- **原始定位**：官方/上游描述：Search A-Share/HK/US finance stock tickers and retrieve finance stock price history. Use when user asks about finance stock codes, recent price changes, or specific company finance stock info.
- **金融业务理解**：这个项目更偏“市场感知层”：把新闻、热榜、财经信源、情绪、预测市场、股票数据、逻辑链路图和报告生成组合起来。它比 Anthropic 官方投研 skill 更接近每日市场跟踪和中文市场资讯流，适合学习如何把外部信息源变成结构化投研输入。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于本项目后续构建“每日金融 AI 信息雷达”：自动抓取公开财经热点，生成中文摘要、影响链路、涉及行业/银行业务模块、需要人工复核的问题清单。
- **风险与治理边界**：治理重点是时效性和来源可靠性。实时新闻、社交舆情和预测市场信息容易噪声很高，必须保留来源、时间、抓取口径，不能把热度、情绪或预测概率直接当成投资结论。

### FSK-073 `skill-creator`

- **来源与路径**：来自 `community-awesome-finance-skills`，上游路径 `skills/skill-creator/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-awesome-finance-skills/skills/skill-creator/SKILL.md`。
- **原始定位**：官方/上游描述：Create or update AgentSkills. Use when designing, structuring, or packaging skills with scripts, references, and assets.
- **金融业务理解**：这个项目更偏“市场感知层”：把新闻、热榜、财经信源、情绪、预测市场、股票数据、逻辑链路图和报告生成组合起来。它比 Anthropic 官方投研 skill 更接近每日市场跟踪和中文市场资讯流，适合学习如何把外部信息源变成结构化投研输入。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于本项目后续构建“每日金融 AI 信息雷达”：自动抓取公开财经热点，生成中文摘要、影响链路、涉及行业/银行业务模块、需要人工复核的问题清单。
- **风险与治理边界**：治理重点是时效性和来源可靠性。实时新闻、社交舆情和预测市场信息容易噪声很高，必须保留来源、时间、抓取口径，不能把热度、情绪或预测概率直接当成投资结论。

## 金融数据源、行情与情绪数据连接

### FSK-074 `finance-sentiment`

- **来源与路径**：来自 `community-himself65-finance-skills`，上游路径 `plugins/data-providers/skills/finance-sentiment/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/data-providers/skills/finance-sentiment/SKILL.md`。
- **原始定位**：官方/上游描述：Fetch structured stock sentiment across Reddit, X.com, news, and Polymarket using the Adanos Finance API. Use this skill whenever the user asks how much people are talking about a stock, how hot a ticker is on social platforms, how many Polymarket bets exist for a company, whether sources are aligned, or to compare stock sentiment across multiple tickers. Triggers include: "social sentiment on TSLA", "how hot is NVDA on X.com", "how many Reddit mentions does AAPL have", "compare sentiment on AMD vs NVDA", "how many Polymarket bets on Microsoft", "is Reddit aligned with X on META", "stock buzz", "bullish percentage", and any mention of cross-source stock sentiment research. This skill is READ-ONLY and does not place trades or modify anything.
- **金融业务理解**：数据源类 skill 关注如何接入行情、基本面、情绪或专业数据接口。它适合学习金融 AI 的数据底座：没有稳定数据源，就很难让 agent 形成可复核输出。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于本项目的 06 数据工程模块，设计“金融数据源目录、字段含义、刷新频率、权限和质量检查”模板。
- **风险与治理边界**：治理重点是数据授权、API key 管理和字段解释。任何付费/授权数据都不能随意公开入库，密钥必须放 Secrets。

### FSK-075 `funda-data`

- **来源与路径**：来自 `community-himself65-finance-skills`，上游路径 `plugins/data-providers/skills/funda-data/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/data-providers/skills/funda-data/SKILL.md`。
- **原始定位**：官方/上游描述：Query Funda AI financial data via two surfaces: the MCP server at https://funda.ai/api/mcp for analyst-grade research synthesis (DCF, comps, earnings previews/recaps, sector deep-dives, SEC filings, transcripts, supply-chain mapping, ownership flow, macro framing) via the agent_chat tool — OR the REST API at https://api.funda.ai/v1 with FUNDA_API_KEY for raw data (real-time quotes, intraday candles, EOD prices, financial statements, options chains/greeks/GEX, supply-chain KG, social sentiment, news, calendars, FRED, ESG, congressional trades, AI hiring signals). Triggers: "funda", "funda.ai", real-time quote, stock price, intraday, balance sheet, income statement, options chain, DCF, comps, earnings preview/recap, analyst estimates, 10-K/10-Q/8-K, transcript, ownership flow, gamma exposure, supply chain, sector deep-dive, congressional trades, FRED. Prefer MCP for synthesis/analysis questions; use REST for raw structured data the MCP declines.
- **金融业务理解**：数据源类 skill 关注如何接入行情、基本面、情绪或专业数据接口。它适合学习金融 AI 的数据底座：没有稳定数据源，就很难让 agent 形成可复核输出。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于本项目的 06 数据工程模块，设计“金融数据源目录、字段含义、刷新频率、权限和质量检查”模板。
- **风险与治理边界**：治理重点是数据授权、API key 管理和字段解释。任何付费/授权数据都不能随意公开入库，密钥必须放 Secrets。

### FSK-076 `hormuz-strait`

- **来源与路径**：来自 `community-himself65-finance-skills`，上游路径 `plugins/data-providers/skills/hormuz-strait/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/data-providers/skills/hormuz-strait/SKILL.md`。
- **原始定位**：官方/上游描述：Check the current status of the Strait of Hormuz — shipping transit data, oil price impact, stranded vessels, insurance risk levels, diplomatic developments, and global trade impact. Use this skill whenever the user asks about the Strait of Hormuz, Hormuz chokepoint, Persian Gulf shipping risk, oil transit disruption, war risk premium in the Gulf, Middle East shipping routes, tanker traffic through Hormuz, oil supply chain risk, or geopolitical risk affecting energy markets. Triggers include: "Hormuz status", "Strait of Hormuz", "is Hormuz open", "shipping through the Gulf", "oil chokepoint", "Persian Gulf tanker traffic", "war risk premium", "Hormuz crisis", "energy supply chain risk", "oil transit disruption", "Middle East shipping", any mention of Hormuz or Persian Gulf in context of oil, shipping, or geopolitical risk.
- **金融业务理解**：数据源类 skill 关注如何接入行情、基本面、情绪或专业数据接口。它适合学习金融 AI 的数据底座：没有稳定数据源，就很难让 agent 形成可复核输出。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于本项目的 06 数据工程模块，设计“金融数据源目录、字段含义、刷新频率、权限和质量检查”模板。
- **风险与治理边界**：治理重点是数据授权、API key 管理和字段解释。任何付费/授权数据都不能随意公开入库，密钥必须放 Secrets。

### FSK-077 `tradingview-reader`

- **来源与路径**：来自 `community-himself65-finance-skills`，上游路径 `plugins/data-providers/skills/tradingview-reader/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/data-providers/skills/tradingview-reader/SKILL.md`。
- **原始定位**：官方/上游描述：Read TradingView desktop app for market data, news, alerts, watchlists, and screener results using opencli (read-only). Use this skill whenever the user wants quotes, options chains, options expiries, screener results across stocks/crypto/forex/futures/bonds, gainers/losers/movers, news headlines or full story bodies, alerts (active list, fire log, offline fires), watchlists including colored flag lists, symbol search/autocomplete, chart state, or screenshots from their local TradingView.app. Triggers include: "options chain for X", "IV on Y", "show me SNDK puts", "TV screener for Y sector", "screen oversold stocks", "TV gainers", "crypto by market cap", "TradingView news on AAPL", "show my watchlists", "red flag list", "list my alerts", "what alerts fired", "search TV for nvidia", "what symbol is on my chart", "screenshot NVDA chart", "TradingView IV skew", "TV expiries for X". This skill is READ-ONLY — it does NOT place trades, modify watchlists, or change chart layouts.
- **金融业务理解**：数据源类 skill 关注如何接入行情、基本面、情绪或专业数据接口。它适合学习金融 AI 的数据底座：没有稳定数据源，就很难让 agent 形成可复核输出。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于本项目的 06 数据工程模块，设计“金融数据源目录、字段含义、刷新频率、权限和质量检查”模板。
- **风险与治理边界**：治理重点是数据授权、API key 管理和字段解释。任何付费/授权数据都不能随意公开入库，密钥必须放 Secrets。

## 市场分析、估值、期权与证券研究工具

### FSK-078 `company-valuation`

- **来源与路径**：来自 `community-himself65-finance-skills`，上游路径 `plugins/market-analysis/skills/company-valuation/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/market-analysis/skills/company-valuation/SKILL.md`。
- **原始定位**：官方/上游描述：Estimate the intrinsic value of a public company using DCF, relative (peer multiple) and sum-of-parts (SOTP) methods, then triangulate to an implied share price with upside/downside versus the current market price. Use this skill whenever the user asks: "what is AAPL worth", "valuation of NVDA", "fair value of TSLA", "intrinsic value", "DCF for MSFT", "build a DCF", "discounted cash flow", "WACC", "terminal value", "implied share price", "upside to fair value", "is X overvalued/undervalued", "relative valuation", "peer comparison valuation", "EV/EBITDA target", "SOTP", "sum of the parts", "how much is [company] worth", "price target from fundamentals", "value this company", or any ticker in the context of computing intrinsic or relative valuation. Default to running ALL three methods (DCF + relative + SOTP-if-applicable) and presenting a blended implied price with a sensitivity table. Do not answer valuation questions from memory — always run the workflow.
- **金融业务理解**：这个项目的市场分析 skill 更强调工具化执行：调用 yfinance、估值模型、期权 payoff、相关性、流动性和 earnings 数据，把研究问题转成可运行的数据分析步骤。它适合补充 Anthropic 官方 skill 在实时数据和可计算分析上的不足。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于做“证券分析小实验”：用公开行情和财务数据跑估值、相关性、流动性或期权收益结构，再把结果写成中文学习笔记。
- **风险与治理边界**：治理重点是数据可得性、默认假设和非投资建议边界。公开数据可能延迟或缺字段，估值输出必须展示假设、敏感性和置信度。

### FSK-079 `earnings-preview`

- **来源与路径**：来自 `community-himself65-finance-skills`，上游路径 `plugins/market-analysis/skills/earnings-preview/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/market-analysis/skills/earnings-preview/SKILL.md`。
- **原始定位**：官方/上游描述：Generate a pre-earnings briefing for any stock using Yahoo Finance data. Use this skill whenever the user wants to prepare for an upcoming earnings report, understand what analysts expect, review a company's beat/miss track record, or get a quick overview before an earnings call. Triggers include: "earnings preview for AAPL", "what to expect from TSLA earnings", "MSFT reports next week", "earnings preview", "pre-earnings analysis", "what are analysts expecting for NVDA", "earnings estimates for", "will GOOGL beat earnings", "earnings beat/miss history", "upcoming earnings", "before earnings", "earnings setup", "consensus estimates", "earnings whisper", "EPS expectations", "what's the street expecting", "earnings season preview", any mention of preparing for or previewing an earnings report, or any request to understand expectations ahead of a company's earnings date. Always use this skill when the user mentions a ticker in context of upcoming earnings, even if they don't say "preview" explicitly.
- **金融业务理解**：这个项目的市场分析 skill 更强调工具化执行：调用 yfinance、估值模型、期权 payoff、相关性、流动性和 earnings 数据，把研究问题转成可运行的数据分析步骤。它适合补充 Anthropic 官方 skill 在实时数据和可计算分析上的不足。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于做“证券分析小实验”：用公开行情和财务数据跑估值、相关性、流动性或期权收益结构，再把结果写成中文学习笔记。
- **风险与治理边界**：治理重点是数据可得性、默认假设和非投资建议边界。公开数据可能延迟或缺字段，估值输出必须展示假设、敏感性和置信度。

### FSK-080 `earnings-recap`

- **来源与路径**：来自 `community-himself65-finance-skills`，上游路径 `plugins/market-analysis/skills/earnings-recap/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/market-analysis/skills/earnings-recap/SKILL.md`。
- **原始定位**：官方/上游描述：Generate a post-earnings analysis for any stock using Yahoo Finance data. Use when the user wants to review what happened after earnings, understand beat/miss results, see stock reaction, or get an earnings recap. Triggers: "AAPL earnings recap", "how did TSLA earnings go", "MSFT earnings results", "did NVDA beat earnings", "post-earnings analysis", "earnings surprise", "what happened with GOOGL earnings", "earnings reaction", "stock moved after earnings", "EPS beat or miss", "revenue beat or miss", "quarterly results for", "how were earnings", "AMZN reported last night", "earnings call recap", or any request about a company's recent earnings outcome. Use this skill when the user references a past earnings event, even if they just say "AAPL reported" or "how did they do".
- **金融业务理解**：这个项目的市场分析 skill 更强调工具化执行：调用 yfinance、估值模型、期权 payoff、相关性、流动性和 earnings 数据，把研究问题转成可运行的数据分析步骤。它适合补充 Anthropic 官方 skill 在实时数据和可计算分析上的不足。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于做“证券分析小实验”：用公开行情和财务数据跑估值、相关性、流动性或期权收益结构，再把结果写成中文学习笔记。
- **风险与治理边界**：治理重点是数据可得性、默认假设和非投资建议边界。公开数据可能延迟或缺字段，估值输出必须展示假设、敏感性和置信度。

### FSK-081 `estimate-analysis`

- **来源与路径**：来自 `community-himself65-finance-skills`，上游路径 `plugins/market-analysis/skills/estimate-analysis/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/market-analysis/skills/estimate-analysis/SKILL.md`。
- **原始定位**：官方/上游描述：Deep-dive into analyst estimates and revision trends for any stock using Yahoo Finance data. Use when the user wants to understand analyst estimate direction, how EPS or revenue forecasts changed over time, compare estimate distributions, or analyze growth projections across periods. Triggers: "estimate analysis for AAPL", "analyst estimate trends for NVDA", "EPS revisions for TSLA", "how have estimates changed for MSFT", "estimate revisions", "EPS trend", "revenue estimates", "consensus changes", "analyst estimates", "estimate distribution", "growth estimates for", "estimate momentum", "revision trend", "forward estimates", "next quarter estimates", "annual estimates", "estimate spread", "bull vs bear estimates", "estimate range", or any request about tracking or comparing analyst estimates/revisions. Use this skill when the user asks about estimates beyond a simple lookup — if they want context, trends, or analysis, this is the right skill.
- **金融业务理解**：这个项目的市场分析 skill 更强调工具化执行：调用 yfinance、估值模型、期权 payoff、相关性、流动性和 earnings 数据，把研究问题转成可运行的数据分析步骤。它适合补充 Anthropic 官方 skill 在实时数据和可计算分析上的不足。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于做“证券分析小实验”：用公开行情和财务数据跑估值、相关性、流动性或期权收益结构，再把结果写成中文学习笔记。
- **风险与治理边界**：治理重点是数据可得性、默认假设和非投资建议边界。公开数据可能延迟或缺字段，估值输出必须展示假设、敏感性和置信度。

### FSK-082 `etf-premium`

- **来源与路径**：来自 `community-himself65-finance-skills`，上游路径 `plugins/market-analysis/skills/etf-premium/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/market-analysis/skills/etf-premium/SKILL.md`。
- **原始定位**：官方/上游描述：Calculate ETF premium/discount vs NAV via Yahoo Finance, and decompose single-day surges into NAV-driven vs structural components (gamma squeeze, dealer hedging, blocked AP arbitrage). Use whenever the user asks about an ETF's premium or discount, NAV comparison, why an ETF diverged from its holdings, or how much of a move is dealer-hedging-driven. Triggers: "ETF premium", "ETF discount", "NAV premium", "is SPY at a premium", "BITO premium", "IBIT premium", "bond ETF discount", "trading above/below NAV", "ETF premium screener", "biggest discount", "compare ETF NAV", "ETF arbitrage", "ETF gamma squeeze", "ETF premium surge", "decompose ETF move", "dealer gamma exposure", "GEX for ETF", "why did this ETF jump", "premium convergence", "AP arbitrage blocked", or any request about the gap between an ETF's price and underlying value. Especially relevant for leveraged, inverse, international, bond, commodity, and crypto ETFs.
- **金融业务理解**：这个项目的市场分析 skill 更强调工具化执行：调用 yfinance、估值模型、期权 payoff、相关性、流动性和 earnings 数据，把研究问题转成可运行的数据分析步骤。它适合补充 Anthropic 官方 skill 在实时数据和可计算分析上的不足。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于做“证券分析小实验”：用公开行情和财务数据跑估值、相关性、流动性或期权收益结构，再把结果写成中文学习笔记。
- **风险与治理边界**：治理重点是数据可得性、默认假设和非投资建议边界。公开数据可能延迟或缺字段，估值输出必须展示假设、敏感性和置信度。

### FSK-083 `options-payoff`

- **来源与路径**：来自 `community-himself65-finance-skills`，上游路径 `plugins/market-analysis/skills/options-payoff/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/market-analysis/skills/options-payoff/SKILL.md`。
- **原始定位**：官方/上游描述：Generate an interactive options payoff curve chart with dynamic parameter controls. Use this skill whenever the user shares an options position screenshot, describes an options strategy, or asks to visualize how an options trade makes or loses money. Triggers include: any mention of butterfly, spread (vertical/calendar/diagonal/ratio), straddle, strangle, condor, covered call, protective put, iron condor, or any multi-leg options structure. Also triggers when a user pastes strike prices, premiums, expiry dates, or says things like "show me the payoff", "draw the P&L curve", "what does this trade look like", or uploads a screenshot from a broker (IBKR, TastyTrade, Robinhood, etc). Always use this skill even if the user only provides partial info — extract what you can and use defaults for the rest.
- **金融业务理解**：这个项目的市场分析 skill 更强调工具化执行：调用 yfinance、估值模型、期权 payoff、相关性、流动性和 earnings 数据，把研究问题转成可运行的数据分析步骤。它适合补充 Anthropic 官方 skill 在实时数据和可计算分析上的不足。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于做“证券分析小实验”：用公开行情和财务数据跑估值、相关性、流动性或期权收益结构，再把结果写成中文学习笔记。
- **风险与治理边界**：治理重点是数据可得性、默认假设和非投资建议边界。公开数据可能延迟或缺字段，估值输出必须展示假设、敏感性和置信度。

### FSK-084 `saas-valuation-compression`

- **来源与路径**：来自 `community-himself65-finance-skills`，上游路径 `plugins/market-analysis/skills/saas-valuation-compression/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/market-analysis/skills/saas-valuation-compression/SKILL.md`。
- **原始定位**：官方/上游描述：Analyze SaaS company valuation compression between funding rounds. Use this skill whenever the user asks about: how much a SaaS company's valuation multiple changed between rounds, why the ARR multiple compressed or expanded, comparing a company's compression to macro benchmarks, or explaining what drove valuation changes for any VC-backed software company. Trigger on phrases like "valuation compression", "ARR multiple", "round-to-round valuation", "multiple change", or when the user asks to compare a company's funding rounds. Always use this skill for any multi-round SaaS valuation analysis — do not try to answer from memory alone.
- **金融业务理解**：这个项目的市场分析 skill 更强调工具化执行：调用 yfinance、估值模型、期权 payoff、相关性、流动性和 earnings 数据，把研究问题转成可运行的数据分析步骤。它适合补充 Anthropic 官方 skill 在实时数据和可计算分析上的不足。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于做“证券分析小实验”：用公开行情和财务数据跑估值、相关性、流动性或期权收益结构，再把结果写成中文学习笔记。
- **风险与治理边界**：治理重点是数据可得性、默认假设和非投资建议边界。公开数据可能延迟或缺字段，估值输出必须展示假设、敏感性和置信度。

### FSK-085 `sepa-strategy`

- **来源与路径**：来自 `community-himself65-finance-skills`，上游路径 `plugins/market-analysis/skills/sepa-strategy/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/market-analysis/skills/sepa-strategy/SKILL.md`。
- **原始定位**：官方/上游描述：Analyze stocks using Mark Minervini's SEPA (Specific Entry Point Analysis) methodology. Use this skill whenever the user mentions SEPA, Minervini, superperformance, trend template, VCP (Volatility Contraction Pattern), Stage 2 uptrend, stage analysis, pivot point breakout, or asks about growth stock screening criteria. Also triggers when the user wants to evaluate whether a stock meets swing trading entry criteria, check moving average alignment (bullish stacking: price above 50MA above 150MA above 200MA), assess breakout quality with volume confirmation, calculate position sizing based on risk percentage, or identify consolidation patterns like cup-with-handle, flat base, bull flag, or high tight flag. Use this skill even when the user simply asks "should I buy this stock" or "is this a good setup" in the context of growth/momentum trading, or when they share a stock chart and want pattern analysis.
- **金融业务理解**：这个项目的市场分析 skill 更强调工具化执行：调用 yfinance、估值模型、期权 payoff、相关性、流动性和 earnings 数据，把研究问题转成可运行的数据分析步骤。它适合补充 Anthropic 官方 skill 在实时数据和可计算分析上的不足。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于做“证券分析小实验”：用公开行情和财务数据跑估值、相关性、流动性或期权收益结构，再把结果写成中文学习笔记。
- **风险与治理边界**：治理重点是数据可得性、默认假设和非投资建议边界。公开数据可能延迟或缺字段，估值输出必须展示假设、敏感性和置信度。

### FSK-086 `stock-correlation`

- **来源与路径**：来自 `community-himself65-finance-skills`，上游路径 `plugins/market-analysis/skills/stock-correlation/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/market-analysis/skills/stock-correlation/SKILL.md`。
- **原始定位**：官方/上游描述：Analyze stock correlations to find related companies and trading pairs. Use when the user asks about correlated stocks, related companies, sector peers, trading pairs, or how two or more stocks move together. Triggers: "what correlates with NVDA", "find stocks related to AMD", "correlation between AAPL and MSFT", "what moves with", "sector peers", "pair trading", "correlated stocks", "when NVDA drops what else drops", "stocks that move together", "beta to", "relative performance", "supply chain partners", "correlation matrix", "co-movement", "related tickers", "sympathy plays", "semiconductor peers", "hedging pair", "realized correlation", "rolling correlation", or any request about stocks that move in tandem or inversely. Also triggers for well-known pairs like AMD/NVDA, GOOGL/AVGO, LITE/COHR. If only one ticker is provided, infer the user wants correlated peers.
- **金融业务理解**：这个项目的市场分析 skill 更强调工具化执行：调用 yfinance、估值模型、期权 payoff、相关性、流动性和 earnings 数据，把研究问题转成可运行的数据分析步骤。它适合补充 Anthropic 官方 skill 在实时数据和可计算分析上的不足。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于做“证券分析小实验”：用公开行情和财务数据跑估值、相关性、流动性或期权收益结构，再把结果写成中文学习笔记。
- **风险与治理边界**：治理重点是数据可得性、默认假设和非投资建议边界。公开数据可能延迟或缺字段，估值输出必须展示假设、敏感性和置信度。

### FSK-087 `stock-liquidity`

- **来源与路径**：来自 `community-himself65-finance-skills`，上游路径 `plugins/market-analysis/skills/stock-liquidity/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/market-analysis/skills/stock-liquidity/SKILL.md`。
- **原始定位**：官方/上游描述：Analyze stock liquidity using bid-ask spreads, volume profiles, order book depth, market impact estimates, and turnover ratios via Yahoo Finance data. Use this skill whenever the user asks about liquidity, trading costs, bid-ask spread, market depth, volume analysis, slippage, market impact, turnover ratio, or how easy/hard it is to trade a stock without moving the price. Triggers: "how liquid is AAPL", "bid-ask spread", "volume analysis", "order book depth", "market impact of a large order", "turnover ratio", "slippage estimate", "can I trade 100k shares without moving the price", "liquidity comparison", "spread analysis", "ADTV", "Amihud illiquidity", "dollar volume", "execution cost estimate", "liquidity score", penny stocks, small caps, or thinly traded securities.
- **金融业务理解**：这个项目的市场分析 skill 更强调工具化执行：调用 yfinance、估值模型、期权 payoff、相关性、流动性和 earnings 数据，把研究问题转成可运行的数据分析步骤。它适合补充 Anthropic 官方 skill 在实时数据和可计算分析上的不足。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于做“证券分析小实验”：用公开行情和财务数据跑估值、相关性、流动性或期权收益结构，再把结果写成中文学习笔记。
- **风险与治理边界**：治理重点是数据可得性、默认假设和非投资建议边界。公开数据可能延迟或缺字段，估值输出必须展示假设、敏感性和置信度。

### FSK-088 `yfinance-data`

- **来源与路径**：来自 `community-himself65-finance-skills`，上游路径 `plugins/market-analysis/skills/yfinance-data/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/market-analysis/skills/yfinance-data/SKILL.md`。
- **原始定位**：官方/上游描述：Fetch financial and market data using the yfinance Python library. Use this skill whenever the user asks for stock prices, historical data, financial statements, options chains, dividends, earnings, analyst recommendations, or any market data. Triggers include: any mention of stock price, ticker symbol (AAPL, MSFT, TSLA, etc.), "get me the financials", "show earnings", "what's the price of", "download stock data", "options chain", "dividend history", "balance sheet", "income statement", "cash flow", "analyst targets", "institutional holders", "compare stocks", "screen for stocks", or any request involving Yahoo Finance data. Always use this skill even if the user only provides a ticker — infer intent from context.
- **金融业务理解**：这个项目的市场分析 skill 更强调工具化执行：调用 yfinance、估值模型、期权 payoff、相关性、流动性和 earnings 数据，把研究问题转成可运行的数据分析步骤。它适合补充 Anthropic 官方 skill 在实时数据和可计算分析上的不足。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于做“证券分析小实验”：用公开行情和财务数据跑估值、相关性、流动性或期权收益结构，再把结果写成中文学习笔记。
- **风险与治理边界**：治理重点是数据可得性、默认假设和非投资建议边界。公开数据可能延迟或缺字段，估值输出必须展示假设、敏感性和置信度。

## 金融 skill 创建、评估与改进

### FSK-089 `skill-creator`

- **来源与路径**：来自 `community-himself65-finance-skills`，上游路径 `plugins/skill-creator/skills/skill-creator/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/skill-creator/skills/skill-creator/SKILL.md`。
- **原始定位**：官方/上游描述：Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, update or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or iterate on skill quality. Triggers: "create a skill", "make a new skill", "build a skill for", "write a skill that", "skill for doing X", "I want a skill to", "new skill", "design a skill", "scaffold a skill", "improve this skill", "optimize this skill", "this skill isn't working well", "evaluate this skill", "score this skill", "how good is this skill", "run evals on", "benchmark this skill", "test this skill's quality", "skill quality", "skill performance". Also triggers when a user describes a repeatable workflow they want to automate, says "I keep doing X manually", "can you remember how to do X", or "turn this into a skill".
- **金融业务理解**：这个 skill 属于金融 AI agent 的辅助能力，更多服务于分析工具、界面生成、skill 创建或特定场景扩展。它的价值在于把金融分析过程产品化、组件化。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可作为后续 labs 的参考，用来把文本分析结果变成可视化、可复用工具或新的中文金融 skill 模板。
- **风险与治理边界**：治理重点是工具边界和可解释性。辅助工具可以提高效率，但不能掩盖输入来源、计算逻辑和人工复核责任。

## 社交媒体与外部研究源只读读取

### FSK-090 `discord-reader`

- **来源与路径**：来自 `community-himself65-finance-skills`，上游路径 `plugins/social-readers/skills/discord-reader/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/social-readers/skills/discord-reader/SKILL.md`。
- **原始定位**：官方/上游描述：Read Discord for financial research using opencli (read-only). Use this skill whenever the user wants to read Discord channels, search for messages in trading servers, view guild/channel info, monitor crypto or market discussion groups, or gather financial sentiment from Discord. Triggers include: "check my Discord", "search Discord for", "read Discord messages", "what's happening in the trading Discord", "show Discord channels", "list my servers", "Discord sentiment on BTC", "what are people saying in Discord about AAPL", "monitor crypto Discord", any mention of Discord in context of reading financial news, market research, or trading community discussions. This skill is READ-ONLY — it does NOT support sending messages, reacting, or any write operations.
- **金融业务理解**：社交读取类 skill 面向外部研究源、社区讨论和平台信息的只读读取。它的价值不是替代研究结论，而是扩大信息输入面，帮助发现市场关注点、叙事变化和潜在事件。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于后续做“舆情与市场叙事观察”实验，但建议只用公开、合规、只读的数据源，不接入个人账号敏感信息。
- **风险与治理边界**：治理重点是隐私、平台条款和噪声过滤。读取社交媒体必须遵守平台规则，不能采集非公开信息或把未经验证的观点当事实。

### FSK-091 `linkedin-reader`

- **来源与路径**：来自 `community-himself65-finance-skills`，上游路径 `plugins/social-readers/skills/linkedin-reader/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/social-readers/skills/linkedin-reader/SKILL.md`。
- **原始定位**：官方/上游描述：Read LinkedIn for financial research using opencli (read-only). Use this skill whenever the user wants to read their LinkedIn feed, search for jobs in the finance/trading industry, view professional posts about markets or earnings, or gather professional sentiment from LinkedIn. Triggers include: "check my LinkedIn feed", "search LinkedIn for", "LinkedIn posts about", "what's on LinkedIn about AAPL", "finance jobs on LinkedIn", "LinkedIn market sentiment", "who's posting about earnings on LinkedIn", "LinkedIn feed", "professional network buzz", "what are analysts saying on LinkedIn", any mention of LinkedIn in context of reading financial news, market research, job searches, or professional commentary. This skill is READ-ONLY — it does NOT support posting, liking, commenting, connecting, or any write operations.
- **金融业务理解**：社交读取类 skill 面向外部研究源、社区讨论和平台信息的只读读取。它的价值不是替代研究结论，而是扩大信息输入面，帮助发现市场关注点、叙事变化和潜在事件。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于后续做“舆情与市场叙事观察”实验，但建议只用公开、合规、只读的数据源，不接入个人账号敏感信息。
- **风险与治理边界**：治理重点是隐私、平台条款和噪声过滤。读取社交媒体必须遵守平台规则，不能采集非公开信息或把未经验证的观点当事实。

### FSK-092 `opencli-reader`

- **来源与路径**：来自 `community-himself65-finance-skills`，上游路径 `plugins/social-readers/skills/opencli-reader/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/social-readers/skills/opencli-reader/SKILL.md`。
- **原始定位**：官方/上游描述：Generic read-only fallback for any source opencli covers but this repo has no dedicated reader for — Yahoo Finance, Bloomberg, Reuters, Barchart, Eastmoney, Xueqiu, Sinafinance, Reddit, HackerNews, Substack, Medium, Weibo, Bilibili, Xiaohongshu, Zhihu, arXiv, Google Scholar, Apple Podcasts, Xiaoyuzhou, Spotify, YouTube, Weixin, Amazon, and more. Triggers: "use opencli to read", "grab the frontpage from hackernews", "read reddit r/wallstreetbets", "fetch Eastmoney hot stocks", "pull Xueqiu feed", "get Bloomberg markets headlines", "search arXiv for", any request to read from a site where a specialized skill does not exist but opencli does. FALLBACK — prefer twitter-reader, linkedin-reader, discord-reader, telegram-reader, or yc-reader when the source matches. READ-ONLY — never invoke write operations.
- **金融业务理解**：社交读取类 skill 面向外部研究源、社区讨论和平台信息的只读读取。它的价值不是替代研究结论，而是扩大信息输入面，帮助发现市场关注点、叙事变化和潜在事件。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于后续做“舆情与市场叙事观察”实验，但建议只用公开、合规、只读的数据源，不接入个人账号敏感信息。
- **风险与治理边界**：治理重点是隐私、平台条款和噪声过滤。读取社交媒体必须遵守平台规则，不能采集非公开信息或把未经验证的观点当事实。

### FSK-093 `telegram-reader`

- **来源与路径**：来自 `community-himself65-finance-skills`，上游路径 `plugins/social-readers/skills/telegram-reader/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/social-readers/skills/telegram-reader/SKILL.md`。
- **原始定位**：官方/上游描述：Read Telegram channels and groups for financial news and market research using tdl (read-only). Use this skill whenever the user wants to read Telegram channels, export messages from financial Telegram groups, list their Telegram chats, search for news in Telegram channels, or gather market intelligence from Telegram. Triggers include: "check my Telegram", "read Telegram channel", "Telegram news", "what's new in my Telegram channels", "export messages from", "list my Telegram chats", "financial news on Telegram", "crypto Telegram", "market news Telegram", any mention of Telegram in context of reading financial news, crypto signals, or market research. This skill is READ-ONLY — it does NOT support sending messages, joining channels, or any write operations.
- **金融业务理解**：社交读取类 skill 面向外部研究源、社区讨论和平台信息的只读读取。它的价值不是替代研究结论，而是扩大信息输入面，帮助发现市场关注点、叙事变化和潜在事件。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于后续做“舆情与市场叙事观察”实验，但建议只用公开、合规、只读的数据源，不接入个人账号敏感信息。
- **风险与治理边界**：治理重点是隐私、平台条款和噪声过滤。读取社交媒体必须遵守平台规则，不能采集非公开信息或把未经验证的观点当事实。

### FSK-094 `twitter-reader`

- **来源与路径**：来自 `community-himself65-finance-skills`，上游路径 `plugins/social-readers/skills/twitter-reader/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/social-readers/skills/twitter-reader/SKILL.md`。
- **原始定位**：官方/上游描述：Read Twitter/X for financial research using opencli (read-only). Use this skill whenever the user wants to read their Twitter feed, search for financial tweets, view bookmarks, look up user profiles, or gather market sentiment from Twitter/X. Triggers include: "check my feed", "search Twitter for", "show my bookmarks", "who follows", "look up @user", "what's trending about", "market sentiment on Twitter", "what are people saying about AAPL", "recent tweets from @elonmusk", "show me @user's posts", "fintwit", any mention of Twitter/X in context of reading financial news or market research. This skill is READ-ONLY — it does NOT support posting, liking, retweeting, or any write operations.
- **金融业务理解**：社交读取类 skill 面向外部研究源、社区讨论和平台信息的只读读取。它的价值不是替代研究结论，而是扩大信息输入面，帮助发现市场关注点、叙事变化和潜在事件。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于后续做“舆情与市场叙事观察”实验，但建议只用公开、合规、只读的数据源，不接入个人账号敏感信息。
- **风险与治理边界**：治理重点是隐私、平台条款和噪声过滤。读取社交媒体必须遵守平台规则，不能采集非公开信息或把未经验证的观点当事实。

### FSK-095 `yc-reader`

- **来源与路径**：来自 `community-himself65-finance-skills`，上游路径 `plugins/social-readers/skills/yc-reader/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/social-readers/skills/yc-reader/SKILL.md`。
- **原始定位**：官方/上游描述：Look up Y Combinator companies, batches, and startup ecosystem data using the yc-oss API (read-only). Use this skill whenever the user wants to research YC-backed startups, find companies in a specific batch or industry, check which YC companies are hiring, explore top YC companies, or analyze startup trends by sector or tag. Triggers include: "YC companies in fintech", "who's in the latest YC batch", "YC startups hiring", "top Y Combinator companies", "find YC companies tagged AI", "W25 batch", "S24 companies", "YC stats", "Y Combinator portfolio", "startup research", "which YC companies do X", "venture research on YC", any mention of Y Combinator, YC batch, or YC-backed companies in the context of startup research, venture analysis, or market intelligence. This is a read-only data source — the API is a static JSON dataset updated daily.
- **金融业务理解**：社交读取类 skill 面向外部研究源、社区讨论和平台信息的只读读取。它的价值不是替代研究结论，而是扩大信息输入面，帮助发现市场关注点、叙事变化和潜在事件。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可用于后续做“舆情与市场叙事观察”实验，但建议只用公开、合规、只读的数据源，不接入个人账号敏感信息。
- **风险与治理边界**：治理重点是隐私、平台条款和噪声过滤。读取社交媒体必须遵守平台规则，不能采集非公开信息或把未经验证的观点当事实。

## 创业公司与一级市场分析工具

### FSK-096 `startup-analysis`

- **来源与路径**：来自 `community-himself65-finance-skills`，上游路径 `plugins/startup-tools/skills/startup-analysis/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/startup-tools/skills/startup-analysis/SKILL.md`。
- **原始定位**：官方/上游描述：Analyze a startup from three perspectives: VC investor, job applicant, and CEO/founder. Use this skill whenever the user wants to evaluate a startup, assess whether to invest in or join a startup, do due diligence, evaluate a job offer from a startup, understand a startup's competitive position, or assess company health and trajectory. Triggers: "analyze this startup", "should I join [company]", "is [company] a good investment", "evaluate [company]", "due diligence on [company]", "what do you think of [startup]", "should I take this startup job offer", "how healthy is [company]", "startup assessment", "company analysis", "is [company] worth joining", "what's the outlook for [company]", "research [company] for me", any mention of evaluating or assessing a startup or tech company from investment, career, or strategic perspectives — provide all three perspectives by default.
- **金融业务理解**：这个 skill 属于金融 AI agent 的辅助能力，更多服务于分析工具、界面生成、skill 创建或特定场景扩展。它的价值在于把金融分析过程产品化、组件化。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可作为后续 labs 的参考，用来把文本分析结果变成可视化、可复用工具或新的中文金融 skill 模板。
- **风险与治理边界**：治理重点是工具边界和可解释性。辅助工具可以提高效率，但不能掩盖输入来源、计算逻辑和人工复核责任。

## 金融分析界面与交互式组件生成

### FSK-097 `generative-ui`

- **来源与路径**：来自 `community-himself65-finance-skills`，上游路径 `plugins/ui-tools/skills/generative-ui/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/ui-tools/skills/generative-ui/SKILL.md`。
- **原始定位**：官方/上游描述：Design system and guidelines for Claude's built-in generative UI — the show_widget tool that renders interactive HTML/SVG widgets inline in claude.ai conversations. This skill provides the complete Anthropic "Imagine" design system so Claude produces high-quality widgets without needing to call read_me first. Use this skill whenever the user asks to visualize data, create an interactive chart, build a dashboard, render a diagram, draw a flowchart, show a mockup, create an interactive explainer, or produce any visual content beyond plain text or markdown. Triggers include: "show me", "visualize", "draw", "chart", "dashboard", "diagram", "flowchart", "widget", "interactive", "mockup", "illustrate", "explain how X works" (with visual), or any request for visual/interactive output. Also triggers when the user wants to display financial data visually, create comparison grids, or build tools with sliders, toggles, or live-updating displays.
- **金融业务理解**：这个 skill 属于金融 AI agent 的辅助能力，更多服务于分析工具、界面生成、skill 创建或特定场景扩展。它的价值在于把金融分析过程产品化、组件化。
- **AI 工作流价值**：它补充了金融 agent 从“会写”到“能查、能算、能画、能跟踪”的能力。对学习者而言，重点是理解它依赖哪些外部工具、数据字段、模型假设和运行环境。
- **可迁移应用方向**：可作为后续 labs 的参考，用来把文本分析结果变成可视化、可复用工具或新的中文金融 skill 模板。
- **风险与治理边界**：治理重点是工具边界和可解释性。辅助工具可以提高效率，但不能掩盖输入来源、计算逻辑和人工复核责任。

## 3. 下一批建议

下一批建议继续分析 `JoelLewis/finance_skills`。它虽然 star 数不如前两个社区项目高，但覆盖财富管理、美国证券合规、交易运营、客户运营和数据集成，结构完整，适合与银行基础体系、合规反洗钱、客户运营和数据治理模块打通。
