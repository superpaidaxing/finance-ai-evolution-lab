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

# 2026 年第 27 周计划（6 月 29 日 – 7 月 5 日）

## 建议主题

**银行场景中的检索增强生成（RAG）：从制度问答到合规辅助**

### 为什么选这个主题

1. 检索增强生成（Retrieval-Augmented Generation，RAG）是当前大语言模型在银行落地最具可行性的技术路径之一。它通过外挂知识库降低幻觉、提高回答可追溯性，天然适配银行对准确性和可审计性的高要求。
2. 项目路线图第 5–8 周建议聚焦 AI 基础能力（提示词、RAG、分类/摘要、智能体），本周进入 RAG 专题正好契合节奏。
3. 前期已积累 155 个银行 AI 用例和 7 批开源项目库，可以在此基础上深入一项关键技术，形成"用例 → 技术 → 治理"的闭环。
4. 多个公开权威来源（NIST、BIS、McKinsey、UK Finance）对大模型可靠性和知识检索风险有专门讨论，可以直接引用。

### 完成标准

- 形成 1 篇 RAG 在银行场景中的阅读笔记（`08-reading-notes/`）。
- 拆解 1 个 RAG 银行用例（如制度问答或合规辅助），记录到 `04-banking-use-cases/`。
- 在 `05-risk-governance-compliance/` 补充 RAG 应用的风险治理要点。
- 周五在本文件完成复盘。

---

## 推荐阅读

### 监管与治理（第一优先级）

| 序号 | 来源 | 标题/内容 | 链接 |
|------|------|-----------|------|
| 1 | NIST | AI 风险管理框架：生成式 AI 概况（Profile），重点关注"信息完整性"和"幻觉"相关条目 | https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence |
| 2 | BIS | 数字化与金融服务中的 AI——巴塞尔委员会对操作风险和第三方依赖的讨论 | https://www.bis.org/bcbs/publ/d575.htm |
| 3 | BIS | 金融领域的生成式 AI 工作论文 | https://www.bis.org/publ/work1194.htm |

### 行业报告（第二优先级）

| 序号 | 来源 | 标题/内容 | 链接 |
|------|------|-----------|------|
| 4 | McKinsey | 生成式 AI 如何帮助银行管理风险与合规 | https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/how-generative-ai-can-help-banks-manage-risk-and-compliance |
| 5 | McKinsey | 金融机构如何改善生成式 AI 治理 | https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/how-financial-institutions-can-improve-their-governance-of-gen-ai |
| 6 | UK Finance | 金融服务中的生成式 AI：机遇与风险管理 | https://www.ukfinance.org.uk/policy-and-guidance/reports-and-publications/generative-ai-action-opportunities-risk-management-financial-services |

### 技术参考（第三优先级，按需查阅）

| 序号 | 来源 | 内容 | 用途 |
|------|------|------|------|
| 7 | LangChain 文档 | RAG 架构与检索链设计 | 理解 RAG 技术实现 |
| 8 | LlamaIndex 文档 | 文档索引与检索管道 | 对比不同 RAG 框架 |
| 9 | MIT Sloan 课程大纲 | AI in Finance 课程中关于领域知识与模型结合的章节 | https://mitsloan.mit.edu/sites/default/files/inline-files/2025JA_15.S52_AI%20in%20Finance_Syllabus.pdf |

---

## 建议产出

| 产出 | 存放路径 | 说明 |
|------|----------|------|
| RAG 银行应用阅读笔记 | `08-reading-notes/rag-in-banking-reading-note.md` | 从推荐阅读中提取 3 个核心观点，连接银行场景 |
| RAG 银行用例拆解 | `04-banking-use-cases/rag-policy-qa-use-case.md` | 拆解"银行制度/合规文档 RAG 问答"用例，包含业务流程、数据需求、AI 能力、风险治理 |
| RAG 风险治理要点 | `05-risk-governance-compliance/rag-risk-governance.md` | RAG 在银行应用中的幻觉风险、数据安全、检索准确性、人工复核机制 |
| 周复盘 | `00-meta/weekly-review.md`（本文件） | 回答每周 7 个固定问题 |

---

## 每天行动清单

### 周一（6 月 29 日）：选题与定义

- **时间**：30–45 分钟
- **行动**：
  1. 阅读本计划，确认本周主题为"银行场景中的 RAG 应用与风险治理"。
  2. 在 `00-meta/weekly-review.md` 填写本周主题、选题原因和完成标准（可直接使用上方内容）。
  3. 浏览推荐阅读列表，选择周二要精读的 1 篇材料（建议从 McKinsey #4 或 NIST #1 开始）。
- **完成标志**：确定本周唯一主线问题，不贪多。

### 周二（6 月 30 日）：输入与阅读

- **时间**：30–45 分钟
- **行动**：
  1. 精读选定的 1 篇材料（建议 McKinsey 的"生成式 AI 如何帮助银行管理风险与合规"）。
  2. 用 `08-reading-notes/reading-note-template.md` 模板记录：
     - 一句话总结
     - 3 个核心观点（重点关注 RAG 在风险合规中的应用描述）
     - 与银行业务的连接（哪些部门/流程能用 RAG）
     - 需要验证或不同意的地方
  3. 保存为 `08-reading-notes/rag-in-banking-reading-note.md`。
- **完成标志**：形成 1 篇短阅读笔记。

### 周三（7 月 1 日）：业务连接

- **时间**：30–45 分钟
- **行动**：
  1. 回答 5 个业务连接问题（聚焦 RAG）：
     - RAG 在银行哪些部门/流程中出现？（合规部、法务部、运营部、客服中心）
     - 过去人工怎么做制度查询和合规问答？（人工翻制度文件、电话咨询法规部）
     - 当前痛点？（制度文件多、更新频繁、员工找不到最新版本、答复不一致）
     - RAG 能增强哪一步？（自动检索最新制度、生成引用原文的回答、减少人工查询）
     - 最大风险？（检索不准导致引用错误条款、幻觉导致编造不存在的制度、缺乏审计留痕）
  2. 将以上内容整理为用例卡片，保存到 `04-banking-use-cases/rag-policy-qa-use-case.md`。
- **完成标志**：1 个银行 RAG 用例拆解完成。

### 周四（7 月 2 日）：AI 方案与治理

- **时间**：30–60 分钟
- **行动**：
  1. 把 RAG 制度问答用例翻译成 AI 方案：
     - 输入：银行内部制度文档（PDF/Word）、员工自然语言提问
     - 输出：带原文引用的回答、相关条款摘要、置信度评分
     - AI 能力：文档向量化 + 语义检索 + 大语言模型生成
     - 评估指标：检索准确率、回答正确率、引用命中率、人工复核率
     - 人工复核：高风险问题（涉及监管红线）必须人工审核
  2. 补充 RAG 风险治理要点到 `05-risk-governance-compliance/rag-risk-governance.md`：
     - 幻觉风险：模型可能编造不存在的制度条款
     - 检索偏差：向量检索可能遗漏关键文档或返回过时版本
     - 数据安全：制度文档可能含敏感信息，向量数据库需要访问控制
     - 可解释性：回答必须标注来源文档和段落
     - 人工复核机制：何时触发升级、如何记录复核结果
- **完成标志**：1 个 AI 方案草案 + 1 份风险治理要点。

### 周五（7 月 3 日）：沉淀与复盘

- **时间**：30–45 分钟
- **行动**：
  1. 检查本周产出文件，确保格式规范、内容完整。
  2. 在 `00-meta/weekly-review.md` 完成本周复盘，回答 7 个固定问题：
     - 本周主题是什么？
     - 我读了什么？
     - 它和银行业务有什么关系？
     - AI 可以做什么？
     - 风险和合规问题是什么？
     - 我沉淀了哪个文件？
     - 下周继续还是换题？
  3. 关闭或更新相关 Issue。
- **完成标志**：GitHub 有一次提交，复盘完成。

### 周六（7 月 4 日）：轻实验（可选）

- **时间**：30–60 分钟（可选）
- **行动**（任选 1 项）：
  1. 用公开的银行年报或监管文件，设计一组 RAG 提示词模板（如"请根据以下文档回答问题，必须引用原文段落"）。
  2. 画一张简单的 RAG 银行制度问答系统架构图（文档 → 分块 → 向量化 → 检索 → 生成 → 人工复核）。
  3. 浏览 LangChain 或 LlamaIndex 文档，记录 RAG 关键组件和银行场景适配要点。
- **完成标志**：不追求完美，只记录过程和问题。

### 周日（7 月 5 日）：休息与回顾

- **时间**：10–15 分钟
- **行动**：
  1. 回顾 `weekly-review.md`，写一句话：本周真正学到什么？
  2. 决定下周是否继续深入 RAG（如扩展到反洗钱 RAG、客户服务 RAG），还是切换到新主题（如智能体 Agent 在银行中的应用）。
- **完成标志**：不内耗，不重启计划，只做微调。

---

## 下周主题预告（供周日决策参考）

- **选项 A**：继续深入 RAG——扩展到反洗钱交易监测 RAG、客户服务 RAG、财报分析 RAG。
- **选项 B**：切换到智能体（Agent）——银行场景中的多步骤自动化工作流，如信贷审批辅助、客户尽调自动化。
- **选项 C**：切换到 AI 评估体系——如何评估银行 AI 系统的准确率、召回率、幻觉率、可解释性。
