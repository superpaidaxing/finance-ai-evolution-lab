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

# 2026-06-02 ~ 2026-06-08 周计划

## 本周建议主题

**NIST AI 风险管理框架在银行大模型场景中的应用**

### 为什么选这个主题

1. **风险治理是金融 AI 落地的硬门槛**：仓库已积累 40+ 银行 AI 真实用例（`04-banking-use-cases/`），但 `05-risk-governance-compliance/` 目前只有一份基础清单。用例丰富而治理薄弱，说明"能不能做"的问题已回答，"该不该做、怎么管"的问题需要补齐。
2. **NIST AI RMF 是全球公认的治理起点**：它提供了 Govern → Map → Measure → Manage 四步框架，与项目"概念层 → 业务层 → 技术层 → 治理层"的四层闭环天然对齐。
3. **生成式 AI 补充材料已发布**：NIST 于 2024 年发布了 AI 600-1（Generative AI Profile），专门针对大模型的幻觉、数据隐私、版权、偏差等风险，直接适用于银行智能客服、信贷分析、投研助手等场景。
4. **衔接路线图第 1 阶段目标**：roadmap 第 1 阶段要求"补齐 AI 基础，梳理金融 AI 全景"，而 NIST AI RMF 正是从治理视角建立 AI 全景的最佳切入点。

### 四层闭环分析预览

| 层级 | 本周要回答的问题 |
| --- | --- |
| 概念层 | NIST AI RMF 的四大功能（治理、映射、度量、管理）分别做什么？ |
| 业务层 | 银行哪些大模型用例（智能客服、信贷分析、反洗钱解释）受 AI RMF 约束最大？ |
| 技术层 | 幻觉率、可解释性、数据泄露、模型漂移——如何用 NIST 框架量化这些风险？ |
| 治理层 | 银行如何把 AI RMF 嵌入现有的模型风险管理（MRM）和三道防线体系？ |

## 推荐阅读

按优先级排列，每篇建议用时 30–45 分钟。

| 优先级 | 材料 | 来源 | 阅读重点 |
| --- | --- | --- | --- |
| ★★★ | NIST AI Risk Management Framework (AI RMF 1.0) | NIST | 四大功能的定义与子类别；Govern 1–6, Map 1–5, Measure 1–4, Manage 1–4 |
| ★★★ | NIST AI 600-1: Generative AI Profile | NIST | 生成式 AI 12 类独特风险（幻觉、数据隐私、有害内容等）；与 AI RMF 子类别的映射 |
| ★★☆ | McKinsey: How generative AI can help banks manage risk and compliance | McKinsey | 银行风控合规场景中生成式 AI 的 3 个用例方向；组织落地建议 |
| ★★☆ | BIS Working Paper 1194: Generative AI and financial stability | BIS/Basel | 大模型对金融稳定的系统性风险分析；监管者视角 |
| ★☆☆ | UK Finance: Generative AI in Action | UK Finance | 客户投诉处理、客户身份识别场景的风险治理实践 |

参考链接：

- NIST AI RMF 1.0: https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI 600-1 Generative AI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- McKinsey: https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/how-generative-ai-can-help-banks-manage-risk-and-compliance
- BIS WP 1194: https://www.bis.org/publ/work1194.htm
- UK Finance: https://www.ukfinance.org.uk/policy-and-guidance/reports-and-publications/generative-ai-action-opportunities-risk-management-financial-services

## 建议产出

本周结束时，争取完成以下 1–2 项沉淀：

1. **阅读笔记**（`08-reading-notes/`）：一篇关于 NIST AI RMF 1.0 或 AI 600-1 的结构化笔记，使用 `reading-note-template.md` 格式。
2. **风险治理清单更新**（`05-risk-governance-compliance/`）：在现有 `ai-risk-checklist.md` 基础上，新增一份"银行大模型风险治理对照表"，将 NIST AI RMF 的子类别映射到银行三道防线。
3. **用例治理标注**（可选）：从 `04-banking-use-cases/2026-latest-bank-ai-use-case-library.md` 中选 3–5 个用例，标注它们在 NIST AI RMF 四大功能中的主要风险点。

## 每天行动清单

### 周一（6 月 2 日）：选题与框架速览

- [ ] 打开 NIST AI RMF 1.0 官网，快速浏览框架总图（Govern / Map / Measure / Manage）
- [ ] 在 `00-meta/weekly-review.md` 确认本周主题已记录（本文件）
- [ ] 用 30 分钟读 AI RMF 1.0 的前 10 页（摘要 + 框架概览）
- [ ] 写下 3 个问题：这个框架对银行大模型应用意味着什么？

### 周二（6 月 3 日）：深入阅读 NIST AI 600-1

- [ ] 阅读 AI 600-1（Generative AI Profile）中的 12 类独特风险列表
- [ ] 标记与银行场景强相关的风险类别（如幻觉、数据隐私、信息安全）
- [ ] 用 `08-reading-notes/reading-note-template.md` 开始记录：一句话总结、3 个核心观点、与银行业务的连接
- [ ] 完成标准：形成一篇 AI 600-1 阅读笔记草稿

### 周三（6 月 4 日）：银行业务连接

- [ ] 从用例库中选 3 个典型用例（建议：UC-001 Lloyds Athena 客服、UC-014 HSBC 信用分析、UC-011 CBA 反欺诈智能体）
- [ ] 对每个用例回答 5 个问题：哪个部门？人工怎么做？痛点？AI 增强哪一步？最大风险？
- [ ] 将风险部分对照 NIST AI RMF 的 Map 和 Measure 功能，标注主要风险子类别
- [ ] 完成标准：3 个用例各有一段"NIST 风险映射"注释

### 周四（6 月 5 日）：AI 方案与治理融合

- [ ] 阅读 McKinsey 银行生成式 AI 风险合规文章（30 分钟）
- [ ] 思考：银行如何将 NIST AI RMF 嵌入现有的模型风险管理（MRM）和三道防线体系？
- [ ] 起草"银行大模型风险治理对照表"框架：NIST 子类别 → 银行防线归属 → 控制措施建议
- [ ] 完成标准：对照表框架初稿完成

### 周五（6 月 6 日）：沉淀与整理

- [ ] 完善阅读笔记，提交到 `08-reading-notes/`
- [ ] 完善风险治理对照表，提交到 `05-risk-governance-compliance/`
- [ ] 更新 `00-meta/weekly-review.md` 中的"本周完成"和"本周学到的关键认知"
- [ ] 关闭或更新一个相关 Issue
- [ ] 完成标准：GitHub 有至少一次实质性更新

### 周六（6 月 7 日）：轻实验（可选）

- [ ] 尝试用 AI 工具（如 ChatGPT/Claude）模拟一次"银行大模型上线前 NIST AI RMF 合规检查"
- [ ] 设计 5 个检查问题，用于评估一个虚拟的"银行智能客服大模型"是否满足 NIST AI RMF 要求
- [ ] 记录实验过程和发现到 `07-labs/`

### 周日（6 月 8 日）：回顾与微调

- [ ] 回顾 `weekly-review.md`
- [ ] 写一句话：本周真正学到什么？
- [ ] 决定下周是否继续深入 NIST AI RMF，还是切换到 BIS/巴塞尔数字金融材料
