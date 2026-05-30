# 金融 AI Skill 资源库

> 本目录专门收集“金融 + AI”相关的开源 skills、agent plugins、工作流模板和深度分析。这里的 skill 不等于可以直接在真实业务里自动决策，而是用于学习金融知识工作如何被结构化、如何被 AI 辅助、如何设置人工复核和治理边界。

## 1. 本目录解决什么问题

很多金融 AI 项目不是从模型开始，而是从“工作流”开始：分析师如何写研究报告，投行如何做 CIM，财务团队如何关账对账，运营团队如何做 KYC，财富顾问如何准备客户检视，基金运营如何核对 NAV。这些工作流如果只靠聊天理解，很容易停留在概念层；skill 的价值在于把触发条件、输入材料、处理步骤、输出格式、质量检查和风险边界写成可复用的结构。

本目录第一批先收录 Anthropic 官方开源的金融服务和财务会计类 skill，后续再分批补充社区中评价较高、特色明显的金融 AI skill，例如市场数据、实时新闻、投资研究、交易分析、合规知识、数据源连接和可视化工具类项目。

## 2. 当前已下载内容

| 批次 | 来源 | 本地位置 | 数量 | 说明 |
| --- | --- | --- | ---: | --- |
| 第 1 批 | `anthropics/financial-services` | `upstream-snapshots/anthropic-financial-services/` | 55 | Anthropic 官方金融服务插件，覆盖投行、股票研究、私募股权、财富管理、基金运营、KYC 运营、财务建模 |
| 第 1 批 | `anthropics/knowledge-work-plugins/finance` | `upstream-snapshots/anthropic-knowledge-work-finance/` | 8 | Anthropic 官方知识工作插件中的财务会计插件，覆盖关账、对账、分录、报表、差异分析、SOX 和审计支持 |
| 第 2 批 | `RKiding/Awesome-finance-skills` | `upstream-snapshots/community-awesome-finance-skills/` | 10 | 社区高星金融 Agent Skills，覆盖实时财经新闻、A/H/美股、情绪、预测、逻辑链路和报告生成 |
| 第 2 批 | `himself65/finance-skills` | `upstream-snapshots/community-himself65-finance-skills/` | 24 | 社区高星 Agent Skills 标准项目，覆盖估值、earnings、ETF、期权、数据源、社交读取和 TradingView |
| 第 3 批 | `JoelLewis/finance_skills` | `upstream-snapshots/community-joellewis-finance-skills/` | 84 | 社区专业金融服务 skill，覆盖财富管理、证券合规、顾问业务、交易运营、客户运营、数据集成和金融数学 |

## 3. 阅读顺序

1. 先读 `source-index.md`，确认每个来源、许可证、下载范围和去重边界。
2. 再读 `anthropic-official-skills-analysis-01.md`，了解 Anthropic 官方金融 skill 的金融场景、AI 价值、银行迁移方向和治理注意事项。
3. 再读 `community-finance-ai-skills-analysis-02.md`，了解社区高星金融 skill 在实时资讯、行情、情绪、数据连接和工具化分析上的特色。
4. 再读 `professional-finance-service-skills-analysis-03.md`，了解专业金融服务 skill 在财富管理、合规、交易运营、客户运营和数据集成上的结构化写法。
5. 如需看原始 skill，进入 `upstream-snapshots/` 对应目录阅读 `SKILL.md`。
6. 后续批次如果新增社区 skill，会继续使用 `FSK-xxx` 编号，不覆盖、不重复。

## 4. 使用边界

- 这些 skill 主要用于学习、研究、提示词设计和工作流拆解。
- 不应用于真实投资建议、交易执行、授信审批、客户准入批准、审计签字或监管报送最终确认。
- 如果迁移到中国银行业场景，需要重新适配中国法律法规、监管口径、机构制度、数据安全和人工复核流程。
- 原始开源项目的许可证文件已随来源快照保留；继续使用或二次分发时应遵守对应许可证。
