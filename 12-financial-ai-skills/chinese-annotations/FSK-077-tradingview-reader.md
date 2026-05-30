# FSK-077 `tradingview-reader` 中文详细注释

## 1. 基本信息

- **Skill 编号**：FSK-077
- **原始名称**：`tradingview-reader`
- **所属领域**：金融数据源、行情与情绪数据连接
- **来源项目**：`community-himself65-finance-skills`
- **原始路径**：`12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/data-providers/skills/tradingview-reader/SKILL.md`

## 2. 这个 skill 是干什么的

原始描述可以理解为：Read TradingView desktop app for market data, news, alerts, watchlists, and screener results using opencli (read-only). Use this skill whenever the user wants quotes, options chains, options expiries, screener results across stocks/crypto/forex/futures/bonds, gainers/losers/movers, news headlines or full story bodies, alerts (active list, fire log, offline fires), watchlists including colored flag lists, symbol search/autocomplete, chart state, or screenshots from their local TradingView.app. Triggers include: "options chain for X", "IV on Y", "show me SNDK puts", "TV screener for Y sector", "screen oversold stocks", "TV gainers", "crypto by market cap", "TradingView news on AAPL", "show my watchlists", "red flag list", "list my alerts", "what alerts fired", "search TV for nvidia", "what symbol is on my chart", "screenshot NVDA chart", "TradingView IV skew", "TV expiries for X". This skill is READ-ONLY — it does NOT place trades, modify watchlists, or change chart layouts.

数据源类 skill 解决金融 AI 的底层输入问题：如何连接行情、基本面、情绪、专业数据和桌面工具。

放到中文语境里，`tradingview-reader` 不是一个独立应用，而是一段可以被 AI 助手调用的专业工作流。它把原来依赖人工经验的金融任务拆成更明确的触发条件、输入材料、处理步骤、输出格式和质量检查点。你阅读它时，不要只看英文标题，而要看它如何规定“先收集什么、再判断什么、最后交付什么”。

## 3. 适合什么时候用

- 原文中的 `Triggers on` 说明了关键词触发方式，可用于以后设计中文 skill 的触发描述。
- 当你想学习“金融数据源、行情与情绪数据连接”这个领域的 AI 工作流拆解方式时，可以先读这个 skill。
- 当你以后要把银行经验改造成中文 skill、提示词模板或自动化实验时，可以把 `tradingview-reader` 作为结构参考。

## 4. 输入材料怎么理解

常见输入包括 API key、行情接口、数据供应商、股票代码、时间范围、字段定义和认证状态。

阅读原文时，凡是出现 source materials、filings、model、ledger、statement、customer record、portfolio、ticker、policy、rules grid、reference data 等词，都可以理解为“AI 不能凭空生成，必须依赖外部输入”。如果没有输入材料，skill 的输出只能是模板或建议，不能当作事实分析。

## 5. 输出成果怎么理解

常见输出是结构化数据表、字段解释、接口调用结果、错误诊断和数据质量提示。

对中文学习者来说，输出成果不一定要照搬英文格式。更重要的是学习它的交付物意识：每个金融任务都应该有明确的结果形态，例如报告、表格、清单、JSON、底稿、图表、会议准备材料或升级理由。以后你自己设计银行 AI 用例时，也要先定义输出物，再决定模型和数据。

## 6. 原始工作流导读

- `TradingView Reader (Read-Only)`（一级标题）：这是原始 skill 的结构节点，可作为阅读导航。
- `Step 1: Ensure opencli + Plugin Are Installed and Ready`（二级标题）：这是实际操作流程，建议逐步对照输入、处理、输出和人工复核点。
- `NOT_INSTALLED — Install opencli`（三级标题）：这是原始 skill 的结构节点，可作为阅读导航。
- `SETUP_NEEDED — Install the TradingView plugin and launch with CDP`（三级标题）：这是原始 skill 的结构节点，可作为阅读导航。
- `Install the plugin`（一级标题）：这是原始 skill 的结构节点，可作为阅读导航。
- `Relaunch TradingView.app with CDP enabled (one-time per session)`（一级标题）：这是原始 skill 的结构节点，可作为阅读导航。
- `Common setup issues`（三级标题）：这是原始 skill 的结构节点，可作为阅读导航。
- `Step 2: Identify What the User Needs`（二级标题）：这是实际操作流程，建议逐步对照输入、处理、输出和人工复核点。
- `Setup / chart inspection`（三级标题）：这是原始 skill 的结构节点，可作为阅读导航。
- `Quotes + options`（三级标题）：这是原始 skill 的结构节点，可作为阅读导航。

这些标题相当于原始 skill 的骨架。建议阅读顺序是：先看触发条件，再看步骤，再看示例，最后看风险/限制/参考文件。这样能避免只记住术语，却没有理解真实金融工作流。

## 7. 金融 + AI 的核心特点

`tradingview-reader` 的核心特点，是把金融专业判断前面的准备工作结构化。AI 最适合做资料整理、格式化、初步检查、摘要、草稿、差异定位和问题清单；但金融结论本身仍然依赖数据质量、制度规则、业务经验和人工复核。

这类 skill 的启发是：金融 AI 不是简单问答，而是“角色 + 材料 + 规则 + 步骤 + 输出 + 审核”的组合。只要能把这些要素写清楚，一个复杂金融任务就可以被拆成可学习、可复用、可测试的流程。

## 8. 可迁移到哪些银行/金融场景

可迁移到本项目的数据工程模块，用于设计金融数据字典、数据源目录和质量检查规则。

如果要迁移到中国银行业，建议按下面四步做：

1. 把英文术语换成中文业务术语。
2. 把美国/海外制度口径换成本地监管、银行制度和业务流程。
3. 把真实客户数据换成公开数据、模拟数据或脱敏样例。
4. 在输出最后增加人工复核、合规边界和禁止自动决策说明。

## 9. 术语和概念提示

- Options 指期权，重点是收益结构、波动率、到期日、行权价和极端情形风险。

## 10. 风险与治理边界

API key 必须放 Secrets；付费/授权数据不能公开入库；字段口径和刷新频率必须记录。

通用底线：不要让 AI 直接做投资建议、交易执行、授信审批、客户准入批准、审计签字、财务报表确认或监管报送最终确认。AI 的职责应限定为辅助整理、提示风险、生成草稿和提高复核效率。

## 11. 学习建议

第一遍只读中文注释，理解 `tradingview-reader` 的业务作用。第二遍打开原始 `SKILL.md`，对照每个标题看它怎样组织步骤。第三遍尝试把它改写成一个中文银行场景，例如“客户经理会前准备”“对账差错分析”“KYC 材料缺口识别”“财报摘要”或“市场早报”。

如果你读完仍然觉得抽象，可以只问自己三个问题：

1. 这个 skill 要帮谁工作？
2. 它需要哪些材料才能工作？
3. 它输出什么东西给人工复核？

这三个问题答清楚，基本就理解了这个 skill 的核心。

## 12. 去重边界

`tradingview-reader` 的注释只解释该 skill 的用途、结构和迁移方向，不与其他同名或相近 skill 合并。
