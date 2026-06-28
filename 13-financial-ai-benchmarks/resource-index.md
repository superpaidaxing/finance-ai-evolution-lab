# 已下载资源索引

> 本索引用于快速找到本次下载的金融 benchmark 资料。`upstream-snapshots` 是选择性快照，不是完整上游镜像；每个子目录都有 `SOURCE.json` 标明来源仓库和 commit。

## 1. 数据规模速览

| 路径 | 已下载内容 | 规模 |
| --- | --- | --- |
| `upstream-snapshots/financebench/data/financebench_open_source.jsonl` | FinanceBench 开源 QA | 150 条 |
| `upstream-snapshots/financebench/data/financebench_document_information.jsonl` | FinanceBench 文档索引 | 361 条 |
| `upstream-snapshots/cflue/data/knowledge/knowledge.json` | CFLUE 金融知识题 | 3,864 条 |
| `upstream-snapshots/cflue/data/application/application.json` | CFLUE 金融应用题 | 125 条 |
| `release-downloads/openfindata_release/extracted/openfindata_release/` | OpenFinData 官方 release 数据 | 19 个任务 JSON，合计约 1,555 条 |
| `upstream-snapshots/bizfinbench/datasets/` | BizFinBench 公开业务任务数据 | 10 个 JSONL，合计约 7,059 条 |
| `upstream-snapshots/cnfinbench/multi-turn/data/` | CNFinBench 多轮任务样例 | 3 个 Excel 文件 |
| `upstream-snapshots/finmteb/finance_mteb/tasks/` | FinMTEB 任务定义 | 覆盖 7 类 embedding/retrieval 任务 |
| `upstream-snapshots/fingpt/fingpt/FinGPT_Benchmark/` | FinGPT Benchmark 代码和配置 | 金融情感、NER、关系抽取、Headline、ConvFinQA、Fineval 等 |
| `upstream-snapshots/pixiu/src/tasks/` | PIXIU/FLARE 任务代码 | 金融 NLP 与预测任务接口 |
| `upstream-snapshots/finben/tasks/` | FinBen 任务 YAML | FinanceIQ、Plutus 等任务配置 |
| `upstream-snapshots/ofll/` | Open Financial LLM Leaderboard 文档 | 榜单和前后端说明 |

## 2. OpenFinData release 任务清单

`release-downloads/openfindata_release/extracted/openfindata_release/` 包含：

- `financial_terminology.json`：金融术语
- `financial_facts.json`：金融事实
- `intent_understanding.json`：金融意图理解
- `entity_recognition.json`：实体识别
- `entity_disambiguation.json`：实体消歧
- `emotion_identification.json`：情绪识别
- `data_inspection.json`：金融数据检查
- `value_extraction.json`：数值提取
- `metric_calculation.json`：指标计算
- `announcement_interpretation.json`：公告解读
- `stock_interpretation.json`：个股解读
- `macro_interpretaiton.json`：宏观解读
- `fund_analysis.json`：基金分析
- `industy_interpretation.json`：行业解读
- `sector_analysis.json`：板块分析
- `market_analysis.json`：行情分析
- `stock_analysis.json`：股票分析
- `business_compliance.json`：业务合规
- `security_compliance.json`：安全合规

> 文件名保持上游原样，包括 `interpretaiton`、`industy` 等拼写。

## 3. BizFinBench 任务清单

`upstream-snapshots/bizfinbench/datasets/` 包含：

| 文件 | 任务 | 条数 |
| --- | --- | --- |
| `Anomalous_Event_Attribution.jsonl` | 异常事件归因 | 1,064 |
| `Anomalous_Event_Attribution_v2.jsonl` | 异常事件归因 v2 | 304 |
| `Emotion_Recognition.jsonl` | 金融情绪识别 | 600 |
| `Financial_Data_Description.jsonl` | 金融数据描述 | 1,461 |
| `Financial_Knowledge_QA.jsonl` | 金融知识问答 | 990 |
| `Financial_Named_Entity_Recognition.jsonl` | 金融命名实体识别 | 433 |
| `Financial_Numerical_Computation.jsonl` | 金融数值计算 | 555 |
| `Financial_Time_Reasoning.jsonl` | 金融时间推理 | 514 |
| `Financial_Tool_Usage.jsonl` | 金融工具使用 | 641 |
| `Stock_Price_Prediction.jsonl` | 股价预测 | 497 |

## 4. 推荐阅读顺序

1. 先读 `README.md` 和 `financial-benchmark-landscape.md` 建立全局地图。
2. 用 `resource-index.md` 找到具体数据文件。
3. 想学文档问答：读 `financebench`。
4. 想学中文产业场景：读 `OpenFinData`、`BizFinBench`、`CNFinBench`。
5. 想学评测框架：读 `FinGPT Benchmark`、`PIXIU`、`FinBen`、`OFLL`。
6. 想学 RAG 检索：读 `FinMTEB`。

## 5. 许可证与使用提醒

- 本目录只用于学习、调研和后续设计自己的评测体系。
- 上游资源协议不一致，有些资源未明确标注商用权限。
- 若要复用到产品、课程、商业资料或公开榜单，需要逐项核对上游 license、citation、数据使用声明。

## 6. 已知上游数据注意事项

- `upstream-snapshots/bizfinbench/datasets/Anomalous_Event_Attribution_v2.jsonl` 按上游 GitHub 原样下载；当前快照的最后一条记录疑似未闭合，严格 JSONL 校验会报错。学习时可先使用 `Anomalous_Event_Attribution.jsonl`，或以后从上游/Hugging Face 重新确认 v2 数据。


## 7. 第 2 批新增资源索引

| 路径 | 已下载内容 | 规模 |
| --- | --- | --- |
| `upstream-snapshots/finqa/dataset/` | FinQA 财报数值推理数据 | train 6,251；dev 883；test 1,147；private_test 919 |
| `upstream-snapshots/convfinqa/data.zip` | ConvFinQA 多轮财报数值问答压缩包 | train 3,037；dev 421；turn 版本合计 14,115 条左右 |
| `upstream-snapshots/tat-qa/dataset_raw/` | TAT-QA 表格 + 文本混合问答 | train 2,201；dev/test 各约 278 个上下文 |
| `upstream-snapshots/multihiertt/` | MultiHiertt README、评估脚本和配置 | 数据需按上游 Google Drive 说明下载；本仓库保留代码/说明快照 |
| `upstream-snapshots/lofin-hirec/` | LOFin/HiREC README、数据说明和依赖 | 完整 SEC 文档集合很大；本仓库保留说明快照 |
| `huggingface-snapshots/finder/` | FinDER 数据卡与 parquet | 5,703 条 query-evidence-answer triplets；未下载 10-K zip |
| `upstream-snapshots/finance-agent-v2/` | Finance Agent Benchmark v2 README、公开题、工具代码 | 金融 Agent 搜索/EDGAR/网页/行情工具评测样例 |
| `upstream-snapshots/finova/` | Finova 中文金融 Agent 数据与评估代码 | NER 360、工具策划 258、意图识别 150、表达 100、合规 200、复杂问题 281 |
| `huggingface-snapshots/financial-phrasebank/` | Financial PhraseBank 数据卡和 zip | 2,264-4,846 条，按标注一致率分版本 |
| `huggingface-snapshots/fiqa-sentiment-classification/` | FiQA Sentiment 数据卡和 parquet | train 822；valid 117；test 234 |
| `upstream-snapshots/finsen/` | FinSen 美国新闻情绪 CSV 和 dataloader | 16,969 条美国新闻情绪/市场数据记录 |
| `upstream-snapshots/finred/` | FinRED README | 关系抽取数据需按上游说明另行访问 |

补充阅读文件：`financial-benchmark-resources-batch-02.md`。
