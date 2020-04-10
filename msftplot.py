import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

import msft

style.use('ggplot')


df = pd.read_csv('msft.csv', parse_dates =True, index_col=0)

df['Adj Close'].plot()
