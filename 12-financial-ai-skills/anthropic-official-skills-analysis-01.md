# Anthropic 官方金融 Skill 深度分析（第 1 批）

> 本文件分析第 1 批下载的 Anthropic 官方金融相关 skill。重点不是逐字翻译原文，而是把每个 skill 放回金融业务、银行学习、AI 工作流和风险治理语境中理解。

## 0. 本批去重说明

| 范围 | 已收录内容 | 不重复边界 |
| --- | --- | --- |
| Anthropic Financial Services | 55 个 skill，覆盖投行、股票研究、私募股权、财富管理、基金运营、KYC、财务建模 | 不重复后续社区市场数据、中文财经新闻和美国投顾合规知识库；后续只补差异能力 |
| Anthropic Knowledge Work Finance | 8 个 skill，覆盖分录、对账、关账、报表、SOX、差异分析 | 不重复银行运营总论；本文件只分析 skill 工作流如何辅助财务会计知识工作 |

## 1. 总体判断

Anthropic 这批金融 skill 的最大价值，是把金融机构和金融服务公司里的“高密度知识工作”拆成了可执行的步骤。它不是一个单纯的金融知识库，也不是一个能直接给投资建议的黑盒模型，而是把分析师、投行、财务、运营、合规、财富顾问等角色的工作过程写成模板：什么时候触发、需要哪些输入、如何组织材料、输出什么文档、哪些地方必须人工复核。

这对本项目很重要。你现在的目标不是马上写一个复杂系统，而是先学会识别金融 AI 的真实落点：AI 不是替代银行审批人、投资顾问或财务签字人，而是帮助他们整理材料、校验一致性、形成草稿、生成底稿、提出缺口和风险点。把这些 skill 拆开看，就能看到金融 AI 从“聊天”进入“流程”的方式。

从银行从业者角度看，本批 skill 可以分成八类：投研、财务建模、投行交易材料、基金运营、客户准入/KYC、私募股权、财富管理、财务会计。每一类都能映射到银行内部的某些真实工作：例如 KYC 对应账户开立和客户尽调，对账对应运营和财务管理，财富管理对应私行/零售顾问，估值和模型对应投研/金融市场/资管，CIM 和 pitch deck 对应公司银行客户经营和投行业务。

## 2. 按领域理解这些 skill

### 2.1 股票研究与投研写作

适合学习卖方/买方投研如何把公告、业绩会、财务模型、行业催化剂和投资观点串成可复核的研究工作流。它对银行从业者的价值，是理解“研究结论不是一句判断，而是证据、模型、事件和风险假设的组合”。

本领域已收录 9 个 skill。阅读时不要只看 skill 名称，要重点看它要求哪些输入、产出什么中间件、哪些判断被保留给人工复核。

### 2.2 财务建模、估值与办公文档自动化

适合学习财务模型、估值、可比公司、Excel/PPT 工作底稿和交易材料如何标准化。对金融 AI 项目而言，这类 skill 很适合拆成“数据抽取、表格校验、假设管理、模型生成、结果复核”的可落地链路。

本领域已收录 13 个 skill。阅读时不要只看 skill 名称，要重点看它要求哪些输入、产出什么中间件、哪些判断被保留给人工复核。

### 2.3 投资银行与并购交易材料

适合学习投行项目中从买方名单、teaser、CIM、数据包、pitch deck 到交易跟踪的材料生产链。对个人学习尤其有用，因为它把高强度知识工作拆成可复用的文档结构和质量控制点。

本领域已收录 9 个 skill。阅读时不要只看 skill 名称，要重点看它要求哪些输入、产出什么中间件、哪些判断被保留给人工复核。

### 2.4 基金运营、估值复核与行政管理

适合学习基金运营中的 NAV、GL、roll-forward、break tracing、variance commentary 等后台流程。它和银行运营、托管、理财估值、资管运营很接近，重点不是生成观点，而是让账、表、差异和解释能被追踪。

本领域已收录 6 个 skill。阅读时不要只看 skill 名称，要重点看它要求哪些输入、产出什么中间件、哪些判断被保留给人工复核。

### 2.5 KYC、客户准入与运营规则

适合学习金融机构客户准入、KYC 文件解析、规则网格、缺口识别和升级路径。它与银行反洗钱、客户尽调、账户开立、受益所有人识别等场景高度相关。

本领域已收录 2 个 skill。阅读时不要只看 skill 名称，要重点看它要求哪些输入、产出什么中间件、哪些判断被保留给人工复核。

### 2.6 私募股权投资、尽调与投后管理

适合学习 PE 从找项目、筛项目、尽调、投委会备忘录、收益分析、投后监控到价值创造计划的全周期方法。它能帮助把“投资判断”拆成数据、假设、证据、风险和行动计划。

本领域已收录 10 个 skill。阅读时不要只看 skill 名称，要重点看它要求哪些输入、产出什么中间件、哪些判断被保留给人工复核。

### 2.7 财富管理、客户建议与组合调整

适合学习财富管理中的客户报告、年度检视、投资建议、财务规划、组合再平衡和税损收割。对银行零售/私人银行很有参考价值，但必须结合本地适当性、销售合规和产品准入规则。

本领域已收录 6 个 skill。阅读时不要只看 skill 名称，要重点看它要求哪些输入、产出什么中间件、哪些判断被保留给人工复核。

### 2.8 财务会计、关账、对账、报表与 SOX 审计支持

适合学习企业财务团队的月结、分录、对账、报表、差异分析和 SOX 控制测试。它对银行运营、财务管理和内控学习有价值，也能启发“AI 如何辅助制作底稿但不替代签字责任”。

本领域已收录 8 个 skill。阅读时不要只看 skill 名称，要重点看它要求哪些输入、产出什么中间件、哪些判断被保留给人工复核。

## 3. 每个 skill 的深度分析

## 股票研究与投研写作

### FSK-001 `catalyst-calendar`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/equity-research/skills/catalyst-calendar/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/equity-research/skills/catalyst-calendar/SKILL.md`。
- **原始定位**：官方描述：Build and maintain a calendar of upcoming catalysts across a coverage universe — earnings dates, conferences, product launches, regulatory decisions, and macro events. Helps prioritize attention and position ahead of events. Triggers on "catalyst calendar", "upcoming events", "what's coming up", "earnings calendar", "event calendar", or "catalyst tracker".
- **金融业务理解**：这个 skill 属于“股票研究与投研写作”领域。适合学习卖方/买方投研如何把公告、业绩会、财务模型、行业催化剂和投资观点串成可复核的研究工作流。它对银行从业者的价值，是理解“研究结论不是一句判断，而是证据、模型、事件和风险假设的组合”。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `catalyst-calendar` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-002 `earnings-analysis`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/equity-research/skills/earnings-analysis/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/equity-research/skills/earnings-analysis/SKILL.md`。
- **原始定位**：官方描述：Create professional equity research earnings update reports (8-12 pages, 3,000-5,000 words) analyzing quarterly results for companies already under coverage. Fast-turnaround format focusing on beat/miss analysis, key metrics, updated estimates, and revised thesis. Includes 1-3 summary tables and 8-12 charts. Use when user requests "earnings update", "quarterly update", "earnings analysis", "Q1/Q2/Q3/Q4 results", or post-earnings report.
- **金融业务理解**：这个 skill 属于“股票研究与投研写作”领域。适合学习卖方/买方投研如何把公告、业绩会、财务模型、行业催化剂和投资观点串成可复核的研究工作流。它对银行从业者的价值，是理解“研究结论不是一句判断，而是证据、模型、事件和风险假设的组合”。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `earnings-analysis` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-003 `earnings-preview`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/equity-research/skills/earnings-preview/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/equity-research/skills/earnings-preview/SKILL.md`。
- **原始定位**：官方描述：Build pre-earnings analysis with estimate models, scenario frameworks, and key metrics to watch. Use before a company reports quarterly earnings to prepare positioning notes, set up bull/bear scenarios, and identify what will move the stock. Triggers on "earnings preview", "what to watch for [company] earnings", "pre-earnings", "earnings setup", or "preview Q[X] for [company]".
- **金融业务理解**：这个 skill 属于“股票研究与投研写作”领域。适合学习卖方/买方投研如何把公告、业绩会、财务模型、行业催化剂和投资观点串成可复核的研究工作流。它对银行从业者的价值，是理解“研究结论不是一句判断，而是证据、模型、事件和风险假设的组合”。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `earnings-preview` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-004 `idea-generation`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/equity-research/skills/idea-generation/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/equity-research/skills/idea-generation/SKILL.md`。
- **原始定位**：官方描述：Systematic stock screening and investment idea sourcing. Combines quantitative screens, thematic research, and pattern recognition to surface new long and short ideas. Use when looking for new ideas, running screens, or conducting thematic sweeps. Triggers on "idea generation", "stock screen", "find ideas", "what looks interesting", "screen for", "new ideas", or "pitch me something".
- **金融业务理解**：这个 skill 属于“股票研究与投研写作”领域。适合学习卖方/买方投研如何把公告、业绩会、财务模型、行业催化剂和投资观点串成可复核的研究工作流。它对银行从业者的价值，是理解“研究结论不是一句判断，而是证据、模型、事件和风险假设的组合”。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `idea-generation` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-005 `initiating-coverage`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/equity-research/skills/initiating-coverage/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/equity-research/skills/initiating-coverage/SKILL.md`。
- **原始定位**：官方描述：Create institutional-quality equity research initiation reports through a 5-task workflow. Tasks must be executed individually with verified prerequisites - (1) company research, (2) financial modeling, (3) valuation analysis, (4) chart generation, (5) final report assembly. Each task produces specific deliverables (markdown docs, Excel models, charts, or DOCX reports). Tasks 3-5 have dependencies on earlier tasks.
- **金融业务理解**：这个 skill 属于“股票研究与投研写作”领域。适合学习卖方/买方投研如何把公告、业绩会、财务模型、行业催化剂和投资观点串成可复核的研究工作流。它对银行从业者的价值，是理解“研究结论不是一句判断，而是证据、模型、事件和风险假设的组合”。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `initiating-coverage` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-006 `model-update`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/equity-research/skills/model-update/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/equity-research/skills/model-update/SKILL.md`。
- **原始定位**：官方描述：Update financial models with new data — quarterly earnings, management guidance, macro changes, or revised assumptions. Adjusts estimates, recalculates valuation, and flags material changes. Use after earnings, guidance updates, or when assumptions need refreshing. Triggers on "update model", "plug earnings", "refresh estimates", "update numbers for [company]", "new guidance", or "revise estimates".
- **金融业务理解**：这个 skill 属于“股票研究与投研写作”领域。适合学习卖方/买方投研如何把公告、业绩会、财务模型、行业催化剂和投资观点串成可复核的研究工作流。它对银行从业者的价值，是理解“研究结论不是一句判断，而是证据、模型、事件和风险假设的组合”。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `model-update` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是假设透明和结果复核。估值、组合和税务相关输出必须列出输入、假设、敏感性、数据日期和“不构成投资/税务建议”的边界。

### FSK-007 `morning-note`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/equity-research/skills/morning-note/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/equity-research/skills/morning-note/SKILL.md`。
- **原始定位**：官方描述：Draft concise morning meeting notes summarizing overnight developments, trade ideas, and key events for coverage stocks. Designed for the 7am morning meeting format — tight, opinionated, actionable. Triggers on "morning note", "morning meeting", "what happened overnight", "trade idea", "morning call prep", or "daily note".
- **金融业务理解**：这个 skill 属于“股票研究与投研写作”领域。适合学习卖方/买方投研如何把公告、业绩会、财务模型、行业催化剂和投资观点串成可复核的研究工作流。它对银行从业者的价值，是理解“研究结论不是一句判断，而是证据、模型、事件和风险假设的组合”。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `morning-note` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-008 `sector-overview`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/equity-research/skills/sector-overview/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/equity-research/skills/sector-overview/SKILL.md`。
- **原始定位**：官方描述：Create comprehensive industry and sector landscape reports covering market dynamics, competitive positioning, key players, and thematic trends. Use for client requests, sector initiations, thematic research pieces, or internal knowledge building. Triggers on "sector overview", "industry report", "market landscape", "sector analysis", "industry deep dive", or "thematic research".
- **金融业务理解**：这个 skill 属于“股票研究与投研写作”领域。适合学习卖方/买方投研如何把公告、业绩会、财务模型、行业催化剂和投资观点串成可复核的研究工作流。它对银行从业者的价值，是理解“研究结论不是一句判断，而是证据、模型、事件和风险假设的组合”。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `sector-overview` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-009 `thesis-tracker`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/equity-research/skills/thesis-tracker/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/equity-research/skills/thesis-tracker/SKILL.md`。
- **原始定位**：官方描述：Maintain and update investment theses for portfolio positions and watchlist names. Track key data points, catalysts, and thesis milestones over time. Use when updating a thesis with new information, reviewing position rationale, or checking if a thesis is still intact. Triggers on "update thesis for [company]", "is my thesis still intact", "thesis check", "add data point to [company]", or "review my positions".
- **金融业务理解**：这个 skill 属于“股票研究与投研写作”领域。适合学习卖方/买方投研如何把公告、业绩会、财务模型、行业催化剂和投资观点串成可复核的研究工作流。它对银行从业者的价值，是理解“研究结论不是一句判断，而是证据、模型、事件和风险假设的组合”。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `thesis-tracker` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

## 财务建模、估值与办公文档自动化

### FSK-010 `3-statement-model`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/financial-analysis/skills/3-statement-model/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/financial-analysis/skills/3-statement-model/SKILL.md`。
- **原始定位**：官方描述：Complete, populate and fill out 3-statement financial model templates (Income Statement, Balance Sheet, Cash Flow Statement) . Use when asked to fill out model templates, complete existing model frameworks, populate financial models with data, complete a partially filled IS/BS/CF framework, or link integrated financial statements within an existing template structure. Triggers include requests to fill in, complete, or populate a 3-statement model template
- **金融业务理解**：这个 skill 属于“财务建模、估值与办公文档自动化”领域。适合学习财务模型、估值、可比公司、Excel/PPT 工作底稿和交易材料如何标准化。对金融 AI 项目而言，这类 skill 很适合拆成“数据抽取、表格校验、假设管理、模型生成、结果复核”的可落地链路。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `3-statement-model` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是假设透明和结果复核。估值、组合和税务相关输出必须列出输入、假设、敏感性、数据日期和“不构成投资/税务建议”的边界。

### FSK-011 `audit-xls`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/financial-analysis/skills/audit-xls/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/financial-analysis/skills/audit-xls/SKILL.md`。
- **原始定位**：官方描述：Audit a spreadsheet for formula accuracy, errors, and common mistakes. Scopes to a selected range, a single sheet, or the entire model (including financial-model integrity checks like BS balance, cash tie-out, and logic sanity). Triggers on "audit this sheet", "check my formulas", "find formula errors", "QA this spreadsheet", "sanity check this", "debug model", "model check", "model won't balance", "something's off in my model", "model review".
- **金融业务理解**：这个 skill 属于“财务建模、估值与办公文档自动化”领域。适合学习财务模型、估值、可比公司、Excel/PPT 工作底稿和交易材料如何标准化。对金融 AI 项目而言，这类 skill 很适合拆成“数据抽取、表格校验、假设管理、模型生成、结果复核”的可落地链路。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `audit-xls` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是“只做辅助与路由，不做最终批准”。需要保留规则来源、证据字段、缺失文件、升级理由和人工复核记录，防止模型把高风险客户或异常交易直接放行。

### FSK-012 `clean-data-xls`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/financial-analysis/skills/clean-data-xls/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/financial-analysis/skills/clean-data-xls/SKILL.md`。
- **原始定位**：官方描述：Clean up messy spreadsheet data — trim whitespace, fix inconsistent casing, convert numbers-stored-as-text, standardize dates, remove duplicates, and flag mixed-type columns. Use when data is messy, inconsistent, or needs prep before analysis. Triggers on "clean this data", "clean up this sheet", "normalize this data", "fix formatting", "dedupe", "standardize this column", "this data is messy".
- **金融业务理解**：这个 skill 属于“财务建模、估值与办公文档自动化”领域。适合学习财务模型、估值、可比公司、Excel/PPT 工作底稿和交易材料如何标准化。对金融 AI 项目而言，这类 skill 很适合拆成“数据抽取、表格校验、假设管理、模型生成、结果复核”的可落地链路。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `clean-data-xls` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-013 `competitive-analysis`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/financial-analysis/skills/competitive-analysis/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/financial-analysis/skills/competitive-analysis/SKILL.md`。
- **原始定位**：官方描述：Framework for building competitive landscape decks — market positioning, competitor deep-dives, comparative analysis, strategic synthesis. Use when the user asks for a competitive landscape, competitor analysis, peer comparison, market positioning assessment, strategic review, or investment memo deck. Also triggers on "who are the competitors to X", "benchmark X against peers", "build a market map", or any request to systematically evaluate competitive dynamics across an industry.
- **金融业务理解**：这个 skill 属于“财务建模、估值与办公文档自动化”领域。适合学习财务模型、估值、可比公司、Excel/PPT 工作底稿和交易材料如何标准化。对金融 AI 项目而言，这类 skill 很适合拆成“数据抽取、表格校验、假设管理、模型生成、结果复核”的可落地链路。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `competitive-analysis` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-014 `comps-analysis`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/financial-analysis/skills/comps-analysis/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/financial-analysis/skills/comps-analysis/SKILL.md`。
- **原始定位**：官方描述：|
- **金融业务理解**：这个 skill 属于“财务建模、估值与办公文档自动化”领域。适合学习财务模型、估值、可比公司、Excel/PPT 工作底稿和交易材料如何标准化。对金融 AI 项目而言，这类 skill 很适合拆成“数据抽取、表格校验、假设管理、模型生成、结果复核”的可落地链路。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `comps-analysis` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-015 `dcf-model`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/financial-analysis/skills/dcf-model/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/financial-analysis/skills/dcf-model/SKILL.md`。
- **原始定位**：官方描述：Real DCF (Discounted Cash Flow) model creation for equity valuation. Retrieves financial data from SEC filings and analyst reports, builds comprehensive cash flow projections with proper WACC calculations, performs sensitivity analysis, and outputs professional Excel models with executive summaries. Use when users need to value a company using DCF methodology, request intrinsic value analysis, or ask for detailed financial modeling with growth projections and terminal value calculations.
- **金融业务理解**：这个 skill 属于“财务建模、估值与办公文档自动化”领域。适合学习财务模型、估值、可比公司、Excel/PPT 工作底稿和交易材料如何标准化。对金融 AI 项目而言，这类 skill 很适合拆成“数据抽取、表格校验、假设管理、模型生成、结果复核”的可落地链路。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `dcf-model` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是假设透明和结果复核。估值、组合和税务相关输出必须列出输入、假设、敏感性、数据日期和“不构成投资/税务建议”的边界。

### FSK-016 `deck-refresh`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/financial-analysis/skills/deck-refresh/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/financial-analysis/skills/deck-refresh/SKILL.md`。
- **原始定位**：官方描述：Updates a presentation with new numbers — quarterly refreshes, earnings updates, comp rolls, rebased market data. Use whenever the user asks to "update the deck with Q4 numbers", "refresh the comps", "roll this forward", "swap in the new earnings", "change all the $485M to $512M", or any request to swap figures across an existing deck without rebuilding it.
- **金融业务理解**：这个 skill 属于“财务建模、估值与办公文档自动化”领域。适合学习财务模型、估值、可比公司、Excel/PPT 工作底稿和交易材料如何标准化。对金融 AI 项目而言，这类 skill 很适合拆成“数据抽取、表格校验、假设管理、模型生成、结果复核”的可落地链路。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `deck-refresh` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-017 `ib-check-deck`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/financial-analysis/skills/ib-check-deck/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/financial-analysis/skills/ib-check-deck/SKILL.md`。
- **原始定位**：官方描述：Investment banking presentation quality checker. Reviews a pitch deck or client-ready presentation for (1) number consistency across slides, (2) data-narrative alignment, (3) language polish against IB standards, (4) visual and formatting QC. Use whenever the user asks to review, check, QC, proof, or do a final pass on a deck, pitch, or client materials — including requests like "check my numbers", "reconcile figures across slides", "is this client-ready", or "what am I missing before I send this out".
- **金融业务理解**：这个 skill 属于“财务建模、估值与办公文档自动化”领域。适合学习财务模型、估值、可比公司、Excel/PPT 工作底稿和交易材料如何标准化。对金融 AI 项目而言，这类 skill 很适合拆成“数据抽取、表格校验、假设管理、模型生成、结果复核”的可落地链路。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `ib-check-deck` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-018 `lbo-model`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/financial-analysis/skills/lbo-model/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/financial-analysis/skills/lbo-model/SKILL.md`。
- **原始定位**：官方描述：This skill should be used when completing LBO (Leveraged Buyout) model templates in Excel for private equity transactions, deal materials, or investment committee presentations. The skill fills in formulas, validates calculations, and ensures professional formatting standards that adapt to any template structure.
- **金融业务理解**：这个 skill 属于“财务建模、估值与办公文档自动化”领域。适合学习财务模型、估值、可比公司、Excel/PPT 工作底稿和交易材料如何标准化。对金融 AI 项目而言，这类 skill 很适合拆成“数据抽取、表格校验、假设管理、模型生成、结果复核”的可落地链路。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `lbo-model` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是假设透明和结果复核。估值、组合和税务相关输出必须列出输入、假设、敏感性、数据日期和“不构成投资/税务建议”的边界。

### FSK-019 `ppt-template-creator`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md`。
- **原始定位**：官方描述：Creates self-contained PPT template SKILLS (not presentations) from user-provided PowerPoint templates. Use ONLY when a user wants to create a reusable skill from their template. For creating actual presentations, use the pptx skill instead.
- **金融业务理解**：这个 skill 属于“财务建模、估值与办公文档自动化”领域。适合学习财务模型、估值、可比公司、Excel/PPT 工作底稿和交易材料如何标准化。对金融 AI 项目而言，这类 skill 很适合拆成“数据抽取、表格校验、假设管理、模型生成、结果复核”的可落地链路。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `ppt-template-creator` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-020 `pptx-author`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/financial-analysis/skills/pptx-author/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/financial-analysis/skills/pptx-author/SKILL.md`。
- **原始定位**：官方描述：Produce a .pptx file on disk (headless) instead of driving a live PowerPoint document — for managed-agent sessions with no open Office app.
- **金融业务理解**：这个 skill 属于“财务建模、估值与办公文档自动化”领域。适合学习财务模型、估值、可比公司、Excel/PPT 工作底稿和交易材料如何标准化。对金融 AI 项目而言，这类 skill 很适合拆成“数据抽取、表格校验、假设管理、模型生成、结果复核”的可落地链路。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `pptx-author` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-021 `skill-creator`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/financial-analysis/skills/skill-creator/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/financial-analysis/skills/skill-creator/SKILL.md`。
- **原始定位**：官方描述：Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.
- **金融业务理解**：这个 skill 属于“财务建模、估值与办公文档自动化”领域。适合学习财务模型、估值、可比公司、Excel/PPT 工作底稿和交易材料如何标准化。对金融 AI 项目而言，这类 skill 很适合拆成“数据抽取、表格校验、假设管理、模型生成、结果复核”的可落地链路。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `skill-creator` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-022 `xlsx-author`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/financial-analysis/skills/xlsx-author/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/financial-analysis/skills/xlsx-author/SKILL.md`。
- **原始定位**：官方描述：Produce a .xlsx file on disk (headless) instead of driving a live Excel workbook — for managed-agent sessions with no open Office app.
- **金融业务理解**：这个 skill 属于“财务建模、估值与办公文档自动化”领域。适合学习财务模型、估值、可比公司、Excel/PPT 工作底稿和交易材料如何标准化。对金融 AI 项目而言，这类 skill 很适合拆成“数据抽取、表格校验、假设管理、模型生成、结果复核”的可落地链路。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `xlsx-author` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

## 基金运营、估值复核与行政管理

### FSK-023 `accrual-schedule`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/fund-admin/skills/accrual-schedule/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/fund-admin/skills/accrual-schedule/SKILL.md`。
- **原始定位**：官方描述：Build the period-end accrual schedule — for each accrual, compute the entry, cite the support, and draft the JE. Use during month-end close; the JE is a draft for controller approval, not a posting.
- **金融业务理解**：这个 skill 属于“基金运营、估值复核与行政管理”领域。适合学习基金运营中的 NAV、GL、roll-forward、break tracing、variance commentary 等后台流程。它和银行运营、托管、理财估值、资管运营很接近，重点不是生成观点，而是让账、表、差异和解释能被追踪。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `accrual-schedule` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-024 `break-trace`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/fund-admin/skills/break-trace/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/fund-admin/skills/break-trace/SKILL.md`。
- **原始定位**：官方描述：Root-cause a reconciliation break to its source transaction or posting — follow the audit trail from the break row back to the originating entry on each side and state what differs and why. Use after gl-recon has classified a break.
- **金融业务理解**：这个 skill 属于“基金运营、估值复核与行政管理”领域。适合学习基金运营中的 NAV、GL、roll-forward、break tracing、variance commentary 等后台流程。它和银行运营、托管、理财估值、资管运营很接近，重点不是生成观点，而是让账、表、差异和解释能被追踪。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `break-trace` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是账务可追溯。AI 可以做差异归类、解释草稿和底稿整理，但不能替代会计确认、审计判断、财务报表签发和权限审批。

### FSK-025 `gl-recon`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/fund-admin/skills/gl-recon/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/fund-admin/skills/gl-recon/SKILL.md`。
- **原始定位**：官方描述：Reconcile general ledger to subledger for a trade date or period — match at the position or transaction level, surface breaks, and classify each break by likely cause. Use for daily or month-end recon runs across asset classes.
- **金融业务理解**：这个 skill 属于“基金运营、估值复核与行政管理”领域。适合学习基金运营中的 NAV、GL、roll-forward、break tracing、variance commentary 等后台流程。它和银行运营、托管、理财估值、资管运营很接近，重点不是生成观点，而是让账、表、差异和解释能被追踪。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `gl-recon` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是账务可追溯。AI 可以做差异归类、解释草稿和底稿整理，但不能替代会计确认、审计判断、财务报表签发和权限审批。

### FSK-026 `nav-tieout`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/fund-admin/skills/nav-tieout/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/fund-admin/skills/nav-tieout/SKILL.md`。
- **原始定位**：官方描述：Tie an LP statement to the fund's NAV pack — recompute the LP's capital account from the NAV components and flag any line that doesn't agree. Use before LP statements are distributed.
- **金融业务理解**：这个 skill 属于“基金运营、估值复核与行政管理”领域。适合学习基金运营中的 NAV、GL、roll-forward、break tracing、variance commentary 等后台流程。它和银行运营、托管、理财估值、资管运营很接近，重点不是生成观点，而是让账、表、差异和解释能被追踪。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `nav-tieout` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是账务可追溯。AI 可以做差异归类、解释草稿和底稿整理，但不能替代会计确认、审计判断、财务报表签发和权限审批。

### FSK-027 `roll-forward`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/fund-admin/skills/roll-forward/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/fund-admin/skills/roll-forward/SKILL.md`。
- **原始定位**：官方描述：Build a roll-forward schedule for a balance-sheet account — beginning balance plus activity less reversals equals ending balance, with each component tied to GL. Use for month-end close packages and audit support.
- **金融业务理解**：这个 skill 属于“基金运营、估值复核与行政管理”领域。适合学习基金运营中的 NAV、GL、roll-forward、break tracing、variance commentary 等后台流程。它和银行运营、托管、理财估值、资管运营很接近，重点不是生成观点，而是让账、表、差异和解释能被追踪。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `roll-forward` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是账务可追溯。AI 可以做差异归类、解释草稿和底稿整理，但不能替代会计确认、审计判断、财务报表签发和权限审批。

### FSK-028 `variance-commentary`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/fund-admin/skills/variance-commentary/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/fund-admin/skills/variance-commentary/SKILL.md`。
- **原始定位**：官方描述：Write flux commentary for every P&L and balance-sheet line over threshold — current vs prior period and vs budget, with the driver explained from underlying activity. Use for the month-end close package and management reporting.
- **金融业务理解**：这个 skill 属于“基金运营、估值复核与行政管理”领域。适合学习基金运营中的 NAV、GL、roll-forward、break tracing、variance commentary 等后台流程。它和银行运营、托管、理财估值、资管运营很接近，重点不是生成观点，而是让账、表、差异和解释能被追踪。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `variance-commentary` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是账务可追溯。AI 可以做差异归类、解释草稿和底稿整理，但不能替代会计确认、审计判断、财务报表签发和权限审批。

## 投资银行与并购交易材料

### FSK-029 `buyer-list`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/investment-banking/skills/buyer-list/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/investment-banking/skills/buyer-list/SKILL.md`。
- **原始定位**：官方描述：Build and organize a universe of potential acquirers for sell-side M&A processes. Identifies strategic and financial buyers, assesses fit, and prioritizes outreach. Use when preparing for a sell-side mandate, building a buyer universe, or evaluating potential partners. Triggers on "buyer list", "buyer universe", "potential acquirers", "who would buy this", "strategic buyers", or "financial sponsors".
- **金融业务理解**：这个 skill 属于“投资银行与并购交易材料”领域。适合学习投行项目中从买方名单、teaser、CIM、数据包、pitch deck 到交易跟踪的材料生产链。对个人学习尤其有用，因为它把高强度知识工作拆成可复用的文档结构和质量控制点。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `buyer-list` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-030 `cim-builder`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/investment-banking/skills/cim-builder/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/investment-banking/skills/cim-builder/SKILL.md`。
- **原始定位**：官方描述：Structure and draft a Confidential Information Memorandum for sell-side M&A processes. Organizes company information into a professional, investor-ready document with consistent formatting and narrative flow. Use when preparing sell-side materials, drafting a CIM, or organizing company data for a sale process. Triggers on "CIM", "confidential information memorandum", "offering memorandum", "info memo", "draft CIM", or "sell-side materials".
- **金融业务理解**：这个 skill 属于“投资银行与并购交易材料”领域。适合学习投行项目中从买方名单、teaser、CIM、数据包、pitch deck 到交易跟踪的材料生产链。对个人学习尤其有用，因为它把高强度知识工作拆成可复用的文档结构和质量控制点。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `cim-builder` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-031 `datapack-builder`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/investment-banking/skills/datapack-builder/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/investment-banking/skills/datapack-builder/SKILL.md`。
- **原始定位**：官方描述：Build professional financial services data packs from various sources including CIMs, offering memorandums, SEC filings, web search, or MCP servers. Extract, normalize, and standardize financial data into investment committee-ready Excel workbooks with consistent structure, proper formatting, and documented assumptions. Use for M&A due diligence, private equity analysis, investment committee materials, and standardizing financial reporting across portfolio companies. Do not use for simple financial calculations or working with already-completed data packs.
- **金融业务理解**：这个 skill 属于“投资银行与并购交易材料”领域。适合学习投行项目中从买方名单、teaser、CIM、数据包、pitch deck 到交易跟踪的材料生产链。对个人学习尤其有用，因为它把高强度知识工作拆成可复用的文档结构和质量控制点。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `datapack-builder` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-032 `deal-tracker`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/investment-banking/skills/deal-tracker/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/investment-banking/skills/deal-tracker/SKILL.md`。
- **原始定位**：官方描述：Track multiple live deals with milestones, deadlines, action items, and status updates. Maintains a deal pipeline view and surfaces upcoming deadlines and overdue items. Use when managing a book of business, tracking process milestones, or preparing for weekly deal reviews. Triggers on "deal tracker", "deal status", "where are we on", "process update", "deal pipeline", or "weekly deal review".
- **金融业务理解**：这个 skill 属于“投资银行与并购交易材料”领域。适合学习投行项目中从买方名单、teaser、CIM、数据包、pitch deck 到交易跟踪的材料生产链。对个人学习尤其有用，因为它把高强度知识工作拆成可复用的文档结构和质量控制点。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `deal-tracker` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-033 `merger-model`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/investment-banking/skills/merger-model/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/investment-banking/skills/merger-model/SKILL.md`。
- **原始定位**：官方描述：Build accretion/dilution analysis for M&A transactions. Models pro forma EPS impact, synergy sensitivities, and purchase price allocation. Use when evaluating a potential acquisition, preparing merger consequences analysis for a pitch, or advising on deal terms. Triggers on "merger model", "accretion dilution", "M&A model", "pro forma EPS", "merger consequences", or "deal impact analysis".
- **金融业务理解**：这个 skill 属于“投资银行与并购交易材料”领域。适合学习投行项目中从买方名单、teaser、CIM、数据包、pitch deck 到交易跟踪的材料生产链。对个人学习尤其有用，因为它把高强度知识工作拆成可复用的文档结构和质量控制点。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `merger-model` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是假设透明和结果复核。估值、组合和税务相关输出必须列出输入、假设、敏感性、数据日期和“不构成投资/税务建议”的边界。

### FSK-034 `pitch-deck`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/investment-banking/skills/pitch-deck/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/investment-banking/skills/pitch-deck/SKILL.md`。
- **原始定位**：官方描述：Populates investment banking pitch deck templates with data from source files. Use when: user provides a PowerPoint template to fill in, user has source data (Excel/CSV) to populate into slides, user mentions populating or filling a pitch deck template, or user needs to transfer data into existing slide layouts. Not for creating presentations from scratch.
- **金融业务理解**：这个 skill 属于“投资银行与并购交易材料”领域。适合学习投行项目中从买方名单、teaser、CIM、数据包、pitch deck 到交易跟踪的材料生产链。对个人学习尤其有用，因为它把高强度知识工作拆成可复用的文档结构和质量控制点。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `pitch-deck` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-035 `process-letter`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/investment-banking/skills/process-letter/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/investment-banking/skills/process-letter/SKILL.md`。
- **原始定位**：官方描述：Draft process letters and bid instructions for sell-side M&A processes. Covers initial indication of interest (IOI) instructions, final bid procedures, and management meeting logistics. Triggers on "process letter", "bid instructions", "IOI letter", "bid procedures", "final round letter", or "management meeting invite".
- **金融业务理解**：这个 skill 属于“投资银行与并购交易材料”领域。适合学习投行项目中从买方名单、teaser、CIM、数据包、pitch deck 到交易跟踪的材料生产链。对个人学习尤其有用，因为它把高强度知识工作拆成可复用的文档结构和质量控制点。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `process-letter` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-036 `fsi-strip-profile`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/investment-banking/skills/strip-profile/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/investment-banking/skills/strip-profile/SKILL.md`。
- **原始定位**：官方描述：|
- **金融业务理解**：这个 skill 属于“投资银行与并购交易材料”领域。适合学习投行项目中从买方名单、teaser、CIM、数据包、pitch deck 到交易跟踪的材料生产链。对个人学习尤其有用，因为它把高强度知识工作拆成可复用的文档结构和质量控制点。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `fsi-strip-profile` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-037 `teaser`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/investment-banking/skills/teaser/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/investment-banking/skills/teaser/SKILL.md`。
- **原始定位**：官方描述：Draft anonymous one-page company teasers for sell-side M&A processes. Creates a compelling summary without revealing the company's identity, designed to gauge buyer interest before NDA execution. Triggers on "teaser", "blind teaser", "anonymous profile", "one-pager for process", or "draft teaser for sell-side".
- **金融业务理解**：这个 skill 属于“投资银行与并购交易材料”领域。适合学习投行项目中从买方名单、teaser、CIM、数据包、pitch deck 到交易跟踪的材料生产链。对个人学习尤其有用，因为它把高强度知识工作拆成可复用的文档结构和质量控制点。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `teaser` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

## KYC、客户准入与运营规则

### FSK-038 `kyc-doc-parse`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/operations/skills/kyc-doc-parse/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/operations/skills/kyc-doc-parse/SKILL.md`。
- **原始定位**：官方描述：Parse an investor or client onboarding packet into structured KYC fields — identity, ownership, control, source of funds, and document inventory. Use as the first step of KYC screening; output feeds the rules engine.
- **金融业务理解**：这个 skill 属于“KYC、客户准入与运营规则”领域。适合学习金融机构客户准入、KYC 文件解析、规则网格、缺口识别和升级路径。它与银行反洗钱、客户尽调、账户开立、受益所有人识别等场景高度相关。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `kyc-doc-parse` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是“只做辅助与路由，不做最终批准”。需要保留规则来源、证据字段、缺失文件、升级理由和人工复核记录，防止模型把高风险客户或异常交易直接放行。

### FSK-039 `kyc-rules`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/operations/skills/kyc-rules/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/operations/skills/kyc-rules/SKILL.md`。
- **原始定位**：官方描述：Apply the firm's KYC/AML rules grid to a parsed onboarding record — assign a risk rating, list every rule outcome with the rule cited, and flag what's missing or escalation-worthy. Use after kyc-doc-parse; this skill decides nothing, it scores and routes.
- **金融业务理解**：这个 skill 属于“KYC、客户准入与运营规则”领域。适合学习金融机构客户准入、KYC 文件解析、规则网格、缺口识别和升级路径。它与银行反洗钱、客户尽调、账户开立、受益所有人识别等场景高度相关。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `kyc-rules` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是“只做辅助与路由，不做最终批准”。需要保留规则来源、证据字段、缺失文件、升级理由和人工复核记录，防止模型把高风险客户或异常交易直接放行。

## 私募股权投资、尽调与投后管理

### FSK-040 `ai-readiness`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/private-equity/skills/ai-readiness/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/private-equity/skills/ai-readiness/SKILL.md`。
- **原始定位**：官方描述：Scan the portfolio for the highest-leverage AI opportunities and rank where to deploy operating-partner time. Ingests quarterly updates and financials across multiple portfolio companies, identifies quick wins at each, and stacks them into a single ranked action list. Use during quarterly portfolio reviews, annual planning, or when deciding which companies get AI investment first. Triggers on "AI readiness", "AI opportunity scan", "where should we deploy AI", "AI across the portfolio", "AI quick wins", or "which portcos are ready for AI".
- **金融业务理解**：这个 skill 属于“私募股权投资、尽调与投后管理”领域。适合学习 PE 从找项目、筛项目、尽调、投委会备忘录、收益分析、投后监控到价值创造计划的全周期方法。它能帮助把“投资判断”拆成数据、假设、证据、风险和行动计划。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `ai-readiness` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-041 `dd-checklist`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/private-equity/skills/dd-checklist/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/private-equity/skills/dd-checklist/SKILL.md`。
- **原始定位**：官方描述：Generate and track comprehensive due diligence checklists tailored to the target company's sector, deal type, and complexity. Covers all major workstreams with request lists, status tracking, and red flag escalation. Use when kicking off diligence, organizing a data room review, or tracking outstanding items. Triggers on "dd checklist", "due diligence tracker", "diligence request list", "what do we still need", or "data room review".
- **金融业务理解**：这个 skill 属于“私募股权投资、尽调与投后管理”领域。适合学习 PE 从找项目、筛项目、尽调、投委会备忘录、收益分析、投后监控到价值创造计划的全周期方法。它能帮助把“投资判断”拆成数据、假设、证据、风险和行动计划。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `dd-checklist` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-042 `dd-meeting-prep`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/private-equity/skills/dd-meeting-prep/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/private-equity/skills/dd-meeting-prep/SKILL.md`。
- **原始定位**：官方描述：Prepare for due diligence meetings — management presentations, expert network calls, customer references, and advisor sessions. Generates targeted question lists, benchmarks to reference, and red flags to probe. Use before any diligence meeting or call. Triggers on "prep for management meeting", "diligence call prep", "expert call questions", "customer reference questions", or "meeting prep for [company]".
- **金融业务理解**：这个 skill 属于“私募股权投资、尽调与投后管理”领域。适合学习 PE 从找项目、筛项目、尽调、投委会备忘录、收益分析、投后监控到价值创造计划的全周期方法。它能帮助把“投资判断”拆成数据、假设、证据、风险和行动计划。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `dd-meeting-prep` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-043 `deal-screening`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/private-equity/skills/deal-screening/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/private-equity/skills/deal-screening/SKILL.md`。
- **原始定位**：官方描述：Quickly screen inbound deal flow — CIMs, teasers, and broker materials — against the fund's investment criteria. Extracts key deal metrics, runs a pass/fail framework, and outputs a one-page screening memo. Use when reviewing new deal flow, triaging inbound materials, or deciding whether to take a first call. Triggers on "screen this deal", "review this CIM", "should we look at this", "triage this teaser", or "deal screening".
- **金融业务理解**：这个 skill 属于“私募股权投资、尽调与投后管理”领域。适合学习 PE 从找项目、筛项目、尽调、投委会备忘录、收益分析、投后监控到价值创造计划的全周期方法。它能帮助把“投资判断”拆成数据、假设、证据、风险和行动计划。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `deal-screening` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-044 `deal-sourcing`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/private-equity/skills/deal-sourcing/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/private-equity/skills/deal-sourcing/SKILL.md`。
- **原始定位**：官方描述：PE deal sourcing workflow — discover target companies, check CRM for existing relationships, and draft personalized founder outreach emails. Use when sourcing new deals, prospecting companies in a sector, or reaching out to founders. Triggers on "find companies", "source deals", "draft founder email", "check if we've seen this company", or "outreach to founder".
- **金融业务理解**：这个 skill 属于“私募股权投资、尽调与投后管理”领域。适合学习 PE 从找项目、筛项目、尽调、投委会备忘录、收益分析、投后监控到价值创造计划的全周期方法。它能帮助把“投资判断”拆成数据、假设、证据、风险和行动计划。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `deal-sourcing` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-045 `ic-memo`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/private-equity/skills/ic-memo/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/private-equity/skills/ic-memo/SKILL.md`。
- **原始定位**：官方描述：Draft a structured investment committee memo for PE deal approval. Synthesizes due diligence findings, financial analysis, and deal terms into a professional IC-ready document. Use when preparing for investment committee, writing up a deal, or creating a formal recommendation. Triggers on "write IC memo", "investment committee memo", "deal write-up", "prepare IC materials", or "recommendation memo".
- **金融业务理解**：这个 skill 属于“私募股权投资、尽调与投后管理”领域。适合学习 PE 从找项目、筛项目、尽调、投委会备忘录、收益分析、投后监控到价值创造计划的全周期方法。它能帮助把“投资判断”拆成数据、假设、证据、风险和行动计划。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `ic-memo` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-046 `portfolio-monitoring`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/private-equity/skills/portfolio-monitoring/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/private-equity/skills/portfolio-monitoring/SKILL.md`。
- **原始定位**：官方描述：Track and analyze portfolio company performance against plan. Ingests monthly/quarterly financial packages (Excel, PDF), extracts KPIs, flags variances to budget, and produces summary dashboards. Use when reviewing portfolio company financials, preparing board materials, or monitoring covenant compliance. Triggers on "review portfolio company", "monthly financials", "how is [company] performing", "covenant check", or "portfolio update".
- **金融业务理解**：这个 skill 属于“私募股权投资、尽调与投后管理”领域。适合学习 PE 从找项目、筛项目、尽调、投委会备忘录、收益分析、投后监控到价值创造计划的全周期方法。它能帮助把“投资判断”拆成数据、假设、证据、风险和行动计划。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `portfolio-monitoring` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是假设透明和结果复核。估值、组合和税务相关输出必须列出输入、假设、敏感性、数据日期和“不构成投资/税务建议”的边界。

### FSK-047 `returns-analysis`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/private-equity/skills/returns-analysis/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/private-equity/skills/returns-analysis/SKILL.md`。
- **原始定位**：官方描述：Build quick IRR/MOIC sensitivity tables for PE deal evaluation. Models returns across entry multiple, leverage, exit multiple, growth, and hold period scenarios. Use when sizing up a deal, stress-testing assumptions, or preparing IC returns exhibits. Triggers on "returns analysis", "IRR sensitivity", "MOIC table", "what's the return at", "model the returns", or "back of the envelope".
- **金融业务理解**：这个 skill 属于“私募股权投资、尽调与投后管理”领域。适合学习 PE 从找项目、筛项目、尽调、投委会备忘录、收益分析、投后监控到价值创造计划的全周期方法。它能帮助把“投资判断”拆成数据、假设、证据、风险和行动计划。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `returns-analysis` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是假设透明和结果复核。估值、组合和税务相关输出必须列出输入、假设、敏感性、数据日期和“不构成投资/税务建议”的边界。

### FSK-048 `unit-economics`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/private-equity/skills/unit-economics/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/private-equity/skills/unit-economics/SKILL.md`。
- **原始定位**：官方描述：Analyze unit economics for PE targets — ARR cohorts, LTV/CAC, net retention, payback periods, revenue quality, and margin waterfall. Essential for software/SaaS, recurring revenue, and subscription businesses. Use when evaluating revenue quality, building a cohort analysis, or assessing customer economics. Triggers on "unit economics", "cohort analysis", "ARR analysis", "LTV CAC", "net retention", "revenue quality", or "customer economics".
- **金融业务理解**：这个 skill 属于“私募股权投资、尽调与投后管理”领域。适合学习 PE 从找项目、筛项目、尽调、投委会备忘录、收益分析、投后监控到价值创造计划的全周期方法。它能帮助把“投资判断”拆成数据、假设、证据、风险和行动计划。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `unit-economics` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-049 `value-creation-plan`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/private-equity/skills/value-creation-plan/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/private-equity/skills/value-creation-plan/SKILL.md`。
- **原始定位**：官方描述：Structure post-acquisition value creation plans with revenue, cost, and operational levers mapped to an EBITDA bridge. Includes 100-day priorities, KPI targets, and accountability frameworks. Use when planning post-close execution, preparing operating partner materials, or building a board-ready value creation roadmap. Triggers on "value creation plan", "100-day plan", "post-close plan", "EBITDA bridge", "operating plan", or "value creation levers".
- **金融业务理解**：这个 skill 属于“私募股权投资、尽调与投后管理”领域。适合学习 PE 从找项目、筛项目、尽调、投委会备忘录、收益分析、投后监控到价值创造计划的全周期方法。它能帮助把“投资判断”拆成数据、假设、证据、风险和行动计划。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `value-creation-plan` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

## 财富管理、客户建议与组合调整

### FSK-050 `client-report`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/wealth-management/skills/client-report/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/wealth-management/skills/client-report/SKILL.md`。
- **原始定位**：官方描述：Generate professional client-facing performance reports with portfolio returns, allocation breakdowns, and market commentary. Suitable for quarterly or annual distribution. Triggers on "client report", "performance report", "quarterly report for [client]", "generate reports", or "client statement".
- **金融业务理解**：这个 skill 属于“财富管理、客户建议与组合调整”领域。适合学习财富管理中的客户报告、年度检视、投资建议、财务规划、组合再平衡和税损收割。对银行零售/私人银行很有参考价值，但必须结合本地适当性、销售合规和产品准入规则。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `client-report` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-051 `client-review`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/wealth-management/skills/client-review/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/wealth-management/skills/client-review/SKILL.md`。
- **原始定位**：官方描述：Prepare for client review meetings with portfolio performance summary, allocation analysis, talking points, and action items. Pulls together account data into a concise meeting-ready format. Use before quarterly reviews, annual checkups, or ad-hoc client meetings. Triggers on "client review", "meeting prep for [client]", "quarterly review", "prep for [client name]", or "client meeting".
- **金融业务理解**：这个 skill 属于“财富管理、客户建议与组合调整”领域。适合学习财富管理中的客户报告、年度检视、投资建议、财务规划、组合再平衡和税损收割。对银行零售/私人银行很有参考价值，但必须结合本地适当性、销售合规和产品准入规则。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `client-review` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-052 `financial-plan`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/wealth-management/skills/financial-plan/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/wealth-management/skills/financial-plan/SKILL.md`。
- **原始定位**：官方描述：Build or update a comprehensive financial plan covering retirement projections, education funding, estate planning, and cash flow analysis. Use for new client onboarding, annual plan reviews, or scenario modeling. Triggers on "financial plan", "retirement plan", "can I retire", "education funding", "estate plan", "cash flow analysis", or "plan update".
- **金融业务理解**：这个 skill 属于“财富管理、客户建议与组合调整”领域。适合学习财富管理中的客户报告、年度检视、投资建议、财务规划、组合再平衡和税损收割。对银行零售/私人银行很有参考价值，但必须结合本地适当性、销售合规和产品准入规则。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `financial-plan` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是来源、版本和人工复核。skill 生成的是工作产品草稿，应记录数据来源、生成时间、引用材料和复核人，避免把模型输出当成最终结论。

### FSK-053 `investment-proposal`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/wealth-management/skills/investment-proposal/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/wealth-management/skills/investment-proposal/SKILL.md`。
- **原始定位**：官方描述：Create professional investment proposals for prospective clients. Covers the firm's approach, proposed allocation, expected outcomes, and fee structure. Use when pitching new clients or presenting a new investment strategy. Triggers on "investment proposal", "prospect presentation", "pitch new client", "proposal for [client]", or "new client presentation".
- **金融业务理解**：这个 skill 属于“财富管理、客户建议与组合调整”领域。适合学习财富管理中的客户报告、年度检视、投资建议、财务规划、组合再平衡和税损收割。对银行零售/私人银行很有参考价值，但必须结合本地适当性、销售合规和产品准入规则。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `investment-proposal` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是假设透明和结果复核。估值、组合和税务相关输出必须列出输入、假设、敏感性、数据日期和“不构成投资/税务建议”的边界。

### FSK-054 `portfolio-rebalance`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/wealth-management/skills/portfolio-rebalance/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/wealth-management/skills/portfolio-rebalance/SKILL.md`。
- **原始定位**：官方描述：Analyze portfolio allocation drift and generate rebalancing trade recommendations across accounts. Considers tax implications, transaction costs, and wash sale rules. Triggers on "rebalance", "portfolio drift", "allocation check", "rebalancing trades", or "my portfolio is out of balance".
- **金融业务理解**：这个 skill 属于“财富管理、客户建议与组合调整”领域。适合学习财富管理中的客户报告、年度检视、投资建议、财务规划、组合再平衡和税损收割。对银行零售/私人银行很有参考价值，但必须结合本地适当性、销售合规和产品准入规则。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `portfolio-rebalance` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是假设透明和结果复核。估值、组合和税务相关输出必须列出输入、假设、敏感性、数据日期和“不构成投资/税务建议”的边界。

### FSK-055 `tax-loss-harvesting`

- **来源与路径**：来自 `anthropic-financial-services`，上游路径 `plugins/vertical-plugins/wealth-management/skills/tax-loss-harvesting/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/wealth-management/skills/tax-loss-harvesting/SKILL.md`。
- **原始定位**：官方描述：Identify tax-loss harvesting opportunities across taxable accounts. Finds positions with unrealized losses, suggests replacement securities, and tracks wash sale windows. Triggers on "tax-loss harvesting", "TLH", "harvest losses", "tax losses", "unrealized losses", or "year-end tax planning".
- **金融业务理解**：这个 skill 属于“财富管理、客户建议与组合调整”领域。适合学习财富管理中的客户报告、年度检视、投资建议、财务规划、组合再平衡和税损收割。对银行零售/私人银行很有参考价值，但必须结合本地适当性、销售合规和产品准入规则。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `tax-loss-harvesting` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是假设透明和结果复核。估值、组合和税务相关输出必须列出输入、假设、敏感性、数据日期和“不构成投资/税务建议”的边界。

## 财务会计、关账、对账、报表与 SOX 审计支持

### FSK-056 `audit-support`

- **来源与路径**：来自 `anthropic-knowledge-work-finance`，上游路径 `finance/skills/audit-support/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-knowledge-work-finance/skills/audit-support/SKILL.md`。
- **原始定位**：官方描述：Support SOX 404 compliance with control testing methodology, sample selection, and documentation standards. Use when generating testing workpapers, selecting audit samples, classifying control deficiencies, or preparing for internal or external audits.
- **金融业务理解**：这个 skill 属于“财务会计、关账、对账、报表与 SOX 审计支持”领域。适合学习企业财务团队的月结、分录、对账、报表、差异分析和 SOX 控制测试。它对银行运营、财务管理和内控学习有价值，也能启发“AI 如何辅助制作底稿但不替代签字责任”。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `audit-support` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是“只做辅助与路由，不做最终批准”。需要保留规则来源、证据字段、缺失文件、升级理由和人工复核记录，防止模型把高风险客户或异常交易直接放行。

### FSK-057 `close-management`

- **来源与路径**：来自 `anthropic-knowledge-work-finance`，上游路径 `finance/skills/close-management/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-knowledge-work-finance/skills/close-management/SKILL.md`。
- **原始定位**：官方描述：Manage the month-end close process with task sequencing, dependencies, and status tracking. Use when planning the close calendar, tracking close progress, identifying blockers, or sequencing close activities by day.
- **金融业务理解**：这个 skill 属于“财务会计、关账、对账、报表与 SOX 审计支持”领域。适合学习企业财务团队的月结、分录、对账、报表、差异分析和 SOX 控制测试。它对银行运营、财务管理和内控学习有价值，也能启发“AI 如何辅助制作底稿但不替代签字责任”。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `close-management` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是账务可追溯。AI 可以做差异归类、解释草稿和底稿整理，但不能替代会计确认、审计判断、财务报表签发和权限审批。

### FSK-058 `financial-statements`

- **来源与路径**：来自 `anthropic-knowledge-work-finance`，上游路径 `finance/skills/financial-statements/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-knowledge-work-finance/skills/financial-statements/SKILL.md`。
- **原始定位**：官方描述：Generate financial statements (income statement, balance sheet, cash flow) with period-over-period comparison and variance analysis. Use when preparing a monthly or quarterly P&L, closing the books and need to flag material variances, comparing actuals to budget, building a financial summary for leadership review, or looking up GAAP presentation requirements and period-end adjustments.
- **金融业务理解**：这个 skill 属于“财务会计、关账、对账、报表与 SOX 审计支持”领域。适合学习企业财务团队的月结、分录、对账、报表、差异分析和 SOX 控制测试。它对银行运营、财务管理和内控学习有价值，也能启发“AI 如何辅助制作底稿但不替代签字责任”。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `financial-statements` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是账务可追溯。AI 可以做差异归类、解释草稿和底稿整理，但不能替代会计确认、审计判断、财务报表签发和权限审批。

### FSK-059 `journal-entry`

- **来源与路径**：来自 `anthropic-knowledge-work-finance`，上游路径 `finance/skills/journal-entry/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-knowledge-work-finance/skills/journal-entry/SKILL.md`。
- **原始定位**：官方描述：Prepare journal entries with proper debits, credits, and supporting detail. Use when booking month-end accruals (AP, payroll, prepaid), recording depreciation or amortization, posting revenue recognition or deferred revenue adjustments, or documenting an entry for audit review.
- **金融业务理解**：这个 skill 属于“财务会计、关账、对账、报表与 SOX 审计支持”领域。适合学习企业财务团队的月结、分录、对账、报表、差异分析和 SOX 控制测试。它对银行运营、财务管理和内控学习有价值，也能启发“AI 如何辅助制作底稿但不替代签字责任”。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `journal-entry` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是账务可追溯。AI 可以做差异归类、解释草稿和底稿整理，但不能替代会计确认、审计判断、财务报表签发和权限审批。

### FSK-060 `journal-entry-prep`

- **来源与路径**：来自 `anthropic-knowledge-work-finance`，上游路径 `finance/skills/journal-entry-prep/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-knowledge-work-finance/skills/journal-entry-prep/SKILL.md`。
- **原始定位**：官方描述：Prepare journal entries with proper debits, credits, and supporting documentation for month-end close. Use when booking accruals, prepaid amortization, fixed asset depreciation, payroll entries, revenue recognition, or any manual journal entry.
- **金融业务理解**：这个 skill 属于“财务会计、关账、对账、报表与 SOX 审计支持”领域。适合学习企业财务团队的月结、分录、对账、报表、差异分析和 SOX 控制测试。它对银行运营、财务管理和内控学习有价值，也能启发“AI 如何辅助制作底稿但不替代签字责任”。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `journal-entry-prep` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是账务可追溯。AI 可以做差异归类、解释草稿和底稿整理，但不能替代会计确认、审计判断、财务报表签发和权限审批。

### FSK-061 `reconciliation`

- **来源与路径**：来自 `anthropic-knowledge-work-finance`，上游路径 `finance/skills/reconciliation/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-knowledge-work-finance/skills/reconciliation/SKILL.md`。
- **原始定位**：官方描述：Reconcile accounts by comparing GL balances to subledgers, bank statements, or third-party data. Use when performing bank reconciliations, GL-to-subledger recs, intercompany reconciliations, or identifying and categorizing reconciling items.
- **金融业务理解**：这个 skill 属于“财务会计、关账、对账、报表与 SOX 审计支持”领域。适合学习企业财务团队的月结、分录、对账、报表、差异分析和 SOX 控制测试。它对银行运营、财务管理和内控学习有价值，也能启发“AI 如何辅助制作底稿但不替代签字责任”。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `reconciliation` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是账务可追溯。AI 可以做差异归类、解释草稿和底稿整理，但不能替代会计确认、审计判断、财务报表签发和权限审批。

### FSK-062 `sox-testing`

- **来源与路径**：来自 `anthropic-knowledge-work-finance`，上游路径 `finance/skills/sox-testing/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-knowledge-work-finance/skills/sox-testing/SKILL.md`。
- **原始定位**：官方描述：Generate SOX sample selections, testing workpapers, and control assessments. Use when planning quarterly or annual SOX 404 testing, pulling a sample for a control (revenue, P2P, ITGC, close), building a testing workpaper template, or evaluating and classifying a control deficiency.
- **金融业务理解**：这个 skill 属于“财务会计、关账、对账、报表与 SOX 审计支持”领域。适合学习企业财务团队的月结、分录、对账、报表、差异分析和 SOX 控制测试。它对银行运营、财务管理和内控学习有价值，也能启发“AI 如何辅助制作底稿但不替代签字责任”。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `sox-testing` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是“只做辅助与路由，不做最终批准”。需要保留规则来源、证据字段、缺失文件、升级理由和人工复核记录，防止模型把高风险客户或异常交易直接放行。

### FSK-063 `variance-analysis`

- **来源与路径**：来自 `anthropic-knowledge-work-finance`，上游路径 `finance/skills/variance-analysis/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/anthropic-knowledge-work-finance/skills/variance-analysis/SKILL.md`。
- **原始定位**：官方描述：Decompose financial variances into drivers with narrative explanations and waterfall analysis. Use when analyzing budget vs. actual, period-over-period changes, revenue or expense variances, or preparing variance commentary for leadership.
- **金融业务理解**：这个 skill 属于“财务会计、关账、对账、报表与 SOX 审计支持”领域。适合学习企业财务团队的月结、分录、对账、报表、差异分析和 SOX 控制测试。它对银行运营、财务管理和内控学习有价值，也能启发“AI 如何辅助制作底稿但不替代签字责任”。
- **AI 工作流价值**：它把一个原本依赖经验的金融任务拆成触发条件、输入材料、处理步骤、输出格式和检查点。对学习者而言，最值得看的不是提示词写法，而是它如何把隐性专家经验显性化。
- **可迁移应用方向**：在本项目中的应用方向：可以把 `variance-analysis` 改造成中文学习模板，进一步连接到银行业务案例、公开年报、监管制度或模拟数据。短期适合做提示词/流程卡片，长期可以做成 RAG、智能体或办公自动化小实验。
- **风险与治理边界**：治理重点是账务可追溯。AI 可以做差异归类、解释草稿和底稿整理，但不能替代会计确认、审计判断、财务报表签发和权限审批。

## 4. 下一批建议

下一批建议优先下载并分析社区中更偏实时市场数据和中文金融资讯的 skill，例如 `RKiding/Awesome-finance-skills` 和 `himself65/finance-skills`。它们与本批官方 skill 的区别在于：本批更像“金融知识工作流程模板”，下一批更像“数据源、新闻、行情、预测和工具连接能力”。两类内容应该互补，而不是重复。
