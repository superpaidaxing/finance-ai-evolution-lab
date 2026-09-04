# 周复盘

## 周期

- 时间范围：
- 本周主线：

## 本周完成

- [ ] 

## 本周学到的关键认知

1. 
2. 
3. 

## 银行业务连接

这个知识点可以连接到哪些银行场景？

- 

## AI 技术连接

涉及哪些 AI 方法或工具？

- 

## 风险与治理提醒

- 

## 下周计划

- [ ] 

## 本周一句话复盘

> 

---

## 下周建议（2026-09-08 至 2026-09-14）：用 NIST AI 风险管理框架审视银行大模型合规问答助手

### 为什么选这个主题

- 仓库前几周已经完成了用例库（`04-banking-use-cases/`）、开源项目库（`11-open-source-finance-ai-projects/`）和 skill 资源库（`12-financial-ai-skills/`），"场景"和"工具"两条线积累较多，但"治理"主线（`05-risk-governance-compliance/`）还只有一份通用清单。
- 路线图第 4 阶段和每周执行计划第 9–12 周都指向 NIST AI 风险管理框架与模型风险管理，现在是补齐治理视角的合适时点。
- 选择"银行制度/合规问答助手"作为落脚场景，是因为它是路线图第 3 阶段的首个建议实验，输入（制度文本）公开可得、不涉及客户数据，最适合练习"用治理框架审视一个具体用例"。

### 本周完成标准

- 只回答一个问题：如果银行要上线一个基于检索增强生成（RAG）的制度问答助手，按 NIST AI RMF 的"治理、映射、度量、管理"四个功能，最少要回答哪些问题、设置哪些控制点？
- 全部使用公开材料和模拟制度文本，不使用任何真实客户数据、内部制度原文或账号密钥。

### 推荐阅读（均为公开来源，按优先级排序）

1. NIST《AI 风险管理框架》（AI RMF 1.0）核心部分：治理（Govern）、映射（Map）、度量（Measure）、管理（Manage）四个功能的概述。https://www.nist.gov/itl/ai-risk-management-framework
2. NIST《生成式人工智能配置文件》（NIST AI 600-1）：重点看"虚构/幻觉（Confabulation）"、"信息完整性"、"数据隐私"、"价值链与组件集成"四类风险及对应建议行动。https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
3. BIS/巴塞尔委员会《银行数字化：对银行与监管的影响》（d575）：只看与 AI/ML、第三方与云服务相关的章节。https://www.bis.org/bcbs/publ/d575.htm
4. McKinsey《金融机构如何改进生成式 AI 治理》：摘 3 类内容——治理组织、控制点、上线流程。https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/how-financial-institutions-can-improve-their-governance-of-gen-ai
5. UK Finance《生成式 AI 在金融服务中的行动、机遇与风险管理》：重点看"输出可靠性"和"第三方风险"两节。https://www.ukfinance.org.uk/policy-and-guidance/reports-and-publications/generative-ai-action-opportunities-risk-management-financial-services
6. （可选）MIT Sloan《AI in Finance》课程大纲：只看"监管影响"一节，用于对照学术视角。https://mitsloan.mit.edu/sites/default/files/inline-files/2025JA_15.S52_AI%20in%20Finance_Syllabus.pdf

### 建议产出

- 必做：`08-reading-notes/` 新增 1 篇阅读笔记《NIST 生成式 AI 配置文件对银行大模型应用的启发》（用 `reading-note-template.md`）。
- 必做：`05-risk-governance-compliance/` 新增 1 份《银行制度问答助手 NIST AI RMF 对照检查表》，按治理/映射/度量/管理四栏列出控制点。
- 选做：`04-banking-use-cases/` 用 `use-case-template.md` 补一张"制度问答助手"用例卡，并在治理一节引用上面的检查表。
- 选做：`07-labs/` 记录一次用公开监管文件做的 RAG 提示词小实验（只记录思路、提示词和问题，不追求跑通系统）。

### 每天行动清单（每天 30–60 分钟）

- 周一（选题日）：在本文件"周期/本周主线"处写下主题、选题原因和完成标准；浏览 NIST AI RMF 页面 15 分钟，弄清四个功能各是什么。
- 周二（输入日）：读 NIST AI 600-1 中"虚构/幻觉""信息完整性""数据隐私"三类风险的建议行动，各摘 1 条；开始写阅读笔记，先填"一句话总结"和"3 个核心观点"。
- 周三（业务连接日）：回答 5 个问题——制度问答在银行哪个部门/流程出现、过去人工怎么做、痛点是什么、AI 能增强哪一步、最大风险是什么；把答案写进阅读笔记"和银行业务的连接"一节。
- 周四（AI 方案日）：把制度问答翻译成 AI 用例草案——输入（制度文本、员工问题）、输出（带引用的答案）、能力（RAG）、评估（引用准确率、拒答率、幻觉率、人工复核抽检）、人工复核放在哪里；开始按治理/映射/度量/管理四栏搭检查表骨架。
- 周五（沉淀日）：补全检查表，每栏至少 3 个控制点（例如：治理—责任人与审批流程；映射—适用范围与禁用问题清单；度量—评估集与幻觉率阈值；管理—上线后监控、回滚与审计留痕）；完成阅读笔记，提交 GitHub 更新，并在本文件"本周完成"处打勾。
- 周六（轻实验日，可选）：用 1–2 份公开监管文件做一次 RAG 提示词试验，记录提示词、3 个测试问题和出现的问题到 `07-labs/`；或阅读 McKinsey / UK Finance 报告各 20 分钟，补充检查表中的"第三方风险"控制点。
- 周日（回顾日）：只看本文件，写一句话——本周真正学到什么；判断下周是继续深化（例如把检查表推广到"投诉处理助手"）还是换题。

### 风险与治理提醒

- 所有示例制度文本必须是公开监管文件或自编模拟文本，不得使用任职机构内部制度原文。
- 实验中不要把任何真实客户、员工或账户信息输入任何模型。
- 检查表只作为个人学习产出，不代表任何机构立场。
