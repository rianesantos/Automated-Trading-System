class RiskManager:
    def __init__(self, max_allocation_per_asset: float, stop_loss: float, stop_gain: float):
        self.max_allocation_per_asset = max_allocation_per_asset
        self.stop_loss = stop_loss
        self.stop_gain = stop_gain

    def _get_portfolio_obj(self, portfolio):
        # If portfolio is a dict, extract the Portfolio object
        if isinstance(portfolio, dict) and 'Portfolio' in portfolio:
            return portfolio['Portfolio']
        return portfolio

    def check_allocation_limits(self, portfolio, total_value: float):
        alerts = []
        portfolio_obj = self._get_portfolio_obj(portfolio)

        for asset in portfolio_obj.assets:
            asset_value = asset['quantity'] * asset['avg_price']
            allocation = asset_value / total_value

            if allocation > self.max_allocation_per_asset:
                alerts.append(f"[ALERT] {asset['name']} exceeded allocation limit: {allocation:.2%}")
        return alerts

    def check_stop_limits(self, current_prices: dict, portfolio):
        alerts = []
        portfolio_obj = self._get_portfolio_obj(portfolio)

        for asset in portfolio_obj.assets:
            name = asset['name']
            avg_price = asset['avg_price']
            current_price = current_prices.get(name)

            if current_price is None:
                continue

            change = (current_price - avg_price) / avg_price

            if change <= -self.stop_loss:
                alerts.append(f"[STOP LOSS] {name} dropped {change:.2%} since purchase.")
            elif change >= self.stop_gain:
                alerts.append(f"[STOP GAIN] {name} rose {change:.2%} since purchase.")
        return alerts
