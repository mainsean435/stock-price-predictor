import pandas as pd
from datetime import datetime
import config
from random import randint, choice
from prophet import Prophet
import os


def get_historical_data(ticker):
  filepath = f"{config.BASE_DIR}/stocks_data/historical_data/{ticker}.csv"
  df = pd.read_csv(filepath)

  df = df.sort_values('Date')
  df['Date'] = df['Date'].apply(
      lambda x: datetime.strptime(x, r'%Y-%m-%d').timestamp()*1000)

  data = dict()
  data['open'] = df[['Date', ' Open']].values.tolist()
  data['high'] = df[['Date', ' High']].values.tolist()
  data['low'] = df[['Date', ' Low']].values.tolist()
  data['close'] = df[['Date', ' Close']].values.tolist()
  data['volume'] = df[['Date', ' Volume']].values.tolist()
  data['previous_close'] = data['close'][-1][1]
  data['change'] = round(data['previous_close'] - data['close'][-2][1], 3)
  data['change_percent'] = round(
      abs(data['change']) / data['previous_close'], 3)
  return data


def get_closing_price(ticker):
    filepath = f"{config.BASE_DIR}/stocks_data/historical_data/{ticker}.csv"
    df = pd.read_csv(filepath)

    df = df.sort_values('Date')
    df['Date'] = df['Date'].apply(
        lambda x: datetime.strptime(x, r'%Y-%m-%d'))
    return df[['Date', ' Close']]


def get_live_price(ticker):
    data = get_historical_data(ticker)
    op = choice(["+", "-"])
    price = data['previous_close']
    price += (randint(0, 30)/10) if op == "+" else -(randint(0, 30)/10)
    return round(price, 2)


def get_predictions(ticker, periods=365):
    data = get_closing_price(ticker)
    data = data.rename(columns={'Date': 'ds', ' Close': 'y'})

    filepath = f"{config.BASE_DIR}/stocks_data/predictions_data/{ticker}.csv"
    if f"{ticker}.csv" not in os.listdir(f"{config.BASE_DIR}/stocks_data/predictions_data/"):
        m = Prophet(daily_seasonality=True)
        m.fit(data)
        future = m.make_future_dataframe(periods=periods)
        prediction = m.predict(future)
        prediction['ds'] = prediction['ds'].apply(lambda x : x.timestamp())
        prediction.index = prediction['ds']
        prediction.to_csv(filepath)
    data = pd.read_csv(filepath)
    return data[['ds', 'yhat']].values.tolist()[-365:]
    
