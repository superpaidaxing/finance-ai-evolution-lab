# 13 金融模型能力评测与 Benchmark 资源库

> 本目录用于收集“所有模型的金融能力评测”相关公开资源：金融大模型 benchmark、金融 NLP/QA/检索/智能体评测、中文金融考试与产业场景数据、公开榜单和可复现实验框架。目标是先建立学习地图，再逐步沉淀一套适合银行从业者的金融 AI 评测体系。

## 1. 这个分类解决什么问题

通用大模型榜单通常只能说明模型的通用语言、代码或推理能力，不能直接回答银行和金融场景最关心的问题：

- 模型是否真的懂金融术语、监管规则、财务报表、金融产品和业务流程？
- 模型能不能基于年报、制度、合同、研报等材料做**可追溯问答**，而不是编答案？
- 模型在数值计算、指标口径、时间推理、行情解读、风险合规判断上是否稳定？
- 模型是否能使用检索、计算器、数据库、行情工具等外部工具完成金融任务？
- 模型输出是否安全、合规、可解释、可复核，能不能进入真实业务流程？

因此，金融模型评测不应只做“答题正确率”，而应逐步覆盖：金融知识、文档问答、数值推理、投研分析、风险合规、工具调用、RAG、Agent、多模态和模型治理。

## 2. 本次已下载的核心公开资源

本次先收集了公开可获取、与金融垂类评测最相关的一批资源，放在：

- `upstream-snapshots/`：从公开 GitHub 项目中选择性下载的 README、任务配置、公开数据或评测代码快照。
- `release-downloads/`：公开 release 数据包下载与解压结果。

| 资源 | 主要方向 | 已下载内容 | 优先学习价值 |
| --- | --- | --- | --- |
| FinanceBench | 英文财报 / SEC 文件开放书问答 | 150 条开源 QA、文档索引、README | 学习“带证据的金融文档问答”如何设计 |
| FinEval | 中文金融大模型综合评测 | README、许可、数据说明 | 学习中文金融专业知识、行业任务、安全能力、多模态评测框架 |
| CFLUE | 中文金融语言理解 | 金融知识题、应用题公开数据 | 学习中文金融考试题 + 应用任务的组织方式 |
| OpenFinData | 中文产业金融评测数据 | README、官方 release zip、19 个任务 JSON | 学习真实产业场景如何拆成金融知识、判别、计算、解读、合规模块 |
| PIXIU / FLARE | 金融 LLM 指令数据与多任务评测 | README、任务代码 | 学习英文金融 NLP、预测任务和金融 LLM 评测管线 |
| FinBen | 综合金融 LLM benchmark | README、任务 YAML | 学习多任务金融 benchmark 与 lm-evaluation-harness 化配置 |
| BizFinBench | 中英双语真实金融业务评测 | README、公开 JSONL 数据 | 学习业务驱动的金融问答、计算、工具调用、时间推理、股价预测等任务 |
| BizFinBench.v2 | 专家级离线/在线金融评测 | README | 学习新一代“真实查询 + 在线评估 + 规则化评分”的设计方向 |
| FinMTEB | 金融文本向量 / 检索评测 | README、64 个任务定义代码 | 学习金融 RAG 的底层 embedding / retrieval 评测 |
| Open Financial LLM Leaderboard | 金融 LLM 开放榜单 | README、前后端说明 | 学习榜单维度、任务分类和持续评测平台思路 |
| FinGPT Benchmark | 开源金融 LLM 指令微调评测 | Benchmark 目录、配置、代码 | 学习金融情感、NER、关系抽取、新闻标题、FinEval/ConvFinQA 等任务串联 |
| CNFinBench | 中文高风险金融场景 / Agent 评测 | README、多轮数据和 judge 说明 | 学习中文金融 agent 端到端执行链评测 |

> 注意：这些资源来自不同上游项目，协议和使用限制不完全相同。正式商用或二次发布前，需要逐项阅读各自目录中的 `LICENSE`、README 与上游说明。

## 3. 建议先从哪几个方向着手

### 方向一：金融知识与专业考试题

适合回答“模型懂不懂金融基础知识”。先看：

- `upstream-snapshots/fineval/README.md`
- `upstream-snapshots/cflue/README.md`
- `upstream-snapshots/finben/tasks/chinese/FinanceIQ.yaml`

建议关注：题目来源、覆盖科目、评分方式、是否能解释错误原因。

### 方向二：财报、制度、合同、研报的可追溯问答

适合银行内部知识库、制度问答、审查辅助、投研报告分析。先看：

- `upstream-snapshots/financebench/`
- `upstream-snapshots/finmteb/finance_mteb/tasks/Retrieval/`
- `upstream-snapshots/ofll/README.md`

建议关注：答案是否必须引用证据、证据粒度、RAG 检索质量、拒答规则。

### 方向三：真实金融业务场景能力

适合从银行实际问题出发构建 benchmark。先看：

- `release-downloads/openfindata_release/extracted/openfindata_release/`
- `upstream-snapshots/bizfinbench/datasets/`
- `upstream-snapshots/cnfinbench/`

建议关注：业务问题如何拆分为金融判别、数值计算、行情解读、合规检查、工具调用和多轮协作。

### 方向四：金融 LLM / Agent 的完整评测管线

适合后续自己跑模型、做榜单或持续评估。先看：

- `upstream-snapshots/pixiu/src/tasks/`
- `upstream-snapshots/finben/tasks/`
- `upstream-snapshots/fingpt/fingpt/FinGPT_Benchmark/`
- `upstream-snapshots/ofll/`

建议关注：如何把任务配置化、指标标准化、结果可复现化。

## 4. 本目录文件

- `financial-benchmark-landscape.md`：公开金融评测体系调研总览。
- `banking-financial-model-evaluation-blueprint.md`：面向银行场景自建 benchmark 的建议蓝图。
- `resource-index.md`：已下载资源、数据规模、路径索引。
- `upstream-snapshots/`：上游项目选择性快照。
- `release-downloads/`：公开 release 数据包下载结果。

## 5. 后续可以迭代的方向

1. 建立自己的“银行场景最小 benchmark”：先做 50-100 道高质量题，不追求规模。
2. 将题目按“知识题、文档证据题、计算题、合规判断题、工具调用题、拒答题”分层。
3. 每个答案都要求：标准答案、证据来源、评分规则、风险说明。
4. 同时评估“裸模型”和“RAG / 工具增强模型”，不要把模型能力和系统能力混在一起。
5. 建一个小型结果表：模型、任务、准确率、证据命中率、幻觉率、拒答率、人工复核结论。
