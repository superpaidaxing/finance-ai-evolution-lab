# 开源金融 AI 项目库——第 7 批（FP-109 至 FP-126）

本批继续扩展金融 + AI 相关开源知识点，重点覆盖股票预测 Transformer、订单簿深度学习、银行流水与票据 OCR、可微分量化金融、事件驱动回测、交易日历、金融 NLP 数据集、财报/业绩会 RAG、金融研究 Agent、AI-ready 量化工具箱和 MCP 化金融工具。

---

| 编号 | 项目 | 方向 | 项目地址 | 开源协议 | 学习问题 |
| --- | --- | --- | --- | --- | --- |
| FP-109 | MASTER | 股票价格预测 / 市场引导 Transformer | [https://github.com/SJTU-DMTai/MASTER](https://github.com/SJTU-DMTai/MASTER) | MIT | 如何用市场信息引导 Transformer 学习股票间相关性和价格趋势？ |
| FP-110 | TLOB | 限价订单簿预测 / 双注意力 Transformer | [https://github.com/LeonardoBerti00/TLOB](https://github.com/LeonardoBerti00/TLOB) | MIT | 如何用 Transformer 对限价订单簿数据做短期价格趋势预测？ |
| FP-111 | AI Bank Statement Document Automation | 银行流水 OCR + LLM + RAG + 智能体 | [https://github.com/johnsonhk88/AI-Bank-Statement-Document-Automation-By-LLM-And-Personal-Finanical-Analysis-Prediction](https://github.com/johnsonhk88/AI-Bank-Statement-Document-Automation-By-LLM-And-Personal-Finanical-Analysis-Prediction) | Apache-2.0 | 如何把银行流水 PDF 自动解析成结构化数据，并支持 RAG 问答和财务分析？ |
| FP-112 | InvOCR | 发票/收据/金融文档 OCR 处理系统 | [https://github.com/fin-officer/invocr](https://github.com/fin-officer/invocr) | Apache-2.0 | 如何构建支持 PDF、图片、JSON、XML 转换的金融票据 OCR 系统？ |
| FP-113 | TorchQuant | PyTorch 可微分量化金融 / 衍生品定价 | [https://github.com/jialuechen/torchquant](https://github.com/jialuechen/torchquant) | 未明确标注 | 如何把期权定价、希腊值和风险管理建成可微分的 PyTorch 计算图？ |
| FP-114 | ml4t-backtest | 事件驱动回测 / 机器学习交易生态 | [https://github.com/ml4t/backtest](https://github.com/ml4t/backtest) | MIT | 如何构建避免未来函数、支持真实执行建模的事件驱动回测引擎？ |
| FP-115 | exchange_calendars | 证券交易日历 / 全球市场时序基础设施 | [https://github.com/gerrymanoim/exchange_calendars](https://github.com/gerrymanoim/exchange_calendars) | Apache-2.0 | 如何为 50+ 全球交易所生成准确的开盘、收盘、休市和午休时间序列？ |
| FP-116 | pandas_market_calendars | 交易日历 / pandas 金融时序工具 | [https://github.com/rsheftel/pandas_market_calendars](https://github.com/rsheftel/pandas_market_calendars) | MIT | 如何在 pandas 中处理交易所节假日、早收盘和有效交易时间？ |
| FP-117 | Financial PhraseBank | 金融情感分析数据集 / 专家标注 | [https://huggingface.co/datasets/takala/financial_phrasebank](https://huggingface.co/datasets/takala/financial_phrasebank) | CC-BY-NC-SA-3.0 | 如何使用专家标注的金融新闻句子训练情感分析模型？ |
| FP-118 | FiNER-ORD | 金融命名实体识别数据集 / NER 基准 | [https://github.com/gtfintechlab/FiNER-ORD](https://github.com/gtfintechlab/FiNER-ORD) | 未明确标注 | 如何训练和评估金融新闻中的公司、人物、地点、金融术语等实体识别模型？ |
| FP-119 | FiNER | 金融 NER 弱监督框架 | [https://github.com/gtfintechlab/FiNER](https://github.com/gtfintechlab/FiNER) | 未明确标注 | 如何用弱监督方法降低金融命名实体识别数据标注成本？ |
| FP-120 | Financial RAG Assistant | 财报/10-K PDF RAG 问答助手 | [https://github.com/Accrame/financial-rag-assistant](https://github.com/Accrame/financial-rag-assistant) | 未明确标注 | 如何构建支持上传财务 PDF、引用来源页并回答问题的 RAG 助手？ |
| FP-121 | Earnings Call Analyzer | 业绩电话会 + SEC 文件 + 市场数据 Agent | [https://github.com/Sapan2003/Earnings-Call-Analyzer](https://github.com/Sapan2003/Earnings-Call-Analyzer) | 未明确标注 | 如何把 SEC 文件、市场数据和网页搜索整合成 AI 投研问答工具？ |
| FP-122 | FinRAGify_App | 业绩电话会 RAG / 投研助手 | [https://github.com/apsinghAnalytics/FinRAGify_App](https://github.com/apsinghAnalytics/FinRAGify_App) | MIT | 如何用 LangChain、FAISS 和重排序模型分析上市公司业绩电话会？ |
| FP-123 | Financial Research Agent | LangGraph 金融研究智能体 / 文件 RAG | [https://github.com/maquiavelo01/financial-research-agent](https://github.com/maquiavelo01/financial-research-agent) | 未明确标注 | 如何用 LangGraph 路由、检索和工具调用构建金融研究智能体？ |
| FP-124 | SEC 10-K Filings Analysis | SEC 10-K RAG / Streamlit 问答 | [https://github.com/guneeshvats/SEC-10-K-FIilings-Analysis](https://github.com/guneeshvats/SEC-10-K-FIilings-Analysis) | 未明确标注 | 如何把 SEC 10-K 文件下载、向量化并做自然语言问答？ |
| FP-125 | py-sec-xbrl | SEC XBRL 财报解析 / 结构化数据底座 | [https://github.com/zhaolewen/py-sec-xbrl](https://github.com/zhaolewen/py-sec-xbrl) | MIT | 如何把 SEC XBRL 财报文件解析为可供 AI 和量化模型使用的结构化数据？ |
| FP-126 | wraquant | AI-native 量化金融工具箱 / MCP | [https://github.com/pr1m8/wraquant](https://github.com/pr1m8/wraquant) | MIT | 如何把风险管理、波动率、衍生品、回测和机器学习整合为 AI Agent 可调用工具箱？ |

---

## FP-109：MASTER

### 项目主要介绍

MASTER 是上海交通大学 DMTai 团队发布的 AAAI 2024 论文官方代码，全称 Market-Guided Stock Transformer for Stock Price Forecasting。它针对股票价格预测中的两个关键问题设计：一是股票之间存在横截面相关性，二是不同市场状态下有效特征会变化。MASTER 通过市场信息引导 Transformer 的特征选择和相关性建模，试图让模型不仅看单只股票的历史序列，还能理解市场整体环境和股票间联动。

项目的核心模型是 stock transformer，通过注意力机制同时建模“momentary correlation”（同一时刻不同股票之间的关系）和“cross-time correlation”（跨时间的序列依赖）。这与传统单股票 LSTM/CNN 预测不同：金融市场中，行业、风格、指数、资金流之间的共同变化经常比单个股票自身历史更重要。

在金融 + AI 学习中，MASTER 值得关注，因为它代表了近年学术界把 Transformer 用于股票预测的一条主线：不是简单把价格序列当作普通时间序列，而是把市场信息、横截面关系和特征选择纳入模型结构。它也与 Microsoft Qlib 生态相关，原始实验基于 Qlib，仓库提供了简化数据和核心代码。

银行投研或资管团队可以从 MASTER 学习“AI 多因子模型”的建模思路。例如，银行理财投研团队要预测一组股票或行业指数的相对表现，就不能只看单资产历史，还要考虑市场状态、行业轮动和因子暴露。MASTER 的市场引导注意力结构可以作为研究参考。

局限在于：股票预测本身噪声极高，论文实验不等于真实可交易收益；代码是研究复现版本，不是生产级投研系统；数据处理和验证流程需要严格防止未来函数；模型在 A 股、港股或债券市场是否有效需要重新验证。

### 金融 + AI 核心特点

- 市场引导 Transformer 建模股票横截面和时间关系
- 关注市场状态下的动态特征选择
- AAAI 2024 官方代码，MIT 协议
- 与 Qlib 量化研究生态相关

### 可学习内容

- 理解该项目所在方向的核心技术和金融业务含义
- 学习如何把开源项目的方法迁移到银行投研、风控、运营或数据平台场景

### 应用方向

- 银行金融 AI 学习和原型验证
- 投研、风控或数据工程方法参考
- 后续小实验和专题复现素材
- 内部 AI 助手/工具链架构设计参考

### 风险与局限

该项目应优先作为学习和原型参考，不能直接用于银行生产。落地前需要核对开源协议、数据许可、模型效果、权限控制、审计要求和监管合规，并使用内部脱敏数据重新验证。

- **项目地址**：[https://github.com/SJTU-DMTai/MASTER](https://github.com/SJTU-DMTai/MASTER)
- **开源协议**：MIT

---

## FP-110：TLOB

### 项目主要介绍

TLOB 是 2025 年发布的限价订单簿（Limit Order Book, LOB）价格趋势预测项目，官方代码对应论文《TLOB: A Novel Transformer Model with Dual Attention for Price Trend Prediction with Limit Order Book Data》。它使用双注意力机制建模订单簿数据中的空间依赖和时间依赖，用于预测短期价格趋势。

限价订单簿是金融市场微观结构的核心数据，记录了不同价格档位上的买卖挂单量。普通 K 线只看到成交后的价格和成交量，而订单簿能看到市场供需的即时结构，例如买一到买十、卖一到卖十的深度变化。TLOB 试图让 Transformer 自动关注哪些价位档和哪些时间片对未来短期价格变化最重要。

项目在 FI-2010 等订单簿基准数据集上评估，并声称在多个预测 horizon 上超过已有方法。它还提出了新的标签方法，以减少传统固定 horizon 标签带来的偏差。这一点对金融 AI 很重要：很多交易预测任务失败并不是模型不好，而是标签定义不合理，导致模型学到噪声或未来信息。

对银行或券商量化团队来说，TLOB 更偏市场微观结构和高频交易研究。即使传统商业银行不直接做高频股票交易，理解 LOB 模型也有助于学习市场流动性、交易成本、订单执行和冲击成本估计。

局限在于：LOB 数据获取成本高、清洗复杂；研究结果通常依赖特定市场和数据集；高频预测极易受交易成本和延迟影响；模型可解释性有限；银行内部使用需要严格区分研究和实盘交易。

### 金融 + AI 核心特点

- 双注意力机制同时捕捉订单簿空间和时间依赖
- 面向限价订单簿短期价格趋势预测
- 包含新的标签方法以减少 horizon 偏差
- MIT 协议，适合微观结构研究

### 可学习内容

- 理解该项目所在方向的核心技术和金融业务含义
- 学习如何把开源项目的方法迁移到银行投研、风控、运营或数据平台场景

### 应用方向

- 银行金融 AI 学习和原型验证
- 投研、风控或数据工程方法参考
- 后续小实验和专题复现素材
- 内部 AI 助手/工具链架构设计参考

### 风险与局限

该项目应优先作为学习和原型参考，不能直接用于银行生产。落地前需要核对开源协议、数据许可、模型效果、权限控制、审计要求和监管合规，并使用内部脱敏数据重新验证。

- **项目地址**：[https://github.com/LeonardoBerti00/TLOB](https://github.com/LeonardoBerti00/TLOB)
- **开源协议**：MIT

---

## FP-111：AI Bank Statement Document Automation

### 项目主要介绍

AI Bank Statement Document Automation 是一个围绕银行流水 PDF 自动化处理的开源项目，结合 YOLOv8 布局检测、OCR、LLM 表格抽取、RAG 问答和 AG2 智能体分析。它的目标是把非结构化银行流水文档转换为结构化交易数据，并进一步生成收入支出分类、趋势分析和月度/年度财务报告。

这个项目非常贴近银行业务，因为银行流水、对账单、收入证明、消费记录等文档在零售金融、信贷审批、小微企业贷、反欺诈和个人财务管理中都很常见。传统处理依赖人工录入和模板解析，但不同银行格式差异很大，扫描件质量不一，表格结构复杂。项目展示了用计算机视觉 + OCR + LLM 组合处理这类文档的完整思路。

技术流程大致是：先用 YOLOv8 或 PDF 工具识别页面布局和表格区域，再用 OCR 提取文本，用 LLM 修正表格结构并转换为 JSON/CSV，之后用向量数据库建立 RAG，使用户可以用自然语言询问“本月最大支出是什么”“收入是否稳定”“有哪些异常交易”。

在银行迁移场景中，它可以启发信贷流水自动解析、客户收支能力评估、财务健康分析、反欺诈流水异常识别等应用。尤其是小微企业或个贷场景，客户上传的流水 PDF 经常是风控评估的重要材料。

局限在于：真实银行流水涉及高度敏感的个人金融信息，不能直接上传到外部模型；OCR 和 LLM 可能产生结构化错误；不同银行格式需要大量适配；财务分析结论不能替代合规审批和人工复核。

### 金融 + AI 核心特点

- YOLOv8 + OCR + LLM 解析银行流水 PDF
- RAG 支持自然语言查询流水内容
- AG2 智能体生成财务分析报告
- 贴近信贷、流水审查和个人财务分析

### 可学习内容

- 理解该项目所在方向的核心技术和金融业务含义
- 学习如何把开源项目的方法迁移到银行投研、风控、运营或数据平台场景

### 应用方向

- 银行金融 AI 学习和原型验证
- 投研、风控或数据工程方法参考
- 后续小实验和专题复现素材
- 内部 AI 助手/工具链架构设计参考

### 风险与局限

该项目应优先作为学习和原型参考，不能直接用于银行生产。落地前需要核对开源协议、数据许可、模型效果、权限控制、审计要求和监管合规，并使用内部脱敏数据重新验证。

- **项目地址**：[https://github.com/johnsonhk88/AI-Bank-Statement-Document-Automation-By-LLM-And-Personal-Finanical-Analysis-Prediction](https://github.com/johnsonhk88/AI-Bank-Statement-Document-Automation-By-LLM-And-Personal-Finanical-Analysis-Prediction)
- **开源协议**：Apache-2.0

---

## FP-112：InvOCR

### 项目主要介绍

InvOCR 是一个面向发票、收据和金融文档的 OCR 处理系统，支持 PDF、PNG、JPG、TIFF 等输入，并能输出 JSON、XML、HTML、PDF 等格式。它提供 FastAPI 服务、CLI 工具、Docker 部署、多语言 OCR、表格抽取、签名检测和格式转换能力。

与单纯的 OCR demo 不同，InvOCR 更像一个企业级文档处理后端：它不仅把图片转文字，还试图完成“文档 → 结构化数据 → 标准格式”的完整转换。对金融场景来说，这类能力可以用于发票报销、供应链金融票据识别、企业开户材料处理、收据归档、费用审计等。

项目支持 Tesseract OCR 和 EasyOCR 多引擎，意味着可以根据语言和文档质量选择不同 OCR 后端。它还提供 REST API 和 CLI，这对银行内部系统集成很重要：前端上传文档，后端异步 OCR，结果进入审批、记账或风控系统。

在金融 + AI 学习中，InvOCR 的价值是帮助理解“文档智能不等于 LLM”。很多场景第一步仍然是 OCR、版面分析、表格检测、字段映射和格式校验；LLM 可以增强抽取和纠错，但不能替代底层文档处理 pipeline。

局限在于：项目规模和社区活跃度较小；复杂版式和低质量扫描件仍可能识别失败；金融票据字段标准因国家和机构不同而差异很大；生产环境需要补充权限控制、审计日志和人工校验。

### 金融 + AI 核心特点

- 多引擎 OCR：Tesseract + EasyOCR
- 支持 PDF/图片到 JSON/XML/HTML/PDF 转换
- FastAPI + CLI + Docker，便于系统集成
- 面向发票、收据和金融文档处理

### 可学习内容

- 理解该项目所在方向的核心技术和金融业务含义
- 学习如何把开源项目的方法迁移到银行投研、风控、运营或数据平台场景

### 应用方向

- 银行金融 AI 学习和原型验证
- 投研、风控或数据工程方法参考
- 后续小实验和专题复现素材
- 内部 AI 助手/工具链架构设计参考

### 风险与局限

该项目应优先作为学习和原型参考，不能直接用于银行生产。落地前需要核对开源协议、数据许可、模型效果、权限控制、审计要求和监管合规，并使用内部脱敏数据重新验证。

- **项目地址**：[https://github.com/fin-officer/invocr](https://github.com/fin-officer/invocr)
- **开源协议**：Apache-2.0

---

## FP-113：TorchQuant

### 项目主要介绍

TorchQuant 是一个基于 PyTorch 的可微分量化金融库，目标是把衍生品定价、风险管理和随机模型校准构建成可自动求导、可 GPU 加速的计算框架。它把金融工具的结构与神经网络组件做类比，例如把期权 payoff 类比为 ReLU/Softplus，把美式期权的提前行权类比为最优停止和门控机制。

传统衍生品定价库通常是数值金融风格，强调解析公式、树模型和 Monte Carlo；TorchQuant 则更强调“可微分”和“深度学习友好”。这意味着模型参数、定价结果和风险敏感度可以在同一个 PyTorch 计算图中传播，便于做模型校准、神经网络近似定价和强化学习对冲。

对银行金融市场部、风险管理部或量化团队来说，这类项目很有启发：未来的风险模型可能不再是完全手工公式，而是将传统金融工程与深度学习框架结合。比如，用神经网络近似复杂衍生品定价函数，用自动微分计算 Greeks，用 GPU 加速 Monte Carlo 场景模拟。

项目覆盖期权定价、债券定价、随机模型、Greeks、VaR/ES、CVA/DVA/MVA/FVA 等内容，虽然成熟度需要验证，但知识点非常密集，适合作为“AI + 金融工程”的学习入口。

局限在于：项目开源协议未清晰标注，商业使用需谨慎；衍生品定价对模型假设、市场数据和校准质量高度敏感；研究库不能直接替代银行经过验证的风险计量系统；复杂金融工程模型需要专业背景。

### 金融 + AI 核心特点

- 基于 PyTorch 自动微分和 GPU 加速
- 覆盖衍生品定价、Greeks、风险指标和模型校准
- 将金融工具结构类比为深度学习机制
- 适合 AI + 金融工程研究

### 可学习内容

- 理解该项目所在方向的核心技术和金融业务含义
- 学习如何把开源项目的方法迁移到银行投研、风控、运营或数据平台场景

### 应用方向

- 银行金融 AI 学习和原型验证
- 投研、风控或数据工程方法参考
- 后续小实验和专题复现素材
- 内部 AI 助手/工具链架构设计参考

### 风险与局限

该项目应优先作为学习和原型参考，不能直接用于银行生产。落地前需要核对开源协议、数据许可、模型效果、权限控制、审计要求和监管合规，并使用内部脱敏数据重新验证。

- **项目地址**：[https://github.com/jialuechen/torchquant](https://github.com/jialuechen/torchquant)
- **开源协议**：未明确标注

---

## FP-114：ml4t-backtest

### 项目主要介绍

ml4t-backtest 是 Machine Learning for Trading 生态中的事件驱动回测引擎，由 Stefan Jansen 相关生态维护。它面向机器学习交易策略，强调真实执行建模、无未来函数、仓位和风险约束、订单行为导出与审计。项目仍处于 beta，但设计理念非常现代。

与轻量级回测框架相比，ml4t-backtest 更关注“研究结果是否可审计、是否接近真实执行”。它支持事件驱动架构、point-in-time correctness、先处理退出订单、同 bar/下一 bar 成交、bid/ask/midpoint 标记、止损止盈、最大持仓、回撤限制、现金/保证金/加密账户策略等。

这对金融 AI 很重要，因为机器学习策略特别容易出现未来函数和回测偏差。模型训练时如果使用了未来数据、成交价假设过于乐观、交易成本漏算，就会得到看起来很好但无法落地的策略。ml4t-backtest 把这些问题作为一等公民处理。

银行投研或资管团队可以从中学习回测引擎的风控和审计设计。例如，模型输出买卖信号后，回测层必须记录每一笔订单、成交、滑点、仓位变化和风险规则触发原因，才能支撑模型验证和投委会审查。

局限在于：项目较新、星标较少，生态成熟度不如 backtrader/Zipline；需要 Python 3.12+；文档和 API 可能继续变化；生产级使用前需大量验证。

### 金融 + AI 核心特点

- 事件驱动回测，强调 point-in-time correctness
- 真实执行建模：bid/ask、滑点、成交规则
- 支持仓位、止损、回撤等风控约束
- ML4T 生态的一部分

### 可学习内容

- 理解该项目所在方向的核心技术和金融业务含义
- 学习如何把开源项目的方法迁移到银行投研、风控、运营或数据平台场景

### 应用方向

- 银行金融 AI 学习和原型验证
- 投研、风控或数据工程方法参考
- 后续小实验和专题复现素材
- 内部 AI 助手/工具链架构设计参考

### 风险与局限

该项目应优先作为学习和原型参考，不能直接用于银行生产。落地前需要核对开源协议、数据许可、模型效果、权限控制、审计要求和监管合规，并使用内部脱敏数据重新验证。

- **项目地址**：[https://github.com/ml4t/backtest](https://github.com/ml4t/backtest)
- **开源协议**：MIT

---

## FP-115：exchange_calendars

### 项目主要介绍

exchange_calendars 是一个用于定义和查询全球证券交易所交易日历的 Python 库，支持 50+ 交易所，包括纽约、伦敦、香港、东京等市场。它可以查询交易日、开盘收盘时间、午休、节假日、早收盘等信息，是金融时序分析中容易被忽视但非常关键的基础设施。

很多金融 AI 项目会犯一个基础错误：把自然日当作交易日，或者用统一的 252 天年化假设处理所有市场。但真实市场有节假日、半日交易、午休、不同时区和交易所特殊安排。exchange_calendars 解决的就是这些“日历细节”，帮助数据对齐、收益计算、回测和风控指标更准确。

在银行场景中，交易日历适用于几乎所有市场数据处理流程：估值系统需要知道某只资产所在市场是否开市；回测系统需要生成有效交易时点；风险系统需要按交易日滚动计算波动率；跨市场组合需要对齐不同时区和休市日。

它也与 Zipline/Quantopian 生态有历史关系，是很多回测和行情系统的底层依赖。虽然它本身不是 AI 模型，但它是金融 AI 数据工程的重要底座。没有正确日历，模型训练数据就可能错位，回测结果也会失真。

局限在于：交易所特殊公告和临时休市可能需要及时更新；场外市场、银行间市场、非标准交易时段可能覆盖不足；在中国市场使用时仍需核对本地交易所公告。

### 金融 + AI 核心特点

- 支持 50+ 全球证券交易所日历
- 处理开盘、收盘、午休、节假日、早收盘
- 回测和金融时序数据对齐的底层基础设施
- Apache-2.0 协议

### 可学习内容

- 理解该项目所在方向的核心技术和金融业务含义
- 学习如何把开源项目的方法迁移到银行投研、风控、运营或数据平台场景

### 应用方向

- 银行金融 AI 学习和原型验证
- 投研、风控或数据工程方法参考
- 后续小实验和专题复现素材
- 内部 AI 助手/工具链架构设计参考

### 风险与局限

该项目应优先作为学习和原型参考，不能直接用于银行生产。落地前需要核对开源协议、数据许可、模型效果、权限控制、审计要求和监管合规，并使用内部脱敏数据重新验证。

- **项目地址**：[https://github.com/gerrymanoim/exchange_calendars](https://github.com/gerrymanoim/exchange_calendars)
- **开源协议**：Apache-2.0

---

## FP-116：pandas_market_calendars

### 项目主要介绍

pandas_market_calendars 是另一个常用的交易日历库，目标是在 pandas 生态中提供交易所假期、开盘、收盘、早收盘和有效交易时间序列。它最初从 Quantopian trading_calendars 衍生而来，长期用于量化研究和回测。

该库的使用方式非常直观：先获取某个市场日历，例如 NYSE，然后查询某段日期的 schedule，或生成仅包含有效交易时间的 DatetimeIndex。这对于高频数据重采样、收益率对齐、交易信号时间戳过滤都非常有用。

在金融 + AI 数据处理中，pandas_market_calendars 的价值在于让模型训练数据更干净。例如，训练一个股票预测模型时，不能把周末、节假日、闭市时段误认为缺失数据；训练一个跨市场模型时，也要正确处理美国开市但香港休市的日期。

银行数据平台可以借鉴它的设计，把内部交易日历、产品开放日、基金申赎日、债券付息日等业务日历统一服务化。AI 模型不应自己猜测日期规则，而应调用权威日历服务。

局限在于：部分交易所日历可能与最新公告存在滞后；复杂场外市场规则需要自定义；与 exchange_calendars 功能有重叠，实际项目中应选择一个标准库，避免口径不一致。

### 金融 + AI 核心特点

- pandas 友好的交易日历和有效交易时间生成
- 支持节假日、早收盘和市场 schedule 查询
- 适合行情清洗、回测和时间序列特征工程
- MIT 协议

### 可学习内容

- 理解该项目所在方向的核心技术和金融业务含义
- 学习如何把开源项目的方法迁移到银行投研、风控、运营或数据平台场景

### 应用方向

- 银行金融 AI 学习和原型验证
- 投研、风控或数据工程方法参考
- 后续小实验和专题复现素材
- 内部 AI 助手/工具链架构设计参考

### 风险与局限

该项目应优先作为学习和原型参考，不能直接用于银行生产。落地前需要核对开源协议、数据许可、模型效果、权限控制、审计要求和监管合规，并使用内部脱敏数据重新验证。

- **项目地址**：[https://github.com/rsheftel/pandas_market_calendars](https://github.com/rsheftel/pandas_market_calendars)
- **开源协议**：MIT

---

## FP-117：Financial PhraseBank

### 项目主要介绍

Financial PhraseBank 是金融情感分析中最经典的数据集之一，由金融和经济新闻句子组成，并由人工专家标注为 positive、negative、neutral。Hugging Face 上的 takala/financial_phrasebank 提供了多个一致性版本，例如 all agree、75% agree、66% agree、50% agree，便于研究者根据标注一致性选择训练集。

它的重要性在于：金融文本的情感判断不能直接套用通用情感模型。比如“公司成本上升”在普通语义中只是事实陈述，但从投资者角度可能是负面；“流动性充足”在金融语境中是正面。Financial PhraseBank 的标注任务明确要求从投资者视角判断句子对股价的潜在影响。

在银行或投研场景中，这个数据集可以作为训练金融情感分类器的入门数据，也可以用于评估 FinBERT、金融大模型或中文翻译模型的情感理解能力。例如，把英文句子翻译成中文后，让模型判断情感，再与原始标签对比，可以检验金融翻译和情感迁移质量。

它还适合用来讲解标注一致性的概念：all agree 数据更干净但规模小，50% agree 数据更大但噪声更高。真实银行 NLP 项目中也会遇到同样问题——标注质量与数据规模之间需要权衡。

局限在于：数据集规模只有几千条；英文新闻句子为主；许可为 CC-BY-NC-SA-3.0，商业使用受限；三分类标签较粗，不覆盖情绪强度、事件类型和因果关系。

### 金融 + AI 核心特点

- 专家标注金融新闻情感数据集
- 提供不同标注一致性版本
- 经典金融情感分析基准
- Hugging Face 可直接加载

### 可学习内容

- 理解该项目所在方向的核心技术和金融业务含义
- 学习如何把开源项目的方法迁移到银行投研、风控、运营或数据平台场景

### 应用方向

- 银行金融 AI 学习和原型验证
- 投研、风控或数据工程方法参考
- 后续小实验和专题复现素材
- 内部 AI 助手/工具链架构设计参考

### 风险与局限

该项目应优先作为学习和原型参考，不能直接用于银行生产。落地前需要核对开源协议、数据许可、模型效果、权限控制、审计要求和监管合规，并使用内部脱敏数据重新验证。

- **项目地址**：[https://huggingface.co/datasets/takala/financial_phrasebank](https://huggingface.co/datasets/takala/financial_phrasebank)
- **开源协议**：CC-BY-NC-SA-3.0

---

## FP-118：FiNER-ORD

### 项目主要介绍

FiNER-ORD 是佐治亚理工 FinTech Lab 发布的金融命名实体识别开放研究数据集，用于金融新闻中的实体识别基准。它包含人工标注的英文金融新闻文章，可用于训练和评估金融领域 NER 模型，例如识别公司、人物、地点、金融术语、产品和组织等实体。

通用 NER 模型在金融文本中经常不够准确，因为金融实体有大量专业缩写、股票代码、产品名称、指数名称、监管机构和金融工具。FiNER-ORD 的价值就在于提供了金融领域专用的实体识别数据和基准代码，让模型学习金融文本中的实体边界和类别。

在银行场景中，金融 NER 是很多高级应用的前置步骤：从新闻中识别借款企业和关联方，从研报中提取行业和公司，从监管公告中识别机构名称，从客户投诉中识别产品和网点。没有稳定的实体识别，后续关系抽取、知识图谱和 RAG 都会受影响。

FiNER-ORD 适合与金融知识图谱项目结合使用：先用 NER 找到实体，再做实体标准化和关系抽取，最终构建企业、行业、产品、事件之间的结构化网络。

局限在于：英文金融新闻为主，中文金融实体体系需要重新标注；开源协议未明确标注，商业使用需谨慎；实体识别只是第一步，实体消歧和标准化仍需额外系统。

### 金融 + AI 核心特点

- 金融新闻命名实体识别开放研究数据集
- 覆盖金融领域专有实体识别任务
- 适合 NER 模型训练和评估
- 可作为金融知识图谱前置数据

### 可学习内容

- 理解该项目所在方向的核心技术和金融业务含义
- 学习如何把开源项目的方法迁移到银行投研、风控、运营或数据平台场景

### 应用方向

- 银行金融 AI 学习和原型验证
- 投研、风控或数据工程方法参考
- 后续小实验和专题复现素材
- 内部 AI 助手/工具链架构设计参考

### 风险与局限

该项目应优先作为学习和原型参考，不能直接用于银行生产。落地前需要核对开源协议、数据许可、模型效果、权限控制、审计要求和监管合规，并使用内部脱敏数据重新验证。

- **项目地址**：[https://github.com/gtfintechlab/FiNER-ORD](https://github.com/gtfintechlab/FiNER-ORD)
- **开源协议**：未明确标注

---

## FP-119：FiNER

### 项目主要介绍

FiNER 是与 FiNER-ORD 相关的金融 NER 弱监督框架项目，重点展示如何用弱监督方法降低金融实体识别数据的人工标注成本。相比完全依赖人工逐字标注，弱监督会使用词典、规则、模式、外部知识库或模型投票生成初始标签，再通过模型学习和校正提高质量。

金融领域标注成本高，因为标注员不仅要懂语言，还要懂金融术语、公司名称、产品名称和上下文含义。FiNER 的学习价值在于：它展示了如何用半自动方式构建金融 NER 数据，而不是一开始就投入大规模人工标注。

在银行内部，这个思路非常实用。银行可能有大量产品说明书、制度文件、合同、客户投诉和公告文本，需要识别产品、机构、客户类型、风险事件等实体。如果完全人工标注，成本很高；弱监督可以先用内部产品字典、机构名录、监管词表生成初始标签，再让模型迭代优化。

FiNER 也可以作为知识图谱建设的前置工具。实体识别质量直接影响图谱质量，而弱监督提供了一种快速启动冷启动数据集的方法。

局限在于：弱监督标签会引入噪声；规则和词典质量决定上限；不同金融机构的实体体系差异大；项目协议未明确，商业使用需核对。

### 金融 + AI 核心特点

- 金融 NER 弱监督框架
- 降低人工标注成本
- 可结合词典、规则和模型生成标签
- 适合内部金融文本冷启动标注

### 可学习内容

- 理解该项目所在方向的核心技术和金融业务含义
- 学习如何把开源项目的方法迁移到银行投研、风控、运营或数据平台场景

### 应用方向

- 银行金融 AI 学习和原型验证
- 投研、风控或数据工程方法参考
- 后续小实验和专题复现素材
- 内部 AI 助手/工具链架构设计参考

### 风险与局限

该项目应优先作为学习和原型参考，不能直接用于银行生产。落地前需要核对开源协议、数据许可、模型效果、权限控制、审计要求和监管合规，并使用内部脱敏数据重新验证。

- **项目地址**：[https://github.com/gtfintechlab/FiNER](https://github.com/gtfintechlab/FiNER)
- **开源协议**：未明确标注

---

## FP-120：Financial RAG Assistant

### 项目主要介绍

Financial RAG Assistant 是一个面向财务文档的 RAG 问答系统，支持上传 10-K 文件、业绩报告等 PDF，使用 LangChain、ChromaDB、OpenAI/Claude 构建向量检索和答案生成，并返回带来源页引用的回答。项目还提供 Streamlit 聊天界面，便于用户直接体验。

这个项目代表了金融 RAG 最常见的产品形态：用户上传一份几百页的财报或 10-K，系统分块、向量化、检索相关片段，然后让大模型回答“主要风险因素是什么”“收入增长来自哪里”“管理层对未来怎么看”等问题。与普通聊天机器人不同，答案必须基于检索到的原文并给出引用。

在银行场景中，这类系统可以迁移到投研报告阅读、授信材料审阅、制度文件问答、财务报表摘要和合规检查。尤其是信贷审批和投研分析中，人工阅读长篇 PDF 非常耗时，RAG 可以先做辅助定位和摘要。

项目的学习价值在于它把 RAG 的基本组件拆得很清楚：PDF 解析、文本切分、embedding、ChromaDB、LangChain chain、聊天界面和引用返回。对初学者来说，它比复杂 Agent 项目更容易理解。

局限在于：RAG 回答质量高度依赖 PDF 解析和分块；OpenAI/Claude API 涉及数据合规和成本；简单 RAG 对表格、财务数字推理和跨页计算能力有限；生产环境需要权限和审计。

### 金融 + AI 核心特点

- 财务 PDF 上传、切分、向量化和问答
- LangChain + ChromaDB + OpenAI/Claude
- 支持来源页引用
- Streamlit 聊天界面

### 可学习内容

- 理解该项目所在方向的核心技术和金融业务含义
- 学习如何把开源项目的方法迁移到银行投研、风控、运营或数据平台场景

### 应用方向

- 银行金融 AI 学习和原型验证
- 投研、风控或数据工程方法参考
- 后续小实验和专题复现素材
- 内部 AI 助手/工具链架构设计参考

### 风险与局限

该项目应优先作为学习和原型参考，不能直接用于银行生产。落地前需要核对开源协议、数据许可、模型效果、权限控制、审计要求和监管合规，并使用内部脱敏数据重新验证。

- **项目地址**：[https://github.com/Accrame/financial-rag-assistant](https://github.com/Accrame/financial-rag-assistant)
- **开源协议**：未明确标注

---

## FP-121：Earnings Call Analyzer

### 项目主要介绍

Earnings Call Analyzer 是一个 AI 投研工具原型，整合 SEC filings、实时市场数据和网页搜索，用 RAG、LangChain agents、Claude API 和 ChromaDB 回答投资研究问题。它的定位比单文档 RAG 更进一步：不仅读文件，还尝试把外部数据和搜索工具接入同一个分析 Agent。

业绩电话会和 SEC 文件是投研分析中信息密度很高的材料，但问题往往跨多个来源：管理层在电话会中说了什么、财报数字是否支持、市场数据有没有反应、外部新闻是否有补充。Earnings Call Analyzer 展示了如何把这些来源统一到一个 AI 工作流里。

对银行投研、财富管理和私人银行团队来说，这类工具可以启发“投研助理”的设计。客户经理或投研人员可以问：某家公司最近财报的主要风险是什么？管理层对 AI 投资怎么看？市场数据和新闻是否支持这个判断？Agent 应该检索文件、调用数据工具、搜索网页并生成有引用的回答。

项目还声称在 17 家蓝筹公司问题上达到较高准确率，虽然需要谨慎看待，但说明它试图做评测，而不是只做 demo。

局限在于：项目规模小，准确率声明需独立复核；依赖外部 LLM API 和网页搜索；多源 Agent 容易产生引用混乱和幻觉；金融投资结论不能直接作为交易建议。

### 金融 + AI 核心特点

- 整合 SEC 文件、市场数据和网页搜索
- RAG + LangChain Agent + Claude + ChromaDB
- 面向投研问题的多源问答
- 尝试做准确率评估

### 可学习内容

- 理解该项目所在方向的核心技术和金融业务含义
- 学习如何把开源项目的方法迁移到银行投研、风控、运营或数据平台场景

### 应用方向

- 银行金融 AI 学习和原型验证
- 投研、风控或数据工程方法参考
- 后续小实验和专题复现素材
- 内部 AI 助手/工具链架构设计参考

### 风险与局限

该项目应优先作为学习和原型参考，不能直接用于银行生产。落地前需要核对开源协议、数据许可、模型效果、权限控制、审计要求和监管合规，并使用内部脱敏数据重新验证。

- **项目地址**：[https://github.com/Sapan2003/Earnings-Call-Analyzer](https://github.com/Sapan2003/Earnings-Call-Analyzer)
- **开源协议**：未明确标注

---

## FP-122：FinRAGify_App

### 项目主要介绍

FinRAGify_App 是一个使用 LangChain、FAISS、GPT-4o-mini 和 Hugging Face reranker 构建的业绩电话会 RAG 应用。用户可以选择公司，针对业绩电话会 transcripts 提问，例如新产品、未来展望、管理层措辞变化等，系统通过向量检索和重排序返回答案。

该项目适合学习“金融 RAG 的增强版检索流程”。简单 RAG 通常只做向量相似度检索，但金融问题对上下文精确性要求高，容易检索到相关但不够准确的片段。FinRAGify 使用 reranking 模型对候选片段重新排序，可以提高答案依据的相关性。

在银行投研场景中，业绩电话会分析很有价值，因为管理层的语气、风险提示和战略表述经常比财务数字更早反映变化。RAG 应用可以帮助分析师快速定位管理层关于收入、成本、AI 投资、监管风险、资本开支等主题的表述。

项目还可以启发“preset questions”设计：不是让用户从零提问，而是预置常见投研问题，如增长驱动、利润率变化、管理层指引、风险因素等，降低使用门槛。

局限在于：项目是概念验证，支持公司范围有限；依赖外部 API；transcript 来源和版权需要核对；电话会文本中的语气和隐含含义仍需要人工判断。

### 金融 + AI 核心特点

- 业绩电话会 transcript RAG
- FAISS 向量库 + Hugging Face reranker
- 支持预置投研问题
- MIT 协议

### 可学习内容

- 理解该项目所在方向的核心技术和金融业务含义
- 学习如何把开源项目的方法迁移到银行投研、风控、运营或数据平台场景

### 应用方向

- 银行金融 AI 学习和原型验证
- 投研、风控或数据工程方法参考
- 后续小实验和专题复现素材
- 内部 AI 助手/工具链架构设计参考

### 风险与局限

该项目应优先作为学习和原型参考，不能直接用于银行生产。落地前需要核对开源协议、数据许可、模型效果、权限控制、审计要求和监管合规，并使用内部脱敏数据重新验证。

- **项目地址**：[https://github.com/apsinghAnalytics/FinRAGify_App](https://github.com/apsinghAnalytics/FinRAGify_App)
- **开源协议**：MIT

---

## FP-123：Financial Research Agent

### 项目主要介绍

Financial Research Agent 是一个基于 LangGraph、LangChain、ChromaDB、Google Gemini 和 Streamlit 的金融研究智能体项目。它将文档检索、工具调用和直接回答组织成 LangGraph 节点，由路由节点决定用户问题应该走检索、工具还是直接响应。

相比普通 RAG 项目，Financial Research Agent 的价值在于展示了“可控 Agent 流程”。用户问题进入后，不是直接丢给 LLM，而是先由 router 判断：如果需要查文档就走 retriever，如果需要计算或公司信息就走 tool executor，如果是简单解释就直接回答。这个结构更接近银行内部 AI 助手需要的可审计流程。

项目的 RAG pipeline 包括 PDF 加载、文本切分、Gemini embeddings、ChromaDB 向量库；Agent 部分包括 graph、nodes、tools 等模块。对学习 LangGraph 的金融应用非常友好，因为代码结构清晰，金融问题也具体。

在银行场景中，可以把它迁移为“内部研究助理”：读取研究报告、制度文件、产品材料，必要时调用计算器、产品库、市场数据工具，再生成答案。这比单纯 RAG 更适合复杂问题。

局限在于：项目为课程/原型性质；生产环境需要权限控制、数据隔离、审计日志和错误回退；Gemini 等外部 API 可能涉及数据合规；工具调用边界需要严格设计。

### 金融 + AI 核心特点

- LangGraph 路由检索和工具调用
- PDF RAG + Gemini embeddings + ChromaDB
- Streamlit 前端
- 适合金融研究 Agent 架构学习

### 可学习内容

- 理解该项目所在方向的核心技术和金融业务含义
- 学习如何把开源项目的方法迁移到银行投研、风控、运营或数据平台场景

### 应用方向

- 银行金融 AI 学习和原型验证
- 投研、风控或数据工程方法参考
- 后续小实验和专题复现素材
- 内部 AI 助手/工具链架构设计参考

### 风险与局限

该项目应优先作为学习和原型参考，不能直接用于银行生产。落地前需要核对开源协议、数据许可、模型效果、权限控制、审计要求和监管合规，并使用内部脱敏数据重新验证。

- **项目地址**：[https://github.com/maquiavelo01/financial-research-agent](https://github.com/maquiavelo01/financial-research-agent)
- **开源协议**：未明确标注

---

## FP-124：SEC 10-K Filings Analysis

### 项目主要介绍

SEC 10-K Filings Analysis 是一个用 LangChain、Streamlit、ChromaDB 和 OpenAI 模型构建的 SEC 10-K 文件问答项目。它包含 SEC 文件下载、文本 ingest、向量数据库构建和前端问答流程，适合学习最基本的 SEC RAG 应用。

10-K 文件通常几百页，包含业务概述、风险因素、管理层讨论、财务报表和脚注，是投研和信用分析的重要来源。该项目展示了如何把 SEC EDGAR 的长文档转化为可检索知识库，让用户用自然语言询问关键问题。

在银行信贷和投研场景中，这类项目可以迁移到“企业年报问答”“授信材料问答”“监管文件问答”。例如，客户经理可以问某上市公司最近 10-K 中披露了哪些债务风险、收入是否集中、主要客户是否变化。

项目结构较朴素，适合初学者理解 RAG 基本流程：下载文件、切分、embedding、存入 ChromaDB、查询、生成答案、Streamlit 展示。它也可以和 sec-parser、edgartools 结合，提升解析和结构化质量。

局限在于：项目未明确开源协议；基础 RAG 对表格和复杂数值推理支持有限；10-K 下载和解析质量影响很大；OpenAI API 使用需考虑数据合规和成本。

### 金融 + AI 核心特点

- SEC 10-K 文件下载和 RAG 问答
- LangChain + Streamlit + ChromaDB
- 适合基础 SEC RAG 学习
- 可与 sec-parser/edgartools 组合

### 可学习内容

- 理解该项目所在方向的核心技术和金融业务含义
- 学习如何把开源项目的方法迁移到银行投研、风控、运营或数据平台场景

### 应用方向

- 银行金融 AI 学习和原型验证
- 投研、风控或数据工程方法参考
- 后续小实验和专题复现素材
- 内部 AI 助手/工具链架构设计参考

### 风险与局限

该项目应优先作为学习和原型参考，不能直接用于银行生产。落地前需要核对开源协议、数据许可、模型效果、权限控制、审计要求和监管合规，并使用内部脱敏数据重新验证。

- **项目地址**：[https://github.com/guneeshvats/SEC-10-K-FIilings-Analysis](https://github.com/guneeshvats/SEC-10-K-FIilings-Analysis)
- **开源协议**：未明确标注

---

## FP-125：py-sec-xbrl

### 项目主要介绍

py-sec-xbrl 是一个用于解析 SEC EDGAR XBRL 文件的 Python 工具，目标是把上市公司提交给 SEC 的 XBRL XML 财报数据解析成更容易被程序访问的结构化结果。它不是一个完整的公告下载平台，而是专注在“拿到 XBRL 文件之后，如何把其中的财务事实、标签和上下文抽取出来”。

XBRL 是财报机器可读化的关键标准。很多金融 AI 项目会直接对年报 PDF 或 HTML 做 RAG，但如果问题涉及收入、净利润、资产负债、现金流等数字，直接从文本里抽取容易出错。XBRL 数据本身已经包含标准化标签、会计期间、单位和上下文，因此更适合做数值分析、财务比率计算、信用模型特征和大模型工具调用。

在银行投研和信贷场景中，py-sec-xbrl 可以作为结构化财务数据管道的一环。例如，先通过 sec-edgar-downloader 下载公司 10-K/10-Q 的 XBRL 包，再用 py-sec-xbrl 解析关键财务指标，最后把结构化指标输入信用评分模型、行业对比模型或 RAG 工具。这样比让 LLM 从 PDF 表格里“猜数字”更可靠。

这个项目的学习价值在于帮助理解“金融文档智能”不只有自然语言问答，还包括标准化数据抽取。对于财务分析类 AI 应用，最好的架构往往是：XBRL/数据库负责准确数字，RAG/LLM 负责解释、总结和引用，两者结合才能减少幻觉。

局限在于：项目较早，维护活跃度有限；主要针对 SEC XBRL，不覆盖中国、香港或欧洲不同披露标准；XBRL taxonomy 复杂，解析结果仍需要字段映射和会计口径校验；它只做解析，不负责下载、清洗、分析和可视化。

### 金融 + AI 核心特点

- 将 SEC XBRL 财报文件解析为机器可读结构化数据
- 适合为金融 AI、信用模型和投研工具提供准确财务数字
- 可与 sec-edgar-downloader、edgartools、RAG 系统组合使用
- MIT 协议，便于学习和二次实验

### 可学习内容

- 理解 XBRL 在财报机器可读化中的作用
- 学习如何把结构化财务数据和 LLM/RAG 结合，减少数字幻觉

### 应用方向

- SEC 财报数据解析和指标抽取
- 信用评分或财务风险模型特征工程
- 投研报告自动化中的财务数据底座
- 财报 RAG 系统的结构化数字补充层

### 风险与局限

项目维护活跃度有限；主要覆盖 SEC XBRL；复杂 taxonomy 需要会计口径校验；不提供下载、分析或可视化能力，生产使用需与其他工具组合。

- **项目地址**：[https://github.com/zhaolewen/py-sec-xbrl](https://github.com/zhaolewen/py-sec-xbrl)
- **开源协议**：MIT

---
## FP-126：wraquant

### 项目主要介绍

wraquant 是一个较新的综合量化金融工具箱，项目自称包含风险管理、制度状态识别、波动率建模、衍生品定价、回测、机器学习和技术分析等模块，并通过 MCP server 将 200+ 工具暴露给 AI Agent 调用。它的定位是“AI-native quant research lab”。

与传统量化库不同，wraquant 从一开始就强调 Agent 可用性：工具函数、工作流 prompt、DuckDB 工作区和 MCP 接口被组织在一起，使 Claude 或其他 MCP 兼容 Agent 可以调用函数、保存中间结果、生成分析报告。这种设计代表了未来金融研究工具的一种方向：人不再只在 notebook 里手写代码，而是和 AI 共同调用结构化工具完成研究。

在银行或资管学习场景中，wraquant 的价值不一定在于每个函数都成熟，而在于它展示了“量化工具箱如何适配 AI Agent”。银行内部如果要构建投研 Agent，也需要把风险指标、估值模型、回测、行情查询、组合优化等能力封装成可审计工具，而不是把所有能力塞进 prompt。

它覆盖的知识点很广：风险指标、GARCH、制度切换、衍生品、回测、技术分析、机器学习、MCP 工具调用。适合作为“AI + 量化平台架构”的参考样本。

局限在于：项目较新、星标少，需要仔细验证函数正确性和测试覆盖；工具数量多不等于质量稳定；生产使用前必须做独立模型验证；MCP Agent 自动调用金融函数也需要权限、限额和审计。

### 金融 + AI 核心特点

- 综合量化金融函数库 + MCP server
- 覆盖风险、波动率、衍生品、回测和机器学习
- 面向 AI Agent 的工具调用设计
- MIT 协议

### 可学习内容

- 理解该项目所在方向的核心技术和金融业务含义
- 学习如何把开源项目的方法迁移到银行投研、风控、运营或数据平台场景

### 应用方向

- 银行金融 AI 学习和原型验证
- 投研、风控或数据工程方法参考
- 后续小实验和专题复现素材
- 内部 AI 助手/工具链架构设计参考

### 风险与局限

该项目应优先作为学习和原型参考，不能直接用于银行生产。落地前需要核对开源协议、数据许可、模型效果、权限控制、审计要求和监管合规，并使用内部脱敏数据重新验证。

- **项目地址**：[https://github.com/pr1m8/wraquant](https://github.com/pr1m8/wraquant)
- **开源协议**：MIT

---
