import akshare as ak
import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import tushare as ts

#
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

data: DataFrame = ak.stock_zh_a_hist(symbol="601318", period="daily", start_date="20200101", end_date='20200318',
                                     adjust="")
data: DataFrame = data[['日期', '最高', '最低', '开盘', '收盘', '成交量']]
data['diff'] = data['收盘'].diff()
data['Signal'] = np.where(data['diff'] > 0, 1, 0)
print(data.head())

# TuShareToken=os.environ.get('tushare')
# ts.set_token(TuShareToken)
# pro = ts.pro_api()
#
# df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20180718')
# print(df)
# plt.figure(figsize=(10, 5))
# data['收盘'].plot(linewidth=2, color='green', grid=True)
# # plt.plot(data['开盘'],linewidth=2,color='red')
#
# plt.scatter(data['收盘'].loc[data.Signal == 1].index, data['收盘'].loc[data.Signal == 1], marker='v', s=80, c='g')
# plt.scatter(data['收盘'].loc[data.Signal == 0].index, data['收盘'].loc[data.Signal == 0], marker='^', s=80, c='r')
# plt.show()
