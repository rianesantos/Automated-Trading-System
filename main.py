from market_data import get_historical_data, get_current_price
from strategies import moving_average_strategy
import matplotlib.pyplot as plt

def main():
    ticker = 'AAPL' #pode ser alterado para qualquer outra
    print("Coletando dados...")
    data = get_historical_data(ticker)
    
    print("Aplicando estrategias...")
    signals = moving_average_strategy(data)
    
    print("Gerando gráficos...")
    plot_signals (signals, ticker)
    
def plot_signals (signals, ticker):
    plt.figure(figsize = (12,6))
    plt.plot(signals['Close'], label = 'Preço de Fechamento', color = 'black')
    plt.plot(signals['Short_MA'], label = 'Média Curta (5)', color = 'blue', linestyle = '--')
    plt.plot(signals['Long_MA'], label = 'Média Longa (20)', color = 'red', linestyle = '--')
    
    #Para marcar pontos de compra e venda.
    buy_signals = signals[signals['Position'] == 1.00] 
    sell_signals = signals[signals['Position'] == -1.00]
    
    plt.plot(buy_signals.index, buy_signals['Close'], '^', markersize = 10, color = 'green', label = 'Compra')
    plt.plot(sell_signals.index, sell_signals['Close'], 'v', markersize = 10, color = 'red', label = 'Venda')
    
    plt.title (f"Estrátegia de Médias Móveis - {ticker}")
    plt.xlabel("Data")
    plt.ylabel("Preço")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    main() 
