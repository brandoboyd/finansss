import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2017,4,8)
end = dt.datetime(2020,4,8)

df = web.DataReader('AMT', 'yahoo', start, end)
df.to_csv('amt.csv')
df = pd.read_csv('amt.csv', parse_dates =True, index_col=0)

df['Adj Close'].plot()

df['200ma'] = df['Adj Close'].rolling(window=200).mean()

print (df.tail())
