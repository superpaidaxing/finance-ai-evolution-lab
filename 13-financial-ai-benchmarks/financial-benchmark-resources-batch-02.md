# 金融模型评测资源库：第 2 批

> 本批次继续补充更偏“可执行评测任务”的公开资源，重点覆盖财报数值推理、表格 + 文本混合问答、长文档 RAG、金融情绪、关系抽取、因果/事件归因，以及金融 Agent / 工具调用评测。

## 1. 本批次总览

| 编号 | 资源 | 方向 | 公开地址 | 已下载位置 | 适合学习的问题 |
| --- | --- | --- | --- | --- | --- |
| FB-013 | FinQA | 财报数值推理 / 程序化计算 | https://github.com/czyssrs/FinQA | `upstream-snapshots/finqa/` | 如何把财报问答拆成检索、推理程序和最终答案 |
| FB-014 | ConvFinQA | 多轮财报数值问答 | https://github.com/czyssrs/ConvFinQA | `upstream-snapshots/convfinqa/` | 如何评估连续追问下的金融计算链 |
| FB-015 | TAT-QA | 表格 + 文本混合金融问答 | https://github.com/NExTplusplus/TAT-QA | `upstream-snapshots/tat-qa/` | 如何同时基于表格和段落回答财报问题 |
| FB-016 | MultiHiertt | 多层级表格 + 文本数值推理 | https://github.com/psunlpgroup/MultiHiertt | `upstream-snapshots/multihiertt/` | 如何评估多表、多层级、长文档的复杂推理 |
| FB-017 | LOFin / HiREC | SEC 文件开放域金融 QA / 分层检索 | https://github.com/deep-over/LOFin-bench-HiREC | `upstream-snapshots/lofin-hirec/` | 如何评估标准化长文档上的开放域 RAG |
| FB-018 | FinDER | 金融 RAG 问答与检索 | https://huggingface.co/datasets/Linq-AI-Research/FinDER | `huggingface-snapshots/finder/` | 如何用专家标注的 query-evidence-answer 评估 RAG |
| FB-019 | Finance Agent Benchmark v2 | 金融 Agent / SEC / 工具调用 | https://github.com/vals-ai/finance-agent-v2 | `upstream-snapshots/finance-agent-v2/` | 如何评估模型用搜索、EDGAR、网页解析和行情工具完成复杂问题 |
| FB-020 | Finova | 中文金融可操作 Agent / 合规安全 | https://github.com/antgroup/Finova | `upstream-snapshots/finova/` | 中文金融 Agent 的工具规划、意图识别、表达与安全如何评测 |
| FB-021 | Financial PhraseBank | 金融新闻情绪分类 | https://huggingface.co/datasets/takala/financial_phrasebank | `huggingface-snapshots/financial-phrasebank/` | 金融情绪三分类的经典基准如何组织 |
| FB-022 | FiQA Sentiment | 金融微博/新闻方面级情绪 | https://huggingface.co/datasets/TheFinAI/fiqa-sentiment-classification | `huggingface-snapshots/fiqa-sentiment-classification/` | 如何评价 aspect-based 金融情绪分析 |
| FB-023 | FinSen | 新闻情绪 + 市场预测 | https://github.com/EagleAdelaide/FinSen_Dataset | `upstream-snapshots/finsen/` | 如何把新闻情绪、时间和市场预测连接起来 |
| FB-024 | FinRED | 金融关系抽取 | https://github.com/soummyaah/FinRED | `upstream-snapshots/finred/` | 金融实体关系抽取任务如何定义 |

## 2. 本批次重点观察

### 2.1 财报数值推理比普通问答更接近银行真实工作

FinQA、ConvFinQA、TAT-QA 和 MultiHiertt 的共同特点是：答案往往不是原文摘抄，而是需要先定位表格或段落，再做多步计算。

对银行场景的启发：

- 信贷审查、财务分析、经营分析不能只测“会不会总结”，必须测“会不会按正确口径算”。
- 建议把“公式/推理程序”作为评分对象，而不只看最终答案。
- 如果模型需要计算，最好强制调用计算器或 Python，而不是让模型直接口算。

### 2.2 RAG 评测要拆成“检索”和“生成”两层

LOFin / HiREC 与 FinDER 都强调金融长文档问答中的检索问题。金融文本常见难点是：

- 查询短且含大量缩写、公司名、指标名。
- 答案分散在 10-K、年报、监管文件等长文档中。
- 证据定位错了，生成模型再强也会答错。

对银行场景的启发：

- 内部制度问答、授信材料问答、审计/合规问答要单独记录 evidence hit rate。
- 对每个答案保留证据片段、文档名、页码/段落 ID。
- 不要只用“答案看起来对不对”评估 RAG。

### 2.3 金融 Agent 评测开始从“会答题”转向“会办事”

Finance Agent Benchmark v2 和 Finova 的思路更接近未来真实业务：模型需要选择工具、查 SEC/网页/行情/数据库、解析信息、再给出答案。

对银行场景的启发：

- 可把“工具选择正确率”“参数正确率”“中间结果可审计性”纳入评分。
- 合规安全需要单独评测，例如是否越权、是否泄露隐私、是否给出不当投资建议。
- Agent 输出要有过程记录，否则难以满足金融机构审计要求。

### 2.4 情绪、关系抽取、因果/事件归因是投研和风控的底层任务

Financial PhraseBank、FiQA Sentiment、FinSen、FinRED 不是完整的大模型综合评测，但适合作为金融 NLP 基础能力测试：

- 情绪分类：新闻、公告、研报观点对市场的正负影响。
- 关系抽取：公司、人物、产品、交易、股权、财务指标之间的关系。
- 事件归因：市场波动由哪些新闻、公告、政策或财报信息驱动。

对银行场景的启发：

- 舆情监测、客户风险预警、投研辅助可以先从这些基础任务拆起。
- 这些任务适合作为“可解释信号”，但不能直接等同于投资建议。

## 3. 对自建银行 benchmark 的补充建议

在第 1 批蓝图基础上，建议新增三类题：

### 3.1 财报数值推理题

```yaml
category: financial_numerical_reasoning
input: 年报表格 + 管理层讨论段落
question: "计算 2024 年手续费及佣金净收入同比增速，并说明变化原因。"
expected_answer:
  number: "x%"
  reasoning_program: "(2024_value - 2023_value) / 2023_value"
  evidence: ["利润表对应科目", "管理层讨论对应段落"]
scoring:
  value_exact_or_tolerance: 0-2
  formula_correctness: 0-2
  evidence_correctness: 0-2
```

### 3.2 RAG 证据检索题

```yaml
category: financial_rag_retrieval
question: "本行个人经营贷对借款人年龄有什么要求？"
corpus: 制度文件集合
expected_evidence:
  document: "个人经营贷管理办法"
  section: "准入条件"
expected_answer: "..."
scoring:
  document_hit: 0-1
  passage_hit: 0-1
  answer_groundedness: 0-2
  hallucination: true/false
```

### 3.3 Agent 工具调用题

```yaml
category: financial_agent_tool_use
question: "根据 A 公司最近三年年报，计算 ROE 变化并解释主要驱动因素。"
tools_allowed:
  - document_search
  - table_extractor
  - calculator
  - citation_checker
expected_tool_sequence:
  - document_search
  - table_extractor
  - calculator
  - citation_checker
scoring:
  tool_selection: 0-2
  parameter_correctness: 0-2
  final_answer: 0-2
  auditability: 0-2
```

## 4. 建议阅读顺序

1. **先读 FinQA**：理解金融数值推理为什么要保留 program / formula。
2. **再读 TAT-QA**：理解表格 + 文本混合问答如何标注和评分。
3. **再读 FinDER / LOFin**：理解金融 RAG 为什么不能只测生成答案。
4. **再读 Finova / Finance Agent Benchmark**：理解金融 Agent 如何评估工具使用和安全。
5. **最后读情绪/关系抽取类资源**：补足投研、舆情、事件归因等底层任务。

## 5. 使用提醒

- `FinQA` 的 `train.json` 较大，但仍低于 GitHub 单文件 100MB 限制。
- `ConvFinQA` 保留上游 `data.zip`，未解压，以避免产生超过 100MB 的单个 JSON 文件。
- `FinDER` 的 10-K 文档包较大，本次只下载了数据 parquet 和 README，没有下载 10-K zip。
- 各资源 license 不一致，商用或二次公开前需要逐项核对。
