# FSK-003 `earnings-preview` 中文详细注释

## 1. 基本信息

- **Skill 编号**：FSK-003
- **原始名称**：`earnings-preview`
- **所属领域**：股票研究与投研写作
- **来源项目**：`anthropic-financial-services`
- **原始路径**：`12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/equity-research/skills/earnings-preview/SKILL.md`

## 2. 这个 skill 是干什么的

原始描述可以理解为：Build pre-earnings analysis with estimate models, scenario frameworks, and key metrics to watch. Use before a company reports quarterly earnings to prepare positioning notes, set up bull/bear scenarios, and identify what will move the stock. Triggers on "earnings preview", "what to watch for [company] earnings", "pre-earnings", "earnings setup", or "preview Q[X] for [company]".

股票研究和投研写作不是简单判断涨跌，而是围绕覆盖公司、行业数据、财务模型、业绩事件、催化剂、估值假设和风险因素形成可复核观点。

放到中文语境里，`earnings-preview` 不是一个独立应用，而是一段可以被 AI 助手调用的专业工作流。它把原来依赖人工经验的金融任务拆成更明确的触发条件、输入材料、处理步骤、输出格式和质量检查点。你阅读它时，不要只看英文标题，而要看它如何规定“先收集什么、再判断什么、最后交付什么”。

## 3. 适合什么时候用

- 原文中的 `Triggers on` 说明了关键词触发方式，可用于以后设计中文 skill 的触发描述。
- 当你想学习“股票研究与投研写作”这个领域的 AI 工作流拆解方式时，可以先读这个 skill。
- 当你以后要把银行经验改造成中文 skill、提示词模板或自动化实验时，可以把 `earnings-preview` 作为结构参考。

## 4. 输入材料怎么理解

常见输入包括公司公告、年报/季报、业绩会文字稿、行业数据、历史财务模型、估值假设、同业公司清单和已有投资观点。

阅读原文时，凡是出现 source materials、filings、model、ledger、statement、customer record、portfolio、ticker、policy、rules grid、reference data 等词，都可以理解为“AI 不能凭空生成，必须依赖外部输入”。如果没有输入材料，skill 的输出只能是模板或建议，不能当作事实分析。

## 5. 输出成果怎么理解

常见输出是研究报告、业绩更新、晨会笔记、行业概览、催化剂日历、模型更新说明和投资观点跟踪表。

对中文学习者来说，输出成果不一定要照搬英文格式。更重要的是学习它的交付物意识：每个金融任务都应该有明确的结果形态，例如报告、表格、清单、JSON、底稿、图表、会议准备材料或升级理由。以后你自己设计银行 AI 用例时，也要先定义输出物，再决定模型和数据。

## 6. 原始工作流导读

- `Earnings Preview`（一级标题）：这是原始 skill 的结构节点，可作为阅读导航。
- `Workflow`（二级标题）：这是实际操作流程，建议逐步对照输入、处理、输出和人工复核点。
- `Step 1: Gather Context`（三级标题）：这是实际操作流程，建议逐步对照输入、处理、输出和人工复核点。
- `Step 2: Key Metrics Framework`（三级标题）：这是实际操作流程，建议逐步对照输入、处理、输出和人工复核点。
- `Step 3: Scenario Analysis`（三级标题）：这是实际操作流程，建议逐步对照输入、处理、输出和人工复核点。
- `Step 4: Catalyst Checklist`（三级标题）：这是实际操作流程，建议逐步对照输入、处理、输出和人工复核点。
- `Step 5: Output`（三级标题）：这是实际操作流程，建议逐步对照输入、处理、输出和人工复核点。
- `Important Notes`（二级标题）：这是风险或常见错误部分，迁移到银行场景时必须优先阅读。

这些标题相当于原始 skill 的骨架。建议阅读顺序是：先看触发条件，再看步骤，再看示例，最后看风险/限制/参考文件。这样能避免只记住术语，却没有理解真实金融工作流。

## 7. 金融 + AI 的核心特点

`earnings-preview` 的核心特点，是把金融专业判断前面的准备工作结构化。AI 最适合做资料整理、格式化、初步检查、摘要、草稿、差异定位和问题清单；但金融结论本身仍然依赖数据质量、制度规则、业务经验和人工复核。

这类 skill 的启发是：金融 AI 不是简单问答，而是“角色 + 材料 + 规则 + 步骤 + 输出 + 审核”的组合。只要能把这些要素写清楚，一个复杂金融任务就可以被拆成可学习、可复用、可测试的流程。

## 8. 可迁移到哪些银行/金融场景

可迁移到银行金融市场部、资管、财富投顾、同业研究和管理层经营分析场景，用于整理公开信息、形成摘要、跟踪事件和生成可复核的分析草稿。

如果要迁移到中国银行业，建议按下面四步做：

1. 把英文术语换成中文业务术语。
2. 把美国/海外制度口径换成本地监管、银行制度和业务流程。
3. 把真实客户数据换成公开数据、模拟数据或脱敏样例。
4. 在输出最后增加人工复核、合规边界和禁止自动决策说明。

## 9. 术语和概念提示

- `earnings-preview` 这个名称本身就是最重要的关键词。建议先拆开理解每个英文词，再结合所属领域判断它处理的是数据、流程、文档、合规还是客户沟通。

## 10. 风险与治理边界

不能把模型输出当成投资建议；必须保留数据来源、发布日期、假设变化、人工复核人和风险提示。涉及个股或产品时，要明确不构成投资建议。

通用底线：不要让 AI 直接做投资建议、交易执行、授信审批、客户准入批准、审计签字、财务报表确认或监管报送最终确认。AI 的职责应限定为辅助整理、提示风险、生成草稿和提高复核效率。

## 11. 学习建议

第一遍只读中文注释，理解 `earnings-preview` 的业务作用。第二遍打开原始 `SKILL.md`，对照每个标题看它怎样组织步骤。第三遍尝试把它改写成一个中文银行场景，例如“客户经理会前准备”“对账差错分析”“KYC 材料缺口识别”“财报摘要”或“市场早报”。

如果你读完仍然觉得抽象，可以只问自己三个问题：

1. 这个 skill 要帮谁工作？
2. 它需要哪些材料才能工作？
3. 它输出什么东西给人工复核？

这三个问题答清楚，基本就理解了这个 skill 的核心。

## 12. 去重边界

`earnings-preview` 的注释只解释公开市场/财富管理相关工作流，不重复投资建议或交易策略结论。
