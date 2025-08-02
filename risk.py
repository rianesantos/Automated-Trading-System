class RiskManager:
    def __init__(self, max_allocation_per_asset: float, stop_loss: float, stop_gain: float):
        self.max_allocation_per_asset = max_allocation_per_asset
        self.stop_loss = stop_loss
        self.stop_gain = stop_gain
    
    def check_allocation_limits(self, portfolio:dict, total_value: float):
        alerts = []
        for asset in portfolio ['Portfolio'].assets:
            asset_value = asset['quantity'] * asset['avg_price']
            allocation = asset_value / total_value
            
            if allocation > self.max_allocation_per_asset:
                alerts.append(f"[ALERTA] {asset['name']} ultrapssou o limite de alocação: {allocation: .2%}")
        return alerts
    
    def check_stop_limits(self, portfolio: dict, total_value: float):
        alerts = []
        
        for asset in portfolio['Portfolio'].assets:
            asset_value = asset['quantity'] * asset['avg_price']
            allocation = asset_value / total_value
            if allocation > self.max_allocation_per_asset:
                alerts.append(f"[ALERTA] {asset['name']} ultrapassou o limite de alocação: {allocation:.2%}")
        return alerts
    
    
    def check_stop_limits(self, current_prices: dict, portfolio: dict):
        alerts = []
        
        for asset in portfolio['Portfolio'].assets:
            name = asset['name']
            avg_price = asset['avg_price']
            current_prices = current_prices.get(name)
            
            if current_prices is None:
                continue
            
            change = (current_prices - avg_price) / avg_price
            
            if change <= -self.stop_loss:
                alerts.append(f"[STOP LOSS] {name} caiu {change:.2%} desde a compra.")
            elif change >= self.stop_gain:
                alerts.append(f"[STOP GAIN] {name} subiu {change:.2%} desde a compra")
        return alerts
