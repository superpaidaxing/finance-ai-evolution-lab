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

# 下周计划：2026-06-22 至 2026-06-28

## 建议主题

**检索增强生成（RAG）在银行合规与知识管理中的应用**

### 为什么选这个主题

1. **路线图对齐**：项目路线图第 1 阶段（基础共识期）明确将"检索增强生成"列为 AI 侧核心能力之一，目前尚未专题展开。
2. **用例库直接支撑**：仓库中已积累的 50+ 真实银行用例中，至少 15 个与 RAG 直接相关：
   - UC-001 Lloyds Athena：13,000 篇内部文章检索，搜索时间从约 59 秒降至约 20 秒
   - UC-006 Bank of America AskGPS：3,200+ 内部文档支持 40,000+ 企业客户服务团队
   - UC-022 Deutsche Bank DB Lumina：研究分析智能体，支持内外部资料检索
   - UC-043 BMO Lumi：8,000+ 政策文档、英法双语生成式问答
   - UC-046 TD 联系中心：RAG + 引用溯源，通话等待时间降低 15%
3. **业务经验连接**：银行合规制度、内部政策、操作手册是典型的 RAG 应用场景——文档量大、更新频繁、准确性要求极高，与 18 年银行从业经验高度匹配。
4. **治理视角突出**：RAG 在金融场景中面临幻觉风险、引用准确性、数据隐私、模型风险管理等治理挑战，适合结合 NIST 和 BIS 框架深入分析。

### 本周完成标准

- 完成 1 篇 RAG 银行应用阅读笔记
- 输出 1 个 RAG 合规问答用例卡片
- 整理 1 份 RAG 银行应用风险清单
- 写 1 篇 500 字阶段性复盘

## 推荐阅读

### 第一优先级：监管与治理框架

| 序号 | 来源 | 标题 / 主题 | 链接 | 阅读重点 |
| --- | --- | --- | --- | --- |
| 1 | NIST | AI 风险管理框架：生成式 AI 特别说明 | https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence | 关注"信息完整性"和"幻觉"相关治理建议，思考对 RAG 系统的约束 |
| 2 | BIS/Basel | 数字化与银行风险 | https://www.bis.org/bcbs/publ/d575.htm | 第三方技术服务风险、操作风险中 AI 依赖的治理 |
| 3 | BIS | AI 与机器学习在金融服务中的应用 | https://www.bis.org/publ/work1194.htm | 金融机构采用 AI 的监管视角与风险考量 |

### 第二优先级：行业报告

| 序号 | 来源 | 标题 / 主题 | 链接 | 阅读重点 |
| --- | --- | --- | --- | --- |
| 4 | McKinsey | 生成式 AI 如何帮助银行管理风险与合规 | https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/how-generative-ai-can-help-banks-manage-risk-and-compliance | RAG 在合规审查、制度问答中的具体应用模式 |
| 5 | McKinsey | 金融机构如何改善生成式 AI 治理 | https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/how-financial-institutions-can-improve-their-governance-of-gen-ai | RAG 系统的模型风险管理框架 |
| 6 | UK Finance | 金融服务中的生成式 AI：机遇与风险管理 | https://www.ukfinance.org.uk/policy-and-guidance/reports-and-publications/generative-ai-action-opportunities-risk-management-financial-services | RAG 在客户尽调、投诉处理中的应用与输出可靠性 |

### 第三优先级：学术与课程

| 序号 | 来源 | 标题 / 主题 | 链接 | 阅读重点 |
| --- | --- | --- | --- | --- |
| 7 | MIT Sloan | AI in Finance 课程大纲 | https://mitsloan.mit.edu/sites/default/files/inline-files/2025JA_15.S52_AI%20in%20Finance_Syllabus.pdf | 领域知识与模型结合、金融机器学习的特殊挑战 |

### 仓库内部参考

- `04-banking-use-cases/2026-latest-bank-ai-use-case-library.md`：重点阅读 UC-001、UC-006、UC-022、UC-043、UC-046 等 RAG 相关用例
- `05-risk-governance-compliance/ai-risk-checklist.md`：现有 AI 风险清单，作为 RAG 风险评估的基础
- `00-meta/source-recommendations.md`：信息来源与优先级参考

## 建议产出

| 产出物 | 存放位置 | 说明 |
| --- | --- | --- |
| RAG 银行应用阅读笔记 | `08-reading-notes/` | 基于推荐阅读材料，记录 RAG 核心概念、银行应用模式、3 个核心观点 |
| RAG 合规知识问答用例卡片 | `04-banking-use-cases/` | 用用例模板拆解"银行合规制度 RAG 问答"场景：业务痛点、AI 方案、数据需求、风险 |
| RAG 银行应用风险清单 | `05-risk-governance-compliance/` | 基于 NIST 和 BIS 框架，列出 RAG 在银行场景中的关键风险点与治理建议 |
| 周复盘 | `00-meta/weekly-review.md` | 500 字阶段性复盘：本周学到什么、与银行经验如何连接、下周是否继续 |

## 每天行动清单

### 周一（6 月 22 日）：选题与定向 ⏱ 30-45 分钟

- [ ] 在 `00-meta/weekly-review.md` 确认本周主题为"RAG 在银行合规与知识管理中的应用"
- [ ] 快速浏览仓库用例库中 5 个 RAG 相关用例（UC-001、UC-006、UC-022、UC-043、UC-046），标记最有启发的 2 个
- [ ] 写下本周学习目标：我希望理解 RAG 在银行中解决什么问题、有什么风险

### 周二（6 月 23 日）：输入日 ⏱ 30-45 分钟

- [ ] 阅读推荐材料第 4 项：McKinsey《生成式 AI 如何帮助银行管理风险与合规》
- [ ] 用 `08-reading-notes/reading-note-template.md` 记录：
  - 一句话总结
  - 3 个核心观点（重点关注 RAG 在合规中的应用模式）
  - 和银行业务的连接
  - 我不同意或需要验证的地方

### 周三（6 月 24 日）：业务连接日 ⏱ 30-45 分钟

- [ ] 回答 5 个业务连接问题：
  1. RAG 合规问答在银行哪个部门/流程里出现？（合规部、法律部、运营部制度查询）
  2. 过去人工怎么做？（人工翻阅制度文件、咨询合规岗位、逐级审批确认）
  3. 当前痛点是什么？（制度文件量大、更新频繁、查找耗时、口径不一致）
  4. RAG 能增强哪一步？（快速检索、精准引用、一致性回答、审计留痕）
  5. 最大风险是什么？（幻觉导致错误合规建议、引用过期制度、缺乏人工复核）
- [ ] 将分析保存到 `04-banking-use-cases/`，形成 RAG 合规问答用例卡片

### 周四（6 月 25 日）：AI 方案与风险日 ⏱ 30-45 分钟

- [ ] 阅读推荐材料第 1 项：NIST AI 风险管理框架（生成式 AI 部分），重点关注与 RAG 相关的风险类别
- [ ] 整理 RAG 银行应用风险清单，包含：
  - 幻觉与事实准确性风险
  - 引用来源可追溯性
  - 数据隐私与内部文档泄露风险
  - 模型更新与知识库版本管理
  - 人工复核机制设计
  - 监管审计留痕要求
- [ ] 保存到 `05-risk-governance-compliance/`

### 周五（6 月 26 日）：沉淀日 ⏱ 30-45 分钟

- [ ] 整理本周阅读笔记，确保格式完整
- [ ] 在 `00-meta/weekly-review.md` 写本周复盘（500 字）
- [ ] 回答 7 个固定问题：本周主题、读了什么、银行关系、AI 能做什么、风险合规、沉淀文件、下周方向
- [ ] 更新一个 GitHub Issue 或关闭一个已完成的 Issue

### 周六（6 月 27 日）：轻实验日（可选）⏱ 30-60 分钟

- [ ] 用公开材料（如 NIST 框架文档）模拟一次 RAG 思路拆解：
  - 定义问题：如何让合规人员快速查到 NIST AI 风险框架中关于"信息完整性"的治理建议？
  - 设计检索策略：文档分块方式、向量化方法、检索排序
  - 设计生成策略：提示词模板、引用格式、幻觉控制
  - 记录过程和问题到 `07-labs/`

### 周日（6 月 28 日）：回顾日 ⏱ 15 分钟

- [ ] 只看 `weekly-review.md`
- [ ] 写一句话：本周真正学到什么？
- [ ] 决定下周是否继续 RAG 主题（建议：如果本周完成度高，下周可转向"RAG 实验验证"或"智能客服与投诉处理"）
