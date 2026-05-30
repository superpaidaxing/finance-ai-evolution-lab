# FSK-023 `accrual-schedule` 中文详细注释

## 1. 基本信息

- **Skill 编号**：FSK-023
- **原始名称**：`accrual-schedule`
- **所属领域**：基金运营、估值复核与行政管理
- **来源项目**：`anthropic-financial-services`
- **原始路径**：`12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/fund-admin/skills/accrual-schedule/SKILL.md`

## 2. 这个 skill 是干什么的

原始描述可以理解为：Build the period-end accrual schedule — for each accrual, compute the entry, cite the support, and draft the JE. Use during month-end close; the JE is a draft for controller approval, not a posting.

基金运营类 skill 关注账、表、估值、净值、roll-forward、差异解释和运营断点追踪，重点是让后台流程可追溯，而不是生成投资观点。

放到中文语境里，`accrual-schedule` 不是一个独立应用，而是一段可以被 AI 助手调用的专业工作流。它把原来依赖人工经验的金融任务拆成更明确的触发条件、输入材料、处理步骤、输出格式和质量检查点。你阅读它时，不要只看英文标题，而要看它如何规定“先收集什么、再判断什么、最后交付什么”。

## 3. 适合什么时候用

- 如果以后把 `accrual-schedule` 改造成中文 skill，应主动补充中文触发词，例如业务场景、材料名称、常见问题和输出形式。
- 当你想学习“基金运营、估值复核与行政管理”这个领域的 AI 工作流拆解方式时，可以先读这个 skill。
- 当你以后要把银行经验改造成中文 skill、提示词模板或自动化实验时，可以把 `accrual-schedule` 作为结构参考。

## 4. 输入材料怎么理解

常见输入包括总账、子账、基金持仓、估值包、银行流水、交易流水、LP/GP 报告、期初期末余额和运营差异明细。

阅读原文时，凡是出现 source materials、filings、model、ledger、statement、customer record、portfolio、ticker、policy、rules grid、reference data 等词，都可以理解为“AI 不能凭空生成，必须依赖外部输入”。如果没有输入材料，skill 的输出只能是模板或建议，不能当作事实分析。

## 5. 输出成果怎么理解

常见输出是 NAV tie-out、GL reconciliation、break tracing、accrual schedule、roll-forward 表和差异说明草稿。

对中文学习者来说，输出成果不一定要照搬英文格式。更重要的是学习它的交付物意识：每个金融任务都应该有明确的结果形态，例如报告、表格、清单、JSON、底稿、图表、会议准备材料或升级理由。以后你自己设计银行 AI 用例时，也要先定义输出物，再决定模型和数据。

## 6. 原始工作流导读

- `Accrual schedule`（一级标题）：这是原始 skill 的结构节点，可作为阅读导航。
- `For each accrual on the policy list`（二级标题）：这是原始 skill 的结构节点，可作为阅读导航。
- `Draft JE`（二级标题）：这是原始 skill 的结构节点，可作为阅读导航。
- `Output`（二级标题）：这是原始 skill 的结构节点，可作为阅读导航。

这些标题相当于原始 skill 的骨架。建议阅读顺序是：先看触发条件，再看步骤，再看示例，最后看风险/限制/参考文件。这样能避免只记住术语，却没有理解真实金融工作流。

## 7. 金融 + AI 的核心特点

`accrual-schedule` 的核心特点，是把金融专业判断前面的准备工作结构化。AI 最适合做资料整理、格式化、初步检查、摘要、草稿、差异定位和问题清单；但金融结论本身仍然依赖数据质量、制度规则、业务经验和人工复核。

这类 skill 的启发是：金融 AI 不是简单问答，而是“角色 + 材料 + 规则 + 步骤 + 输出 + 审核”的组合。只要能把这些要素写清楚，一个复杂金融任务就可以被拆成可学习、可复用、可测试的流程。

## 8. 可迁移到哪些银行/金融场景

可迁移到银行理财估值、托管运营、资管后台、清算对账、财务运营和内控检查。

如果要迁移到中国银行业，建议按下面四步做：

1. 把英文术语换成中文业务术语。
2. 把美国/海外制度口径换成本地监管、银行制度和业务流程。
3. 把真实客户数据换成公开数据、模拟数据或脱敏样例。
4. 在输出最后增加人工复核、合规边界和禁止自动决策说明。

## 9. 术语和概念提示

- `accrual-schedule` 这个名称本身就是最重要的关键词。建议先拆开理解每个英文词，再结合所属领域判断它处理的是数据、流程、文档、合规还是客户沟通。

## 10. 风险与治理边界

AI 不能替代会计确认、估值责任、审计判断和报表签发。必须保留原始凭证、差异原因、调整分录和复核记录。

通用底线：不要让 AI 直接做投资建议、交易执行、授信审批、客户准入批准、审计签字、财务报表确认或监管报送最终确认。AI 的职责应限定为辅助整理、提示风险、生成草稿和提高复核效率。

## 11. 学习建议

第一遍只读中文注释，理解 `accrual-schedule` 的业务作用。第二遍打开原始 `SKILL.md`，对照每个标题看它怎样组织步骤。第三遍尝试把它改写成一个中文银行场景，例如“客户经理会前准备”“对账差错分析”“KYC 材料缺口识别”“财报摘要”或“市场早报”。

如果你读完仍然觉得抽象，可以只问自己三个问题：

1. 这个 skill 要帮谁工作？
2. 它需要哪些材料才能工作？
3. 它输出什么东西给人工复核？

这三个问题答清楚，基本就理解了这个 skill 的核心。

## 12. 去重边界

`accrual-schedule` 的注释只解释 skill 如何组织底稿和检查流程，不重复银行运营、财报和会计基础知识。
