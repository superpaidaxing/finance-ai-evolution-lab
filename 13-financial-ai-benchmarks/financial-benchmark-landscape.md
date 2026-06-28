# 金融模型能力评测体系调研总览

> 结论：已经有一批公开的金融垂类 benchmark，但它们关注点不同。适合银行从业者的路线不是只选一个榜单，而是组合“金融知识 + 文档证据问答 + 数值计算 + 合规风险 + 工具调用 + RAG/检索 + Agent 工作流”。

## 1. 公开评测体系总览

| 名称 | 语言 | 核心评测对象 | 典型任务 | 适合学习的问题 | 本仓库下载位置 |
| --- | --- | --- | --- | --- | --- |
| FinanceBench | 英文 | LLM 对上市公司财报/SEC 文件的开放书问答 | 财报问答、证据定位、拒答 | 如何设计带证据的财务问答题；如何衡量 RAG 幻觉 | `upstream-snapshots/financebench/` |
| FinEval | 中文 | 中文金融大模型综合能力 | 金融学术知识、行业知识、安全、Agent、多模态、严谨性 | 中文金融专业能力如何分层评测 | `upstream-snapshots/fineval/` |
| CFLUE | 中文 | 中文金融语言理解 | 金融知识考试题、金融应用任务 | 中文金融知识与应用题如何组织成 benchmark | `upstream-snapshots/cflue/` |
| OpenFinData | 中文 | 真实产业金融场景大模型评测 | 金融术语、事实、判别、计算、研报/基金/行情分析、合规 | 如何把产业金融任务拆成可评测 JSON 数据 | `release-downloads/openfindata_release/` |
| PIXIU / FLARE | 英文为主 | 金融 LLM、指令数据和多任务评测 | 情感、标题、NER、关系抽取、QA、预测 | 金融 LLM 评测代码如何组织；任务如何统一接口 | `upstream-snapshots/pixiu/` |
| FinBen | 多语种/英文为主 | 综合金融 LLM benchmark | 信息抽取、风险、预测、决策、QA、Greek Plutus 等 | 如何用任务 YAML 接入 lm-eval 类框架 | `upstream-snapshots/finben/` |
| BizFinBench | 中英双语 | 真实业务驱动金融能力 | 异常事件归因、金融计算、工具使用、知识问答、股价预测、NER | 如何从真实业务问题构造高难度金融 benchmark | `upstream-snapshots/bizfinbench/` |
| BizFinBench.v2 | 中英双语 | 专家级离线/在线金融能力对齐 | 真实查询、规则化评分、在线市场任务 | 未来金融评测如何结合动态数据与可复现规则 | `upstream-snapshots/bizfinbench-v2/` |
| FinMTEB | 中英双语 | 金融文本 embedding / retrieval | 分类、聚类、检索、重排、STS、摘要 | RAG 系统不能只测生成，必须单独测向量与检索 | `upstream-snapshots/finmteb/` |
| Open Financial LLM Leaderboard | 英文为主 | 金融 LLM/Agent 持续榜单 | 信息抽取、文本分析、QA、生成、风险、预测、决策 | 如何建立持续榜单与多维任务分类 | `upstream-snapshots/ofll/` |
| FinGPT Benchmark | 英文 + 中文任务 | 开源金融 LLM 指令微调与评测 | FPB、FiQA、NER、FinRED、Headline、ConvFinQA、FinEval | 如何把微调、测试集和任务模板串起来 | `upstream-snapshots/fingpt/` |
| CNFinBench | 中文 | 高风险金融场景与 Agent 执行链 | 需求解析、路径规划、工具调用、结果验证、多轮交互 | 中文金融 Agent 如何从“会答题”走向“会执行” | `upstream-snapshots/cnfinbench/` |

## 2. 能力维度拆解

### 2.1 金融知识能力

代表资源：FinEval、CFLUE、FinanceIQ、OpenFinData 金融术语/金融事实。

适合测：

- 金融产品、会计、证券、银行、保险、监管常识。
- 专业术语解释是否准确。
- 选择题、判断题、简答题表现。

局限：

- 容易变成“考试题背诵”。
- 不一定代表真实业务可用性。
- 对 RAG、工具调用、证据追溯能力覆盖不足。

### 2.2 金融文档问答与证据能力

代表资源：FinanceBench、FinMTEB Retrieval、OFLL QA 类任务。

适合测：

- 年报、10-K、10-Q、制度、合同、研报的定位与问答。
- 答案是否能给出证据片段。
- 找不到答案时是否能拒答。
- RAG 的检索命中率、引用准确率、生成幻觉率。

这是银行落地优先级很高的方向，因为内部制度问答、客户经理助手、审查辅助和投研阅读都依赖这一能力。

### 2.3 数值计算与财务推理能力

代表资源：OpenFinData 指标计算/数据检查/数值提取、BizFinBench Financial Numerical Computation、FinQA、TAT-QA、ConvFinQA。

适合测：

- 财务指标口径是否理解正确。
- 数字提取、单位换算、同比/环比、比例/增速计算是否准确。
- 多步计算链是否稳定。

银行场景建议强制使用可审计计算器或代码工具，避免让模型“心算”。

### 2.4 风险合规与安全能力

代表资源：FinEval 金融安全、OpenFinData business/security compliance、OFLL 风险管理类任务。

适合测：

- 是否识别违规营销、投资建议越界、隐私泄露、反洗钱/制裁风险。
- 是否能给出合规边界和人工复核提示。
- 是否会在高风险问题上拒答或转人工。

银行内部 benchmark 应把这类题目单列，不能只混入总分。

### 2.5 金融市场、投研与预测能力

代表资源：BizFinBench Stock Price Prediction、PIXIU/FLARE prediction tasks、OFLL forecasting / decision-making。

适合测：

- 新闻、公告、财报、行情数据的解释能力。
- 方向预测、事件影响分析、风险提示。
- 投研报告摘要与观点一致性。

注意：预测任务容易受时间窗口、数据泄露和市场噪声影响，适合做研究和方法比较，不适合直接作为真实交易依据。

### 2.6 工具调用与 Agent 能力

代表资源：BizFinBench Financial Tool Usage、CNFinBench、OFLL agent/decision-making、FinBen。

适合测：

- 模型是否能判断何时需要查数据、算指标、检索文件或调用业务系统。
- 多步任务是否能规划、执行、校验。
- 最终答案是否可追溯、可复核。

这类评测最接近真实业务流程，但也最复杂，需要把权限、安全边界和人工复核设计进去。

### 2.7 Embedding / Retrieval 能力

代表资源：FinMTEB。

适合测：

- 金融文本向量模型在中文/英文金融语料上的语义匹配、检索、重排能力。
- RAG 系统是否因为 embedding 不适配金融术语而召回错误文档。

建议：如果要做银行知识库，先测检索，再测生成。否则不知道错误来自“没检索到”还是“模型编错”。

## 3. 对银行场景的推荐优先级

1. **制度/报告/合同/财报问答**：最容易形成可落地 Demo，也最适合加入证据引用。
2. **数值计算与指标口径**：金融场景高频、错误成本高，必须单独测。
3. **合规与拒答能力**：金融模型不能只追求回答率，必须测试边界意识。
4. **工具调用与流程执行**：适合逐步升级成客户经理助手、审查助手、运营助手。
5. **投研预测类**：可作为方法学习和展示，但需要非常谨慎地解释局限。
6. **模型榜单复现**：适合了解行业水平，但不应替代自己的业务测试集。

## 4. 一个最小可行金融 benchmark 的建议结构

| 模块 | 题量建议 | 数据来源 | 评分方式 |
| --- | --- | --- | --- |
| 金融知识 | 20-30 | 公开题库 + 自己整理的银行术语 | accuracy / 人工复核 |
| 文档证据问答 | 20-30 | 年报、制度、公开监管文件 | 答案正确率 + 证据命中率 + 幻觉率 |
| 数值计算 | 15-20 | 财报表格、指标口径、模拟业务数据 | exact match / 容差判断 / 计算链检查 |
| 风险合规 | 15-20 | 营销话术、投诉、反洗钱、隐私样例 | 合规判断 + 拒答/转人工是否正确 |
| 工具调用 | 10-15 | 检索、计算器、行情/数据库模拟工具 | 工具选择正确率 + 最终结果正确率 |
| 业务场景综合题 | 5-10 | 信贷、客服、运营、管理分析案例 | 专家评分 rubric |

