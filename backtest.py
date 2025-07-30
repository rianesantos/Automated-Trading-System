import pandas as pd

def backtest_strategy(signals, initial_cash = 10000):
    portfolio = pd.DataFrame(index = signals.index)
    portfolio ['Holdings'] = pd.Series(0.0, index = signals.index, dtype = 'float64')
    portfolio['Cash'] = pd.Series(initial_cash, index = signals.index, dtype = 'float64')
    portfolio['Total'] = pd.Series(initial_cash, index = signals.index, dtype = 'float64')
    
    position = 0 # Quantidadae de ações compradas
    cash = initial_cash
    
    for i in range(1, len(signals)):
        price = signals['Close'].iloc[i]
        if isinstance(price, pd.Series):
                price = price.iloc[0]
                price = float(price)

        signal = signals ['Position'].iloc[i]
        
        if signal == 1:
            # Compra total
            
            position = cash // price
            cash -= position * price
            
        elif signal == -1:
            # Venda total
            cash += position * price
            position = 0
        
    portfolio.loc[portfolio.index[i], 'Holdings'] = float(position * price)
    portfolio.loc[portfolio.index[i], 'Cash'] = float(cash)
    portfolio.loc[portfolio.index[i], 'Total'] = float(position * price + cash)



    return portfolio
