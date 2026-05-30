# FSK-036 `fsi-strip-profile` 中文详细注释

## 1. 基本信息

- **Skill 编号**：FSK-036
- **原始名称**：`fsi-strip-profile`
- **所属领域**：投资银行与并购交易材料
- **来源项目**：`anthropic-financial-services`
- **原始路径**：`12-financial-ai-skills/upstream-snapshots/anthropic-financial-services/plugins/vertical-plugins/investment-banking/skills/strip-profile/SKILL.md`

## 2. 这个 skill 是干什么的

原始描述可以理解为：Creates professional investment banking strip profiles (company profiles) for pitch books, deal materials, and client presentations. Generates 1-4 information-dense slides with quadrant layouts, charts, and tables.

投行 skill 把交易材料生产链拆开：买方名单、teaser、CIM、pitch deck、数据包、流程函和 deal tracker，重点是材料结构、叙事逻辑和过程管理。

放到中文语境里，`fsi-strip-profile` 不是一个独立应用，而是一段可以被 AI 助手调用的专业工作流。它把原来依赖人工经验的金融任务拆成更明确的触发条件、输入材料、处理步骤、输出格式和质量检查点。你阅读它时，不要只看英文标题，而要看它如何规定“先收集什么、再判断什么、最后交付什么”。

## 3. 适合什么时候用

- 如果以后把 `fsi-strip-profile` 改造成中文 skill，应主动补充中文触发词，例如业务场景、材料名称、常见问题和输出形式。
- 当你想学习“投资银行与并购交易材料”这个领域的 AI 工作流拆解方式时，可以先读这个 skill。
- 当你以后要把银行经验改造成中文 skill、提示词模板或自动化实验时，可以把 `fsi-strip-profile` 作为结构参考。

## 4. 输入材料怎么理解

常见输入包括公司介绍、历史财务、预测、客户/产品/市场资料、管理层访谈、行业数据、交易时间表和潜在买方名单。

阅读原文时，凡是出现 source materials、filings、model、ledger、statement、customer record、portfolio、ticker、policy、rules grid、reference data 等词，都可以理解为“AI 不能凭空生成，必须依赖外部输入”。如果没有输入材料，skill 的输出只能是模板或建议，不能当作事实分析。

## 5. 输出成果怎么理解

常见输出是买方筛选表、CIM 框架、teaser、pitch deck、datapack、process letter、交易进度表和管理层问答准备稿。

对中文学习者来说，输出成果不一定要照搬英文格式。更重要的是学习它的交付物意识：每个金融任务都应该有明确的结果形态，例如报告、表格、清单、JSON、底稿、图表、会议准备材料或升级理由。以后你自己设计银行 AI 用例时，也要先定义输出物，再决定模型和数据。

## 6. 原始工作流导读

- `Workflow`（二级标题）：这是实际操作流程，建议逐步对照输入、处理、输出和人工复核点。
- `1. Clarify Requirements`（三级标题）：这是原始 skill 的结构节点，可作为阅读导航。
- `2. Research & Planning`（三级标题）：这是原始 skill 的结构节点，可作为阅读导航。
- `3. Slide-by-Slide Creation`（三级标题）：这是原始 skill 的结构节点，可作为阅读导航。
- `Slide Format Requirements`（二级标题）：这是原始 skill 的结构节点，可作为阅读导航。
- `Information Density is Critical`（三级标题）：这是原始 skill 的结构节点，可作为阅读导航。
- `Visual Reference`（三级标题）：这是知识底座或引用资料部分，适合建立术语和方法框架。
- `First Page Layout`（二级标题）：这是原始 skill 的结构节点，可作为阅读导航。
- `Slide Setup (CRITICAL)`（三级标题）：这是原始 skill 的结构节点，可作为阅读导航。
- `Slide Coordinate System`（三级标题）：这是原始 skill 的结构节点，可作为阅读导航。

这些标题相当于原始 skill 的骨架。建议阅读顺序是：先看触发条件，再看步骤，再看示例，最后看风险/限制/参考文件。这样能避免只记住术语，却没有理解真实金融工作流。

## 7. 金融 + AI 的核心特点

`fsi-strip-profile` 的核心特点，是把金融专业判断前面的准备工作结构化。AI 最适合做资料整理、格式化、初步检查、摘要、草稿、差异定位和问题清单；但金融结论本身仍然依赖数据质量、制度规则、业务经验和人工复核。

这类 skill 的启发是：金融 AI 不是简单问答，而是“角色 + 材料 + 规则 + 步骤 + 输出 + 审核”的组合。只要能把这些要素写清楚，一个复杂金融任务就可以被拆成可学习、可复用、可测试的流程。

## 8. 可迁移到哪些银行/金融场景

可迁移到银行公司客户经营、并购撮合、投行业务学习、客户营销材料和企业研究报告。

如果要迁移到中国银行业，建议按下面四步做：

1. 把英文术语换成中文业务术语。
2. 把美国/海外制度口径换成本地监管、银行制度和业务流程。
3. 把真实客户数据换成公开数据、模拟数据或脱敏样例。
4. 在输出最后增加人工复核、合规边界和禁止自动决策说明。

## 9. 术语和概念提示

- `fsi-strip-profile` 这个名称本身就是最重要的关键词。建议先拆开理解每个英文词，再结合所属领域判断它处理的是数据、流程、文档、合规还是客户沟通。

## 10. 风险与治理边界

交易材料不能夸大事实或隐藏重大风险；客户数据、交易信息和商业秘密必须脱敏，最终材料需法务、业务和管理层确认。

通用底线：不要让 AI 直接做投资建议、交易执行、授信审批、客户准入批准、审计签字、财务报表确认或监管报送最终确认。AI 的职责应限定为辅助整理、提示风险、生成草稿和提高复核效率。

## 11. 学习建议

第一遍只读中文注释，理解 `fsi-strip-profile` 的业务作用。第二遍打开原始 `SKILL.md`，对照每个标题看它怎样组织步骤。第三遍尝试把它改写成一个中文银行场景，例如“客户经理会前准备”“对账差错分析”“KYC 材料缺口识别”“财报摘要”或“市场早报”。

如果你读完仍然觉得抽象，可以只问自己三个问题：

1. 这个 skill 要帮谁工作？
2. 它需要哪些材料才能工作？
3. 它输出什么东西给人工复核？

这三个问题答清楚，基本就理解了这个 skill 的核心。

## 12. 去重边界

`fsi-strip-profile` 的注释只解释该 skill 的用途、结构和迁移方向，不与其他同名或相近 skill 合并。
