# FSK-087 `stock-liquidity` 中文详细注释

## 1. 基本信息

- **Skill 编号**：FSK-087
- **原始名称**：`stock-liquidity`
- **所属领域**：市场分析、估值、期权与证券研究工具
- **来源项目**：`community-himself65-finance-skills`
- **原始路径**：`12-financial-ai-skills/upstream-snapshots/community-himself65-finance-skills/plugins/market-analysis/skills/stock-liquidity/SKILL.md`

## 2. 这个 skill 是干什么的

原始描述可以理解为：Analyze stock liquidity using bid-ask spreads, volume profiles, order book depth, market impact estimates, and turnover ratios via Yahoo Finance data. Use this skill whenever the user asks about liquidity, trading costs, bid-ask spread, market depth, volume analysis, slippage, market impact, turnover ratio, or how easy/hard it is to trade a stock without moving the price. Triggers: "how liquid is AAPL", "bid-ask spread", "volume analysis", "order book depth", "market impact of a large order", "turnover ratio", "slippage estimate", "can I trade 100k shares without moving the price", "liquidity comparison", "spread analysis", "ADTV", "Amihud illiquidity", "dollar volume", "execution cost estimate", "liquidity score", penny stocks, small caps, or thinly traded securities.

市场分析工具类 skill 更强调可执行计算：估值、财报预览/复盘、分析师预期、ETF 折溢价、期权 payoff、相关性、流动性和行情数据。

放到中文语境里，`stock-liquidity` 不是一个独立应用，而是一段可以被 AI 助手调用的专业工作流。它把原来依赖人工经验的金融任务拆成更明确的触发条件、输入材料、处理步骤、输出格式和质量检查点。你阅读它时，不要只看英文标题，而要看它如何规定“先收集什么、再判断什么、最后交付什么”。

## 3. 适合什么时候用

- 原文中的 `Triggers on` 说明了关键词触发方式，可用于以后设计中文 skill 的触发描述。
- 当你想学习“市场分析、估值、期权与证券研究工具”这个领域的 AI 工作流拆解方式时，可以先读这个 skill。
- 当你以后要把银行经验改造成中文 skill、提示词模板或自动化实验时，可以把 `stock-liquidity` 作为结构参考。

## 4. 输入材料怎么理解

常见输入包括股票代码、公开行情、财务报表、估值假设、同业清单、期权参数、ETF 净值、成交量和收益率序列。

阅读原文时，凡是出现 source materials、filings、model、ledger、statement、customer record、portfolio、ticker、policy、rules grid、reference data 等词，都可以理解为“AI 不能凭空生成，必须依赖外部输入”。如果没有输入材料，skill 的输出只能是模板或建议，不能当作事实分析。

## 5. 输出成果怎么理解

常见输出是估值区间、敏感性表、财报预览/复盘、期权收益图、相关性矩阵、流动性评估和数据拉取结果。

对中文学习者来说，输出成果不一定要照搬英文格式。更重要的是学习它的交付物意识：每个金融任务都应该有明确的结果形态，例如报告、表格、清单、JSON、底稿、图表、会议准备材料或升级理由。以后你自己设计银行 AI 用例时，也要先定义输出物，再决定模型和数据。

## 6. 原始工作流导读

- `Stock Liquidity Analysis Skill`（一级标题）：这是原始 skill 的结构节点，可作为阅读导航。
- `Step 1: Ensure Dependencies Are Available`（二级标题）：这是实际操作流程，建议逐步对照输入、处理、输出和人工复核点。
- `Step 2: Route to the Correct Sub-Skill`（二级标题）：这是实际操作流程，建议逐步对照输入、处理、输出和人工复核点。
- `Defaults`（三级标题）：这是原始 skill 的结构节点，可作为阅读导航。
- `Sub-Skill A: Liquidity Dashboard`（二级标题）：这是原始 skill 的结构节点，可作为阅读导航。
- `A1: Fetch data and compute all metrics`（三级标题）：这是原始 skill 的结构节点，可作为阅读导航。
- `A2: Interpret and present`（三级标题）：这是原始 skill 的结构节点，可作为阅读导航。
- `Sub-Skill B: Spread Analysis`（二级标题）：这是原始 skill 的结构节点，可作为阅读导航。
- `B1: Current spread from quote`（三级标题）：这是原始 skill 的结构节点，可作为阅读导航。
- `B2: Options spread context`（三级标题）：这是原始 skill 的结构节点，可作为阅读导航。

这些标题相当于原始 skill 的骨架。建议阅读顺序是：先看触发条件，再看步骤，再看示例，最后看风险/限制/参考文件。这样能避免只记住术语，却没有理解真实金融工作流。

## 7. 金融 + AI 的核心特点

`stock-liquidity` 的核心特点，是把金融专业判断前面的准备工作结构化。AI 最适合做资料整理、格式化、初步检查、摘要、草稿、差异定位和问题清单；但金融结论本身仍然依赖数据质量、制度规则、业务经验和人工复核。

这类 skill 的启发是：金融 AI 不是简单问答，而是“角色 + 材料 + 规则 + 步骤 + 输出 + 审核”的组合。只要能把这些要素写清楚，一个复杂金融任务就可以被拆成可学习、可复用、可测试的流程。

## 8. 可迁移到哪些银行/金融场景

可迁移到公开市场研究小实验、财富产品解释、金融市场部学习和风险指标练习。

如果要迁移到中国银行业，建议按下面四步做：

1. 把英文术语换成中文业务术语。
2. 把美国/海外制度口径换成本地监管、银行制度和业务流程。
3. 把真实客户数据换成公开数据、模拟数据或脱敏样例。
4. 在输出最后增加人工复核、合规边界和禁止自动决策说明。

## 9. 术语和概念提示

- `stock-liquidity` 这个名称本身就是最重要的关键词。建议先拆开理解每个英文词，再结合所属领域判断它处理的是数据、流程、文档、合规还是客户沟通。

## 10. 风险与治理边界

数据可能延迟、缺失或口径不一；估值和交易分析不构成投资建议，必须展示假设和不确定性。

通用底线：不要让 AI 直接做投资建议、交易执行、授信审批、客户准入批准、审计签字、财务报表确认或监管报送最终确认。AI 的职责应限定为辅助整理、提示风险、生成草稿和提高复核效率。

## 11. 学习建议

第一遍只读中文注释，理解 `stock-liquidity` 的业务作用。第二遍打开原始 `SKILL.md`，对照每个标题看它怎样组织步骤。第三遍尝试把它改写成一个中文银行场景，例如“客户经理会前准备”“对账差错分析”“KYC 材料缺口识别”“财报摘要”或“市场早报”。

如果你读完仍然觉得抽象，可以只问自己三个问题：

1. 这个 skill 要帮谁工作？
2. 它需要哪些材料才能工作？
3. 它输出什么东西给人工复核？

这三个问题答清楚，基本就理解了这个 skill 的核心。

## 12. 去重边界

`stock-liquidity` 的注释只解释公开市场/财富管理相关工作流，不重复投资建议或交易策略结论。
