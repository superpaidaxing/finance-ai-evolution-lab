# 专业金融服务 Skill 深度分析（第 3 批）

> 本文件分析 `JoelLewis/finance_skills`。这个项目不是 Anthropic 官方项目，但结构完整、金融专业覆盖面广，适合补充财富管理、证券合规、交易运营、客户运营和数据集成等知识点。

## 0. 本批去重说明

| 来源 | 已收录内容 | 不重复边界 |
| --- | --- | --- |
| `JoelLewis/finance_skills` | 84 个 skill，覆盖 core、wealth-management、compliance、advisory-practice、trading-operations、client-operations、data-integration | 与第 1 批/第 2 批同名 skill 不直接合并；本批按“专业知识百科 + 美国证券/投顾/运营口径”定位 |

## 1. 总体判断

第 3 批的价值在于“专业覆盖面”和“金融知识颗粒度”。如果说第 1 批 Anthropic 官方 skill 强在高端金融知识工作的流程模板，第 2 批社区 skill 强在市场数据和工具连接，那么本批更像一套金融服务行业的知识技能库：它把财富管理、合规、顾问业务、交易运营、客户运营和数据集成拆成很多独立技能，适合系统学习金融机构各条线的工作语言。

但要特别注意，本批大量内容采用美国证券、投顾、经纪商和 FINRA/SEC/FinCEN 语境。它很适合学习“专业 skill 如何写”，也适合横向对比监管与运营流程，但不能直接替代中国银行业监管规则。后续如果迁移到本项目，应做本地化改写：把美国法规则替换为中国监管制度、银行内部制度、真实业务流程和人工复核要求。

## 2. 每个 skill 的深度分析

## 财富顾问业务与客户经营流程

### FSK-098 `advisor-dashboards`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/advisory-practice/skills/advisor-dashboards/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/advisory-practice/skills/advisor-dashboards/SKILL.md`。
- **原始定位**：上游描述：Design, build, and optimize dashboards for RIA practice management with AUM tracking, revenue analytics, and KPI frameworks. Use when the user asks about tracking firm-level metrics, monitoring advisor productivity, measuring organic growth rate, analyzing client retention and attrition, building executive or branch manager views, setting up exception alerts for NIGO or rebalancing drift, benchmarking against industry peers, or designing role-based dashboard access. Also trigger when users mention 'how is the practice doing', 'revenue per advisor', 'client attrition', 'net new assets', 'effective fee rate', 'practice benchmarking', 'AUM growth decomposition', 'advisor capacity', or 'referral tracking'.
- **金融业务理解**：这一类关注顾问日常经营：客户 onboarding、CRM 生命周期、客户检视、proposal、收费、订单管理、next-best-action 和仪表盘。它更接近财富顾问/客户经理的工作台设计。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于构思“客户经理 AI 助手”：会前准备、客户分层、客户检视纪要、下一步行动建议、产品说明草稿和合规提醒。
- **风险与治理边界**：治理重点是客户隐私和销售合规。任何客户画像、下一步行动、产品建议都必须受制于授权数据、适当性规则和人工确认。

### FSK-099 `client-onboarding`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/advisory-practice/skills/client-onboarding/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/advisory-practice/skills/client-onboarding/SKILL.md`。
- **原始定位**：上游描述：Design and implement end-to-end client onboarding workflows from prospect intake through funded account, covering KYC verification, document collection, e-signature, and custodian submission. Use when the user asks about building a digital onboarding flow, integrating identity verification or CIP checks, reducing NIGO rejection rates, opening complex account types like trusts or entities, connecting to custodian APIs, designing suitability questionnaires, or comparing advisor-assisted vs self-service models. Also trigger when users mention 'new account opening', 'onboarding bottleneck', 'KYC integration', 'beneficial ownership', 'OFAC screening', 'account funding', or 'onboarding automation'.
- **金融业务理解**：这一类关注顾问日常经营：客户 onboarding、CRM 生命周期、客户检视、proposal、收费、订单管理、next-best-action 和仪表盘。它更接近财富顾问/客户经理的工作台设计。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于构思“客户经理 AI 助手”：会前准备、客户分层、客户检视纪要、下一步行动建议、产品说明草稿和合规提醒。
- **风险与治理边界**：治理重点是客户隐私和销售合规。任何客户画像、下一步行动、产品建议都必须受制于授权数据、适当性规则和人工确认。

### FSK-100 `client-reporting-delivery`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/advisory-practice/skills/client-reporting-delivery/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/advisory-practice/skills/client-reporting-delivery/SKILL.md`。
- **原始定位**：上游描述：Design, generate, and deliver client performance reports across all channels, covering quarterly reports, tax reporting, portal integration, and compliance review. Use when the user asks about building or redesigning report templates, choosing what to include in quarterly or annual client reports, transitioning from print to digital delivery, integrating a client portal, presenting net-of-fee performance with benchmarks, managing report production timelines, or handling e-delivery consent. Also trigger when users mention 'client reporting', 'quarterly performance report', 'report customization', 'tax lot report', '1099 supplement', 'report disclaimers', 'UHNW reporting', or 'report QA process'.
- **金融业务理解**：这一类关注顾问日常经营：客户 onboarding、CRM 生命周期、客户检视、proposal、收费、订单管理、next-best-action 和仪表盘。它更接近财富顾问/客户经理的工作台设计。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于构思“客户经理 AI 助手”：会前准备、客户分层、客户检视纪要、下一步行动建议、产品说明草稿和合规提醒。
- **风险与治理边界**：治理重点是客户隐私和销售合规。任何客户画像、下一步行动、产品建议都必须受制于授权数据、适当性规则和人工确认。

### FSK-101 `client-review-prep`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/advisory-practice/skills/client-review-prep/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/advisory-practice/skills/client-review-prep/SKILL.md`。
- **原始定位**：上游描述：Prepare advisors for client review meetings by assembling context packages, performance summaries, drift analysis, talking points, and meeting agendas. Use when the user asks about preparing for a client review, building a pre-meeting checklist, generating talking points for an upcoming meeting, identifying allocation drift before a review, automating review prep workflows, or assembling a meeting package with exhibits. Also trigger when users mention 'client meeting prep', 'review preparation', 'what should I discuss with my client', 'proactive recommendations', 'life event triggered review', 'meeting agenda', or 'compliance pre-check before review'.
- **金融业务理解**：这一类关注顾问日常经营：客户 onboarding、CRM 生命周期、客户检视、proposal、收费、订单管理、next-best-action 和仪表盘。它更接近财富顾问/客户经理的工作台设计。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于构思“客户经理 AI 助手”：会前准备、客户分层、客户检视纪要、下一步行动建议、产品说明草稿和合规提醒。
- **风险与治理边界**：治理重点是客户隐私和销售合规。任何客户画像、下一步行动、产品建议都必须受制于授权数据、适当性规则和人工确认。

### FSK-102 `crm-client-lifecycle`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/advisory-practice/skills/crm-client-lifecycle/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/advisory-practice/skills/crm-client-lifecycle/SKILL.md`。
- **原始定位**：上游描述：Design and optimize CRM systems and client lifecycle workflows for advisory firms, covering segmentation, household management, service tiers, and retention analytics. Use when the user asks about client segmentation models, building household structures, defining service tier SLAs, scheduling reviews, tracking lifecycle stages from prospect through estate, identifying at-risk clients, analyzing wallet share, consolidating held-away assets, or evaluating CRM platforms. Also trigger when users mention 'client segmentation', 'retention risk', 'at-risk clients', 'household linking', 'multi-generational', 'service tiers', 'Redtail', 'Wealthbox', 'Salesforce for advisors', 'referral tracking', or 'contact gap'.
- **金融业务理解**：这一类关注顾问日常经营：客户 onboarding、CRM 生命周期、客户检视、proposal、收费、订单管理、next-best-action 和仪表盘。它更接近财富顾问/客户经理的工作台设计。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于构思“客户经理 AI 助手”：会前准备、客户分层、客户检视纪要、下一步行动建议、产品说明草稿和合规提醒。
- **风险与治理边界**：治理重点是客户隐私和销售合规。任何客户画像、下一步行动、产品建议都必须受制于授权数据、适当性规则和人工确认。

### FSK-103 `fee-billing`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/advisory-practice/skills/fee-billing/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/advisory-practice/skills/fee-billing/SKILL.md`。
- **原始定位**：上游描述：Build and manage advisory fee billing operations from fee schedule design through calculation, collection, revenue recognition, and compliance disclosure. Use when the user asks about tiered or breakpoint fee schedules, billing cycle configuration, AUM valuation for billing, direct-debit vs invoice collection, GAAP revenue recognition for fees, ADV Part 2A or Reg BI fee disclosure, diagnosing billing exceptions or refunds, migrating from spreadsheet billing to automated systems, or forecasting advisory revenue. Also trigger when users mention 'fee calculation', 'billing engine', 'effective fee rate', 'household billing aggregation', 'mid-period adjustment', 'billing in advance vs arrears', 'fee compression', or 'ERISA 408(b)(2)'.
- **金融业务理解**：这一类关注顾问日常经营：客户 onboarding、CRM 生命周期、客户检视、proposal、收费、订单管理、next-best-action 和仪表盘。它更接近财富顾问/客户经理的工作台设计。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于构思“客户经理 AI 助手”：会前准备、客户分层、客户检视纪要、下一步行动建议、产品说明草稿和合规提醒。
- **风险与治理边界**：治理重点是客户隐私和销售合规。任何客户画像、下一步行动、产品建议都必须受制于授权数据、适当性规则和人工确认。

### FSK-104 `financial-planning-integration`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/advisory-practice/skills/financial-planning-integration/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/advisory-practice/skills/financial-planning-integration/SKILL.md`。
- **原始定位**：上游描述：Integrate financial planning engines with the advisor technology stack, covering goal-based frameworks, Monte Carlo simulation, plan-to-portfolio linkage, and tax-aware strategies. Use when the user asks about connecting planning tools to CRM or PMS, building goal-based financial plans, running Monte Carlo probability-of-success analysis, linking plan outputs to portfolio construction, modeling Roth conversions or withdrawal sequencing, optimizing Social Security claiming strategies, projecting RMDs under SECURE 2.0, or synchronizing assumptions across systems. Also trigger when users mention 'eMoney', 'MoneyGuidePro', 'RightCapital', 'plan probability of success', 'what-if scenarios', 'retirement income plan', 'tax-loss harvesting in the plan', 'IRMAA planning', or 'plan-to-IPS linkage'.
- **金融业务理解**：这一类关注顾问日常经营：客户 onboarding、CRM 生命周期、客户检视、proposal、收费、订单管理、next-best-action 和仪表盘。它更接近财富顾问/客户经理的工作台设计。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于构思“客户经理 AI 助手”：会前准备、客户分层、客户检视纪要、下一步行动建议、产品说明草稿和合规提醒。
- **风险与治理边界**：治理重点是客户隐私和销售合规。任何客户画像、下一步行动、产品建议都必须受制于授权数据、适当性规则和人工确认。

### FSK-105 `financial-planning-workflow`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/advisory-practice/skills/financial-planning-workflow/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/advisory-practice/skills/financial-planning-workflow/SKILL.md`。
- **原始定位**：上游描述：Orchestrate the complete advisor workflow for assembling and delivering a comprehensive financial plan, from data gathering through recommendations and ongoing monitoring. Use when the user asks about building a financial plan for a client, structuring a planning engagement, coordinating retirement and education and estate goals into one plan, running scenario analysis across a full financial picture, prioritizing competing recommendations, preparing for a plan presentation meeting, or deciding when a plan needs updating. Also trigger when users mention 'comprehensive financial plan', 'discovery meeting', 'cash flow analysis', 'retirement modeling', 'education funding gap', 'plan delivery', 'savings rate', 'plan update trigger', or 'is my client on track'.
- **金融业务理解**：这一类关注顾问日常经营：客户 onboarding、CRM 生命周期、客户检视、proposal、收费、订单管理、next-best-action 和仪表盘。它更接近财富顾问/客户经理的工作台设计。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于构思“客户经理 AI 助手”：会前准备、客户分层、客户检视纪要、下一步行动建议、产品说明草稿和合规提醒。
- **风险与治理边界**：治理重点是客户隐私和销售合规。任何客户画像、下一步行动、产品建议都必须受制于授权数据、适当性规则和人工确认。

### FSK-106 `next-best-action`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/advisory-practice/skills/next-best-action/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/advisory-practice/skills/next-best-action/SKILL.md`。
- **原始定位**：上游描述：Design and implement next-best-action engines that surface proactive, prioritized recommendations to advisors based on portfolio, life, market, and compliance events. Use when the user asks about building event-driven advisor alerts, designing trigger logic for portfolio drift or large cash movements, prioritizing competing actions across a book of business, routing NBA recommendations to the right team member, measuring NBA acceptance rates, or automating compliance-driven actions like annual review reminders. Also trigger when users mention 'next best action', 'advisor nudges', 'proactive outreach', 'what should I do for this client', 'event-driven triggers', 'action queue', 'client contact gap', 'RMD reminder', or 'advisor productivity tool'.
- **金融业务理解**：这一类关注顾问日常经营：客户 onboarding、CRM 生命周期、客户检视、proposal、收费、订单管理、next-best-action 和仪表盘。它更接近财富顾问/客户经理的工作台设计。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于构思“客户经理 AI 助手”：会前准备、客户分层、客户检视纪要、下一步行动建议、产品说明草稿和合规提醒。
- **风险与治理边界**：治理重点是客户隐私和销售合规。任何客户画像、下一步行动、产品建议都必须受制于授权数据、适当性规则和人工确认。

### FSK-107 `order-management-advisor`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/advisory-practice/skills/order-management-advisor/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/advisory-practice/skills/order-management-advisor/SKILL.md`。
- **原始定位**：上游描述：Manage the advisor trade lifecycle from order entry through settlement, covering block trading, allocation, pre-trade compliance, custodian routing, and error correction. Use when the user asks about designing an OMS for an RIA, executing model portfolio changes across many accounts, structuring block trades with fair allocation, configuring pre-trade compliance rules or restricted lists, routing orders to multiple custodians, handling trade errors or corrections, managing cash in trading workflows, or evaluating OMS platforms. Also trigger when users mention 'block trade', 'trade allocation', 'order management system', 'iRebal', 'Orion Trading', 'Tamarac Trading', 'best execution', 'trade error', 'mutual fund vs ETF orders', or 'audit trail'.
- **金融业务理解**：这一类关注顾问日常经营：客户 onboarding、CRM 生命周期、客户检视、proposal、收费、订单管理、next-best-action 和仪表盘。它更接近财富顾问/客户经理的工作台设计。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于构思“客户经理 AI 助手”：会前准备、客户分层、客户检视纪要、下一步行动建议、产品说明草稿和合规提醒。
- **风险与治理边界**：治理重点是客户隐私和销售合规。任何客户画像、下一步行动、产品建议都必须受制于授权数据、适当性规则和人工确认。

### FSK-108 `portfolio-management-systems`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/advisory-practice/skills/portfolio-management-systems/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/advisory-practice/skills/portfolio-management-systems/SKILL.md`。
- **原始定位**：上游描述：Select, configure, and operate portfolio management systems for advisory firms, covering model portfolios, UMA/sleeve management, drift monitoring, rebalancing, and custodian data feeds. Use when the user asks about choosing a PMS platform, building or distributing model portfolios, implementing UMA or sleeve-based management, setting drift monitoring thresholds, aggregating held-away assets, reconciling PMS with custodian records, configuring PMS-based billing, or troubleshooting custodian feed issues. Also trigger when users mention 'portfolio management system', 'Orion', 'Black Diamond', 'Tamarac', 'Addepar', 'Advent APX', 'model portfolio', 'sleeve management', 'rebalancing engine', 'custodian feed', or 'PMS migration'.
- **金融业务理解**：这一类关注顾问日常经营：客户 onboarding、CRM 生命周期、客户检视、proposal、收费、订单管理、next-best-action 和仪表盘。它更接近财富顾问/客户经理的工作台设计。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于构思“客户经理 AI 助手”：会前准备、客户分层、客户检视纪要、下一步行动建议、产品说明草稿和合规提醒。
- **风险与治理边界**：治理重点是客户隐私和销售合规。任何客户画像、下一步行动、产品建议都必须受制于授权数据、适当性规则和人工确认。

### FSK-109 `proposal-generation`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/advisory-practice/skills/proposal-generation/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/advisory-practice/skills/proposal-generation/SKILL.md`。
- **原始定位**：上游描述：Generate end-to-end investment proposals covering risk profiling, model portfolio recommendation, fee illustration, projections, and compliance review. Use when the user asks about creating a proposal for a prospect, mapping risk questionnaire scores to model portfolios, building fee illustrations with tiered costs, producing Monte Carlo or scenario projections, analyzing a prospect's current portfolio for improvement opportunities, reviewing proposals for SEC Marketing Rule compliance, or designing proposal templates for a multi-advisor firm. Also trigger when users mention 'investment proposal', 'proposal generation', 'risk profiling', 'Riskalyze', 'Nitrogen', 'fee illustration', 'transition analysis', 'current vs proposed portfolio', or 'proposal compliance review'.
- **金融业务理解**：这一类关注顾问日常经营：客户 onboarding、CRM 生命周期、客户检视、proposal、收费、订单管理、next-best-action 和仪表盘。它更接近财富顾问/客户经理的工作台设计。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于构思“客户经理 AI 助手”：会前准备、客户分层、客户检视纪要、下一步行动建议、产品说明草稿和合规提醒。
- **风险与治理边界**：治理重点是客户隐私和销售合规。任何客户画像、下一步行动、产品建议都必须受制于授权数据、适当性规则和人工确认。

## 客户运营、账户流程与后台作业

### FSK-110 `account-maintenance`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/client-operations/skills/account-maintenance/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/client-operations/skills/account-maintenance/SKILL.md`。
- **原始定位**：上游描述：Process account maintenance requests across the full account lifecycle. Use when changing a client address or contact info and verifying identity, updating beneficiary designations after marriage divorce birth or death, re-registering or re-titling an account to a trust or new entity, selecting tax lot accounting methods or fixing cost basis records, applying legal holds compliance holds or Reg T freezes, setting up systematic withdrawals automatic investments or dividend reinvestment, processing a death notification or estate account setup, handling a QDRO or divorce decree for retirement accounts, responding to power of attorney or guardianship situations, closing accounts and managing escheatment, or designing periodic account review and data quality programs.
- **金融业务理解**：这一类覆盖账户开立、账户维护、转托管、公司行为、对账、直通处理和工作流自动化。它与银行柜面、运营、托管、清算和客户服务后台高度相关。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行运营流程拆成“输入材料、系统字段、校验规则、异常队列、SLA、人工复核”的标准模板。
- **风险与治理边界**：治理重点是流程权限和审计留痕。AI 可以辅助填单、识别缺口和归类异常，但不能替代经办、复核、授权和客户确认。

### FSK-111 `account-opening-compliance`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/client-operations/skills/account-opening-compliance/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/client-operations/skills/account-opening-compliance/SKILL.md`。
- **原始定位**：上游描述：Embed compliance controls into account opening workflows and verify regulatory readiness. Use when designing CIP/KYC identity verification gates for new accounts, implementing OFAC and sanctions screening at onboarding, collecting beneficial ownership certification for entity or trust accounts, building risk-based approval tiers that route applications by risk level, adding senior investor protections or trusted contact procedures, automating compliance screening and exception tracking, establishing CDD risk ratings and ongoing monitoring triggers, preparing account opening procedures for SEC or FINRA examination, remediating audit or exam deficiencies in onboarding compliance, or assessing the handoff from opening compliance to ongoing surveillance.
- **金融业务理解**：这一类覆盖账户开立、账户维护、转托管、公司行为、对账、直通处理和工作流自动化。它与银行柜面、运营、托管、清算和客户服务后台高度相关。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行运营流程拆成“输入材料、系统字段、校验规则、异常队列、SLA、人工复核”的标准模板。
- **风险与治理边界**：治理重点是流程权限和审计留痕。AI 可以辅助填单、识别缺口和归类异常，但不能替代经办、复核、授权和客户确认。

### FSK-112 `account-opening-workflow`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/client-operations/skills/account-opening-workflow/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/client-operations/skills/account-opening-workflow/SKILL.md`。
- **原始定位**：上游描述：Design and operate back-office account opening processes from application intake through activation. Use when building account opening automation or improving STP rates, reducing NIGO rejection rates from custodians or clearing firms, defining document requirements for trusts entities IRAs or estate accounts, implementing approval workflows and regulatory holds for complex account types, setting up multi-custodian account opening across Schwab Fidelity or Pershing, designing account numbering titling or classification schemes, troubleshooting account opening failures or processing delays, integrating with custodian or clearing firm submission systems, or benchmarking account opening cycle times and operational efficiency.
- **金融业务理解**：这一类覆盖账户开立、账户维护、转托管、公司行为、对账、直通处理和工作流自动化。它与银行柜面、运营、托管、清算和客户服务后台高度相关。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行运营流程拆成“输入材料、系统字段、校验规则、异常队列、SLA、人工复核”的标准模板。
- **风险与治理边界**：治理重点是流程权限和审计留痕。AI 可以辅助填单、识别缺口和归类异常，但不能替代经办、复核、授权和客户确认。

### FSK-113 `account-transfers`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/client-operations/skills/account-transfers/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/client-operations/skills/account-transfers/SKILL.md`。
- **原始定位**：上游描述：Process and manage account transfers between and within financial institutions. Use when handling full or partial ACAT transfers between broker-dealers, troubleshooting ACAT rejection codes or FINRA Rule 11870 timeline issues, setting up non-ACAT transfers like mutual fund direct transfers or DTC free deliveries, processing internal journal entries to move assets between accounts, handling retirement account rollovers or Roth conversions with proper tax reporting, managing estate transfers with cost basis step-up and date-of-death valuations, reconciling assets after transfer completion including residual credits and fractional shares, coordinating multi-account household transfers across different account types, or building transfer tracking dashboards and client communication workflows.
- **金融业务理解**：这一类覆盖账户开立、账户维护、转托管、公司行为、对账、直通处理和工作流自动化。它与银行柜面、运营、托管、清算和客户服务后台高度相关。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行运营流程拆成“输入材料、系统字段、校验规则、异常队列、SLA、人工复核”的标准模板。
- **风险与治理边界**：治理重点是流程权限和审计留痕。AI 可以辅助填单、识别缺口和归类异常，但不能替代经办、复核、授权和客户确认。

### FSK-114 `corporate-actions`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/client-operations/skills/corporate-actions/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/client-operations/skills/corporate-actions/SKILL.md`。
- **原始定位**：上游描述：Process and manage corporate actions from announcement through settlement. Use when handling dividends stock splits reverse splits mergers or spin-offs, managing voluntary elections for tender offers rights offerings or exchange offers, calculating record date and ex-date entitlements under current settlement cycles, building client notification workflows for upcoming corporate actions, collecting and submitting voluntary action elections to DTC or custodians, calculating fractional share handling or proration for reorganization events, adjusting cost basis and tax lots after corporate actions, reconciling expected entitlements against actual receipts, investigating missed or incorrectly processed corporate actions, or designing corporate action processing systems and controls.
- **金融业务理解**：这一类覆盖账户开立、账户维护、转托管、公司行为、对账、直通处理和工作流自动化。它与银行柜面、运营、托管、清算和客户服务后台高度相关。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行运营流程拆成“输入材料、系统字段、校验规则、异常队列、SLA、人工复核”的标准模板。
- **风险与治理边界**：治理重点是流程权限和审计留痕。AI 可以辅助填单、识别缺口和归类异常，但不能替代经办、复核、授权和客户确认。

### FSK-115 `reconciliation`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/client-operations/skills/reconciliation/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/client-operations/skills/reconciliation/SKILL.md`。
- **原始定位**：上游描述：Design and operate reconciliation processes that ensure data accuracy across portfolio management custodian and clearing systems. Use when building or evaluating a daily position cash or transaction reconciliation process, investigating discrepancies between internal systems and custodian records, diagnosing recurring break patterns especially from corporate actions or pricing differences, setting tolerance thresholds for position cash or market value matching, implementing three-way reconciliation across advisor system custodian and clearing firm, designing break investigation workflows with aging and escalation, normalizing data across multi-custodian feeds from Schwab Fidelity or Pershing, reconciling cost basis tax lots or accrued income across systems, evaluating reconciliation platforms like Arcesium Duco or Advent Geneva, or preparing for regulatory examinations on books and records accuracy.
- **金融业务理解**：这一类覆盖账户开立、账户维护、转托管、公司行为、对账、直通处理和工作流自动化。它与银行柜面、运营、托管、清算和客户服务后台高度相关。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行运营流程拆成“输入材料、系统字段、校验规则、异常队列、SLA、人工复核”的标准模板。
- **风险与治理边界**：治理重点是流程权限和审计留痕。AI 可以辅助填单、识别缺口和归类异常，但不能替代经办、复核、授权和客户确认。

### FSK-116 `stp-automation`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/client-operations/skills/stp-automation/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/client-operations/skills/stp-automation/SKILL.md`。
- **原始定位**：上游描述：Design and implement straight-through processing and operational automation for securities operations. Use when measuring STP rates and identifying manual touchpoints in an existing process, replacing review-all workflows with exception-based processing, selecting automation patterns for account opening trade processing settlement reconciliation or billing, designing integration between portfolio management custodian CRM and order management systems, building exception queuing categorization and auto-resolution workflows, evaluating RPA vs API-based vs hybrid automation for legacy systems, establishing operational controls and audit trails for automated environments, conducting process mining or root cause analysis on exception volumes, or setting STP rate targets and continuous improvement programs.
- **金融业务理解**：这一类覆盖账户开立、账户维护、转托管、公司行为、对账、直通处理和工作流自动化。它与银行柜面、运营、托管、清算和客户服务后台高度相关。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行运营流程拆成“输入材料、系统字段、校验规则、异常队列、SLA、人工复核”的标准模板。
- **风险与治理边界**：治理重点是流程权限和审计留痕。AI 可以辅助填单、识别缺口和归类异常，但不能替代经办、复核、授权和客户确认。

### FSK-117 `workflow-automation`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/client-operations/skills/workflow-automation/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/client-operations/skills/workflow-automation/SKILL.md`。
- **原始定位**：上游描述：Design and implement workflow automation with task routing approval chains and SLA monitoring for securities operations. Use when building a new operational workflow for account opening maintenance transfers or corporate actions, implementing task routing logic based on type priority or capacity, designing multi-level approval chains with dollar thresholds and delegation of authority, defining escalation rules for aging work items approaching SLA breach, selecting a workflow engine or BPM platform like Camunda Pega or ServiceNow, modeling an operational process as a state machine with defined transitions, adding audit trail and logging for SEC Rule 17a-3 or FINRA supervisory obligations, migrating from email-and-spreadsheet tracking to a structured workflow system, or measuring cycle time throughput queue depth and rework rate.
- **金融业务理解**：这一类覆盖账户开立、账户维护、转托管、公司行为、对账、直通处理和工作流自动化。它与银行柜面、运营、托管、清算和客户服务后台高度相关。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行运营流程拆成“输入材料、系统字段、校验规则、异常队列、SLA、人工复核”的标准模板。
- **风险与治理边界**：治理重点是流程权限和审计留痕。AI 可以辅助填单、识别缺口和归类异常，但不能替代经办、复核、授权和客户确认。

## 证券合规、反洗钱与监管要求

### FSK-118 `advertising-compliance`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/compliance/skills/advertising-compliance/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/compliance/skills/advertising-compliance/SKILL.md`。
- **原始定位**：上游描述：Ensure investment advertising and marketing materials comply with SEC Marketing Rule and FINRA Rule 2210. Use when the user asks about performance advertising, showing backtested or hypothetical returns, net vs gross performance presentation, client testimonials or endorsements in marketing, social media posts by advisers or reps, third-party ratings in pitchbooks, or advertising recordkeeping. Also trigger when users mention 'can we show this track record', 'pitchbook compliance review', 'marketing rule violations', 'cherry-picking performance periods', 'predecessor performance portability', 'extracted performance', or ask whether a website, one-pager, or presentation needs compliance approval.
- **金融业务理解**：这一类集中在美国证券和投资顾问合规，包括 KYC、AML、Reg BI、受托责任、广告合规、记录保存、隐私和监管检查。它适合作为“合规知识如何写进 skill”的优秀样本。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于对照中国银行业反洗钱、消费者保护、销售适当性、数据安全和监管检查要求，设计中文本地化合规 skill。
- **风险与治理边界**：治理重点是法域差异和规则引用。原 skill 引用 FINRA、SEC、FinCEN、ERISA、GIPS 等美国规则，不能直接作为中国业务判断依据。

### FSK-119 `advice-standards`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/compliance/skills/advice-standards/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/compliance/skills/advice-standards/SKILL.md`。
- **原始定位**：上游描述：Determine when a product, platform, or communication crosses the regulatory line from education into investment advice requiring registration. Use when the user asks about the definition of investment advice under the Advisers Act, whether a fintech feature or AI chatbot constitutes advice, the publisher's exclusion for newsletters or model portfolios, broker-dealer solely incidental exclusion, what triggers a 'recommendation' under Reg BI, or DOL education vs advice safe harbors. Also trigger when users ask 'do I need to register as an investment adviser', 'does this app give investment advice', 'is this tool just education or advice', 'robo-adviser registration', or 'disclaimer language for financial content'.
- **金融业务理解**：这一类集中在美国证券和投资顾问合规，包括 KYC、AML、Reg BI、受托责任、广告合规、记录保存、隐私和监管检查。它适合作为“合规知识如何写进 skill”的优秀样本。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于对照中国银行业反洗钱、消费者保护、销售适当性、数据安全和监管检查要求，设计中文本地化合规 skill。
- **风险与治理边界**：治理重点是法域差异和规则引用。原 skill 引用 FINRA、SEC、FinCEN、ERISA、GIPS 等美国规则，不能直接作为中国业务判断依据。

### FSK-120 `anti-money-laundering`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/compliance/skills/anti-money-laundering/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/compliance/skills/anti-money-laundering/SKILL.md`。
- **原始定位**：上游描述：Guide BSA/AML compliance program design and operation for broker-dealers, banks, and investment advisers. Use when the user asks about suspicious activity reports, currency transaction reports, OFAC screening, structuring detection, or FinCEN requirements. Also trigger when users mention 'large cash deposit', 'sanctions check', 'money laundering red flags', 'customer risk rating', 'unusual transaction patterns', 'wire to a foreign country', 'SDN list', 'tipping off a client about a SAR', 'AML audit', 'correspondent account due diligence', or ask whether a transaction needs to be reported.
- **金融业务理解**：这一类集中在美国证券和投资顾问合规，包括 KYC、AML、Reg BI、受托责任、广告合规、记录保存、隐私和监管检查。它适合作为“合规知识如何写进 skill”的优秀样本。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于对照中国银行业反洗钱、消费者保护、销售适当性、数据安全和监管检查要求，设计中文本地化合规 skill。
- **风险与治理边界**：治理重点是法域差异和规则引用。原 skill 引用 FINRA、SEC、FinCEN、ERISA、GIPS 等美国规则，不能直接作为中国业务判断依据。

### FSK-121 `books-and-records`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/compliance/skills/books-and-records/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/compliance/skills/books-and-records/SKILL.md`。
- **原始定位**：上游描述：Guide the design and maintenance of recordkeeping programs under SEC Rules 17a-3, 17a-4, and 204-2. Use when the user asks about document retention schedules, how long to keep trade records or customer complaints, WORM storage requirements, email or text message archiving, social media capture, BYOD compliance policies, or electronic storage audit trails. Also trigger when users mention 'we got an exam request for records', 'migrating to a new archiving vendor', 'blotter retention', 'order ticket requirements', 'off-channel communications', 'WhatsApp archiving', or ask how long specific records must be kept.
- **金融业务理解**：这一类集中在美国证券和投资顾问合规，包括 KYC、AML、Reg BI、受托责任、广告合规、记录保存、隐私和监管检查。它适合作为“合规知识如何写进 skill”的优秀样本。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于对照中国银行业反洗钱、消费者保护、销售适当性、数据安全和监管检查要求，设计中文本地化合规 skill。
- **风险与治理边界**：治理重点是法域差异和规则引用。原 skill 引用 FINRA、SEC、FinCEN、ERISA、GIPS 等美国规则，不能直接作为中国业务判断依据。

### FSK-122 `client-disclosures`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/compliance/skills/client-disclosures/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/compliance/skills/client-disclosures/SKILL.md`。
- **原始定位**：上游描述：Guide the creation, content, and delivery of required client disclosure documents for investment advisers and broker-dealers. Use when the user asks about Form ADV Part 2A or 2B content, Form CRS requirements, prospectus delivery obligations, privacy notice delivery, trade confirmation timing, account statement distribution, or electronic vs paper delivery compliance. Also trigger when users mention 'onboarding document checklist', 'what disclosures do we owe new clients', 'annual brochure update', 'brochure supplement for a new adviser', 'CRS conversation starters', or ask when and how disclosure documents must be delivered.
- **金融业务理解**：这一类集中在美国证券和投资顾问合规，包括 KYC、AML、Reg BI、受托责任、广告合规、记录保存、隐私和监管检查。它适合作为“合规知识如何写进 skill”的优秀样本。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于对照中国银行业反洗钱、消费者保护、销售适当性、数据安全和监管检查要求，设计中文本地化合规 skill。
- **风险与治理边界**：治理重点是法域差异和规则引用。原 skill 引用 FINRA、SEC、FinCEN、ERISA、GIPS 等美国规则，不能直接作为中国业务判断依据。

### FSK-123 `conflicts-of-interest`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/compliance/skills/conflicts-of-interest/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/compliance/skills/conflicts-of-interest/SKILL.md`。
- **原始定位**：上游描述：Identify, disclose, and mitigate conflicts of interest in advisory and brokerage relationships under Reg BI and fiduciary duty. Use when the user asks about compensation-based conflicts, proprietary product incentives, revenue sharing disclosure, principal trading consent, soft dollar arrangements, pay-to-play restrictions, gifts and entertainment limits, personal trading policies, or code of ethics requirements. Also trigger when users mention 'is this a conflict', 'recommending our own funds', 'higher payout on annuities', 'outside business activity conflicts', 'allocation fairness across accounts', 'political contribution to a pension board member', or ask how to disclose or eliminate a conflict.
- **金融业务理解**：这一类集中在美国证券和投资顾问合规，包括 KYC、AML、Reg BI、受托责任、广告合规、记录保存、隐私和监管检查。它适合作为“合规知识如何写进 skill”的优秀样本。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于对照中国银行业反洗钱、消费者保护、销售适当性、数据安全和监管检查要求，设计中文本地化合规 skill。
- **风险与治理边界**：治理重点是法域差异和规则引用。原 skill 引用 FINRA、SEC、FinCEN、ERISA、GIPS 等美国规则，不能直接作为中国业务判断依据。

### FSK-124 `examination-readiness`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/compliance/skills/examination-readiness/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/compliance/skills/examination-readiness/SKILL.md`。
- **原始定位**：上游描述：Prepare for and respond to SEC and FINRA regulatory examinations across the full exam lifecycle. Use when the user asks about exam notification letters, document request lists, deficiency letter responses, mock examination programs, annual compliance reviews under Rule 206(4)-7, or SEC/FINRA examination priorities. Also trigger when users mention 'we just got an exam letter', 'preparing for our first SEC exam', 'how to respond to a deficiency finding', 'staff interview preparation', 'what does OCIE look for', 'examination readiness checklist', 'sweep exam on off-channel comms', or ask what to expect during a regulatory audit.
- **金融业务理解**：这一类集中在美国证券和投资顾问合规，包括 KYC、AML、Reg BI、受托责任、广告合规、记录保存、隐私和监管检查。它适合作为“合规知识如何写进 skill”的优秀样本。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于对照中国银行业反洗钱、消费者保护、销售适当性、数据安全和监管检查要求，设计中文本地化合规 skill。
- **风险与治理边界**：治理重点是法域差异和规则引用。原 skill 引用 FINRA、SEC、FinCEN、ERISA、GIPS 等美国规则，不能直接作为中国业务判断依据。

### FSK-125 `fee-disclosure`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/compliance/skills/fee-disclosure/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/compliance/skills/fee-disclosure/SKILL.md`。
- **原始定位**：上游描述：Guide fee disclosure compliance across advisory, brokerage, fund, and retirement plan contexts. Use when the user asks about Form ADV Item 5 fee schedules, prospectus fee table format, Reg BI cost disclosure obligations, 12b-1 fee transparency, revenue sharing arrangements, wrap fee program costs, or ERISA 408(b)(2) service provider fee disclosure. Also trigger when users mention 'hidden fees', 'total cost to the client', 'are we disclosing all layers of fees', 'expense ratio comparison', 'fee billing in advance vs arrears', 'share class selection', 'indirect compensation', or ask whether fee disclosures are complete and compliant.
- **金融业务理解**：这一类集中在美国证券和投资顾问合规，包括 KYC、AML、Reg BI、受托责任、广告合规、记录保存、隐私和监管检查。它适合作为“合规知识如何写进 skill”的优秀样本。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于对照中国银行业反洗钱、消费者保护、销售适当性、数据安全和监管检查要求，设计中文本地化合规 skill。
- **风险与治理边界**：治理重点是法域差异和规则引用。原 skill 引用 FINRA、SEC、FinCEN、ERISA、GIPS 等美国规则，不能直接作为中国业务判断依据。

### FSK-126 `fiduciary-standards`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/compliance/skills/fiduciary-standards/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/compliance/skills/fiduciary-standards/SKILL.md`。
- **原始定位**：上游描述：Apply fiduciary duty standards across the investment advisory landscape, including IA Act Section 206, ERISA, DOL rules, and CFA Institute standards. Use when the user asks whether a fiduciary standard applies, how fiduciary duty differs from Reg BI or suitability, what the duty of care and duty of loyalty require, ERISA Section 404 prudent expert obligations, PTE 2020-02 rollover exemptions, or state-level fiduciary developments. Also trigger when users mention 'are we a fiduciary here', 'best interest vs suitability', 'dual registrant hat switching', 'retirement plan adviser obligations', 'DOL fiduciary rule', or ask what standard of care applies to a recommendation.
- **金融业务理解**：这一类集中在美国证券和投资顾问合规，包括 KYC、AML、Reg BI、受托责任、广告合规、记录保存、隐私和监管检查。它适合作为“合规知识如何写进 skill”的优秀样本。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于对照中国银行业反洗钱、消费者保护、销售适当性、数据安全和监管检查要求，设计中文本地化合规 skill。
- **风险与治理边界**：治理重点是法域差异和规则引用。原 skill 引用 FINRA、SEC、FinCEN、ERISA、GIPS 等美国规则，不能直接作为中国业务判断依据。

### FSK-127 `gips-compliance`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/compliance/skills/gips-compliance/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/compliance/skills/gips-compliance/SKILL.md`。
- **原始定位**：上游描述：Ensure investment firms satisfy CFA Institute GIPS requirements for composite construction, performance calculation, presentation, and verification. Use when the user asks about building composites, time-weighted return calculation, GIPS-compliant presentations, error correction policies, pooled fund reporting, wrap fee or SMA program performance, or GIPS advertising guidelines. Also trigger when users mention 'claiming GIPS compliance', 'composite membership rules', 'terminated portfolio returns', 'gross vs net of fees under GIPS', 'GIPS verification findings', 'can we show this track record to prospects', or ask whether a firm's performance reporting meets GIPS standards.
- **金融业务理解**：这一类集中在美国证券和投资顾问合规，包括 KYC、AML、Reg BI、受托责任、广告合规、记录保存、隐私和监管检查。它适合作为“合规知识如何写进 skill”的优秀样本。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于对照中国银行业反洗钱、消费者保护、销售适当性、数据安全和监管检查要求，设计中文本地化合规 skill。
- **风险与治理边界**：治理重点是法域差异和规则引用。原 skill 引用 FINRA、SEC、FinCEN、ERISA、GIPS 等美国规则，不能直接作为中国业务判断依据。

### FSK-128 `investment-suitability`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/compliance/skills/investment-suitability/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/compliance/skills/investment-suitability/SKILL.md`。
- **原始定位**：上游描述：Assess investment suitability obligations under FINRA Rules 2111 and 2090 across all three suitability prongs. Use when the user asks about reasonable-basis, customer-specific, or quantitative suitability, product-specific concerns for complex products, leveraged ETFs, variable annuities, or alternatives, household-level suitability, hold recommendations, or the institutional suitability exemption. Also trigger when users mention 'is this investment suitable', 'turnover ratio is too high', 'cost-to-equity ratio', 'churning metrics', 'suitability questionnaire design', 'complex product due diligence', 'customer refused to provide their risk tolerance', or ask whether a recommendation fits a customer's profile.
- **金融业务理解**：这一类集中在美国证券和投资顾问合规，包括 KYC、AML、Reg BI、受托责任、广告合规、记录保存、隐私和监管检查。它适合作为“合规知识如何写进 skill”的优秀样本。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于对照中国银行业反洗钱、消费者保护、销售适当性、数据安全和监管检查要求，设计中文本地化合规 skill。
- **风险与治理边界**：治理重点是法域差异和规则引用。原 skill 引用 FINRA、SEC、FinCEN、ERISA、GIPS 等美国规则，不能直接作为中国业务判断依据。

### FSK-129 `know-your-customer`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/compliance/skills/know-your-customer/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/compliance/skills/know-your-customer/SKILL.md`。
- **原始定位**：上游描述：Guide the implementation of customer identification, due diligence, and ongoing monitoring under FINRA Rule 2090, CIP, and the FinCEN CDD Rule. Use when the user asks about customer onboarding identity verification, beneficial ownership collection for entity accounts, enhanced due diligence for PEPs or high-risk customers, customer risk rating systems, KYC refresh triggers, or documentary vs non-documentary verification. Also trigger when users mention 'account opening requirements', 'who is the beneficial owner', 'new client identity check', 'how often to update KYC', 'essential facts for the account', 'foreign customer onboarding', or ask what information must be gathered before opening an account.
- **金融业务理解**：这一类集中在美国证券和投资顾问合规，包括 KYC、AML、Reg BI、受托责任、广告合规、记录保存、隐私和监管检查。它适合作为“合规知识如何写进 skill”的优秀样本。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于对照中国银行业反洗钱、消费者保护、销售适当性、数据安全和监管检查要求，设计中文本地化合规 skill。
- **风险与治理边界**：治理重点是法域差异和规则引用。原 skill 引用 FINRA、SEC、FinCEN、ERISA、GIPS 等美国规则，不能直接作为中国业务判断依据。

### FSK-130 `privacy-data-security`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/compliance/skills/privacy-data-security/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/compliance/skills/privacy-data-security/SKILL.md`。
- **原始定位**：上游描述：Design and operate privacy and data security programs for SEC-registered firms under Reg S-P, Reg S-ID, and SEC cybersecurity expectations. Use when the user asks about privacy notices, the Safeguards Rule, identity theft prevention programs, breach notification obligations, vendor security due diligence, incident response planning, data classification, or state privacy law compliance. Also trigger when users mention 'customer data was exposed', 'do we need to notify clients of a breach', 'cybersecurity exam prep', 'cloud vendor risk assessment', 'encrypting client data', 'BYOD security policy', 'Red Flags Rule', 'NY DFS 500 requirements', or ask how to handle a cybersecurity incident.
- **金融业务理解**：这一类集中在美国证券和投资顾问合规，包括 KYC、AML、Reg BI、受托责任、广告合规、记录保存、隐私和监管检查。它适合作为“合规知识如何写进 skill”的优秀样本。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于对照中国银行业反洗钱、消费者保护、销售适当性、数据安全和监管检查要求，设计中文本地化合规 skill。
- **风险与治理边界**：治理重点是法域差异和规则引用。原 skill 引用 FINRA、SEC、FinCEN、ERISA、GIPS 等美国规则，不能直接作为中国业务判断依据。

### FSK-131 `reg-bi`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/compliance/skills/reg-bi/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/compliance/skills/reg-bi/SKILL.md`。
- **原始定位**：上游描述：Analyze broker-dealer recommendations under SEC Regulation Best Interest's four obligations: Disclosure, Care, Conflict of Interest, and Compliance. Use when the user asks whether a recommendation satisfies Reg BI, what triggers the 'recommendation' standard, how to evaluate reasonably available alternatives, rollover recommendation compliance, dual-registrant capacity disclosure, share class or account type recommendations, or Reg BI examination preparation. Also trigger when users mention 'best interest standard for brokers', 'is this a Reg BI recommendation', 'care obligation documentation', 'sales contest elimination requirement', 'Form CRS delivery', or ask how Reg BI differs from suitability or fiduciary duty.
- **金融业务理解**：这一类集中在美国证券和投资顾问合规，包括 KYC、AML、Reg BI、受托责任、广告合规、记录保存、隐私和监管检查。它适合作为“合规知识如何写进 skill”的优秀样本。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于对照中国银行业反洗钱、消费者保护、销售适当性、数据安全和监管检查要求，设计中文本地化合规 skill。
- **风险与治理边界**：治理重点是法域差异和规则引用。原 skill 引用 FINRA、SEC、FinCEN、ERISA、GIPS 等美国规则，不能直接作为中国业务判断依据。

### FSK-132 `regulatory-reporting`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/compliance/skills/regulatory-reporting/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/compliance/skills/regulatory-reporting/SKILL.md`。
- **原始定位**：上游描述：Guide regulatory filing obligations and deadlines for investment advisers, broker-dealers, and large traders. Use when the user asks about Form PF filing thresholds, 13F institutional holdings reports, 13H large trader filings, Form ADV amendment timing, FOCUS report preparation, blue sheet requests, CAT reporting infrastructure, or FINRA short interest and TRACE reporting. Also trigger when users mention 'filing deadline calendar', 'do we need to file Form PF', 'crossed the $100M 13F threshold', 'annual updating amendment', 'CAT clock synchronization', 'how to respond to a blue sheet request', 'FOCUS report errors', or ask which regulatory filings a firm must make and when.
- **金融业务理解**：这一类集中在美国证券和投资顾问合规，包括 KYC、AML、Reg BI、受托责任、广告合规、记录保存、隐私和监管检查。它适合作为“合规知识如何写进 skill”的优秀样本。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于对照中国银行业反洗钱、消费者保护、销售适当性、数据安全和监管检查要求，设计中文本地化合规 skill。
- **风险与治理边界**：治理重点是法域差异和规则引用。原 skill 引用 FINRA、SEC、FinCEN、ERISA、GIPS 等美国规则，不能直接作为中国业务判断依据。

### FSK-133 `sales-practices`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/compliance/skills/sales-practices/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/compliance/skills/sales-practices/SKILL.md`。
- **原始定位**：上游描述：Identify and prevent sales practice violations under FINRA and SEC rules governing broker-dealer conduct. Use when the user asks about churning or excessive trading metrics, mutual fund breakpoint discounts, selling away or private securities transactions, outside business activities, unauthorized trading, supervisory procedure design, senior investor protections, trusted contact persons, variable annuity suitability, or options account approval. Also trigger when users mention 'turnover ratio is high', 'rep did trades without authorization', 'breakpoint abuse', 'trusted contact for elderly client', 'selling away from the firm', 'supervision failure', '1035 exchange review', 'marking the close', or ask whether a broker's conduct violates FINRA rules.
- **金融业务理解**：这一类集中在美国证券和投资顾问合规，包括 KYC、AML、Reg BI、受托责任、广告合规、记录保存、隐私和监管检查。它适合作为“合规知识如何写进 skill”的优秀样本。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于对照中国银行业反洗钱、消费者保护、销售适当性、数据安全和监管检查要求，设计中文本地化合规 skill。
- **风险与治理边界**：治理重点是法域差异和规则引用。原 skill 引用 FINRA、SEC、FinCEN、ERISA、GIPS 等美国规则，不能直接作为中国业务判断依据。

## 金融数学与统计基础

### FSK-134 `return-calculations`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/core/skills/return-calculations/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/core/skills/return-calculations/SKILL.md`。
- **原始定位**：上游描述：Compute and compare investment return metrics including TWR, MWR/IRR, CAGR, and annualized returns. Use when the user asks about portfolio performance calculation, comparing manager returns, linking sub-period returns, understanding why different return methods give different numbers, or converting returns across time periods. Also trigger when users mention 'how much did I make', 'annual return', 'compound growth', 'dollar-weighted vs time-weighted', 'what was my rate of return', 'geometric vs arithmetic mean', 'log returns', or ask about the effect of cash flows on reported returns.
- **金融业务理解**：这一类是所有金融分析的数学底座，包括收益率、时间价值、IRR、现值、统计分布、协方差和回归等。对银行从业者来说，它能把日常看到的收益、期限、利率、风险指标重新连接到底层计算逻辑。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可迁移到本项目的 AI/ML 基础和金融基础模块，用来做“金融计算公式 + Python 小实验 + 银行业务解释”的入门练习。
- **风险与治理边界**：治理重点是公式口径和输入单位。收益率、期限、年化、现金流方向和频率一旦设错，结果会完全不同，必须保留计算假设和复核样例。

### FSK-135 `statistics-fundamentals`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/core/skills/statistics-fundamentals/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/core/skills/statistics-fundamentals/SKILL.md`。
- **原始定位**：上游描述：Apply statistical methods to financial data including descriptive statistics, covariance estimation, regression, hypothesis testing, and resampling. Use when the user asks about return distributions, correlation between assets, building a covariance matrix, running a CAPM regression, testing whether alpha is significant, checking if returns are normal, or estimating confidence intervals. Also trigger when users mention 'volatility', 'how correlated are these', 'fat tails', 'skewness', 'R-squared', 'beta of a fund', 'bootstrap a Sharpe ratio', 'shrinkage estimator', 'Ledoit-Wolf', or ask why their optimizer produces unstable weights.
- **金融业务理解**：这一类是所有金融分析的数学底座，包括收益率、时间价值、IRR、现值、统计分布、协方差和回归等。对银行从业者来说，它能把日常看到的收益、期限、利率、风险指标重新连接到底层计算逻辑。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可迁移到本项目的 AI/ML 基础和金融基础模块，用来做“金融计算公式 + Python 小实验 + 银行业务解释”的入门练习。
- **风险与治理边界**：治理重点是公式口径和输入单位。收益率、期限、年化、现金流方向和频率一旦设错，结果会完全不同，必须保留计算假设和复核样例。

### FSK-136 `time-value-of-money`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/core/skills/time-value-of-money/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/core/skills/time-value-of-money/SKILL.md`。
- **原始定位**：上游描述：Calculate present value, future value, NPV, IRR, loan payments, and amortization schedules across all compounding conventions. Use when the user asks about discounting cash flows, valuing an annuity or perpetuity, comparing investments with different timing, building a mortgage amortization table, or evaluating whether a project is worth pursuing. Also trigger when users mention 'what is it worth today', 'how much will I have in 20 years', 'monthly payment on a loan', 'discount rate', 'Gordon growth model', 'effective annual rate', 'continuous compounding', or ask how to compare a lump sum versus a stream of payments.
- **金融业务理解**：这一类是所有金融分析的数学底座，包括收益率、时间价值、IRR、现值、统计分布、协方差和回归等。对银行从业者来说，它能把日常看到的收益、期限、利率、风险指标重新连接到底层计算逻辑。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可迁移到本项目的 AI/ML 基础和金融基础模块，用来做“金融计算公式 + Python 小实验 + 银行业务解释”的入门练习。
- **风险与治理边界**：治理重点是公式口径和输入单位。收益率、期限、年化、现金流方向和频率一旦设错，结果会完全不同，必须保留计算假设和复核样例。

## 金融数据集成、质量与主数据

### FSK-137 `data-quality`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/data-integration/skills/data-quality/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/data-integration/skills/data-quality/SKILL.md`。
- **原始定位**：上游描述：Design and operate data quality programs for financial data — golden source architecture, validation rules, data lineage, exception management, profiling, and governance. Use when building validation rules for pricing or client data pipelines, designing a data quality monitoring framework, establishing golden source designations across systems, implementing data lineage for BCBS 239 or MiFID II, investigating reconciliation breaks or billing errors traced to bad data, preparing for regulatory exams on data accuracy, building data quality scorecards, or defining data stewardship roles. Trigger on: data quality, golden source, data lineage, data validation, data profiling, exception management, data governance, BCBS 239, data completeness, data accuracy, validation rules, data anomaly, data stewardship, data quality scorecard.
- **金融业务理解**：这一类关注金融数据接入、参考数据、市场数据、集成模式和数据质量，是金融 AI 能否稳定落地的基础设施层。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于扩展本项目的 06 数据工程模块，建立金融数据字典、数据质量规则、主数据管理和接口治理模板。
- **风险与治理边界**：治理重点是数据血缘、授权和质量监控。需要记录来源、刷新频率、字段含义、缺失值处理、异常阈值和访问权限。

### FSK-138 `integration-patterns`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/data-integration/skills/integration-patterns/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/data-integration/skills/integration-patterns/SKILL.md`。
- **原始定位**：上游描述：Design and implement integration architectures connecting financial systems — APIs, FIX protocol, ISO 20022, event-driven patterns, batch feeds, idempotency, and resilience. Use when building custodian integration pipelines, implementing FIX connectivity for order routing, designing ISO 20022 or SWIFT migration messaging, building batch file processing for custodian feeds or EOD reconciliation, implementing idempotency for transaction APIs, designing retry or circuit breaker patterns, mapping data between systems with different schemas, or troubleshooting integration failures causing recon breaks. Trigger on: FIX protocol, ISO 20022, custodian feed, batch processing, API design, idempotency, circuit breaker, dead letter queue, data mapping, integration architecture, SWIFT migration, mTLS, file feed, event-driven, message broker.
- **金融业务理解**：这一类关注金融数据接入、参考数据、市场数据、集成模式和数据质量，是金融 AI 能否稳定落地的基础设施层。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于扩展本项目的 06 数据工程模块，建立金融数据字典、数据质量规则、主数据管理和接口治理模板。
- **风险与治理边界**：治理重点是数据血缘、授权和质量监控。需要记录来源、刷新频率、字段含义、缺失值处理、异常阈值和访问权限。

### FSK-139 `market-data`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/data-integration/skills/market-data/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/data-integration/skills/market-data/SKILL.md`。
- **原始定位**：上游描述：Design and manage market data infrastructure — real-time and delayed feeds, Level 1/2/3 depth, consolidated tape vs direct feeds, vendor selection, licensing, and distribution architecture. Use when choosing between real-time and delayed data, evaluating market data vendors like Bloomberg or Refinitiv, designing ticker plants or fan-out architecture, managing exchange data licensing and entitlements, diagnosing stale quotes or missing ticks, deciding between SIP and direct exchange feeds, or assessing Level 2/3 depth-of-book requirements for trading. Trigger on: market data, Level 1/2/3, depth of book, consolidated tape, SIP, direct feed, NBBO, ticker plant, B-PIPE, data license, non-display use, market data entitlements, conflation, tick data, real-time feed.
- **金融业务理解**：这一类关注金融数据接入、参考数据、市场数据、集成模式和数据质量，是金融 AI 能否稳定落地的基础设施层。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于扩展本项目的 06 数据工程模块，建立金融数据字典、数据质量规则、主数据管理和接口治理模板。
- **风险与治理边界**：治理重点是数据血缘、授权和质量监控。需要记录来源、刷新频率、字段含义、缺失值处理、异常阈值和访问权限。

### FSK-140 `reference-data`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/data-integration/skills/reference-data/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/data-integration/skills/reference-data/SKILL.md`。
- **原始定位**：上游描述：Design and manage reference data systems — security master, client master, account master, identifier mapping, pricing data, and governance. Use when building or evaluating a security master database, mapping identifiers across systems (CUSIP to ISIN, SEDOL to FIGI), designing client master models for onboarding or KYC, defining account master attributes across custodians, implementing pricing validation with vendor hierarchy, establishing reference data governance and stewardship, handling identifier changes from corporate actions, or troubleshooting data quality issues traced to stale prices or missing identifiers. Trigger on: security master, CUSIP, ISIN, SEDOL, FIGI, client master, account master, pricing data, reference data, golden source, MDM, master data, identifier mapping, data governance, pricing validation.
- **金融业务理解**：这一类关注金融数据接入、参考数据、市场数据、集成模式和数据质量，是金融 AI 能否稳定落地的基础设施层。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于扩展本项目的 06 数据工程模块，建立金融数据字典、数据质量规则、主数据管理和接口治理模板。
- **风险与治理边界**：治理重点是数据血缘、授权和质量监控。需要记录来源、刷新频率、字段含义、缺失值处理、异常阈值和访问权限。

## 交易运营、清算交收与操作风险

### FSK-141 `counterparty-risk`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/trading-operations/skills/counterparty-risk/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/trading-operations/skills/counterparty-risk/SKILL.md`。
- **原始定位**：上游描述：Guide counterparty credit risk measurement and management for OTC and securities trading. Use when measuring current or potential future exposure to a counterparty, setting or reviewing counterparty credit limits, evaluating ISDA Master Agreement netting benefits, designing collateral management or CSA terms, assessing central clearing mandates under Dodd-Frank or EMIR, monitoring counterparty creditworthiness via CDS spreads or ratings, managing Herstatt or settlement risk in FX, quantifying wrong-way risk, or building real-time exposure dashboards. Also use for counterparty default scenarios, credit deterioration events, EAD and SA-CCR calculations, and CVA capital charges.
- **金融业务理解**：这一类覆盖交易前合规、交易执行、订单生命周期、交易后合规、清算交收、保证金、交易对手风险、交易所连接和操作风险。它适合理解“交易不是点击买卖，而是一条很长的运营和控制链”。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于补充金融市场、资管、托管和运营模块，设计交易生命周期、清算交收、异常处理和风险控制的学习图谱。
- **风险与治理边界**：治理重点是只读和禁止自动交易。任何 AI 工具都不能绕过授权、额度、合规校验和人工确认去执行交易。

### FSK-142 `exchange-connectivity`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/trading-operations/skills/exchange-connectivity/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/trading-operations/skills/exchange-connectivity/SKILL.md`。
- **原始定位**：上游描述：Guide the design and management of trading venue connectivity and market data infrastructure. Use when building or troubleshooting FIX sessions for order routing or drop copy, integrating exchange protocols like OUCH, ITCH, PITCH, or Pillar, designing market data feed architecture, handling trading halts or circuit breakers or LULD bands, mapping symbology across CUSIP/ISIN/SEDOL/FIGI, planning co-location or proximity hosting, designing failover and DR for exchange connectivity, implementing Rule 15c3-5 market access controls, building session scheduling for pre-market and post-market windows, resolving FIX sequence number gaps, or planning CAT reporting infrastructure.
- **金融业务理解**：这一类覆盖交易前合规、交易执行、订单生命周期、交易后合规、清算交收、保证金、交易对手风险、交易所连接和操作风险。它适合理解“交易不是点击买卖，而是一条很长的运营和控制链”。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于补充金融市场、资管、托管和运营模块，设计交易生命周期、清算交收、异常处理和风险控制的学习图谱。
- **风险与治理边界**：治理重点是只读和禁止自动交易。任何 AI 工具都不能绕过授权、额度、合规校验和人工确认去执行交易。

### FSK-143 `margin-operations`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/trading-operations/skills/margin-operations/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/trading-operations/skills/margin-operations/SKILL.md`。
- **原始定位**：上游描述：Guide margin lending, margin requirements, and margin call operations for brokerage and advisory accounts. Use when calculating Reg T initial margin or buying power, determining maintenance margin or house requirements, evaluating portfolio margin eligibility under OCC TIMS, generating or resolving margin calls (fed call, house call, exchange call, day-trade call), designing forced liquidation waterfall logic, structuring securities-backed lines of credit (SBLOC), computing margin interest impact on returns, assessing concentrated position margin, understanding pattern day trader rules, or reviewing FINRA 4210 and Reg U requirements. Also covers SMA calculations and short margin mechanics.
- **金融业务理解**：这一类覆盖交易前合规、交易执行、订单生命周期、交易后合规、清算交收、保证金、交易对手风险、交易所连接和操作风险。它适合理解“交易不是点击买卖，而是一条很长的运营和控制链”。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于补充金融市场、资管、托管和运营模块，设计交易生命周期、清算交收、异常处理和风险控制的学习图谱。
- **风险与治理边界**：治理重点是只读和禁止自动交易。任何 AI 工具都不能绕过授权、额度、合规校验和人工确认去执行交易。

### FSK-144 `operational-risk`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/trading-operations/skills/operational-risk/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/trading-operations/skills/operational-risk/SKILL.md`。
- **原始定位**：上游描述：Guide identification, measurement, and management of operational risk in trading and brokerage operations. Use when designing trade error detection and correction procedures, investigating trade breaks and reconciliation failures, classifying loss events under Basel taxonomy, developing key risk indicators (KRIs) and dashboards, responding to system outages or data feed failures or order routing errors, conducting root cause analysis after a trade error or settlement fail, planning business continuity and disaster recovery for trading desks, preparing for FINRA or SEC operational risk examinations, or assessing technology risk in OMS and market data systems. Also covers fat-finger errors, error account P&L, and corrective action tracking.
- **金融业务理解**：这一类覆盖交易前合规、交易执行、订单生命周期、交易后合规、清算交收、保证金、交易对手风险、交易所连接和操作风险。它适合理解“交易不是点击买卖，而是一条很长的运营和控制链”。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于补充金融市场、资管、托管和运营模块，设计交易生命周期、清算交收、异常处理和风险控制的学习图谱。
- **风险与治理边界**：治理重点是只读和禁止自动交易。任何 AI 工具都不能绕过授权、额度、合规校验和人工确认去执行交易。

### FSK-145 `order-lifecycle`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/trading-operations/skills/order-lifecycle/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/trading-operations/skills/order-lifecycle/SKILL.md`。
- **原始定位**：上游描述：Guide the design and implementation of order lifecycle management in trading systems. Use when building an order state machine for an OMS or EMS, implementing or debugging FIX protocol connectivity to exchanges, handling cancel/replace race conditions, defining pre-submission validation rules (buying power, position limits, restricted lists), selecting order types and time-in-force instructions, designing multi-leg or OCO or bracket orders, building CAT-compliant audit trails, troubleshooting order rejections or unexpected state transitions, hardening an OMS against edge cases, or implementing order persistence and recovery for failover. Also covers FIX message flows, ClOrdID chaining, and partial fill aggregation.
- **金融业务理解**：这一类覆盖交易前合规、交易执行、订单生命周期、交易后合规、清算交收、保证金、交易对手风险、交易所连接和操作风险。它适合理解“交易不是点击买卖，而是一条很长的运营和控制链”。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于补充金融市场、资管、托管和运营模块，设计交易生命周期、清算交收、异常处理和风险控制的学习图谱。
- **风险与治理边界**：治理重点是只读和禁止自动交易。任何 AI 工具都不能绕过授权、额度、合规校验和人工确认去执行交易。

### FSK-146 `post-trade-compliance`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/trading-operations/skills/post-trade-compliance/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/trading-operations/skills/post-trade-compliance/SKILL.md`。
- **原始定位**：上游描述：Guide post-trade compliance monitoring and trade surveillance system design. Use when building alert logic to detect churning, front-running, cherry-picking, layering, spoofing, wash trading, or marking the close, implementing post-trade best execution review, evaluating allocation fairness with pro-rata verification or dispersion analysis, designing exception-based monitoring workflows with escalation paths, correlating trading with MNPI events for insider trading detection, building personal trading surveillance for preclearance and blackout enforcement, determining SAR or blue sheet or CAT reporting triggers, or tuning surveillance thresholds to reduce false positives. Also covers turnover ratios, cost-to-equity ratios, and investigation case management.
- **金融业务理解**：这一类覆盖交易前合规、交易执行、订单生命周期、交易后合规、清算交收、保证金、交易对手风险、交易所连接和操作风险。它适合理解“交易不是点击买卖，而是一条很长的运营和控制链”。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于补充金融市场、资管、托管和运营模块，设计交易生命周期、清算交收、异常处理和风险控制的学习图谱。
- **风险与治理边界**：治理重点是只读和禁止自动交易。任何 AI 工具都不能绕过授权、额度、合规校验和人工确认去执行交易。

### FSK-147 `pre-trade-compliance`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/trading-operations/skills/pre-trade-compliance/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/trading-operations/skills/pre-trade-compliance/SKILL.md`。
- **原始定位**：上游描述：Guide the design and implementation of automated pre-trade compliance systems that validate orders before execution. Use when building a compliance rule engine for an RIA or broker-dealer, configuring hard blocks and soft blocks, maintaining restricted and watch lists including MNPI-driven restrictions, setting concentration limits at security/sector/issuer level, implementing position limits or short selling controls, enforcing wash sale detection or free-riding prevention or pattern day trader identification, applying client-specific ESG screens or legal constraints, designing compliance override workflows with authorization and documentation, backtesting compliance rules, or evaluating compliance check latency impact on execution quality.
- **金融业务理解**：这一类覆盖交易前合规、交易执行、订单生命周期、交易后合规、清算交收、保证金、交易对手风险、交易所连接和操作风险。它适合理解“交易不是点击买卖，而是一条很长的运营和控制链”。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于补充金融市场、资管、托管和运营模块，设计交易生命周期、清算交收、异常处理和风险控制的学习图谱。
- **风险与治理边界**：治理重点是只读和禁止自动交易。任何 AI 工具都不能绕过授权、额度、合规校验和人工确认去执行交易。

### FSK-148 `settlement-clearing`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/trading-operations/skills/settlement-clearing/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/trading-operations/skills/settlement-clearing/SKILL.md`。
- **原始定位**：上游描述：Guide the understanding and management of trade settlement and clearing processes. Use when designing settlement workflows for T+1 compliance, understanding DTC/NSCC/FICC clearing infrastructure, analyzing continuous net settlement (CNS) netting obligations, setting up institutional trade processing (affirmation, confirmation, allocation, matching), investigating settlement fails and designing fail reduction programs, implementing buy-in procedures under Reg SHO Rule 204, assessing corporate action impact on pending settlements, evaluating DVP/RVP mechanics for institutional deliveries, handling when-issued or as-of trades, or managing settlement bank relationships and intraday liquidity. Also covers FX funding gaps for cross-border T+1 settlement.
- **金融业务理解**：这一类覆盖交易前合规、交易执行、订单生命周期、交易后合规、清算交收、保证金、交易对手风险、交易所连接和操作风险。它适合理解“交易不是点击买卖，而是一条很长的运营和控制链”。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于补充金融市场、资管、托管和运营模块，设计交易生命周期、清算交收、异常处理和风险控制的学习图谱。
- **风险与治理边界**：治理重点是只读和禁止自动交易。任何 AI 工具都不能绕过授权、额度、合规校验和人工确认去执行交易。

### FSK-149 `trade-execution`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/trading-operations/skills/trade-execution/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/trading-operations/skills/trade-execution/SKILL.md`。
- **原始定位**：上游描述：Guide the design, evaluation, and monitoring of trade execution quality and best execution practices. Use when assessing best execution obligations under FINRA Rule 5310 or RIA fiduciary duty, designing smart order routing across exchanges and dark pools, selecting execution algorithms (VWAP, TWAP, implementation shortfall, POV), building transaction cost analysis (TCA) for pre-trade estimation or post-trade measurement, analyzing bid-ask spread decomposition or market impact or information leakage, conducting best execution committee reviews, evaluating payment for order flow (PFOF) arrangements, interpreting Rule 605/606 reports, or handling fixed income or ETF execution via RFQ protocols. Also covers Reg NMS Order Protection Rule and venue fee structures.
- **金融业务理解**：这一类覆盖交易前合规、交易执行、订单生命周期、交易后合规、清算交收、保证金、交易对手风险、交易所连接和操作风险。它适合理解“交易不是点击买卖，而是一条很长的运营和控制链”。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于补充金融市场、资管、托管和运营模块，设计交易生命周期、清算交收、异常处理和风险控制的学习图谱。
- **风险与治理边界**：治理重点是只读和禁止自动交易。任何 AI 工具都不能绕过授权、额度、合规校验和人工确认去执行交易。

## 财富管理、资产配置与投资知识

### FSK-150 `alternatives`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/alternatives/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/alternatives/SKILL.md`。
- **原始定位**：上游描述：Analyze alternative investments including hedge funds, private equity, and venture capital. Use when the user asks about hedge fund strategies (long/short, macro, event-driven), PE or VC performance metrics (IRR, TVPI, DPI), fee structures ('2-and-20', carry, hurdle rates), the J-curve effect, illiquidity premiums, lock-up periods, or hedge fund replication. Also trigger when users mention 'managed futures', 'CTA', 'fund of funds', 'vintage year', 'capital calls', 'distributions', 'carried interest', or ask how to evaluate an alternative investment manager.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-151 `asset-allocation`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/asset-allocation/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/asset-allocation/SKILL.md`。
- **原始定位**：上游描述：Determine how to distribute capital across asset classes using strategic and tactical allocation frameworks. Use when the user asks about portfolio allocation, mean-variance optimization, Black-Litterman, risk parity, glide paths, or target-date strategies. Also trigger when users mention 'how much in stocks vs bonds', '60/40 portfolio', 'policy portfolio', 'core-satellite', 'liability-driven investing', 'asset-liability matching', or ask how to split their money across investments.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-152 `bet-sizing`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/bet-sizing/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/bet-sizing/SKILL.md`。
- **原始定位**：上游描述：Determine how much capital to allocate to individual positions within a portfolio. Use when the user asks about position sizing, the Kelly criterion, fractional Kelly, risk budgeting, or conviction weighting. Also trigger when users mention 'how much to put in one stock', 'maximum position size', 'how concentrated should my portfolio be', 'number of holdings', 'VaR budget per position', 'how big a bet', or ask about scaling position sizes with volatility.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-153 `commodities`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/commodities/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/commodities/SKILL.md`。
- **原始定位**：上游描述：Analyze commodity markets including futures curve dynamics, roll yield, and supply/demand fundamentals. Use when the user asks about commodity investing, commodity ETFs, contango, backwardation, roll yield, commodity indices (GSCI, BCOM), or commodities as an inflation hedge. Also trigger when users mention 'oil prices', 'gold as a safe haven', 'agricultural futures', 'convenience yield', 'storage costs', 'natural gas', 'copper demand', or ask why commodity ETF returns differ from spot price changes.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-154 `currencies-and-fx`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/currencies-and-fx/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/currencies-and-fx/SKILL.md`。
- **原始定位**：上游描述：Analyze currency markets, exchange rate mechanics, and FX risk management for international portfolios. Use when the user asks about exchange rates, FX hedging, interest rate parity, carry trades, forward premiums, cross rates, or currency overlay programs. Also trigger when users mention 'strong dollar', 'weak euro', 'hedging foreign stocks', 'purchasing power parity', 'currency risk in my portfolio', 'EUR/USD', 'yen carry trade', or ask whether to hedge international investments.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-155 `debt-management`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/debt-management/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/debt-management/SKILL.md`。
- **原始定位**：上游描述：Provide frameworks for managing and paying off personal debt effectively. Use when the user asks about debt payoff strategies (avalanche vs snowball), refinancing decisions, debt consolidation, debt-to-income ratios, or the opportunity cost of paying off debt vs investing. Also trigger when users mention 'which debt to pay first', 'should I refinance', 'credit card debt', 'student loan payoff', 'DTI for mortgage', 'balance transfer', 'good debt vs bad debt', or ask how to get out of debt faster.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-156 `digital-assets`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/digital-assets/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/digital-assets/SKILL.md`。
- **原始定位**：上游描述：Analyze digital assets including cryptocurrency fundamentals, blockchain mechanics, DeFi protocols, and on-chain metrics. Use when the user asks about crypto investing, Bitcoin, Ethereum, staking yields, DeFi lending, impermanent loss, or on-chain valuation metrics. Also trigger when users mention 'blockchain', 'proof of stake', 'proof of work', 'smart contracts', 'NFTs', 'stablecoins', 'NVT ratio', 'TVL', 'crypto portfolio allocation', 'halving', or ask about risks and returns of cryptocurrency.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-157 `diversification`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/diversification/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/diversification/SKILL.md`。
- **原始定位**：上游描述：Build diversified portfolios using correlation analysis, efficient frontier construction, and factor-based diversification. Use when the user asks about portfolio variance, correlation effects, the efficient frontier, minimum variance portfolios, diversification ratios, or factor diversification. Also trigger when users mention 'don't put all eggs in one basket', 'how many stocks do I need', 'correlation breakdown in a crisis', 'are my holdings really diversified', 'risk contributions', or ask why diversification fails during market crashes.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-158 `emergency-fund`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/emergency-fund/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/emergency-fund/SKILL.md`。
- **原始定位**：上游描述：Size and structure an emergency fund based on individual circumstances, income stability, and expense profile. Use when the user asks about emergency fund sizing, how many months of expenses to save, where to keep emergency savings, or tiered fund structures. Also trigger when users mention 'rainy day fund', 'how much cash should I keep', 'high-yield savings account', 'money market fund', 'freelancer cash reserve', 'variable income buffer', or ask what counts as an emergency expense.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-159 `equities`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/equities/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/equities/SKILL.md`。
- **原始定位**：上游描述：Analyze equity securities, factor models, and equity portfolio construction. Use when the user asks about stocks, equity valuation ratios, index construction methods, or style analysis. Also trigger when users mention 'P/E ratio', 'growth vs value', 'market cap weighting', 'sector allocation', 'GICS classification', 'earnings per share', 'Fama-French factors', 'CAPM', 'dividend yield', 'PEG ratio', 'EV/EBITDA', or ask which factors explain equity returns.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-160 `finance-psychology`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/finance-psychology/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/finance-psychology/SKILL.md`。
- **原始定位**：上游描述：Recognize and mitigate cognitive biases that impair financial decisions, and coach clients toward values-driven financial lives. Use when the user asks about behavioral finance, money psychology, loss aversion, overconfidence, herd behavior, or emotional investing. Also trigger when users mention 'why do I panic sell', 'money fights with my spouse', 'I can never save enough', 'fear of investing', 'lifestyle creep', 'keeping up with the Joneses', 'Rich Life', 'money scripts', or ask how emotions affect financial decisions.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-161 `fixed-income-corporate`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/fixed-income-corporate/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/fixed-income-corporate/SKILL.md`。
- **原始定位**：上游描述：Analyze corporate bonds and credit instruments including investment grade and high yield debt. Use when the user asks about corporate bonds, credit spreads (OAS, Z-spread, G-spread), credit ratings, default probabilities, callable bonds, or private credit. Also trigger when users mention 'junk bonds', 'fallen angel', 'yield-to-worst', 'covenant analysis', 'CDS spreads', 'recovery rates', 'direct lending', 'mezzanine debt', 'BBB downgrade risk', or ask how to evaluate corporate credit risk.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-162 `fixed-income-municipal`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/fixed-income-municipal/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/fixed-income-municipal/SKILL.md`。
- **原始定位**：上游描述：Analyze municipal bonds including tax-equivalent yield calculations, GO vs revenue bond evaluation, and muni credit analysis. Use when the user asks about municipal bonds, tax-exempt income, tax-equivalent yield, AMT bonds, or muni credit quality. Also trigger when users mention 'muni bonds', 'tax-free bonds', 'state tax exemption', 'general obligation', 'revenue bonds', 'Build America Bonds', 'muni yield ratio', 'de minimis rule', or ask whether munis make sense for their tax bracket.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-163 `fixed-income-sovereign`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/fixed-income-sovereign/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/fixed-income-sovereign/SKILL.md`。
- **原始定位**：上游描述：Analyze government bonds including US Treasuries, yield curves, duration, convexity, and TIPS. Use when the user asks about Treasury bonds, sovereign debt, yield curve construction, interest rate risk, duration, convexity, TIPS, or breakeven inflation rates. Also trigger when users mention 'T-bills', 'T-notes', 'bond pricing', 'yield to maturity', 'inverted yield curve', 'forward rates', 'spot rates', 'DV01', 'real yields', or ask how bonds react to interest rate changes.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-164 `fixed-income-structured`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/fixed-income-structured/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/fixed-income-structured/SKILL.md`。
- **原始定位**：上游描述：Analyze structured fixed income products including mortgage-backed securities, asset-backed securities, and CLOs. Use when the user asks about MBS, ABS, CLOs, CDOs, prepayment risk, tranching, or waterfall structures. Also trigger when users mention 'mortgage bonds', 'agency MBS', 'pass-through securities', 'PSA prepayment speed', 'negative convexity', 'extension risk', 'contraction risk', 'CMO tranches', 'securitization', or ask how structured products redistribute credit and prepayment risk.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-165 `forward-risk`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/forward-risk/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/forward-risk/SKILL.md`。
- **原始定位**：上游描述：Estimate potential future losses using VaR, Expected Shortfall, Monte Carlo simulation, and stress testing. Use when the user asks about Value-at-Risk, CVaR, Expected Shortfall, scenario analysis, stress testing, or factor-based risk decomposition. Also trigger when users mention 'how much could I lose', 'worst-case scenario', 'tail risk', 'risk budget', 'component VaR', 'marginal VaR', '99% confidence loss', 'Monte Carlo simulation', or ask how to project portfolio risk forward.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-166 `fund-vehicles`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/fund-vehicles/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/fund-vehicles/SKILL.md`。
- **原始定位**：上游描述：Compare and select investment vehicles including mutual funds, ETFs, index funds, and separately managed accounts. Use when the user asks about ETF vs mutual fund, expense ratios, fund tax efficiency, ETF creation/redemption, tracking error, or share class comparisons. Also trigger when users mention 'which fund should I buy', 'Vanguard vs Fidelity', 'index fund costs', '12b-1 fees', 'load vs no-load', 'SMA vs ETF', 'fund turnover ratio', 'securities lending', or ask how fees compound over time.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-167 `historical-risk`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/historical-risk/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/historical-risk/SKILL.md`。
- **原始定位**：上游描述：Quantify realized risk from historical data using volatility estimators, drawdown analysis, and downside risk metrics. Use when the user asks about historical volatility, maximum drawdown, drawdown duration, historical VaR, downside deviation, semi-variance, or tracking error. Also trigger when users mention 'how risky has this been', 'worst decline', 'Parkinson estimator', 'Yang-Zhang', 'peak-to-trough loss', 'recovery time', 'annualized volatility', or ask how to measure past investment risk.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-168 `investment-policy`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/investment-policy/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/investment-policy/SKILL.md`。
- **原始定位**：上游描述：Construct comprehensive Investment Policy Statements governing return objectives, risk tolerance, and portfolio constraints. Use when the user asks about building an IPS, setting return objectives, assessing risk tolerance, defining investment constraints, or establishing rebalancing and benchmark policies. Also trigger when users mention 'investment plan', 'policy portfolio', 'risk capacity vs willingness', 'spending rate for an endowment', 'foundation payout', 'manager selection criteria', or ask how to document their investment strategy.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-169 `lending`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/lending/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/lending/SKILL.md`。
- **原始定位**：上游描述：Analyze lending products including mortgages, HELOCs, and personal loans with amortization and comparison tools. Use when the user asks about mortgage comparison, fixed vs ARM rates, loan qualification, amortization schedules, extra payments, or buying points. Also trigger when users mention 'monthly payment calculation', '15-year vs 30-year mortgage', 'PMI', 'APR vs interest rate', 'HELOC', 'home equity', 'should I buy down the rate', 'biweekly payments', or ask how much house they can afford.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-170 `liquidity-management`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/liquidity-management/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/liquidity-management/SKILL.md`。
- **原始定位**：上游描述：Plan and manage cash flow to ensure adequate liquidity while minimizing opportunity cost of excess cash. Use when the user asks about cash flow forecasting, CD or bond laddering, liquidity tiers, income smoothing for variable earners, or sweep strategies. Also trigger when users mention 'T-bill ladder', 'where to park cash', 'irregular income budgeting', 'freelancer cash management', 'lumpy expenses', 'liquidity ratio', 'how much cash to hold', or ask how to plan for large upcoming expenses.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-171 `performance-attribution`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/performance-attribution/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/performance-attribution/SKILL.md`。
- **原始定位**：上游描述：Decompose portfolio returns into explainable components to identify where value was added or lost. Use when the user asks about Brinson attribution, allocation vs selection effects, factor-based attribution, fixed-income attribution, or currency attribution. Also trigger when users mention 'what drove my returns', 'was it stock picking or sector bets', 'alpha decomposition', 'multi-period linking', 'interaction effect', 'active return breakdown', or ask why their portfolio outperformed or underperformed the benchmark.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-172 `performance-metrics`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/performance-metrics/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/performance-metrics/SKILL.md`。
- **原始定位**：上游描述：Evaluate investment performance on a risk-adjusted basis using industry-standard ratios and capture analysis. Use when the user asks about Sharpe ratio, Sortino ratio, Information Ratio, Treynor ratio, Calmar ratio, Omega ratio, or upside/downside capture. Also trigger when users mention 'risk-adjusted returns', 'return per unit of risk', 'M-squared', 'is this fund worth the volatility', 'how to compare two managers', 'capture ratio', or ask which investment performed better after accounting for risk.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-173 `performance-reporting`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/performance-reporting/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/performance-reporting/SKILL.md`。
- **原始定位**：上游描述：Generate clear, accurate performance reports for investment portfolios with benchmarks, attribution, and risk dashboards. Use when the user asks about portfolio performance reports, return summaries, benchmark comparison, risk dashboards, goal progress tracking, or GIPS-compliant reporting. Also trigger when users mention 'quarterly report', 'how did my portfolio do', 'time-weighted vs money-weighted return', 'annualized returns', 'net-of-fee performance', 'rolling Sharpe', or ask how to present investment results to clients.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-174 `qualitative-valuation`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/qualitative-valuation/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/qualitative-valuation/SKILL.md`。
- **原始定位**：上游描述：Assess business quality, competitive positioning, and sustainability of value creation beyond financial models. Use when the user asks about economic moats, competitive advantages, Porter's Five Forces, management quality, ESG integration, or business model analysis. Also trigger when users mention 'does this company have a moat', 'switching costs', 'network effects', 'brand value', 'management track record', 'capital allocation', 'insider ownership', 'red flags', or ask whether a company's advantage is durable.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-175 `quantitative-valuation`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/quantitative-valuation/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/quantitative-valuation/SKILL.md`。
- **原始定位**：上游描述：Estimate intrinsic value of stocks and companies using DCF, dividend discount models, comparable multiples, and residual income. Use when the user asks about discounted cash flow, DCF models, WACC, terminal value, dividend discount models, comparable multiples, or sum-of-the-parts valuation. Also trigger when users mention 'what is this stock worth', 'fair value estimate', 'Gordon growth model', 'free cash flow valuation', 'cost of equity', 'sensitivity analysis', 'exit multiple', or ask whether a stock is overvalued or undervalued.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-176 `real-assets`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/real-assets/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/real-assets/SKILL.md`。
- **原始定位**：上游描述：Analyze real estate and infrastructure investments including REITs, direct property valuation, and infrastructure assets. Use when the user asks about real estate investing, REITs, cap rates, NOI, FFO, AFFO, property valuation, or infrastructure investments. Also trigger when users mention 'rental property analysis', 'cash-on-cash return', 'gross rent multiplier', 'REIT dividends', 'real estate sectors', 'cell towers', 'toll roads', 'LTV ratio', 'DSCR', or ask whether to invest in real estate directly or through REITs.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-177 `rebalancing`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/rebalancing/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/rebalancing/SKILL.md`。
- **原始定位**：上游描述：Maintain portfolio allocations over time using calendar-based, threshold-based, and tax-efficient rebalancing strategies. Use when the user asks about when to rebalance, rebalancing bands, transaction cost trade-offs, tax-efficient rebalancing, or the rebalancing premium. Also trigger when users mention 'my portfolio drifted', 'how often should I rebalance', 'rebalancing across taxable and IRA accounts', 'volatility harvesting', 'buy low sell high automatically', or ask whether to use cash flows to rebalance.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-178 `savings-goals`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/savings-goals/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/savings-goals/SKILL.md`。
- **原始定位**：上游描述：Plan and track savings for specific financial goals including retirement, education, and home purchase. Use when the user asks about required savings rates, 529 plans, retirement accumulation targets, down payment planning, or goal prioritization. Also trigger when users mention 'how much do I need to save each month', 'am I on track for retirement', 'college savings', 'safe withdrawal rate', '4% rule', 'FIRE savings rate', 'catch-up contributions', 'employer match', or ask how to balance competing savings goals.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-179 `tax-efficiency`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/tax-efficiency/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/tax-efficiency/SKILL.md`。
- **原始定位**：上游描述：Maximize after-tax returns through strategic asset location, tax-loss harvesting, gain/loss management, and withdrawal sequencing. Use when the user asks about asset location, tax-loss harvesting, Roth conversions, tax-efficient withdrawals, tax lot selection, or charitable giving with appreciated securities. Also trigger when users mention 'which account should I hold bonds in', 'wash-sale rule', 'tax drag', 'Roth vs Traditional', 'RMD planning', 'bracket stuffing', 'HIFO vs FIFO', or ask how to minimize taxes on investments.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-180 `tax-loss-harvesting`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/tax-loss-harvesting/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/tax-loss-harvesting/SKILL.md`。
- **原始定位**：上游描述：Execute a complete tax-loss harvesting workflow from candidate identification through post-harvest monitoring. Use when the user asks about finding TLH candidates, gain/loss budgeting, replacement security selection, wash-sale compliance, or harvest execution planning. Also trigger when users mention 'unrealized losses in my portfolio', 'swap ETFs for tax purposes', 'harvest losses before year-end', 'substantially identical security', 'wash-sale window', 'NIIT offset', 'loss carryforward', or ask how much tax they can save by harvesting.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

### FSK-181 `volatility-modeling`

- **来源与路径**：来自 `community-joellewis-finance-skills`，上游路径 `plugins/wealth-management/skills/volatility-modeling/SKILL.md`，本地路径 `12-financial-ai-skills/upstream-snapshots/community-joellewis-finance-skills/plugins/wealth-management/skills/volatility-modeling/SKILL.md`。
- **原始定位**：上游描述：Model, forecast, and interpret volatility using time-series models and options-implied measures. Use when the user asks about EWMA, GARCH models, implied volatility, volatility surfaces, volatility term structure, or the VIX. Also trigger when users mention 'volatility smile', 'volatility skew', 'realized vs implied vol', 'volatility risk premium', 'vol clustering', 'mean-reverting volatility', 'options pricing inputs', 'RiskMetrics', 'decay factor', or ask how to forecast future volatility for risk management.
- **金融业务理解**：这一类覆盖财富管理从资产类别、风险计量、估值、组合构建、再平衡、税务效率到行为金融的知识链。它比 Anthropic 官方财富管理 skill 更像一套系统投资知识百科。
- **AI 工作流价值**：它把金融专业知识写成可以被 agent 调用的“能力片段”。这种写法适合学习如何把长期经验沉淀成 skill：先定义适用场景，再列核心概念，再给例子和常见误区。
- **可迁移应用方向**：可用于把银行私行/零售财富管理拆成中文知识卡片：客户风险承受能力、资产配置、产品解释、组合回顾、绩效归因和适当性提醒。
- **风险与治理边界**：治理重点是适当性、非投资建议和本地监管差异。美国语境下的税务、产品、受托责任和披露规则不能直接套用中国银行业，需要重新本地化。

## 3. 下一批建议

下一批如果继续扩展，可以选择 `KRASA-AI/finance-ai-skills` 中偏 CFO、FP&A、预算、现金流预测和并购材料的 prompt 型 skill；也可以继续搜索更偏银行、反洗钱、信贷评分、监管科技和金融数据标注的开源 skill。新增前应继续先查 `source-index.md`，避免重复收录同一主题。
