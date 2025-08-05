from typing import Dict

class RealTimeNotifier:
    
    def __init__(self, price_threshold: float = 0.05):
        self.price_threshold = price_threshold # ex: 5% de variação
        self.last_prices = {}
        
    def update_and_check(self, current_prices: Dict[str, float]):
        alerts = []
        
        for ticker, new_price in current_prices.items():
            if ticker in self.last_prices:
                old_price = self.last_prices[ticker]
                if old_price is not None and new_price is not None:
                    change = (new_price - old_price) / old_price
                    if abs (change) >= self.price_threshold:
                        direction = "subiu" if change > 0 else "caiu"
                        alerts.append(f"[ALETA] {ticker} {direction} {change:.2%} desde o ultimo preco.")
            self.last_prices[ticker] = new_price
        return alerts
    
    def notify_portfolio_change(self, ticker: str, action: str, quantity: int):
        return f"[CARTEIRA] {action.upper()} de {quantity} unidades de {ticker}."
