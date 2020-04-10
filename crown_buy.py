import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2017,4,8)
end = dt.datetime(2020,4,8)
today = dt.datetime(2020,4,8)

df = web.DataReader('CCI', 'yahoo', start, end)
df.to_csv('cci.csv')
df = pd.read_csv('cci.csv', parse_dates =True, index_col=0)

df['Adj Close'].plot()

df['200ma'] = df['Adj Close'].rolling(window=200).mean()

print (df.tail())

df2 = web.DataReader('CCI', 'yahoo', today, today)
now = df2['Adj Close'].values 

#Determine the object type for this bracketed response
print(type(now))
print(now[0])

#Access the integer in the numpy array
todaynum = now[0]

if todaynum >20:
    print ("Buy Crown Castle Dummy!")
