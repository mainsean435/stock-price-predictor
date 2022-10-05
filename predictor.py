
from prophet import Prophet
from utils import get_close_price

def get_predictions(symbol, periods=365):
  data = get_close_price(symbol)
  data = data.rename(columns={'Date':'ds', ' Close':'y'})
  m = Prophet(daily_seasonality = True)
  m.fit(data)
  
  future = m.make_future_dataframe(periods=periods)
  prediction = m.predict(future)
  prediction['ds'] = prediction['ds'].apply(lambda x : x.timestamp())
  return prediction[['ds', 'yhat']].values.tolist()




