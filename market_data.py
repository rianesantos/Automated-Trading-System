import yfinance as yf
import pandas as pd

def get_historical_data(ticker, period = '6mo', interval = '1d'):
    data = yf.download(ticker, period = period, interval = interval)
    return data

def get_current_price (ticker):
    stock = yf.Ticker(ticker)
    todays_data = stock.history(period = '1d')
    return todays_data['Fechar'].iloc[-1]
