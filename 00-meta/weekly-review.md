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

# 下周建议主题（2026-08-17 至 2026-08-23）

## 1. 本周建议主题

**用 NIST AI 风险管理框架，给银行大模型用例做一次治理体检。**

选它的三个理由：

1. 仓库里 `04-banking-use-cases/` 和 `11-open-source-finance-ai-projects/` 已经积累了不少「能做什么」的素材，但 `05-risk-governance-compliance/` 只有一份通用清单，缺少「能不能上线、谁签字、怎么监控」这一层。
2. 治理视角是 18 年银行经验最容易形成差异化的地方：模型风险管理、人工复核、审计留痕、第三方与外包风险，本来就是银行的既有语言。
3. 治理框架是可复用资产。用例会过时，评估清单可以套用在之后每一个用例上。

本周完成标准（一句话）：能用一页清单，对任意一个银行大模型用例给出「可上线 / 需整改 / 不建议做」的结论，并说明依据。

## 2. 推荐阅读（全部公开来源）

按优先级，本周只需读完前两项，其余作为补充：

1. NIST AI 风险管理框架总览（治理、映射、度量、管理四个职能）
   - https://www.nist.gov/itl/ai-risk-management-framework
2. NIST 生成式 AI 专项配套文件（生成式 AI 的特有风险与缓解措施）
   - https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
3. UK Finance：金融服务生成式 AI 的机会与风险管理（投诉处理、客户尽调、输出可靠性、第三方风险）
   - https://www.ukfinance.org.uk/policy-and-guidance/reports-and-publications/generative-ai-action-opportunities-risk-management-financial-services
4. McKinsey：金融机构如何治理生成式 AI
   - https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/how-financial-institutions-can-improve-their-governance-of-gen-ai
5. 巴塞尔委员会 / 国际清算银行：数字化对银行与监管的影响，重点看第三方科技服务与操作风险
   - https://www.bis.org/bcbs/publ/d575.htm
6. MIT Sloan 金融 AI 课程大纲，重点看金融机器学习的特殊挑战与监管影响那几讲
   - https://mitsloan.mit.edu/sites/default/files/inline-files/2025JA_15.S52_AI%20in%20Finance_Syllabus.pdf

阅读方法：不求读完，每份材料只抓三条能写进清单的可执行要求。

## 3. 建议产出（3 个文件，都可以只写一页）

1. `05-risk-governance-compliance/genai-use-case-governance-checklist.md`
   银行大模型用例治理评估清单 v1。按 NIST 四职能组织：治理（谁负责、谁签字）、映射（用例边界与影响等级）、度量（评估指标与测试方法）、管理（上线条件、监控、退役）。每条都给「证据要求」，例如「留存 100 条人工复核样本」。
2. `08-reading-notes/2026-08-nist-ai-rmf-genai-note.md`
   阅读笔记：一句话总结 + 3 个核心观点 + 与银行现有模型风险管理制度的异同 + 我不同意或需要验证的地方。
3. `04-banking-use-cases/` 里选一个已有用例（建议投诉处理或制度问答），用新清单做一次实测，把结论写在用例文件末尾：可上线 / 需整改 / 不建议做，以及卡在哪一条。

安全底线：全部使用公开资料和虚构示例，不写入任何真实客户数据、内部制度原文、系统截图、账号或密钥。

## 4. 每天行动清单

### 周一（8/17）选题日，30 分钟

- 在本文件顶部的周复盘模板里填写「时间范围」和「本周主线」。
- 写下本周完成标准，以及你想用清单检验的那个用例名称。
- 只做决定，不开始读材料。

### 周二（8/18）输入日，45 分钟

- 读推荐阅读第 1 项，只看四个职能的定义和分类结构。
- 建立 `08-reading-notes/2026-08-nist-ai-rmf-genai-note.md`，先写一句话总结和 3 个核心观点。

### 周三（8/19）业务连接日，45 分钟

- 读推荐阅读第 2 项，抓出生成式 AI 特有风险（幻觉、提示注入、信息泄露、内容溯源、供应链）。
- 回答：这五类风险在银行现有的哪些制度里已经有对应控制？哪些完全没有对应？
- 把答案补进阅读笔记的「与银行制度异同」一节。

### 周四（8/20）方案日，60 分钟

- 读推荐阅读第 3 项（UK Finance），补充金融行业的具体控制动作。
- 起草 `05-risk-governance-compliance/genai-use-case-governance-checklist.md`，四个职能每个 5–8 条，每条附证据要求。

### 周五（8/21）沉淀日，45 分钟

- 用清单实测一个已有用例，写出结论和卡点。
- 提交一次 GitHub 更新（网页端编辑即可），并填写本周复盘。

### 周六（8/22）轻输出日，可选 60 分钟

- 写一篇 500–800 字短文：《银行现成的模型风险管理制度，哪些能直接管住大模型，哪些管不住》，放进 `09-career-and-output/`。
- 或者做一个轻实验：让大模型自评一个用例是否满足清单，记录它漏掉了哪几条。

### 周日（8/23）回顾日，15 分钟

- 只看本文件，写一句话复盘。
- 决定下周是继续深化治理（例如第三方模型风险、上线后监控指标），还是切回业务用例。

## 5. 下周结束时应该能回答

1. NIST 的四个职能分别在银行内部对应哪个部门？
2. 生成式 AI 有哪几类风险是银行现有制度覆盖不到的？
3. 我的清单里，哪一条最容易让一个用例被否掉？
4. 这份清单能不能直接拿去和风险、合规、科技部门讨论？
