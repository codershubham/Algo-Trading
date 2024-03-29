#indicators_calculation.py

import yfinance as yf
#from plot import *
import pandas_ta as ta
#import pandas as pd


def calculate_macd(ticker):
    # get ticker data 
    df = yf.Ticker(ticker).history(period='1y')[map(str.title, ['open', 'close', 'low', 'high', 'volume'])]
    # calculate MACD values
    df.ta.macd(close='close', fast=12, slow=26, append=True)
    # Force lowercase (optional)
    df.columns = [x.lower() for x in df.columns]
    return df


def calculate_heikin_ashi(ticker):
    #df = yf.Ticker(ticker).history(period='1y')[map(str.title, ['open', 'close', 'low', 'high', 'volume'])]
    #df = df.ta.ha(open=df["open"], high=df["high"], low=df["low"], close=df["close"])
    #create_plot(df)
    return


def calculate_sma(period, list_of_price):
    return


#list of price, first index would be the oldest day price
def calculate_ema(period, list_of_price, smoothing, first_day_ema):
    return
