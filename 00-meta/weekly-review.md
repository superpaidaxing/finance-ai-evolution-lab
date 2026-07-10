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

# 周计划：2026-07-13 至 2026-07-19（反洗钱与交易监测中的生成式 AI）

> 本段是为下周准备的执行计划，按 `weekly-execution-plan.md` 的周一到周日节奏展开。完成后可把关键结论回填到上面的复盘模板。

## 本周建议主题

**主题：银行反洗钱与交易监测中的生成式 AI 应用与治理（AML / 交易监测 + 大模型）。**

为什么选它：

- 反洗钱与交易监测是银行合规的核心场景，也是 18 年银行经验最有护城河的领域之一，容易把业务判断转化为 AI 用例。
- 它天然贯穿本项目的四层闭环：概念（什么是可疑交易与预警）、业务（银行反洗钱流程与痛点）、技术（分类、摘要、检索增强生成、可疑交易报告草拟）、治理（模型风险、可解释、人工复核、监管留痕）。
- 五大公开来源都能覆盖到，材料充足且权威：NIST AI 风险管理框架、国际清算银行 / 巴塞尔委员会、McKinsey、MIT Sloan、UK Finance。
- 与既有目录衔接顺畅：产出可分别落到 `04-banking-use-cases/`、`05-risk-governance-compliance/`、`08-reading-notes/`。

本周完成标准：

- 只聚焦这一个主线问题，不扩散到其他场景。
- 至少沉淀 1 篇阅读笔记 + 1 个银行用例卡片 + 1 条风险治理清单更新。
- 想清楚“大模型在交易监测中到底放在哪一步、人工复核放在哪里”。

## 推荐阅读（均为公开来源）

优先读和银行、合规强相关，且能转化为用例与治理清单的材料：

1. **NIST AI 风险管理框架**（治理语言，重点看 Govern / Map / Measure / Manage 四步）
   - https://www.nist.gov/itl/ai-risk-management-framework
   - 生成式 AI 配套文件：https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
2. **国际清算银行 / 巴塞尔委员会**（监管者视角看 AI、操作风险、第三方与云服务）
   - https://www.bis.org/bcbs/publ/d575.htm
   - https://www.bis.org/publ/work1194.htm
3. **McKinsey：生成式 AI 与银行风险合规**（用例、风险、组织落地三类内容）
   - https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/how-generative-ai-can-help-banks-manage-risk-and-compliance
4. **UK Finance / Accenture：金融服务生成式 AI**（客户尽调、输出可靠性、数据隐私、第三方风险）
   - https://www.ukfinance.org.uk/policy-and-guidance/reports-and-publications/generative-ai-action-opportunities-risk-management-financial-services
5. **MIT Sloan：金融 AI 课程大纲**（金融机器学习的特殊挑战、领域知识与模型结合、监管影响）
   - https://mitsloan.mit.edu/sites/default/files/inline-files/2025JA_15.S52_AI%20in%20Finance_Syllabus.pdf

阅读方法：每份材料只抓 3 个观点（用例 / 风险 / 落地方式），不求读完。

## 建议产出

本周结束时，GitHub 上应至少新增或更新以下内容：

- `08-reading-notes/`：1 篇阅读笔记，记录一句话总结、3 个核心观点、与反洗钱业务的连接、需要验证的疑点。
- `04-banking-use-cases/`：1 个用例卡片，主题为“交易监测预警的可疑交易报告草拟与解释”，包含业务痛点、AI 能做什么、数据需求、评估方式、人工复核点。
- `05-risk-governance-compliance/`：在 `ai-risk-checklist.md` 追加一组“AML 场景大模型风险清单”（幻觉、可解释、误报漏报、数据隐私、第三方模型、审计留痕）。
- 在本文件顶部的复盘模板中回填本周主线与一句话复盘。

安全提醒：全程只用公开材料与模拟/脱敏示例，不使用任何真实客户数据、内部银行资料、账号或密钥。

## 每天行动清单（2026-07-13 至 2026-07-19）

- **周一（07-13）选题日 · 约 30 分钟**：在本文件写下本周主题“反洗钱与交易监测中的生成式 AI”、为什么选它、本周完成标准，确认只保留这一个主线问题。
- **周二（07-14）输入日 · 约 45 分钟**：从上面推荐阅读中选 1 份（建议先读 UK Finance 或 McKinsey），阅读 30–45 分钟，用阅读笔记模板抓住 3 个核心观点。
- **周三（07-15）业务连接日 · 约 30 分钟**：回答 5 个问题——交易监测在银行哪个部门/流程出现、过去人工怎么做、当前痛点、AI 能增强哪一步、最大风险是什么；把结论写入 `04-banking-use-cases/`。
- **周四（07-16）AI 方案日 · 约 45 分钟**：把“可疑交易报告草拟与解释”翻译成 AI 用例——明确输入（交易记录、客户信息、预警规则命中）、输出（摘要 / 解释 / 报告草稿）、所需能力（检索增强生成 + 大模型摘要）、评估方式（误报率、人工节省时间、可解释性）、人工复核放在提交监管前。
- **周五（07-17）沉淀日 · 约 45 分钟**：结合 NIST 四步和巴塞尔操作风险视角，在 `05-risk-governance-compliance/ai-risk-checklist.md` 追加 AML 风险清单；关闭或更新一个 Issue；在本文件写本周复盘。
- **周六（07-18）轻实验/轻输出日 · 可选，约 30–45 分钟**：用模拟（非真实）交易样本，写一段“可疑交易解释”提示词，并让 AI 生成一份报告草稿，记录效果与问题；或写 300–800 字小观点。
- **周日（07-19）回顾日 · 约 15 分钟**：只看本文件，写一句话“本周真正学到什么”，并决定下周是继续深挖 AML，还是切换到客户尽调（KYC）主题。

