---
name: portfolio-management-systems
description: "Select, configure, and operate portfolio management systems for advisory firms, covering model portfolios, UMA/sleeve management, drift monitoring, rebalancing, and custodian data feeds. Use when the user asks about choosing a PMS platform, building or distributing model portfolios, implementing UMA or sleeve-based management, setting drift monitoring thresholds, aggregating held-away assets, reconciling PMS with custodian records, configuring PMS-based billing, or troubleshooting custodian feed issues. Also trigger when users mention 'portfolio management system', 'Orion', 'Black Diamond', 'Tamarac', 'Addepar', 'Advent APX', 'model portfolio', 'sleeve management', 'rebalancing engine', 'custodian feed', or 'PMS migration'."
---

# Portfolio Management Systems

## Purpose

Enable Claude to advise on the selection, configuration, and operation of portfolio
management systems (PMS) within registered investment advisory firms. This skill covers
the full PMS lifecycle: platform architecture, model portfolio construction, sleeve-based
and UMA management, drift monitoring, rebalancing, held-away asset aggregation, portfolio
accounting, trading integration, performance calculation, billing, and custodian data
feeds. It equips Claude to guide advisors, operations teams, and technology leaders
through PMS implementation decisions, day-to-day operational workflows, and
troubleshooting reconciliation or data-quality issues.

## Layer

10 — Advisory Practice (Front Office)

## Direction

both

## When to Use

- An advisor or RIA asks about selecting or migrating to a portfolio management platform
- Questions arise about building, maintaining, or distributing model portfolios
- A firm wants to implement UMA or sleeve-based account management
- An operations team needs guidance on drift monitoring thresholds or rebalancing configuration
- A practice seeks to aggregate held-away assets for holistic financial planning views
- Questions involve daily reconciliation between a PMS and custodian records
- An advisor asks how trades flow from the PMS to the order management system or custodian
- Discussion involves PMS-based performance calculation (TWR, MWR) or composite construction
- A firm needs to configure fee schedules, billing runs, or billable-AUM calculations in the PMS
- Questions concern custodian data feeds, multi-custodian management, or feed troubleshooting
- Trigger phrases: "portfolio management system," "Orion," "Black Diamond," "Tamarac,"
  "Addepar," "model portfolio," "UMA," "sleeve," "rebalancing engine," "drift monitoring,"
  "held-away assets," "portfolio accounting," "reconciliation," "custodian feed," "PMS billing"


## Core Concepts

> For detailed specifications, platform comparison tables, and architecture diagrams, see `references/platform-details.md`.

### 1. Portfolio Management System Architecture

The PMS is the operational nerve center of an advisory practice, orchestrating data flow between custodians, trading platforms, reporting engines, CRM, and planning tools. Core functions include portfolio construction, model management, rebalancing, trading, performance reporting, and billing. Major platforms: Orion, Black Diamond, Tamarac, Addepar, Morningstar Direct, Advent/APX. The PMS serves as the firm's Investment Book of Record (IBOR), which must be reconciled daily against the custodian's Official Book of Record (OBOR).

### 2. Model Portfolio Management

Model portfolios define target allocations (asset classes, securities, weights) applied consistently across client accounts. Types include strategic (SAA), tactical (TAA overlays), and specialty models (income, ESG, tax-managed). Firms typically use a two-tier hierarchy (firm-level + advisor-customized). Model changes trigger versioning, account identification, trade proposal generation, and tax-aware transition. Third-party model marketplaces (BlackRock, DFA, Vanguard, PIMCO) allow smaller firms to access institutional-quality investment management.

### 3. Sleeve-Based and UMA Architecture

Unified Managed Accounts (UMAs) divide a single custodial account into virtual sub-accounts (sleeves), each following its own strategy or manager. Benefits: cross-sleeve tax optimization, simplified reporting, reduced account proliferation, and unified cash management. Cash waterfall rules govern deposits, withdrawals, and income allocation across sleeves. UMAs differ from SMAs (single-strategy, one manager) and mutual fund wraps (indirect ownership, limited customization). Typical minimums: $250K-$1M+.

### 4. Drift Monitoring and Rebalancing

Drift is the divergence of actual weights from targets caused by differential returns and cash flows. Measured as absolute drift (percentage-point difference) or relative drift (percentage of target). Threshold configurations range from conservative (3%/15%) to permissive (7%/30%). Rebalancing approaches: calendar-based, threshold-based, opportunistic (cash-flow-directed), and hybrid. Tax-aware rebalancing incorporates capital gains minimization, loss harvesting, wash sale avoidance, and gain budgets.

### 5. Held-Away Asset Aggregation

A complete client picture requires visibility into all assets, including employer plans, stock options, RSUs, bank accounts, and accounts at other custodians. Data sources: aggregation services (Plaid, Yodlee, MX, ByAllAccounts), custodian feeds, manual entry, and employer plan integrations. Challenges include data staleness, categorization errors, and broken connections. The PMS should provide both managed-only and total-household reporting views.

### 6. Portfolio Accounting and Reconciliation

Portfolio accounting tracks positions, transactions, cost basis, cash flows, and accrued income. Daily reconciliation compares PMS against custodian across three dimensions: positions, transactions, and cash. Breaks require classification, root-cause diagnosis, correction, and documentation. Common break sources: corporate actions (splits, mergers, spin-offs, DRIP), trade settlement timing, and data feed issues. Cost basis methods: specific identification, FIFO, and average cost.

### 7. Trading and Order Management Integration

The PMS generates trade proposals from model changes, rebalancing triggers, cash flows, and ad-hoc instructions. In larger firms, trades flow through a separate OMS for compliance checks, block aggregation, and execution routing. Block trading aggregates orders across accounts for best execution with pro-rata allocation. Pre-trade checks cover restricted securities, concentration limits, client restrictions, regulatory limits, and cash minimums. Implementation methods: direct custodian trading, third-party EMS, and mutual fund trading platforms.

### 8. Performance Calculation Engine

The PMS computes returns at multiple levels: security, sleeve, account, household, model, composite, and firm. TWR (time-weighted) eliminates cash flow impact for manager evaluation and GIPS compliance. MWR (money-weighted/IRR) reflects the investor's actual experience. Daily performance provides the most precise TWR; monthly uses approximations like Modified Dietz. Benchmarks (primary, blended, custom) must be tracked at the same frequency as portfolio returns.

### 9. Billing and Fee Calculation

Fee structures: AUM-based (flat or tiered/breakpoint), flat/retainer, performance-based (qualified clients only), and blended. Billing frequency: quarterly (most common), monthly, or annual. Advance billing requires proration; arrears billing delays revenue recognition. Billable AUM determination requires clear policies on included/excluded assets and household aggregation. Fee deduction via direct debit (most common) or invoice. Revenue tracking covers client, advisor, model, and strategy dimensions.

### 10. Custodian Integration and Data Feeds

Custodian integration provides the data backbone: positions, transactions, cash, cost basis, corporate actions, and new accounts flow from custodian to PMS; trade instructions and fee invoices flow from PMS to custodian. Integration methods: proprietary batch feeds (CSV/XML), FIX protocol, APIs, and third-party aggregators. Feed timing: EOD batch (most common), intraday updates, and real-time streaming. Multi-custodian management requires data normalization, consolidated views, custodian-specific trade routing, and separate reconciliation. Custodian transitions (e.g., TD Ameritrade to Schwab) require account mapping, feed migration, and historical data transfer.

## Worked Examples

### Example 1: PMS Migration for a Growing RIA

**Scenario:**

A $500M RIA with 800 client households has been managing portfolios using Excel
spreadsheets and the custodian's online platform. The firm operates 12 model
portfolios across two custodians (Schwab and Fidelity). As the firm grows, the
spreadsheet approach creates unacceptable operational risk: rebalancing is
inconsistent, performance reporting is delayed by weeks, and the firm recently
discovered it had been billing a client at the wrong fee rate for two quarters.
The firm decides to implement Orion as its portfolio management system.

**Design Considerations:**

**Platform selection criteria:**

- Multi-custodian support (Schwab and Fidelity integration required).
- Rebalancing engine capable of handling 12+ models across 800+ households.
- Tax-aware rebalancing with wash sale tracking.
- Automated billing with tiered fee schedule support.
- Performance reporting with composite construction for marketing materials.
- Integration with the firm's existing CRM (Salesforce).
- Client portal for on-demand performance access.

**Data migration planning:**

- Export current positions and cost basis from both custodians.
- Reconstruct historical transactions from custodian records (typically 3-5
  years for performance history, full history for cost basis).
- Map existing security positions to Orion's security master.
- Import client and account demographic data from CRM.
- Establish the 12 model portfolios in Orion with target allocations and
  security selections.

**Model setup and configuration:**

- Define each of the 12 models with target weights, drift bands, and
  rebalancing rules.
- Assign each client account to the appropriate model.
- Configure substitution rules for taxable vs. tax-deferred accounts.
- Set drift thresholds (the firm selects 5% absolute / 25% relative).
- Configure cash reserve rules (2% minimum cash per account).

**Custodian feed setup:**

- Establish Schwab data feeds: positions, transactions, cash balances,
  cost basis, corporate actions. Test file delivery and parsing.
- Establish Fidelity data feeds: same data categories. Test independently.
- Configure daily reconciliation jobs for both custodians.
- Validate initial reconciliation: resolve any breaks before go-live.

**Go-live workflow:**

- Run parallel operations for 30 days (maintain spreadsheets alongside Orion).
- Compare rebalancing recommendations from both systems.
- Validate performance calculations against custodian-reported returns.
- Validate billing calculations against historical invoices.
- Train advisors and operations staff on the new workflows.
- Decommission spreadsheet processes after successful parallel period.

**Analysis:**

The migration represents a significant operational transformation. The firm should
budget 3-6 months for full implementation, including 1-2 months for data migration
and setup, 1 month for parallel testing, and 1-2 months for staff training and
workflow refinement. Key risks include data quality issues during migration
(especially historical cost basis), disruption to client reporting during the
transition, and staff resistance to new workflows. The firm should designate a
dedicated project manager and plan for temporary increases in operations staffing
during the transition. Post-implementation, the firm should expect significant
efficiency gains: rebalancing that previously took two days per quarter should
complete in hours, billing errors should be eliminated by automated fee calculation,
and performance reports should be available daily rather than weeks after quarter-end.

### Example 2: UMA/Sleeve Implementation for HNW Clients

**Scenario:**

A wealth management firm serving high-net-worth clients ($1M+ investable assets)
currently manages client portfolios using 3-5 separate SMAs per client, each
following a different strategy. This creates operational burden (multiple account
statements, separate rebalancing for each SMA, inability to coordinate tax
management across accounts) and client confusion. The firm decides to transition
its HNW clients to a UMA/sleeve-based structure using its existing PMS (Tamarac).

**Design Considerations:**

**Sleeve structure design:**

The firm designs a five-sleeve UMA architecture:

| Sleeve | Allocation Range | Strategy | Management |
|---|---|---|---|
| Core U.S. Equity | 25-45% | Broad U.S. equity exposure | Firm proprietary model |
| International Equity | 10-25% | Developed and emerging markets | DFA model via Tamarac |
| Fixed Income | 15-35% | Investment-grade and municipal bonds | PIMCO model |
| Alternatives | 5-15% | Real assets, liquid alternatives | Third-party manager |
| Tactical Overlay | 0-10% | Short-term tactical tilts | CIO discretion |

Cash is managed at the total account level rather than within individual sleeves,
with a 2% minimum cash target.

**Model assignment rules:**

- Each client's Investment Policy Statement (IPS) dictates the overall allocation
  across sleeves based on their risk profile.
- Conservative clients: higher fixed income and lower alternatives allocation.
- Aggressive clients: higher equity and alternatives allocation.
- Sleeve-level models operate independently within their assigned allocation.
- The overlay manager (CIO) can make tactical adjustments within the overlay
  sleeve without affecting other sleeves.

**Cross-sleeve tax management:**

- The PMS overlay engine monitors unrealized gains and losses across all sleeves.
- When rebalancing triggers a sell in one sleeve, the overlay engine checks
  whether a loss can be harvested in another sleeve to offset the gain.
- Wash sale rules are monitored across sleeves: if the fixed income sleeve sells
  a bond fund at a loss, the equity sleeve cannot purchase a substantially
  identical fund within 30 days.
- Year-end tax management: the overlay engine runs a cross-sleeve analysis to
  identify harvesting opportunities before December 31.

**Reporting configuration:**

- **Client-facing reports** show total UMA performance alongside per-sleeve
  performance attribution, so clients understand how each strategy contributes.
- **Internal reports** track model-level performance (how well each model
  performed independent of client cash flows) and implementation efficiency
  (how closely client accounts track their assigned models).
- **Billing reports** calculate fees on total UMA AUM (not per-sleeve).
- **Household reports** aggregate across multiple UMAs and non-UMA accounts
  for clients with more than one account.

**Analysis:**

The UMA transition consolidates 3-5 accounts per client into a single account,
reducing custodian fees, simplifying client statements, and enabling cross-strategy
tax optimization that was previously impossible. The firm should expect a 2-3 month
transition per client cohort, as existing SMA positions must be transferred in-kind
to the new UMA account structure. Tax implications of the transition must be
carefully managed — the firm should avoid realizing gains during the restructuring
by transferring positions in-kind wherever possible. The ongoing operational benefit
is substantial: the overlay manager can rebalance all sleeves simultaneously,
dividends and income flow to a single cash pool, and withdrawals can be sourced
from the most tax-efficient sleeve. The firm should track client satisfaction
metrics before and after the transition, anticipating improvement in client
comprehension of their portfolio structure and investment strategy.

### Example 3: Reconciliation Break Investigation and Resolution

**Scenario:**

An advisory practice managing $350M across 600 accounts discovers during its
Monday morning reconciliation review that 48 accounts (8% of the total) show
position discrepancies between the PMS and the custodian (Schwab). The breaks
range from minor share-count differences to entirely missing positions. The
operations team needs to diagnose the causes, resolve the breaks, and implement
controls to prevent recurrence.

**Design Considerations:**

**Break classification and diagnosis:**

The operations team categorizes the 48 breaks into root-cause buckets:

| Category | Count | Typical Cause |
|---|---|---|
| Missed corporate action | 18 | A stock split processed at custodian but not reflected in PMS |
| Trade settlement timing | 12 | Friday trades settled at custodian over the weekend but PMS shows pending |
| Data feed failure | 8 | The Saturday custodian file failed to load due to a format change in one field |
| Dividend reinvestment | 6 | DRIP shares added at custodian but PMS not configured for auto-DRIP on these accounts |
| Genuine error | 4 | Trades executed at custodian but not initiated through PMS (advisor placed directly) |

**Resolution workflow:**

1. **Corporate action breaks (18 accounts):** The PMS operations team identifies
   that a widely-held equity (held in 18 accounts) underwent a 3:1 stock split
   on the prior Thursday. The custodian processed the split automatically, but
   the PMS corporate action module failed to pick it up from the data feed. The
   team manually applies the split in the PMS, adjusting share counts and cost
   basis for all 18 accounts.

2. **Settlement timing breaks (12 accounts):** These breaks are expected and
   will self-resolve when Monday's end-of-day reconciliation runs. The team marks
   them as "expected timing difference" and monitors for resolution.

3. **Data feed failure (8 accounts):** The Saturday batch file from Schwab
   contained a format change in the corporate action field that caused the PMS
   file parser to reject the entire file for 8 accounts. The team contacts the
   PMS vendor to update the parser, manually imports the affected data, and
   re-runs reconciliation for those accounts.

4. **DRIP configuration (6 accounts):** Six accounts are configured for dividend
   reinvestment at the custodian but the PMS does not reflect this setting. When
   dividends reinvest into fractional shares, the PMS records a cash dividend
   instead. The team updates the DRIP flag in the PMS for these accounts and
   adjusts positions to match the custodian.

5. **Unauthorized trades (4 accounts):** An advisor placed 4 trades directly
   through the custodian platform without going through the PMS. The team enters
   the trades into the PMS after the fact and counsels the advisor on the
   requirement to use the PMS for all trade activity.

**Controls to reduce future breaks:**

- **Automated corporate action processing:** Configure the PMS to automatically
  apply mandatory corporate actions (splits, mergers) from the custodian data
  feed, with alerts for actions requiring manual review (tenders, elections).
- **Feed monitoring:** Implement automated alerts when custodian data files
  fail to arrive, arrive with unexpected format changes, or contain fewer
  records than expected.
- **DRIP audit:** Run a quarterly audit comparing DRIP settings in the PMS
  against custodian DRIP elections for all accounts.
- **Trade workflow enforcement:** Configure custodian access so that advisors
  cannot place trades directly; all trades must originate from the PMS.
- **Daily break dashboard:** Implement a dashboard showing break counts by
  category, age, and resolution status, with escalation rules for breaks
  older than 3 business days.

**Analysis:**

An 8% break rate is above the industry target of under 2% for well-run operations.
The immediate resolution of the 48 breaks eliminates the risk of incorrect
performance reports or billing. However, the more important outcome is the
implementation of preventive controls. Automated corporate action processing alone
should eliminate the largest break category (37.5% of all breaks). Feed monitoring
prevents silent data-quality failures that can cascade into reporting and billing
errors. The trade workflow enforcement addresses a compliance concern: trades placed
outside the PMS bypass pre-trade compliance checks and block-trading allocations,
creating best-execution and fair-allocation risks. The firm should target a break
rate below 1% within 90 days of implementing these controls and track the metric
weekly in operations meetings.

## Common Pitfalls

1. **Treating the PMS as the official record.** The custodian, not the PMS,
   maintains the legally authoritative record of client assets. When discrepancies
   exist, the custodian record governs. Firms that rely solely on PMS data without
   reconciliation risk reporting incorrect positions and performance.

2. **Neglecting daily reconciliation.** Firms that reconcile weekly or monthly
   allow breaks to compound, making root-cause diagnosis much harder. A corporate
   action missed on Monday may cause cascading errors in performance, billing,
   and rebalancing throughout the week.

3. **Over-engineering drift thresholds.** Setting drift bands too tight (e.g., 1%
   absolute) generates excessive trading, increasing costs and tax drag. Setting
   bands too loose (e.g., 10% absolute) allows portfolios to deviate significantly
   from the intended risk profile. Calibrate thresholds based on asset class
   volatility and client tax sensitivity.

4. **Ignoring wash sale rules across accounts.** Tax-loss harvesting in one account
   while purchasing substantially identical securities in another account with the
   same tax ID disallows the loss. The PMS must monitor wash sale windows across
   all accounts for a client or household.

5. **Stale held-away data.** Aggregated held-away data that has not refreshed in
   weeks or months can lead to materially incorrect total-household allocation views
   and flawed planning recommendations. Implement alerts for stale connections and
   establish a process for client re-authentication.

6. **Inconsistent model governance.** Allowing advisors to freely modify firm models
   without oversight creates style drift and compliance risk. Establish clear
   policies on which model elements advisors can customize and require documentation
   of deviations.

7. **Cost basis discrepancies between PMS and custodian.** The PMS and custodian may
   calculate cost basis differently, especially after corporate actions, transfers,
   or wash sale adjustments. If the firm relies on PMS cost basis for tax-loss
   harvesting decisions but the custodian reports different basis to the IRS
   (Form 1099-B), clients may face unexpected tax consequences.

8. **Billing on stale or unreconciled data.** Calculating fees on PMS positions that
   have not been reconciled against the custodian may result in over- or under-billing.
   Always reconcile before running billing.

9. **Failing to test custodian feed changes.** Custodians periodically update their
   data feed formats. Firms that do not monitor for format changes or test in a
   staging environment before production risk silent data-import failures.

10. **Overlooking performance calculation methodology.** Reporting MWR when TWR
    is appropriate (or vice versa) can mislead clients or violate GIPS standards.
    Understand when each methodology is appropriate and clearly label which method
    is used in client-facing reports.

## Cross-References

- **asset-allocation** (Layer 4, wealth-management) — PMS implements the strategic
  and tactical asset allocation defined in the client's investment policy. Model
  portfolios in the PMS are the operational expression of asset allocation decisions.
- **rebalancing** (Layer 4, wealth-management) — The PMS rebalancing engine applies
  rebalancing theory (threshold-based, calendar-based, opportunistic) to live client
  portfolios. The rebalancing skill defines the theory; this skill covers the
  system implementation.
- **tax-efficiency** (Layer 5, wealth-management) — PMS tax-loss harvesting,
  wash sale monitoring, and tax-aware rebalancing apply the tax-efficiency
  principles defined in the tax-efficiency skill to operational workflows.
- **performance-metrics** (Layer 1a, wealth-management) — The PMS calculates the
  return metrics (TWR, MWR, alpha, Sharpe ratio) defined in the performance-metrics
  skill. That skill defines the math; this skill covers how the PMS implements the
  calculations.
- **performance-reporting** (Layer 8, wealth-management) — The PMS generates the
  underlying performance data that feeds client-facing performance reports. The
  reporting skill covers presentation and communication; this skill covers
  calculation and data infrastructure.
- **gips-compliance** (Layer 9, compliance) — PMS composite construction and
  performance calculation must satisfy GIPS requirements for firms that claim
  compliance. The GIPS skill defines the standards; this skill covers the PMS
  configuration needed to meet them.
- **order-management-advisor** (Layer 10, advisory-practice) — The OMS receives
  trade lists generated by the PMS. This skill covers trade list generation; the
  OMS skill covers order routing, execution, and allocation.
- **financial-planning-integration** (Layer 10, advisory-practice) — The PMS
  current portfolio (including held-away aggregation) feeds financial planning
  tools for projections and scenario analysis.
- **fee-billing** (Layer 10, advisory-practice) — The PMS fee engine handles
  billing calculations described here. The fee-billing skill covers the broader
  billing operations workflow including invoicing, collections, and revenue
  recognition.
- **client-reporting-delivery** (Layer 10, advisory-practice) — PMS performance
  data, portfolio holdings, and asset allocation feeds the client reporting and
  delivery workflow.
