import matplotlib.pyplot as plt
import pandas as pd
from utils.get_stock_data import get_stock_data_from_akshare

zgpa = get_stock_data_from_akshare()
turtle = pd.DataFrame(index=zgpa.index)
turtle['date'] = zgpa['Date']
turtle['high'] = zgpa['Close'].shift(1).rolling(5).max()
turtle['low'] = zgpa['Close'].shift(1).rolling(5).min()
turtle['buy'] = zgpa['Close'] > turtle['high']
turtle['sell'] = zgpa['Close'] < turtle['low']
turtle['orders'] = 0

position = 0
# print(turtle.sell.values)
for k in range(len(turtle)):
    if turtle.buy[k] and position == 0:
        turtle.orders.values[k] = 1
        position = 1
    elif turtle.sell[k] and position > 0:
        turtle.orders.values[k] = -1
        position = 0

# plt.figure(figsize=(10,5))
# plt.plot(zgpa['Close'],lw=2,color='red',label='Close')
# plt.plot(turtle['high'],lw=2,color='green',ls='--',label='High')
# plt.plot(turtle['low'],lw=2,color='blue',ls='--',label='Low')
# plt.scatter(turtle.loc[turtle.orders==1].index,zgpa['Close'][turtle.orders==1],color='red',marker='^',label='Buy',s=80)
# plt.scatter(turtle.loc[turtle.orders==-1].index,zgpa['Close'][turtle.orders==-1],marker='v',s=80,color='g',label='Sell')
# plt.legend()
# plt.grid()
# plt.show()

initial_cash = 20000
positions = pd.DataFrame(index=turtle.index).fillna(0.0)
# positions['Date'] = turtle['date']
positions['stock'] = 100 * turtle['orders'].cumsum()
portfolio=positions.multiply(zgpa['Close'],axis=0)
portfolio['holding_value']=(positions.multiply(zgpa['Close'],axis=0))
pos_diff=positions.diff()
portfolio['cash']=initial_cash-(pos_diff.multiply(zgpa['Close'],axis=0)).cumsum()
portfolio['total']=portfolio['cash']+portfolio['holding_value']

plt.figure(figsize=(10,5))
plt.plot(portfolio['total'],label='total')
plt.plot(portfolio['holding_value'],'--',label='holding_value')
plt.grid()
plt.legend()
plt.show()