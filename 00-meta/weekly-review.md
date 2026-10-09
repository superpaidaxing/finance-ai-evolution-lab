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

## 2026 年第 42 周建议计划（2026-10-12 至 2026-10-18）

> 本段由每周学习助理生成。所有材料均来自公开来源，练习只使用自编模拟数据，不涉及任何真实客户数据、内部银行资料、账号密钥或敏感信息。

### 本周建议主题

**主题：银行大模型应用的上线前评估与测试——如何衡量幻觉、准确性与稳健性。**

核心问题只有一个：**一个银行大模型应用（以“制度问答助手”为例），要通过哪些测试、达到什么指标，才有资格上线？**

### 为什么选它

- 前几周已覆盖 NIST AI 风险管理框架、反洗钱、检索增强生成（RAG）、投诉处理、信贷、第三方风险、模型风险与人工复核、上线后监控和智能体，但“上线前怎么测、用什么指标判断够不够好”一直是空白：上线后监控需要基线，人工复核需要知道模型在哪些问题上容易错，这些都依赖上线前评估。
- 路线图正在从第 2 阶段“场景深挖期”进入第 3 阶段“实验验证期”，目标是从“知道”进入“能验证”。评估方法是所有实验（制度问答助手、投诉摘要、可疑交易解释模板）的共同前提，学一次可以反复复用。
- 第 4 阶段治理框架期明确列出“幻觉与可靠性”，NIST AI RMF 的“度量（Measure）”职能和 UK Finance 报告都把“输出准确性”列为金融业生成式 AI 的头号风险之一，公开材料充足。
- 对银行从业者而言，最有价值的不是写评估代码，而是能判断：**哪些错误是可以容忍的、哪些错误是一票否决的**——这正是业务经验的优势。

### 本周完成标准

- 产出 1 篇阅读笔记、1 份“上线前评估检查表”、1 份自编测试题集与评分表（20 题即可）、1 段周复盘。
- 能用自己的话讲清楚 4 个概念：幻觉、事实一致性（有据可依）、稳健性、人工复核的“锚定效应”。

### 推荐阅读（全部为公开来源，按优先级排序）

1. NIST：《AI RMF：生成式 AI 配置文件》（NIST AI 600-1，主读，选读相关章节）
   https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
   重点看：“虚构/幻觉（Confabulation）”“信息完整性”风险条目，以及“度量（Measure）”职能下与测试、评估、验证相关的建议动作。
2. NIST：《AI RMF Playbook》（工具书，查阅“Measure”部分）
   https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook
   重点看：Measure 2.x 中关于测试集代表性、性能指标、稳健性和可解释性的建议，挑 5 条翻译成银行语言。
3. UK Finance / Accenture：《Generative AI in Action: Opportunities & Risk Management in Financial Services》（主读，案例部分）
   https://www.ukfinance.org.uk/policy-and-guidance/reports-and-publications/generative-ai-action-opportunities-risk-management-financial-services
   重点看：报告聚焦的三类风险中的“输出准确性”，以及案例中“工具自动对照原文检查 + 人工质检”的双重校验方式。
4. McKinsey：《Capturing the full value of generative AI in banking》（选读）
   https://www.mckinsey.com/industries/financial-services/our-insights/capturing-the-full-value-of-generative-ai-in-banking
   重点看：银行如何用专家验证、自动化校验方法和操作手册来控制幻觉，以及“专家复核难以规模化”的问题。
5. MIT Sloan：《To help improve the accuracy of generative AI, add speed bumps》（短文，约 15 分钟）
   https://mitsloan.mit.edu/ideas-made-to-matter/to-help-improve-accuracy-generative-ai-add-speed-bumps
   重点看：人工复核者容易“锚定”在 AI 输出上、高估自己的纠错能力；以及通过“减速带”设计提示复核者核查的思路。
6. NIST：ARIA（Assessing Risks and Impacts of AI）项目介绍（选读）
   https://www.nist.gov/news-events/news/2024/05/nist-launches-aria-new-program-advance-sociotechnical-testing-and
   重点看：模型测试、红队测试、现场测试三个层级的区别——对应银行的“单元测试、对抗测试、试点运行”。
7. BIS FSI Papers No 24：《Managing explanations: how regulators can address AI explainability》（选读）
   https://www.bis.org/fsi/fsipapers24.htm
   重点看：监管者对可解释性的期望如何影响评估设计，例如是否要求答案附带引用依据。

### 建议产出

- `08-reading-notes/`：新增《NIST AI 600-1 与 UK Finance 报告：生成式 AI 输出准确性怎么评估》阅读笔记（使用 `reading-note-template.md`）。
- `05-risk-governance-compliance/`：新增《银行大模型应用上线前评估检查表》，至少包含：测试集是否覆盖高风险问题、幻觉率与引用正确率阈值、拒答是否得当、对抗/诱导提问测试、一票否决错误类型、评估结果的审批与留档。
- `07-labs/`：使用 `experiment-template.md` 记录一次小实验——用**自编**的 20 道制度问答测试题（含 5 道“资料里没有答案”的题、5 道诱导性提问），给出评分表：正确 / 部分正确 / 幻觉 / 应拒答未拒答。
- 本文件：周日回答周复盘 7 个问题。

### 每天行动清单（每天 30–60 分钟）

- **周一（10/12，选题日，30 分钟）**：在本文件写下本周主题、选题理由和完成标准；凭直觉写下“如果我是审批人，制度问答助手要满足哪 3 个条件才敢上线”，周日再对照修正。
- **周二（10/13，输入日，45 分钟）**：读 NIST AI 600-1 中“虚构/幻觉”和“信息完整性”条目（25 分钟），再读 UK Finance 报告“输出准确性”部分和一个案例（20 分钟）；按模板记录一句话总结、3 个核心观点、与银行业务的连接、需要验证的地方。
- **周三（10/14，业务连接日，45 分钟）**：先读 MIT Sloan 短文（15 分钟）；然后回答 5 个问题：制度问答在哪个部门/流程出现（如分行合规咨询、柜面操作规程查询）？过去人工怎么做？痛点是什么？AI 能增强哪一步？最大风险是什么？再列出 3 类“一票否决”错误（例如：编造不存在的制度条款、给错审批权限或金额阈值、把已废止制度当现行制度）。
- **周四（10/15，AI 方案日，60 分钟）**：把评估翻译成可执行方案：输入（自编问题 + 公开或自编的制度片段）、输出（答案 + 引用依据）、评估指标（答案正确率、引用正确率、幻觉率、正确拒答率、人工改写率）、测试层级（参考 ARIA：模型测试 / 红队诱导测试 / 小范围试点）、人工复核点（高风险问题必须人工确认、评估结果需二道防线审阅）；浏览 NIST AI RMF Playbook 的 Measure 部分，挑 5 条写进方案。
- **周五（10/16，沉淀日，45 分钟）**：把周三、周四内容整理成《银行大模型应用上线前评估检查表》，放入 `05-risk-governance-compliance/`；提交 GitHub 更新，关闭或更新一个相关 Issue。
- **周六（10/17，轻实验日，可选，45–60 分钟）**：自编 3–5 段模拟制度条款和 20 道测试题，让大语言模型作答并要求给出引用；按评分表逐题打分，统计幻觉率和正确拒答率；特别记录“看起来很专业但其实是编的”答案，写入 `07-labs/`。
- **周日（10/18，回顾日，20 分钟）**：只看本文件，回答周复盘 7 个问题；修正周一写的“3 个上线条件”；写一句话“本周真正学到什么”；决定下周继续深入（例如用评估结果设计人工复核抽样规则）还是换题（例如客户身份识别与尽调、管理驾驶舱）。

### 风险与治理提醒

- 全程只使用公开报告和自编模拟数据，不使用任何真实客户数据、内部制度原文、系统账号或密钥。
- 评估集要包含“资料中没有答案”的问题：银行场景中“不知道就说不知道”比“答得流畅”更重要。
- 平均正确率高不代表能上线：一票否决类错误要单独统计，出现即不通过。
- 人工复核不是万能的：复核者容易锚定 AI 输出，需要通过引用对照、高亮待核实内容、抽样复核等机制降低漏检。
- 评估结果、测试集版本、模型版本和审批意见要留档，作为上线后监控的基线和审计依据。
