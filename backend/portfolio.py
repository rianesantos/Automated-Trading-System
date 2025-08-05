import pandas as pd

class Portfolio:
    def __init__(self):
        self.assets = []
        self.balance = 0.0
        self.trade_history = []
        
    def add_assets(self, name, quantity, price):
        asset = {
            'name': name,
            'quantity': quantity,
            'purchase_price': price,
            'current_price' : price
        }
        self.assets.append(asset)
        self.trade_history.append({
            'type' : 'BUY',
            'ticker' : name,
            'quantity' : quantity,
            'price' : price,
            'timestamp' : pd.Timestamp.now()
        })
        
    def sell_assets (self, ticker, price):
        total_sold = 0
        assets_to_keep = []
        
        for asset in self.assets:
            if asset['name'] == ticker:
                total_sold += asset ['quantity'] * price
            else:
                assets_to_keep.append(asset)
        
        self.assets = assets_to_keep
        self.balance += total_sold
        return total_sold
    
    def sell_all (self, current_price, asset) :
        total = 0.0
        if self.assets:
            total = sum(asset['quantity'] * current_price for asset in self.assets)
            self.trade_history ({
                'type' : 'SELL',
                'ticker' : self.assets[0]['name'],
                'quantity' : sum (asset['quantity'] for asset in self.assets),
                'price' : current_price,
                'timestamp' : pd.Timestamp.now
            }) 
            self.assets.clear ()
        return total
    
    def get_total_value(self, current_prices):
        assets_value = sum(
            asset['quantity'] * (current_prices.get(asset['name']) or 0.0)
            for asset in self.assets
        )
        return self.balance + assets_value

    def calculate_total_value(self):
        total = 0.0
        for asset in self.assets:
            total += asset ['quantity'] * asset ['price']
        return total
    
    def list_portfolio(self):
        if not self.assets:
            print("A carteira está vazia")
            return

        print("\n === Posições Atuais ===")
        for asset in self.assets:
            print(f"{asset['name']}: {asset['quantity']} ações | "
                f"Preço médio: ${asset['purchase_price']:.2f} | "
                f"Valor atual: ${asset['quantity'] * asset['current_price']:.2f}")
        print(f"Saldo disponível: ${self.balance:.2f}")
        print("==============================")
