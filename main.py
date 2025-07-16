from market_data import get_historical_data, get_current_price

def main():
    ticker = 'AAPL' #pode ser alterado para qualquer outra
    print("Coletando dados...")
    data = get_historical_data(ticker)
    print(data.tail())
    
    print (f"\n Último preço de {ticker}: R${get_current_price(ticker):.2f}")
    
if __name__ == "__main__":
    main() 
