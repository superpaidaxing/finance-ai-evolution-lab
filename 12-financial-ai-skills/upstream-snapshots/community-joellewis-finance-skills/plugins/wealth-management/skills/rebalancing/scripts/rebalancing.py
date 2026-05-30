# /// script
# dependencies = ["numpy"]
# requires-python = ">=3.11"
# ///
"""
Rebalancing Toolkit
====================
Drift measurement, threshold-based rebalancing triggers, trade generation,
transaction cost estimation, tax-aware lot selection, Leland optimal band
widths, and rebalancing premium estimation.

Part of Layer 4 (Portfolio Construction) in the finance skills framework.
"""

import numpy as np


class DriftAnalyzer:
    """Measure portfolio drift and determine rebalancing triggers.

    Parameters
    ----------
    target_weights : np.ndarray
        Array of target portfolio weights summing to 1.0.
    asset_names : list[str] or None, optional
        Names for each asset. Default is None (uses integer indices).
    """

    def __init__(
        self,
        target_weights: np.ndarray,
        asset_names: list[str] | None = None,
    ):
        self.target_weights = np.asarray(target_weights, dtype=np.float64)
        self.n_assets = len(self.target_weights)
        self.asset_names = asset_names or [str(i) for i in range(self.n_assets)]

    def compute_drift(self, current_weights: np.ndarray) -> np.ndarray:
        """Compute the drift of each asset from its target weight.

        Parameters
        ----------
        current_weights : np.ndarray
            Array of current portfolio weights.

        Returns
        -------
        np.ndarray
            Drift_i = w_actual_i - w_target_i. Positive means overweight,
            negative means underweight.
        """
        current = np.asarray(current_weights, dtype=np.float64)
        return current - self.target_weights

    def absolute_drift(self, current_weights: np.ndarray) -> np.ndarray:
        """Compute absolute drift for each asset.

        Parameters
        ----------
        current_weights : np.ndarray
            Array of current portfolio weights.

        Returns
        -------
        np.ndarray
            |w_actual_i - w_target_i| for each asset.
        """
        return np.abs(self.compute_drift(current_weights))

    def relative_drift(self, current_weights: np.ndarray) -> np.ndarray:
        """Compute relative drift for each asset.

        Parameters
        ----------
        current_weights : np.ndarray
            Array of current portfolio weights.

        Returns
        -------
        np.ndarray
            |Drift_i| / w_target_i for each asset. Returns inf for assets
            with zero target weight.
        """
        abs_drift = self.absolute_drift(current_weights)
        with np.errstate(divide="ignore", invalid="ignore"):
            rel = np.where(
                self.target_weights > 0,
                abs_drift / self.target_weights,
                np.where(abs_drift > 0, np.inf, 0.0),
            )
        return rel

    def max_absolute_drift(self, current_weights: np.ndarray) -> float:
        """Compute the maximum absolute drift across all assets.

        Parameters
        ----------
        current_weights : np.ndarray
            Array of current portfolio weights.

        Returns
        -------
        float
            max(|w_actual_i - w_target_i|).
        """
        return float(np.max(self.absolute_drift(current_weights)))

    def check_threshold(
        self,
        current_weights: np.ndarray,
        absolute_threshold: float | None = None,
        relative_threshold: float | None = None,
    ) -> dict:
        """Check whether rebalancing is triggered based on thresholds.

        Parameters
        ----------
        current_weights : np.ndarray
            Array of current portfolio weights.
        absolute_threshold : float or None, optional
            Absolute drift threshold (e.g., 0.05 for 5%). If any asset
            drifts by more than this, trigger rebalancing. Default is None.
        relative_threshold : float or None, optional
            Relative drift threshold (e.g., 0.25 for 25%). If any asset's
            drift relative to its target exceeds this, trigger rebalancing.
            Default is None.

        Returns
        -------
        dict
            - 'triggered': bool, whether rebalancing is triggered
            - 'absolute_breaches': list of asset names breaching absolute threshold
            - 'relative_breaches': list of asset names breaching relative threshold
        """
        abs_drift = self.absolute_drift(current_weights)
        rel_drift = self.relative_drift(current_weights)

        abs_breaches = []
        rel_breaches = []

        if absolute_threshold is not None:
            for i in range(self.n_assets):
                if abs_drift[i] > absolute_threshold:
                    abs_breaches.append(self.asset_names[i])

        if relative_threshold is not None:
            for i in range(self.n_assets):
                if rel_drift[i] > relative_threshold:
                    rel_breaches.append(self.asset_names[i])

        triggered = len(abs_breaches) > 0 or len(rel_breaches) > 0

        return {
            "triggered": triggered,
            "absolute_breaches": abs_breaches,
            "relative_breaches": rel_breaches,
        }


class TradeGenerator:
    """Generate rebalancing trades to move from current to target weights.

    Parameters
    ----------
    target_weights : np.ndarray
        Array of target portfolio weights summing to 1.0.
    asset_names : list[str] or None, optional
        Names for each asset. Default is None (uses integer indices).
    """

    def __init__(
        self,
        target_weights: np.ndarray,
        asset_names: list[str] | None = None,
    ):
        self.target_weights = np.asarray(target_weights, dtype=np.float64)
        self.n_assets = len(self.target_weights)
        self.asset_names = asset_names or [str(i) for i in range(self.n_assets)]

    def compute_trades(
        self,
        current_weights: np.ndarray,
        portfolio_value: float,
    ) -> list[dict]:
        """Compute the trades needed to rebalance to target weights.

        Parameters
        ----------
        current_weights : np.ndarray
            Array of current portfolio weights.
        portfolio_value : float
            Total portfolio value in dollars.

        Returns
        -------
        list[dict]
            List of trade dictionaries, each containing:
            - 'asset': str, asset name
            - 'direction': str, 'BUY' or 'SELL'
            - 'weight_change': float, signed change in weight
            - 'dollar_amount': float, absolute dollar amount to trade
        """
        current = np.asarray(current_weights, dtype=np.float64)
        weight_changes = self.target_weights - current

        trades = []
        for i in range(self.n_assets):
            if abs(weight_changes[i]) < 1e-10:
                continue
            direction = "BUY" if weight_changes[i] > 0 else "SELL"
            trades.append({
                "asset": self.asset_names[i],
                "direction": direction,
                "weight_change": float(weight_changes[i]),
                "dollar_amount": float(abs(weight_changes[i]) * portfolio_value),
            })

        return trades

    def cash_flow_rebalance(
        self,
        current_weights: np.ndarray,
        portfolio_value: float,
        cash_flow: float,
    ) -> list[dict]:
        """Use an incoming cash flow to move toward target weights.

        Directs the cash flow to the most underweight assets without
        selling any existing positions.

        Parameters
        ----------
        current_weights : np.ndarray
            Array of current portfolio weights.
        portfolio_value : float
            Current total portfolio value (before cash flow).
        cash_flow : float
            Dollar amount of incoming cash (positive for deposits).

        Returns
        -------
        list[dict]
            List of purchase dictionaries, each containing:
            - 'asset': str, asset name
            - 'dollar_amount': float, amount to invest in this asset
        """
        current = np.asarray(current_weights, dtype=np.float64)
        current_dollars = current * portfolio_value
        new_total = portfolio_value + cash_flow
        target_dollars = self.target_weights * new_total

        # Shortfall: how much each asset needs to reach target
        shortfall = target_dollars - current_dollars
        # Only buy underweight assets
        shortfall = np.maximum(shortfall, 0.0)

        total_shortfall = np.sum(shortfall)
        if total_shortfall == 0:
            # All assets are at or above target; invest proportionally
            allocations = self.target_weights * cash_flow
        elif total_shortfall <= cash_flow:
            # Can fill all shortfalls with cash left over
            remainder = cash_flow - total_shortfall
            allocations = shortfall + self.target_weights * remainder
        else:
            # Not enough cash to fill all shortfalls; allocate proportionally
            allocations = shortfall * (cash_flow / total_shortfall)

        purchases = []
        for i in range(self.n_assets):
            if allocations[i] > 0.01:  # Skip negligible amounts
                purchases.append({
                    "asset": self.asset_names[i],
                    "dollar_amount": float(allocations[i]),
                })

        return purchases


class TransactionCostEstimator:
    """Estimate transaction costs for rebalancing trades.

    All methods are static and do not require instantiation.
    """

    @staticmethod
    def total_cost(
        trade_dollars: np.ndarray,
        commission_per_trade: float = 0.0,
        spread_bps: np.ndarray | float = 5.0,
        market_impact_bps: np.ndarray | float = 0.0,
    ) -> dict:
        """Estimate total transaction costs for a set of trades.

        Parameters
        ----------
        trade_dollars : np.ndarray
            Array of absolute dollar amounts for each trade.
        commission_per_trade : float, optional
            Fixed commission per trade in dollars. Default is 0.0.
        spread_bps : np.ndarray or float, optional
            Half-spread in basis points. Can be a single value or per-asset
            array. Default is 5.0 bps.
        market_impact_bps : np.ndarray or float, optional
            Market impact in basis points. Default is 0.0 bps.

        Returns
        -------
        dict
            - 'total_commission': float, total commissions
            - 'total_spread_cost': float, total spread costs
            - 'total_impact_cost': float, total market impact costs
            - 'total_cost': float, sum of all costs
            - 'cost_bps': float, total cost as basis points of trade value
        """
        trades = np.asarray(trade_dollars, dtype=np.float64)
        n_trades = int(np.sum(trades > 0))
        total_trade_value = float(np.sum(trades))

        # Commissions
        total_commission = commission_per_trade * n_trades

        # Spread costs (half-spread applied to each trade)
        spread = np.broadcast_to(
            np.asarray(spread_bps, dtype=np.float64), trades.shape
        )
        total_spread = float(np.sum(trades * spread / 10_000.0))

        # Market impact
        impact = np.broadcast_to(
            np.asarray(market_impact_bps, dtype=np.float64), trades.shape
        )
        total_impact = float(np.sum(trades * impact / 10_000.0))

        total = total_commission + total_spread + total_impact
        cost_bps = (total / total_trade_value * 10_000.0) if total_trade_value > 0 else 0.0

        return {
            "total_commission": total_commission,
            "total_spread_cost": total_spread,
            "total_impact_cost": total_impact,
            "total_cost": total,
            "cost_bps": cost_bps,
        }


class TaxAwareLotSelector:
    """Select tax lots for rebalancing sales to minimize tax impact.

    Parameters
    ----------
    lots : list[dict]
        List of tax lot dictionaries, each containing:
        - 'shares': float, number of shares
        - 'cost_basis': float, cost basis per share
        - 'current_price': float, current market price per share
        - 'holding_days': int, number of days held
    long_term_threshold : int, optional
        Number of days for long-term capital gains treatment. Default is 365.
    short_term_rate : float, optional
        Tax rate on short-term capital gains. Default is 0.37.
    long_term_rate : float, optional
        Tax rate on long-term capital gains. Default is 0.20.
    """

    def __init__(
        self,
        lots: list[dict],
        long_term_threshold: int = 365,
        short_term_rate: float = 0.37,
        long_term_rate: float = 0.20,
    ):
        self.lots = lots
        self.long_term_threshold = long_term_threshold
        self.short_term_rate = short_term_rate
        self.long_term_rate = long_term_rate

    def _lot_tax_impact(self, lot: dict, shares_to_sell: float) -> float:
        """Compute the tax impact of selling shares from a specific lot.

        Parameters
        ----------
        lot : dict
            Tax lot dictionary.
        shares_to_sell : float
            Number of shares to sell from this lot.

        Returns
        -------
        float
            Dollar tax liability (positive) or tax benefit (negative) from
            the sale.
        """
        gain_per_share = lot["current_price"] - lot["cost_basis"]
        total_gain = gain_per_share * shares_to_sell
        rate = (
            self.long_term_rate
            if lot["holding_days"] >= self.long_term_threshold
            else self.short_term_rate
        )
        return total_gain * rate

    def select_lots_min_tax(self, shares_needed: float) -> list[dict]:
        """Select lots to sell that minimize total tax impact.

        Prioritizes:
        1. Lots with losses (tax benefit)
        2. Long-term lots with smallest gains
        3. Short-term lots with smallest gains

        Parameters
        ----------
        shares_needed : float
            Total number of shares to sell.

        Returns
        -------
        list[dict]
            List of sale instructions, each containing:
            - 'lot_index': int
            - 'shares_to_sell': float
            - 'tax_impact': float
            - 'gain_per_share': float
        """
        # Score each lot by tax cost per share sold
        lot_scores = []
        for i, lot in enumerate(self.lots):
            gain = lot["current_price"] - lot["cost_basis"]
            rate = (
                self.long_term_rate
                if lot["holding_days"] >= self.long_term_threshold
                else self.short_term_rate
            )
            tax_per_share = gain * rate
            lot_scores.append((i, tax_per_share, lot["shares"]))

        # Sort by tax cost per share (sell cheapest-tax lots first)
        lot_scores.sort(key=lambda x: x[1])

        sales = []
        remaining = shares_needed
        for lot_idx, tax_per_share, available_shares in lot_scores:
            if remaining <= 0:
                break
            sell = min(remaining, available_shares)
            tax_impact = self._lot_tax_impact(self.lots[lot_idx], sell)
            gain = self.lots[lot_idx]["current_price"] - self.lots[lot_idx]["cost_basis"]
            sales.append({
                "lot_index": lot_idx,
                "shares_to_sell": sell,
                "tax_impact": tax_impact,
                "gain_per_share": gain,
            })
            remaining -= sell

        return sales

    def tax_loss_harvest_candidates(
        self,
        min_loss: float = 0.0,
    ) -> list[dict]:
        """Identify lots eligible for tax-loss harvesting.

        Parameters
        ----------
        min_loss : float, optional
            Minimum total unrealized loss to qualify. Default is 0.0.

        Returns
        -------
        list[dict]
            List of harvesting candidates, each containing:
            - 'lot_index': int
            - 'unrealized_loss': float (negative number)
            - 'tax_benefit': float (positive number)
            - 'shares': float
            - 'holding_days': int
        """
        candidates = []
        for i, lot in enumerate(self.lots):
            unrealized = (lot["current_price"] - lot["cost_basis"]) * lot["shares"]
            if unrealized < -min_loss:
                rate = (
                    self.long_term_rate
                    if lot["holding_days"] >= self.long_term_threshold
                    else self.short_term_rate
                )
                tax_benefit = abs(unrealized) * rate
                candidates.append({
                    "lot_index": i,
                    "unrealized_loss": unrealized,
                    "tax_benefit": tax_benefit,
                    "shares": lot["shares"],
                    "holding_days": lot["holding_days"],
                })

        # Sort by tax benefit descending
        candidates.sort(key=lambda x: x["tax_benefit"], reverse=True)
        return candidates


def leland_optimal_band(
    transaction_cost: float,
    risk_aversion: float,
    asset_variance: float,
) -> float:
    """Compute the Leland (2000) optimal no-trade band width.

    Parameters
    ----------
    transaction_cost : float
        Round-trip transaction cost as a decimal (e.g., 0.002 for 20 bps).
    risk_aversion : float
        Investor's risk aversion parameter.
    asset_variance : float
        Variance of the asset's returns.

    Returns
    -------
    float
        Optimal half-band width: band ~ (3*tc / (2*lambda*sigma^2))^(1/3).
        Rebalance when drift exceeds this amount.
    """
    if risk_aversion == 0 or asset_variance == 0:
        return 0.0
    return float((3.0 * transaction_cost / (2.0 * risk_aversion * asset_variance)) ** (1.0 / 3.0))


def rebalancing_premium_estimate(
    weights: np.ndarray,
    asset_variances: np.ndarray,
    portfolio_variance: float,
) -> float:
    """Estimate the rebalancing premium (volatility harvesting benefit).

    Parameters
    ----------
    weights : np.ndarray
        Array of portfolio weights.
    asset_variances : np.ndarray
        Array of individual asset variances.
    portfolio_variance : float
        Portfolio variance (w' * Sigma * w).

    Returns
    -------
    float
        Estimated rebalancing premium:
        RP ~ (1/2) * sum(w_i * sigma_i^2) - (1/2) * sigma_p^2.
        Positive when diversification is present.
    """
    w = np.asarray(weights, dtype=np.float64)
    v = np.asarray(asset_variances, dtype=np.float64)
    weighted_var = float(np.sum(w * v))
    return 0.5 * weighted_var - 0.5 * portfolio_variance


if __name__ == "__main__":
    # ----------------------------------------------------------------
    # Demo: Rebalancing toolkit on a 3-asset portfolio
    # ----------------------------------------------------------------
    np.random.seed(42)

    asset_names = ["US Equity", "Intl Equity", "US Bonds"]
    target_weights = np.array([0.60, 0.20, 0.20])
    portfolio_value = 1_000_000.0

    # After market movement: equity rallied, bonds flat
    current_weights = np.array([0.68, 0.17, 0.15])

    print("=" * 60)
    print("Rebalancing Toolkit - Demo")
    print("=" * 60)

    # --- Drift Analysis ---
    print("\n--- Drift Analysis ---")
    drift = DriftAnalyzer(target_weights, asset_names)
    d = drift.compute_drift(current_weights)
    abs_d = drift.absolute_drift(current_weights)
    rel_d = drift.relative_drift(current_weights)

    print(f"  {'Asset':15s}  {'Target':>8s}  {'Current':>8s}  {'Drift':>8s}  {'|Drift|':>8s}  {'Rel%':>8s}")
    for i, name in enumerate(asset_names):
        print(f"  {name:15s}  {target_weights[i]*100:7.1f}%  {current_weights[i]*100:7.1f}%  "
              f"{d[i]*100:+7.1f}%  {abs_d[i]*100:7.1f}%  {rel_d[i]*100:7.1f}%")
    print(f"  Max absolute drift: {drift.max_absolute_drift(current_weights)*100:.1f}%")

    # --- Threshold Check ---
    print("\n--- Threshold Check ---")
    for thresh in [0.03, 0.05, 0.10]:
        result = drift.check_threshold(current_weights, absolute_threshold=thresh)
        status = "TRIGGERED" if result["triggered"] else "OK"
        breaches = ", ".join(result["absolute_breaches"]) if result["absolute_breaches"] else "none"
        print(f"  Threshold {thresh*100:.0f}%: {status:9s} (breaches: {breaches})")

    # --- Trade Generation ---
    print("\n--- Rebalancing Trades ---")
    gen = TradeGenerator(target_weights, asset_names)
    trades = gen.compute_trades(current_weights, portfolio_value)
    for trade in trades:
        print(f"  {trade['direction']:4s} {trade['asset']:15s}: "
              f"${trade['dollar_amount']:>12,.2f} ({trade['weight_change']*100:+.1f}%)")

    # --- Cash Flow Rebalancing ---
    print("\n--- Cash Flow Rebalancing ($50,000 deposit) ---")
    purchases = gen.cash_flow_rebalance(current_weights, portfolio_value, 50_000)
    for p in purchases:
        print(f"  BUY  {p['asset']:15s}: ${p['dollar_amount']:>12,.2f}")

    # --- Transaction Cost Estimation ---
    print("\n--- Transaction Cost Estimate ---")
    trade_amounts = np.array([t["dollar_amount"] for t in trades])
    costs = TransactionCostEstimator.total_cost(
        trade_amounts,
        commission_per_trade=0.0,
        spread_bps=3.0,
        market_impact_bps=2.0,
    )
    print(f"  Spread cost:    ${costs['total_spread_cost']:>10,.2f}")
    print(f"  Impact cost:    ${costs['total_impact_cost']:>10,.2f}")
    print(f"  Total cost:     ${costs['total_cost']:>10,.2f} ({costs['cost_bps']:.1f} bps)")

    # --- Tax-Aware Lot Selection ---
    print("\n--- Tax-Aware Lot Selection (selling 500 shares of US Equity) ---")
    lots = [
        {"shares": 200, "cost_basis": 80.0, "current_price": 120.0, "holding_days": 400},
        {"shares": 300, "cost_basis": 100.0, "current_price": 120.0, "holding_days": 200},
        {"shares": 150, "cost_basis": 130.0, "current_price": 120.0, "holding_days": 100},
        {"shares": 100, "cost_basis": 110.0, "current_price": 120.0, "holding_days": 500},
    ]
    selector = TaxAwareLotSelector(lots)
    sales = selector.select_lots_min_tax(shares_needed=500)
    total_tax = 0.0
    for sale in sales:
        lot = lots[sale["lot_index"]]
        lt = "LT" if lot["holding_days"] >= 365 else "ST"
        print(f"  Lot {sale['lot_index']}: sell {sale['shares_to_sell']:.0f} shares, "
              f"gain/sh=${sale['gain_per_share']:.2f}, "
              f"tax=${sale['tax_impact']:.2f} ({lt})")
        total_tax += sale["tax_impact"]
    print(f"  Total tax impact: ${total_tax:.2f}")

    # --- Tax-Loss Harvesting Candidates ---
    print("\n--- Tax-Loss Harvesting Candidates ---")
    candidates = selector.tax_loss_harvest_candidates()
    for c in candidates:
        print(f"  Lot {c['lot_index']}: loss=${c['unrealized_loss']:.2f}, "
              f"tax benefit=${c['tax_benefit']:.2f}, "
              f"{c['shares']:.0f} shares, held {c['holding_days']} days")

    # --- Leland Optimal Bands ---
    print("\n--- Leland Optimal Band Widths ---")
    scenarios = [
        ("Low cost, low vol", 0.001, 3.0, 0.04**2),
        ("Low cost, high vol", 0.001, 3.0, 0.20**2),
        ("High cost, low vol", 0.005, 3.0, 0.04**2),
        ("High cost, high vol", 0.005, 3.0, 0.20**2),
    ]
    for desc, tc, lam, var in scenarios:
        band = leland_optimal_band(tc, lam, var)
        print(f"  {desc:25s}: band = {band*100:.2f}% (+/-)")

    # --- Rebalancing Premium ---
    print("\n--- Rebalancing Premium Estimate ---")
    asset_vols = np.array([0.16, 0.18, 0.04])
    asset_vars = asset_vols ** 2
    # Approximate portfolio variance for a 60/20/20 portfolio
    port_var = 0.0105 ** 2 * 100  # placeholder; use actual covariance in practice
    # Use a more realistic estimate
    corr_matrix = np.array([
        [1.00, 0.75, 0.10],
        [0.75, 1.00, 0.05],
        [0.10, 0.05, 1.00],
    ])
    cov_matrix = np.outer(asset_vols, asset_vols) * corr_matrix
    port_var = float(target_weights @ cov_matrix @ target_weights)
    rp = rebalancing_premium_estimate(target_weights, asset_vars, port_var)
    print(f"  Weighted avg variance: {np.sum(target_weights * asset_vars)*100:.4f}%")
    print(f"  Portfolio variance:    {port_var*100:.4f}%")
    print(f"  Rebalancing premium:   {rp*100:.4f}% (annualized estimate)")

    print("\n" + "=" * 60)
    print("Demo complete.")
    print("=" * 60)
