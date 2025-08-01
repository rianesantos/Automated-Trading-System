import pandas as pd
from portfolio import Portfolio

def create_dataframe(signals, portfolio, initial_cash):
    df = pd.DataFrame(index = signals.index)
    df ['Holdings'] = 0.0
    df['Cash'] = float(initial_cash)
    df['Total'] = float(initial_cash)
    
    current_cash = initial_cash
    current_assets = 0
    
    for i in range(1, len (signals)):
        price = signals ['Close'].iloc[i]
        signal = signals ['Position'].iloc[i]
        
        if signal == 1:
            current_assets = current_cash // price
            current_cash -= current_assets * price
        elif signal == -1:
            current_cash += current_cash * price 
            current_assets = 0
            
            df.at[df.index[i], 'Holdings'] = float(current_assets * price)
            df.at[df.index[i], 'Cash'] = float(current_cash)
            df.at[df.index[i], 'Total'] = float(current_assets * price + current_cash)
            
        return df

def backtest_strategy(signals, ticker = 'AAPL',initial_cash = 10000):
    portfolio = Portfolio()
    portfolio.balance = initial_cash
    
    for i in range(1, len(signals)):
        price = float(signals['Close'].iloc[i] if isinstance(signals['Close'].iloc[i], pd.Series)
                      else signals ['Close'].iloc[i])
        signal = signals ['Position'].iloc[i]
        
        if signal == 1:
            buy_quantity = int (portfolio.balance // price)
            if buy_quantity > 0:
                portfolio.add_assets(ticker, buy_quantity, price)
                portfolio.balance -= buy_quantity * price
        elif signal == -1:
            portfolio.sell_assets(ticker, price)
    
    return {
        'DataFrame' : create_dataframe(signals, portfolio, initial_cash),
        'Portfolio' : portfolio
    }
