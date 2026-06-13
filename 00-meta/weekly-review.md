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

# 2026-05-18 ~ 2026-05-24 周计划

## 本周建议主题

**银行反洗钱与客户尽调（AML/KYC）中的 AI 应用**

### 为什么选这个主题

1. 反洗钱与客户尽调是银行合规的核心领域，监管要求高、人工成本大、误报率高，是 AI 落地的高价值场景。
2. 大语言模型可以在可疑交易解释、客户风险画像、尽调文档审阅、监管报告生成等环节大幅提升效率。
3. 该主题覆盖项目四层闭环——概念层（AML/KYC 定义）、业务层（银行真实流程）、技术层（自然语言处理、知识图谱、大语言模型）、治理层（合规红线、模型风险、可解释性）。
4. 公开来源丰富，BIS/Basel、NIST、McKinsey、UK Finance 均有相关材料。

### 本周完成标准

- 完成 1 篇 AML/KYC + AI 主题的阅读笔记。
- 拆解至少 1 个银行反洗钱 AI 应用场景。
- 形成 1 份 AML AI 用例草案（输入、输出、评估、风险）。
- 在 `weekly-review.md` 写下本周复盘。

## 推荐阅读

### 第一优先级：监管与治理框架

| 来源 | 材料 | 链接 |
|------|------|------|
| BIS/Basel | *Sound management of risks related to money laundering and financing of terrorism* | https://www.bis.org/bcbs/publ/d545.htm |
| BIS | *Newsletter on digital fraud and banking* | https://www.bis.org/publ/bcbs_nl36.htm |
| NIST | *AI Risk Management Framework (AI RMF 1.0)* | https://www.nist.gov/itl/ai-risk-management-framework |
| NIST | *AI RMF Generative AI Profile* | https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence |

### 第二优先级：行业报告

| 来源 | 材料 | 链接 |
|------|------|------|
| McKinsey | *How generative AI can help banks manage risk and compliance* | https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/how-generative-ai-can-help-banks-manage-risk-and-compliance |
| McKinsey | *How financial institutions can improve their governance of gen AI* | https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/how-financial-institutions-can-improve-their-governance-of-gen-ai |
| UK Finance | *Generative AI in action: opportunities, risk management, financial services* | https://www.ukfinance.org.uk/policy-and-guidance/reports-and-publications/generative-ai-action-opportunities-risk-management-financial-services |

### 第三优先级：课程与学术

| 来源 | 材料 | 链接 |
|------|------|------|
| MIT Sloan | *AI in Finance* 课程大纲（含 AI 风控、合规章节） | https://mitsloan.mit.edu/sites/default/files/inline-files/2025JA_15.S52_AI%20in%20Finance_Syllabus.pdf |
| arXiv/SSRN | 关键词：`anti-money laundering machine learning`、`LLM KYC compliance` | https://arxiv.org/ |

## 建议产出

| 产出类型 | 保存位置 | 说明 |
|----------|----------|------|
| 阅读笔记 | `08-reading-notes/2026-05-aml-kyc-ai-reading-note.md` | 选 1 篇推荐材料，用阅读笔记模板记录 |
| 银行用例拆解 | `04-banking-use-cases/aml-kyc-ai-use-case.md` | 拆解 1 个 AML/KYC 场景的 AI 应用 |
| AI 用例草案 | `03-financial-ai-topics/aml-kyc-llm-application.md` | 写清输入、输出、AI 能力、评估、风险 |
| 风险治理清单 | `05-risk-governance-compliance/aml-ai-risk-checklist.md` | 列出 AML AI 落地的合规与风险要点 |
| 周复盘 | `00-meta/weekly-review.md` | 回答每周 7 个问题 |

## 每天行动清单

### 周一（5 月 18 日）：选题日

- [ ] 确认本周主题：银行反洗钱与客户尽调中的 AI 应用。
- [ ] 阅读本计划，明确本周完成标准。
- [ ] 在 GitHub Project 或 Issue 中标记本周主线。
- [ ] 快速浏览 McKinsey 报告目录，了解 AML + 生成式 AI 的框架。

### 周二（5 月 19 日）：输入日

- [ ] 精读 McKinsey《How generative AI can help banks manage risk and compliance》中与 AML 相关的章节（30-45 分钟）。
- [ ] 用 `08-reading-notes/reading-note-template.md` 模板记录：
  - 一句话总结
  - 3 个核心观点
  - 和银行反洗钱业务的连接
  - 需要验证的地方
- [ ] 保存为 `08-reading-notes/2026-05-aml-kyc-ai-reading-note.md`。

### 周三（5 月 20 日）：业务连接日

- [ ] 回答 5 个问题，把 AML/KYC 连接到你的银行经验：
  1. 反洗钱在银行哪个部门/流程里出现？
  2. 过去人工怎么做客户尽调和可疑交易甄别？
  3. 当前痛点是什么（误报率高？人工复核慢？制度更新跟不上？）
  4. AI 能增强哪一步（交易监测、客户风险评分、尽调文档审阅、可疑行为解释）？
  5. 最大风险是什么（漏报、模型偏见、不可解释、监管不认可）？
- [ ] 保存到 `04-banking-use-cases/aml-kyc-ai-use-case.md`。

### 周四（5 月 21 日）：AI 方案日

- [ ] 把 AML/KYC 业务问题翻译成 AI 问题：
  1. 输入：交易流水、客户资料、制度文本、历史可疑报告。
  2. 输出：可疑交易标记、风险评分、尽调摘要、监管报告草稿。
  3. AI 能力：自然语言处理、分类模型、大语言模型摘要、检索增强生成。
  4. 评估：误报率下降比例、人工复核时间节省、合规可解释性。
  5. 人工复核放在哪里：最终可疑报告提交前必须人工审核。
- [ ] 保存到 `03-financial-ai-topics/aml-kyc-llm-application.md`。

### 周五（5 月 22 日）：沉淀日

- [ ] 整理 AML AI 落地的风险与治理要点，保存到 `05-risk-governance-compliance/aml-ai-risk-checklist.md`。
- [ ] 在 `00-meta/weekly-review.md` 写本周复盘，回答 7 个问题。
- [ ] 关闭或更新 1 个相关 Issue。

### 周六（5 月 23 日）：轻实验日（可选）

- [ ] 用大语言模型设计一组 AML 场景提示词，例如：
  - "请根据以下交易记录，判断是否存在可疑洗钱行为并给出理由。"
  - "请将以下客户尽调材料摘要为结构化风险评估报告。"
- [ ] 用公开模拟数据测试提示词效果，记录到 `07-labs/`。

### 周日（5 月 24 日）：回顾日

- [ ] 回看 `weekly-review.md`，写一句话总结本周收获。
- [ ] 决定下周是否继续深入 AML/KYC，还是切换到新主题（如智能客服或信贷审批）。 
