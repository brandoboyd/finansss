import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2019,4,8)
end = dt.datetime(2020,4,8)

df = web.DataReader('MSFT', 'yahoo', start, end)
df.to_csv('msft.csv')
df = pd.read_csv('msft.csv', parse_dates =True, index_col=0)

df['Adj Close'].plot()
