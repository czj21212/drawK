# -*- coding: utf-8 -*-
"""
Created on Sun May 31 22:10:51 2020

@author: Jenny Lu
"""

import re,time,csv,datetime
import urllib.request
import matplotlib as mpl
import matplotlib.pyplot as plt
import mpl_finance as mpf
import matplotlib.dates as mpd
from matplotlib.backends.backend_pdf import PdfPages
from pandas import DataFrame, Series
import pandas as pd; import numpy as np
from matplotlib import dates as mdates

stock_b_code = 'abc010' #股票名称
filename = 'stockdata.xlsx'
returndata = pd.read_excel(filename, sheet_name=stock_b_code, index_col = 0, encoding = 'gbk')
returndata = pd.DataFrame(returndata)

# Wash data
returndata.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
returndata.index.name = 'DateTime'
returndata=returndata.ix[3:]
#returndata['DateTime'] = returndata.index.map(mdates.date2num)
#returndata = returndata.sort_index()
#    returndata.drop('amount', axis=1, inplace = True)
#returndata.drop(returndata.index[:3]) # 删除多余的行
(m, n)=np.shape(returndata)

# get the price data 
pr = []
for i in range(0,m):
#    temp = [int(j) for j in returndata.index.values[i].split('/')]
#    temp = tuple(temp)
    date_time = datetime.datetime.strptime(returndata.index.values[i].replace(" ", ""), '%Y/%m/%d')
    t = mdates.date2num(date_time)
#    print(temp)
    pr.extend([[
        t,
        returndata.Open.values[i],
        returndata.High.values[i],
        returndata.Low.values[i],
        returndata.Close.values[i],
        returndata.Volume.values[i]
        ]])
		  
quotes = pr[0:]

#print(quotes)

fig,ax = plt.subplots(figsize=(30,6))
fig.subplots_adjust(bottom=0.2)
mpf.candlestick_ohlc(ax,quotes,width=0.4,colorup='r',colordown='g')
plt.grid(False)
ax.xaxis_date()
ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=30) 
#pdf = PdfPages()
plt.savefig(stock_b_code + '.pdf')
plt.show()

print ('savefig...')


