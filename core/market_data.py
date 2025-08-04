import yfinance as yf
import pandas as pd
from typing import Union, Dict

def get_historical_data (ticker: Union [str, list], period: str = '6mo', interval: str = '1d') -> pd.DataFrame:
    try: 
        data = yf.download(ticker, period = period, interval = interval, progress = False, auto_adjust = True)
        return data
    
    except Exception as e:
        print(f"Erro ao obter dados historicos para {ticker}: {str(e)}")
        return pd.DataFrame
    
def get_current_price(tickers: Union[str, list]) -> Dict[str, float]:
    if isinstance(tickers, str):
        tickers = [tickers]

    prices = {}

    try:
        data = yf.download(tickers, period='1d', auto_adjust = True, group_by='ticker', progress=False)

        for ticker in tickers:
            try:
                # Verifica se os dados retornaram no formato com múltiplos tickers
                if ticker in data.columns.get_level_values(0):
                    close_price = data[ticker]['Close'].iloc[-1]
                else:
                    close_price = data['Close'].iloc[-1]
                
                prices[ticker] = float(close_price)
                print(f"[INFO] Preço atual de {ticker}: {close_price}")

            except Exception as e:
                prices[ticker] = None
                print(f"[ERRO] Não foi possível obter preço para {ticker}: {e}")

        return prices

    except Exception as e:
        print(f"[ERRO GERAL] Falha ao baixar dados de mercado: {e}")
        return {ticker: None for ticker in tickers}
