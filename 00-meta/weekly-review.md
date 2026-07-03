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

## 2026-W28 周计划（2026-07-06 至 2026-07-12）

### 本周建议主题

**检索增强生成（RAG）在银行合规与制度问答中的应用**

选题理由：

1. 项目路线图当前处于"AI 基础能力"阶段（第 5-8 周），检索增强生成是核心能力之一。
2. 银行合规制度问答是 RAG 在金融领域最典型、最易落地的场景——银行内部制度文件量大、更新快、查阅频繁，员工需要快速准确地找到相关条款。
3. 本主题同时覆盖技术层（RAG 架构、向量检索、大模型问答）和治理层（幻觉风险、数据安全、审计留痕），符合项目"四层闭环"要求。
4. 公开资料丰富：NIST AI 风险管理框架、BIS/Basel 数字金融报告、McKinsey 合规 AI 文章均有直接相关内容。

### 推荐阅读

| 序号 | 来源 | 标题/链接 | 阅读重点 |
|------|------|-----------|----------|
| 1 | NIST | [AI 风险管理框架 — 生成式 AI 补充](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | 生成式 AI 风险分类、幻觉与可靠性评估方法 |
| 2 | BIS/Basel | [数字化与银行风险](https://www.bis.org/bcbs/publ/d575.htm) | 第三方技术服务风险、操作风险中的 AI 因素 |
| 3 | McKinsey | [生成式 AI 帮助银行管理风险与合规](https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/how-generative-ai-can-help-banks-manage-risk-and-compliance) | 合规场景用例、风险管控框架、组织落地方式 |
| 4 | McKinsey | [金融机构改善生成式 AI 治理](https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/how-financial-institutions-can-improve-their-governance-of-gen-ai) | 模型治理、人工复核机制、审批流程 |
| 5 | UK Finance | [金融服务生成式 AI 实践](https://www.ukfinance.org.uk/policy-and-guidance/reports-and-publications/generative-ai-action-opportunities-risk-management-financial-services) | 客户尽调、合规问答、输出可靠性、数据隐私 |
| 6 | MIT Sloan | [AI in Finance 课程大纲](https://mitsloan.mit.edu/sites/default/files/inline-files/2025JA_15.S52_AI%20in%20Finance_Syllabus.pdf) | 领域知识与模型结合、AI 系统在金融中的特殊挑战 |

### 建议产出

1. **阅读笔记 1 篇**：选择上述 1-2 篇材料，按 `08-reading-notes/reading-note-template.md` 格式记录核心观点、银行业务连接、存疑点。
2. **银行用例卡片 1 张**：在 `04-banking-use-cases/` 新增"银行合规制度 RAG 问答助手"用例，包含业务痛点、AI 能力匹配、数据需求、风险。
3. **RAG 技术拆解笔记 1 篇**：在 `03-financial-ai-topics/` 记录 RAG 架构要点（文档切分、向量嵌入、检索策略、大模型生成、人工复核），结合银行制度场景。
4. **风险治理清单更新**：在 `05-risk-governance-compliance/ai-risk-checklist.md` 补充 RAG 场景的特有风险（幻觉引用、过时制度、权限泄漏、审计留痕）。

### 每天行动清单

#### 周一（7 月 6 日）— 选题与定义日（30 分钟）

- [ ] 确认本周主题：检索增强生成（RAG）在银行合规制度问答中的应用
- [ ] 在 `weekly-review.md` 写下选题动机和本周完成标准
- [ ] 快速浏览 NIST 生成式 AI 补充文档目录，标记本周要精读的章节

#### 周二（7 月 7 日）— 输入日（45 分钟）

- [ ] 精读 McKinsey 合规 AI 文章（推荐阅读第 3 篇），重点摘录：
  - 银行合规场景中 RAG 的 3 个典型用例
  - 生成式 AI 在合规领域的风险提醒
  - 组织落地时的关键障碍
- [ ] 用阅读笔记模板记录到 `08-reading-notes/`

#### 周三（7 月 8 日）— 业务连接日（30 分钟）

- [ ] 回答 5 个银行业务连接问题：
  1. 银行合规制度问答目前在哪些部门使用？（合规部、风控部、运营部、前台业务人员）
  2. 过去人工怎么查制度？（翻阅 PDF、搜索内网、问合规专员）
  3. 当前痛点是什么？（制度分散、版本混乱、回答不一致、耗时长）
  4. RAG 能增强哪一步？（自动检索相关条款 → 生成结构化回答 → 标注来源）
  5. 最大风险是什么？（幻觉引用错误制度、过时版本、权限越界、缺少审计留痕）
- [ ] 将用例写入 `04-banking-use-cases/`

#### 周四（7 月 9 日）— AI 方案日（45 分钟）

- [ ] 撰写 RAG 技术拆解笔记，回答：
  - 输入：员工自然语言提问 + 银行制度文档库
  - 输出：结构化回答 + 引用来源段落 + 置信度标记
  - AI 能力：文档切分 → 向量嵌入 → 相似度检索 → 大模型生成 → 人工复核
  - 评估指标：引用准确率、回答覆盖率、幻觉率、人工节省时间
  - 人工复核节点：高风险问答需合规专员二次确认
- [ ] 保存到 `03-financial-ai-topics/`

#### 周五（7 月 10 日）— 沉淀日（30 分钟）

- [ ] 更新 `05-risk-governance-compliance/ai-risk-checklist.md`，补充 RAG 场景风险：
  - 幻觉引用：模型生成的引用段落并非原文
  - 过时制度：向量库未及时更新已废止文件
  - 权限泄漏：不同岗位应看到不同密级的制度
  - 审计留痕：每次问答需记录输入、检索结果、生成输出
- [ ] 在 `weekly-review.md` 写本周复盘
- [ ] 关闭或更新相关 Issue

#### 周六（7 月 11 日）— 轻实验日（可选，30 分钟）

- [ ] 设计一个 RAG 合规问答的提示词模板（不需要真实数据，用模拟制度条款即可）
- [ ] 记录提示词设计思路和期望输出格式到 `07-labs/`

#### 周日（7 月 12 日）— 回顾日（10 分钟）

- [ ] 回顾本周学到什么，写一句话复盘
- [ ] 决定下周是否继续 RAG 深入（如：RAG 评估方法、向量数据库选型）还是切换新主题
