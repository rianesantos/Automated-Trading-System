from fastAPI.models.market_model import HistoricalDataRequest
from typing import Dict
import yfinance as yf
import pandas as pd

class MarketService:
    @staticmethod
    def get_historical_data(request: HistoricalDataRequest) -> pd.DataFrame:
        data = yf.download(
            tickers = request.ticker,
            period = request.period,
            interval = request.interval,
            auto_adjust = True,
            progress = False
        )
        return data.reset_index()

    @staticmethod
    def get_current_prices(tickers: list) -> Dict[str, float]:
        data = yf.download(
            tickers = tickers,
            period = '1d',
            group_by = 'ticker',
            progress = False
        )
        return {ticker: data[ticker]['Close'].iloc[-1] for ticker in tickers}
