import akshare as ak
import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import tushare as ts
# 显示所有列
pd.set_option('display.max_columns', None)
# # 显示所有行
pd.set_option('display.max_rows', None)
# 不换行显示
pd.set_option('display.width', 1000)
# 设置选项
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180)  # 设置打印宽度(**重要**)

start_date = '20200101'
end_date = '20200320'

data: DataFrame = ak.stock_zh_a_hist(symbol="601318", period="daily", start_date=start_date, end_date=end_date,
                                     adjust="")
# data: DataFrame = data[['日期', '最高', '最低', '开盘', '收盘', '成交量']]
# print(data)

zgpa:DataFrame=data[['日期', '最高', '最低', '开盘', '收盘', '成交量']]
zgpa.columns=['Date', 'High', 'Low', 'Open', 'Close', 'Volume']
zgpa.set_index('Date', inplace=True)
zgpa_signal=pd.DataFrame(index=zgpa.index)
zgpa_signal['price']=zgpa['Close']
zgpa_signal['diff']=zgpa_signal['price'].diff()
zgpa_signal=zgpa_signal.fillna(0.0)
zgpa_signal['signal']=np.where(zgpa_signal['diff']>=0,0,1)
zgpa_signal['order']=zgpa_signal['signal'].diff()*100


initial_cash=20000
zgpa_signal['stock']=zgpa_signal['order']*zgpa_signal['price']
zgpa_signal['cash']=initial_cash-(zgpa_signal['order'].diff()*zgpa_signal['price']).cumsum()
# zgpa_signal['order_diff']=zgpa_signal['order'].diff()
# zgpa_signal['diff_cal']=initial_cash-(zgpa_signal['order_diff']*zgpa_signal['price']).cumsum()
zgpa_signal['total']=zgpa_signal['stock']+zgpa_signal['cash']
zgpa_signal['stock_value']=zgpa_signal['order'].cumsum()*zgpa_signal['price']
print(zgpa_signal)

plt.figure(figsize=(10, 6))
plt.plot(zgpa_signal['total'])
plt.plot(zgpa_signal['order'].cumsum()*zgpa_signal['price'],'--',label='stock value')

plt.grid()
plt.legend(loc='center right')
plt.show()