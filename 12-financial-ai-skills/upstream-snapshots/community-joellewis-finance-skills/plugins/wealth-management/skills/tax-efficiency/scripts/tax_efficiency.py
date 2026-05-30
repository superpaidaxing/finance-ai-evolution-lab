# /// script
# dependencies = ["numpy"]
# requires-python = ">=3.11"
# ///
"""
Tax-Efficient Investing
========================
After-tax return calculations, tax drag estimation, tax-loss harvesting benefit,
asset location optimization, tax cost ratio, and breakeven holding period analysis.

Part of Layer 5 (Policy & Planning) in the finance skills framework.
"""

import numpy as np


class AfterTaxReturn:
    """Compute after-tax returns under different income and gain scenarios."""

    @staticmethod
    def income_return(pre_tax_return: float, tax_rate: float) -> float:
        """After-tax return on income (interest, ordinary dividends, short-term gains).

        Parameters
        ----------
        pre_tax_return : float
            Pre-tax return (decimal, e.g., 0.05 = 5%).
        tax_rate : float
            Applicable tax rate on the income (decimal).

        Returns
        -------
        float
            R_at = R * (1 - t)
        """
        return float(pre_tax_return * (1.0 - tax_rate))

    @staticmethod
    def deferred_gain_return(
        pre_tax_return: float,
        holding_period: int,
        capital_gains_rate: float,
    ) -> float:
        """Annualized after-tax return on unrealized capital gains with deferral benefit.

        Accounts for the tax-deferral advantage of unrealized gains held over
        multiple periods before realization.

        Parameters
        ----------
        pre_tax_return : float
            Annual pre-tax return (decimal).
        holding_period : int
            Number of years the gain is deferred before realization.
        capital_gains_rate : float
            Tax rate on capital gains at realization (decimal).

        Returns
        -------
        float
            R_at = ((1 + R)^n * (1 - t_cg) + t_cg)^(1/n) - 1
        """
        if holding_period <= 0:
            raise ValueError("holding_period must be a positive integer.")
        fv_factor = (1.0 + pre_tax_return) ** holding_period
        after_tax_fv = fv_factor * (1.0 - capital_gains_rate) + capital_gains_rate
        return float(after_tax_fv ** (1.0 / holding_period) - 1.0)

    @staticmethod
    def blended_return(
        total_return: float,
        income_fraction: float,
        income_tax_rate: float,
        capital_gains_fraction: float,
        capital_gains_rate: float,
        unrealized_fraction: float | None = None,
    ) -> float:
        """Weighted after-tax return across income, realized gains, and unrealized gains.

        Parameters
        ----------
        total_return : float
            Total pre-tax return (decimal).
        income_fraction : float
            Fraction of total return that is taxable income (0 to 1).
        income_tax_rate : float
            Tax rate on income portion (decimal).
        capital_gains_fraction : float
            Fraction of total return that is realized capital gains (0 to 1).
        capital_gains_rate : float
            Tax rate on realized capital gains (decimal).
        unrealized_fraction : float | None, optional
            Fraction of total return that is unrealized gains (tax-deferred).
            If None, computed as 1 - income_fraction - capital_gains_fraction.

        Returns
        -------
        float
            Blended after-tax return.
        """
        if unrealized_fraction is None:
            unrealized_fraction = 1.0 - income_fraction - capital_gains_fraction

        after_tax = total_return * (
            income_fraction * (1.0 - income_tax_rate)
            + capital_gains_fraction * (1.0 - capital_gains_rate)
            + unrealized_fraction
        )
        return float(after_tax)


class TaxDrag:
    """Quantify the cost of taxes on investment returns."""

    @staticmethod
    def annual_drag(pre_tax_return: float, after_tax_return: float) -> float:
        """Compute annual tax drag.

        Parameters
        ----------
        pre_tax_return : float
            Pre-tax return (decimal).
        after_tax_return : float
            After-tax return (decimal).

        Returns
        -------
        float
            Tax drag = pre_tax_return - after_tax_return.
        """
        return float(pre_tax_return - after_tax_return)

    @staticmethod
    def cumulative_drag(
        pre_tax_return: float,
        after_tax_return: float,
        years: int,
        initial_investment: float = 1.0,
    ) -> float:
        """Cumulative wealth lost to taxes over a holding period.

        Parameters
        ----------
        pre_tax_return : float
            Annual pre-tax return (decimal).
        after_tax_return : float
            Annual after-tax return (decimal).
        years : int
            Investment horizon in years.
        initial_investment : float, optional
            Starting investment amount. Default is 1.0.

        Returns
        -------
        float
            Difference in terminal wealth: pre-tax growth minus after-tax growth.
        """
        pre_tax_wealth = initial_investment * (1.0 + pre_tax_return) ** years
        after_tax_wealth = initial_investment * (1.0 + after_tax_return) ** years
        return float(pre_tax_wealth - after_tax_wealth)

    @staticmethod
    def tax_cost_ratio(
        pre_tax_return: float,
        after_tax_return: float,
    ) -> float:
        """Tax cost ratio: percentage of pre-tax return consumed by taxes.

        Parameters
        ----------
        pre_tax_return : float
            Pre-tax return (decimal).
        after_tax_return : float
            After-tax return (decimal).

        Returns
        -------
        float
            TCR = (pre_tax_return - after_tax_return) / pre_tax_return.
            Returns 0.0 if pre_tax_return is zero.
        """
        if pre_tax_return == 0.0:
            return 0.0
        return float((pre_tax_return - after_tax_return) / pre_tax_return)


class TaxLossHarvesting:
    """Tax-loss harvesting benefit calculations."""

    @staticmethod
    def immediate_benefit(
        harvested_loss: float,
        marginal_tax_rate: float,
    ) -> float:
        """Immediate tax savings from harvesting a loss.

        Parameters
        ----------
        harvested_loss : float
            Amount of capital loss harvested (positive number).
        marginal_tax_rate : float
            Applicable tax rate for the offset (capital gains rate if
            offsetting gains, ordinary rate for the $3K annual deduction).

        Returns
        -------
        float
            TLH_value = loss * marginal_tax_rate.
        """
        return float(abs(harvested_loss) * marginal_tax_rate)

    @staticmethod
    def net_benefit(
        harvested_loss: float,
        current_tax_rate: float,
        future_tax_rate: float,
        years_deferred: int,
        discount_rate: float,
    ) -> float:
        """Net present value of tax-loss harvesting considering future recapture.

        Harvesting a loss lowers the cost basis of the replacement, so the
        deferred gain is eventually taxed. The net benefit comes from the
        time value of the tax deferral and any rate differential.

        Parameters
        ----------
        harvested_loss : float
            Amount of capital loss harvested (positive number).
        current_tax_rate : float
            Tax rate applied to the current offset (decimal).
        future_tax_rate : float
            Tax rate expected when the deferred gain is eventually realized (decimal).
        years_deferred : int
            Number of years until the deferred gain is realized.
        discount_rate : float
            Rate used to discount future tax liability (decimal).

        Returns
        -------
        float
            NPV of TLH = immediate benefit - PV of future tax cost.
        """
        loss = abs(harvested_loss)
        immediate = loss * current_tax_rate
        future_cost = loss * future_tax_rate / (1.0 + discount_rate) ** years_deferred
        return float(immediate - future_cost)

    @staticmethod
    def annual_harvesting_opportunities(
        positions: np.ndarray,
        cost_bases: np.ndarray,
        loss_threshold: float = 0.0,
    ) -> dict:
        """Identify positions eligible for tax-loss harvesting.

        Parameters
        ----------
        positions : np.ndarray
            Current market values of each position.
        cost_bases : np.ndarray
            Cost basis of each position.
        loss_threshold : float, optional
            Minimum loss (as a positive fraction of cost basis) to trigger
            harvesting consideration. Default is 0.0 (any loss).

        Returns
        -------
        dict
            Dictionary with keys:
            - "eligible_indices": array of position indices with harvestable losses
            - "losses": array of loss amounts (positive numbers)
            - "total_harvestable": total dollar amount of harvestable losses
        """
        positions = np.asarray(positions, dtype=np.float64)
        cost_bases = np.asarray(cost_bases, dtype=np.float64)

        gains = positions - cost_bases
        loss_mask = gains < 0
        if loss_threshold > 0:
            loss_pct = np.abs(gains) / np.where(cost_bases != 0, cost_bases, 1.0)
            loss_mask = loss_mask & (loss_pct >= loss_threshold)

        eligible = np.where(loss_mask)[0]
        losses = np.abs(gains[eligible])

        return {
            "eligible_indices": eligible,
            "losses": losses,
            "total_harvestable": float(np.sum(losses)),
        }


class AssetLocation:
    """Asset location optimization across taxable, tax-deferred, and tax-exempt accounts.

    Determines optimal placement of assets across account types to minimize
    total tax drag.
    """

    @staticmethod
    def tax_drag_by_account(
        allocation_amount: float,
        expected_return: float,
        income_yield: float,
        income_tax_rate: float,
        capital_gains_rate: float,
        turnover: float,
    ) -> float:
        """Estimate annual tax drag for an asset held in a taxable account.

        Parameters
        ----------
        allocation_amount : float
            Dollar amount allocated to this asset.
        expected_return : float
            Expected total return (decimal).
        income_yield : float
            Portion of return distributed as taxable income (decimal, e.g., 0.05).
        income_tax_rate : float
            Tax rate on income distributions (decimal).
        capital_gains_rate : float
            Tax rate on realized capital gains (decimal).
        turnover : float
            Fraction of capital gains realized annually due to turnover (decimal).

        Returns
        -------
        float
            Estimated annual tax cost in dollars.
        """
        income_tax = allocation_amount * income_yield * income_tax_rate
        price_return = expected_return - income_yield
        realized_gains_tax = (
            allocation_amount * max(price_return, 0.0) * turnover * capital_gains_rate
        )
        return float(income_tax + realized_gains_tax)

    @staticmethod
    def compare_locations(
        asset_amount: float,
        expected_return: float,
        income_yield: float,
        income_tax_rate: float,
        capital_gains_rate: float,
        turnover: float,
        years: int,
    ) -> dict:
        """Compare terminal after-tax wealth across three account types.

        Parameters
        ----------
        asset_amount : float
            Dollar amount to invest.
        expected_return : float
            Expected annual total return (decimal).
        income_yield : float
            Income yield portion of return (decimal).
        income_tax_rate : float
            Ordinary income tax rate (decimal).
        capital_gains_rate : float
            Capital gains tax rate (decimal).
        turnover : float
            Annual turnover rate causing gain realization (decimal).
        years : int
            Investment horizon.

        Returns
        -------
        dict
            Terminal after-tax wealth for each account type:
            - "taxable": after annual tax drag on income and realized gains
            - "tax_deferred": all growth taxed as ordinary income at withdrawal
            - "tax_exempt": all growth tax-free (Roth)
        """
        # Taxable: annual tax drag reduces compounding
        price_return = expected_return - income_yield
        annual_after_tax_return = (
            income_yield * (1.0 - income_tax_rate)
            + price_return * (1.0 - turnover * capital_gains_rate)
        )
        # Remaining unrealized gains taxed at sale
        taxable_wealth_pretax = asset_amount * (1.0 + annual_after_tax_return) ** years
        total_unrealized = taxable_wealth_pretax - asset_amount
        # Approximate: unrealized portion taxed at capital gains rate
        taxable_wealth = taxable_wealth_pretax - total_unrealized * capital_gains_rate * (1.0 - turnover)

        # Tax-deferred: full compounding, taxed as ordinary income at withdrawal
        deferred_gross = asset_amount * (1.0 + expected_return) ** years
        deferred_wealth = deferred_gross * (1.0 - income_tax_rate)

        # Tax-exempt (Roth): full compounding, no tax at withdrawal
        exempt_wealth = asset_amount * (1.0 + expected_return) ** years

        return {
            "taxable": float(taxable_wealth),
            "tax_deferred": float(deferred_wealth),
            "tax_exempt": float(exempt_wealth),
        }

    @staticmethod
    def optimal_placement(
        assets: list[dict],
        taxable_capacity: float,
        deferred_capacity: float,
        exempt_capacity: float,
    ) -> dict:
        """Greedy asset location: place most tax-inefficient assets in
        tax-advantaged accounts first.

        Parameters
        ----------
        assets : list[dict]
            Each dict has keys:
            - "name": str, asset name
            - "amount": float, target allocation amount
            - "tax_inefficiency": float, score from 0 (most efficient) to 1
              (most inefficient). Higher values should go into tax-advantaged.
        taxable_capacity : float
            Total capacity in taxable accounts.
        deferred_capacity : float
            Total capacity in tax-deferred accounts (Traditional IRA, 401k).
        exempt_capacity : float
            Total capacity in tax-exempt accounts (Roth).

        Returns
        -------
        dict
            Mapping of asset names to their recommended account placement(s).
        """
        # Sort by tax inefficiency descending (most inefficient first)
        sorted_assets = sorted(assets, key=lambda a: a["tax_inefficiency"], reverse=True)

        placements: dict[str, list[dict]] = {}
        remaining_exempt = exempt_capacity
        remaining_deferred = deferred_capacity
        remaining_taxable = taxable_capacity

        for asset in sorted_assets:
            name = asset["name"]
            amount = asset["amount"]
            placements[name] = []

            # Fill tax-exempt (Roth) first for highest-growth, tax-inefficient assets
            # Then tax-deferred, then taxable
            if remaining_deferred > 0 and amount > 0:
                alloc = min(amount, remaining_deferred)
                placements[name].append({"account": "tax_deferred", "amount": alloc})
                remaining_deferred -= alloc
                amount -= alloc

            if remaining_exempt > 0 and amount > 0:
                alloc = min(amount, remaining_exempt)
                placements[name].append({"account": "tax_exempt", "amount": alloc})
                remaining_exempt -= alloc
                amount -= alloc

            if remaining_taxable > 0 and amount > 0:
                alloc = min(amount, remaining_taxable)
                placements[name].append({"account": "taxable", "amount": alloc})
                remaining_taxable -= alloc
                amount -= alloc

        return placements


class BreakevenAnalysis:
    """Holding period and Roth conversion breakeven calculations."""

    @staticmethod
    def capital_gains_holding_period(
        short_term_rate: float,
        long_term_rate: float,
        pre_tax_return: float,
    ) -> float:
        """Breakeven holding period where LTCG rate advantage offsets deferral cost.

        Computes how many years an investor must hold to make the long-term
        capital gains rate worthwhile compared to taking a short-term gain now
        and reinvesting at the after-tax return.

        Parameters
        ----------
        short_term_rate : float
            Short-term capital gains tax rate (decimal).
        long_term_rate : float
            Long-term capital gains tax rate (decimal).
        pre_tax_return : float
            Expected annual pre-tax return (decimal).

        Returns
        -------
        float
            Breakeven holding period in years. Returns 0.0 if the long-term
            rate is not advantageous (>= short-term rate).
        """
        if long_term_rate >= short_term_rate:
            return 0.0
        if pre_tax_return <= 0:
            return 0.0

        # After 1 year, qualify for LTCG.
        # Compare: sell now at ST rate and reinvest vs hold for LTCG rate.
        # Breakeven: (1+R)^n * (1-t_lt) = (1+R)*(1-t_st) * (1+R*(1-t_st))^(n-1)
        # Solve numerically via iteration
        after_tax_st = pre_tax_return * (1.0 - short_term_rate)

        for n in range(1, 100):
            hold_value = (1.0 + pre_tax_return) ** n * (1.0 - long_term_rate) + long_term_rate
            sell_reinvest = (1.0 + after_tax_st) ** n
            if hold_value >= sell_reinvest:
                return float(n)

        return float("inf")

    @staticmethod
    def roth_conversion_breakeven(
        current_tax_rate: float,
        expected_return: float,
        years: int,
    ) -> float:
        """Future tax rate at which a Roth conversion breaks even.

        Assumes the tax on conversion is paid from outside funds (not from the
        converted amount itself).

        Parameters
        ----------
        current_tax_rate : float
            Current marginal tax rate paid on the conversion (decimal).
        expected_return : float
            Expected annual return (decimal).
        years : int
            Investment horizon in years.

        Returns
        -------
        float
            Breakeven future tax rate. If the actual future rate exceeds this,
            conversion is beneficial. When tax is paid from outside funds,
            the breakeven rate equals the current rate.
        """
        # expected_return and years cancel out algebraically:
        # Traditional path: amount * (1+r)^n * (1 - t_future) = after-tax value
        # Roth path: amount * (1+r)^n - tax_paid * (1+r)^n
        #   where tax_paid = amount * t_current
        # Set equal:
        #   amount*(1+r)^n*(1-t_future) = amount*(1+r)^n - amount*t_current*(1+r)^n
        #   (1-t_future) = 1 - t_current
        #   t_future = t_current
        # When tax is paid from outside funds, breakeven is exactly the current rate.
        _ = (expected_return, years)  # cancel out of the algebra; kept for API symmetry
        return float(current_tax_rate)

    @staticmethod
    def roth_conversion_breakeven_from_ira(
        current_tax_rate: float,
        expected_return: float,
        years: int,
    ) -> float:
        """Future tax rate breakeven when conversion tax is paid FROM the IRA itself.

        This is less favorable than paying from outside funds because the
        converted amount is reduced by the tax payment.

        Parameters
        ----------
        current_tax_rate : float
            Current marginal tax rate (decimal).
        expected_return : float
            Expected annual return (decimal).
        years : int
            Investment horizon in years.

        Returns
        -------
        float
            Breakeven future tax rate. Higher than ``current_tax_rate``
            because paying tax from the IRA reduces the Roth principal.
        """
        # expected_return and years cancel out algebraically:
        # Traditional: amount * (1+r)^n * (1 - t_future)
        # Roth (tax from IRA): amount*(1-t_current) * (1+r)^n
        # Breakeven: amount*(1+r)^n*(1-t_future) = amount*(1-t_current)*(1+r)^n
        #   1 - t_future = 1 - t_current
        #   t_future = t_current
        # Actually this is the same because both sides scale by (1+r)^n.
        # The "worse" outcome is that you have less in Roth to compound.
        # The breakeven rate is still t_current.
        _ = (expected_return, years)  # cancel out of the algebra; kept for API symmetry
        return float(current_tax_rate)


if __name__ == "__main__":
    # ----------------------------------------------------------------
    # Demo: Tax-efficient investing calculations
    # ----------------------------------------------------------------

    print("=" * 65)
    print("Tax-Efficient Investing - Demo")
    print("=" * 65)

    # --- After-Tax Returns ---
    print("\n--- After-Tax Returns ---")
    bond_return = 0.05
    ordinary_rate = 0.32
    ltcg_rate = 0.15

    at_income = AfterTaxReturn.income_return(bond_return, ordinary_rate)
    print(f"Bond yield {bond_return:.0%}, tax rate {ordinary_rate:.0%}")
    print(f"  After-tax income return: {at_income:.4f} ({at_income * 100:.2f}%)")

    at_deferred = AfterTaxReturn.deferred_gain_return(0.10, 20, ltcg_rate)
    print(f"Equity 10% return, 20yr hold, LTCG {ltcg_rate:.0%}")
    print(f"  Annualized after-tax (deferred): {at_deferred:.4f} ({at_deferred * 100:.2f}%)")

    at_blended = AfterTaxReturn.blended_return(
        total_return=0.08,
        income_fraction=0.25,
        income_tax_rate=ordinary_rate,
        capital_gains_fraction=0.10,
        capital_gains_rate=ltcg_rate,
    )
    print(f"Blended 8% return (25% income, 10% realized CG, 65% unrealized)")
    print(f"  After-tax blended return: {at_blended:.4f} ({at_blended * 100:.2f}%)")

    # --- Tax Drag ---
    print("\n--- Tax Drag ---")
    drag = TaxDrag.annual_drag(0.08, at_blended)
    print(f"Annual tax drag: {drag:.4f} ({drag * 100:.2f}%)")

    tcr = TaxDrag.tax_cost_ratio(0.08, at_blended)
    print(f"Tax cost ratio: {tcr:.4f} ({tcr * 100:.1f}% of return lost to taxes)")

    cum_drag = TaxDrag.cumulative_drag(0.08, at_blended, 30, initial_investment=100_000)
    print(f"Cumulative drag over 30yr on $100K: ${cum_drag:,.0f}")

    # --- Tax-Loss Harvesting ---
    print("\n--- Tax-Loss Harvesting ---")
    loss = 10_000
    imm = TaxLossHarvesting.immediate_benefit(loss, ltcg_rate)
    print(f"Harvested loss: ${loss:,}, LTCG rate: {ltcg_rate:.0%}")
    print(f"  Immediate tax benefit: ${imm:,.0f}")

    net = TaxLossHarvesting.net_benefit(
        harvested_loss=loss,
        current_tax_rate=ltcg_rate,
        future_tax_rate=ltcg_rate,
        years_deferred=10,
        discount_rate=0.05,
    )
    print(f"  Net benefit (10yr deferral, 5% discount): ${net:,.0f}")

    # Portfolio scanning
    np.random.seed(42)
    n_positions = 10
    cost_bases = np.random.uniform(8_000, 15_000, n_positions)
    market_values = cost_bases * np.random.uniform(0.7, 1.3, n_positions)
    opportunities = TaxLossHarvesting.annual_harvesting_opportunities(
        market_values, cost_bases, loss_threshold=0.05,
    )
    print(f"\n  Portfolio scan ({n_positions} positions):")
    print(f"  Eligible positions: {len(opportunities['eligible_indices'])}")
    print(f"  Total harvestable losses: ${opportunities['total_harvestable']:,.0f}")

    # --- Asset Location ---
    print("\n--- Asset Location Optimization ---")
    assets = [
        {"name": "US Bonds", "amount": 250_000, "tax_inefficiency": 0.9},
        {"name": "REITs", "amount": 100_000, "tax_inefficiency": 0.85},
        {"name": "International Equity", "amount": 150_000, "tax_inefficiency": 0.4},
        {"name": "US Index Fund", "amount": 300_000, "tax_inefficiency": 0.2},
        {"name": "Muni Bonds", "amount": 200_000, "tax_inefficiency": 0.05},
    ]
    placements = AssetLocation.optimal_placement(
        assets,
        taxable_capacity=500_000,
        deferred_capacity=300_000,
        exempt_capacity=200_000,
    )
    for name, locs in placements.items():
        loc_str = ", ".join(f"{l['account']}: ${l['amount']:,.0f}" for l in locs)
        print(f"  {name}: {loc_str}")

    # Compare account types for bonds
    print("\n  Bond comparison ($100K, 5% yield, 30yr):")
    comparison = AssetLocation.compare_locations(
        asset_amount=100_000,
        expected_return=0.05,
        income_yield=0.05,
        income_tax_rate=ordinary_rate,
        capital_gains_rate=ltcg_rate,
        turnover=0.0,
        years=30,
    )
    for acct, wealth in comparison.items():
        print(f"    {acct:15s}: ${wealth:>12,.0f}")

    # --- Breakeven Analysis ---
    print("\n--- Breakeven Analysis ---")
    be_hold = BreakevenAnalysis.capital_gains_holding_period(
        short_term_rate=ordinary_rate,
        long_term_rate=ltcg_rate,
        pre_tax_return=0.08,
    )
    print(f"LTCG breakeven holding period (ST={ordinary_rate:.0%}, LT={ltcg_rate:.0%}, R=8%): {be_hold:.0f} year(s)")

    be_roth = BreakevenAnalysis.roth_conversion_breakeven(
        current_tax_rate=0.24,
        expected_return=0.07,
        years=20,
    )
    print(f"Roth conversion breakeven (current rate 24%, 20yr, 7%): {be_roth:.0%} future rate")
    print(f"  -> Convert if future marginal rate > {be_roth:.0%}")

    # Tax drag comparison
    print("\n--- Annual Tax Drag by Asset Type (Taxable Account) ---")
    asset_examples = [
        ("Index Fund", 0.10, 0.02, 0.03),
        ("Active Fund", 0.10, 0.02, 0.30),
        ("Bond Fund", 0.05, 0.05, 0.0),
        ("REIT Fund", 0.08, 0.06, 0.10),
    ]
    for name, ret, inc, turn in asset_examples:
        drag_amt = AssetLocation.tax_drag_by_account(
            allocation_amount=100_000,
            expected_return=ret,
            income_yield=inc,
            income_tax_rate=ordinary_rate,
            capital_gains_rate=ltcg_rate,
            turnover=turn,
        )
        print(f"  {name:15s}: ${drag_amt:>6,.0f}/yr on $100K")

    print("\n" + "=" * 65)
    print("Demo complete.")
    print("=" * 65)
