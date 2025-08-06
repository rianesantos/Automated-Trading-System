import pandas as pd
from portfolio import Portfolio

def create_dataframe(signals, portfolio, initial_cash):
    df = pd.DataFrame(index=signals.index)
    df['Holdings'] = 0.0
    df['Cash'] = float(initial_cash)
    df['Total'] = float(initial_cash)
    
    current_cash = initial_cash
    current_assets = 0
    
    for i in range(1, len(signals)):
        price = signals['Close'].iloc[i]

        if hasattr(price, "item"):
            price = price.item()
        else:
            price = float(price)
        
        signal = signals['Position'].iloc[i]
        
        # Buy
        if signal == 1:
            qty = int(current_cash // price)
            if qty > 0:
                current_assets += qty
                current_cash -= qty * price
        
        # Sell
        elif signal == -1:
            if current_assets > 0:
                current_cash += current_assets * price
                current_assets = 0
        
        # Update DataFrame
        df.at[df.index[i], 'Holdings'] = current_assets * price
        df.at[df.index[i], 'Cash'] = current_cash
        df.at[df.index[i], 'Total'] = current_assets * price + current_cash

    return df

def backtest_strategy(signals, ticker='AAPL', initial_cash=10000):
    portfolio = Portfolio()
    portfolio.balance = initial_cash
    
    for i in range(1, len(signals)):
        price = signals['Close'].iloc[i]
        # Converte com segurança para float
        if hasattr(price, "item"):
            price = price.item()
        else:
            price = float(price)
        
        signal = signals['Position'].iloc[i]
        
        # Buy
        if signal == 1:
            buy_quantity = int(portfolio.balance // price)
            if buy_quantity > 0:
                portfolio.add_assets(ticker, buy_quantity, price)
                portfolio.balance -= buy_quantity * price
        
        # Sell
        elif signal == -1:
            portfolio.sell_assets(ticker, price)
    
    return {
        'DataFrame': create_dataframe(signals, portfolio, initial_cash),
        'Portfolio': portfolio
    }
