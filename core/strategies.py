import pandas as pd

def moving_average_strategy(data, short_window = 5, long_window = 20):
    signals = data.copy()
    
    signals['Short_MA'] = signals ['Close'].rolling(window = short_window).mean()
    signals['Long_MA'] = signals ['Close'].rolling(window = long_window).mean()
    signals['Signal'] = 0

    signals.fillna(0, inplace=True) 
    signals.iloc[short_window:, signals.columns.get_loc('Signal')] = (
        signals['Short_MA'].iloc[short_window:] > signals['Long_MA'].iloc[short_window:]).astype(int)
    
    signals['Position'] = signals['Signal'].diff()
    
    return signals   
