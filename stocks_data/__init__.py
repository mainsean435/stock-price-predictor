import pandas as pd
from datetime import datetime
import config


def get_data(symbol):
  filepath = f"{config.BASE_DIR}/stocks_data/{symbol}.csv"
  df = pd.read_csv(filepath)

  df = df.sort_values('Date')
  df['Date'] = df['Date'].apply(
      lambda x: datetime.strptime(x, r'%Y-%m-%d').timestamp())

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
