from market_data import get_historical_data, get_current_price
from strategies import moving_average_strategy
from backtest import backtest_strategy
from risk import RiskManager
from alerts import RealTimeNotifier
from portfolio import Portfolio
import matplotlib.pyplot as plt

notifier = RealTimeNotifier()
Portfolio = Portfolio()

def plot_signals (signals, ticker):
    plt.figure(figsize = (12,6))
    plt.plot(signals['Close'], label = 'Closing price', color = 'black')
    plt.plot(signals['Short_MA'], label = 'Short-term moving average (5d)', color = 'blue', linestyle = '--')
    plt.plot(signals['Long_MA'], label = 'Long-term moving average (20d)', color = 'red', linestyle = '--')
    
    #Para marcar pontos de compra e venda.
    buy_signals = signals[signals['Position'] == 1.00] 
    sell_signals = signals[signals['Position'] == -1.00]
    
    plt.plot(buy_signals.index, buy_signals['Close'], '^', markersize = 10, color = 'green', label = 'Sell')
    plt.plot(sell_signals.index, sell_signals['Close'], 'v', markersize = 10, color = 'red', label = 'Buy')
    
    plt.title (f"Moving Averages Strategy - {ticker}")
    plt.xlabel("DataReal-time data")
    plt.ylabel("Price")
    plt.legend()
    plt.tight_layout()
    plt.ioff()
    plt.show()
    plt.close()

def analyze_stock(ticker):
    print(f"\n 🔍︎ Analyzing {ticker}...")
    
    print("📈 Fetching historical data...")
    data = get_historical_data(ticker)
    if data.empty:
        print("✖ Failed to fetch data...")
        return
    
    print("⚙️ Running MA crossover strategy...")
    signals = moving_average_strategy (data)
    
    print("📊 Generating chart...")
    plot_signals(signals, ticker)
    
    print("💼 Running backtest...")
    result = backtest_strategy(signals, ticker)
    current_prices = get_current_price(ticker)
    total_value = result['Portfolio'].get_total_value(current_prices)
    
    print(f"💰 Current portfolio value: ${total_value:.2f}")
    
    print("🚨 Checking market alerts...")
    alerts = notifier.update_and_check ({ticker: current_prices.get(ticker)})
    for alert in alerts:
        print(alert)
        
    print("📉 Risk assessment...")
    risk_manager = RiskManager(0.5, 0.1, 0.2)
    portfolio_obj = result['Portfolio']
    risk_alerts = risk_manager.check_allocation_limits(portfolio_obj, total_value)

    
    for alert in risk_alerts:
        print (alert)
        
    global Portfolio
    portfolio = result['Portfolio']
    
def show_portfolio():
    if not Portfolio.assets:
        print("📭 Your portfolio is empty.")
        return
    
    print("\n📂 Current Portfolio:")
    for asset in Portfolio.assets:
        print(f"{asset['name']} - {asset['quantity']} share @ ${asset['avg_pride']:.2f}")
    print(f"💵 Balance: ${Portfolio.balance:.2f}")
    
def menu():
        while True:
            print("\n===== MAIN MENU =====")
            print("1. Analyze a stock")
            print("2.View current portfolio")
            print("3. Exit")
            option = input("Select an option: ")
            
            if option == "1":
                ticker = input("Enter ticker (ex: AAPL): ").upper()
                analyze_stock(ticker)
            elif option == "2":
                show_portfolio()
            elif option == "3":
                print("👋 Exiting...")
                break
            else:
                print("✖ Invalid option. Please try again")

if __name__ == "__main__":
    menu()
    
