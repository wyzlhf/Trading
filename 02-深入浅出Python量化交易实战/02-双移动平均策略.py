import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from utils.get_stock_data import get_stock_data_from_akshare

zgpa = get_stock_data_from_akshare()
# print(zgpa)
strategy = pd.DataFrame(index=zgpa.index)
strategy['signal'] = 0
# print(zgpa['Close'])
strategy['avg_5'] = zgpa['Close'].rolling(window=5).mean()
strategy['avg_10'] = zgpa['Close'].rolling(window=10).mean()
strategy['signal'] = np.where(strategy['avg_5'] > strategy['avg_10'], 1, 0)
strategy['order'] = strategy['signal'].diff()

# plt.figure(figsize=(10, 5))
# plt.plot(zgpa['Close'], lw=2, color='red', label='price')
# plt.plot(strategy['avg_5'], lw=2, color='blue', label='avg 5', ls='--')
# plt.plot(strategy['avg_10'], lw=2, color='green', label='avg 10', ls='-.')
# plt.scatter(strategy.loc[strategy.order == 1].index, zgpa['Close'][strategy.order == 1], marker='^', s=80, color='red',
#             label='Buy')
# plt.scatter(strategy.loc[strategy.order == -1].index, zgpa['Close'][strategy.order == -1], marker='v', s=80, color='g',
#             label='Sell')
# plt.legend()
# plt.grid()
# plt.show()

"""开始回测
应该注意回测代码的实现
这个很重要"""
initial_cash=20000
positions=pd.DataFrame(index=strategy.index).fillna(0)
positions['stock']=strategy['signal']*100
# print(positions)
# print('----------------')
portfolio=pd.DataFrame(index=strategy.index)
portfolio['stock value']=positions.multiply(zgpa['Close'],axis=0)
order=positions.diff()
# print(order)
portfolio['cash']=initial_cash-order.multiply(zgpa['Close'],axis=0).cumsum()
portfolio['total']=portfolio['cash']+portfolio['stock value']
# print(portfolio)

plt.figure(figsize=(10,5))
plt.plot(portfolio['total'],lw=2,color='red',label='total')
plt.plot(portfolio['stock value'],lw=2,color='blue',label='stock value',ls='--')
plt.legend()
plt.grid()
plt.show()