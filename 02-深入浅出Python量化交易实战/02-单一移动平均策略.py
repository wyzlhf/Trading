import akshare as ak
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

from utils.get_stock_data import get_stock_data_from_akshare
from utils.get_keys import get_tushare_key
from pylab import mpl
mpl.rcParams["font.sans-serif"] = ["Arial Unicode MS"] ## mac
plt.rcParams['font.family']=['Arial Unicode MS'] ## mac
mpl.rcParams["font.sans-serif"] = ["SimHei"] ## win
plt.rcParams['font.family']=['SimHei'] ## win
mpl.rcParams["axes.unicode_minus"] = False




# zgpa = get_stock_data_from_akshare()
# period = 10
# avg_10 = []
# avg_value = []
# # print(zgpa['Close'])
# for price in zgpa['Close']:
#     avg_10.append(price)
#     if len(avg_10) > period:
#         del avg_10[0]
#     avg_value.append(np.mean(avg_10))
#
# zgpa = zgpa.assign(avg_10=pd.Series(avg_value, index=zgpa.index))
# print(zgpa)
# plt.figure(figsize=(10, 6))
# plt.plot(zgpa['Close'], lw=2, c='k')
# plt.plot(zgpa['avg_10'], '--', lw=5, c='b')
# plt.legend('123')
# plt.grid()
# plt.show()


def get_SMA_data() -> DataFrame:
    zgpa: DataFrame = get_stock_data_from_akshare()
    period: int = 10
    avg_10: list = []
    avg_value: list = []
    for price in zgpa['Close']:
        avg_10.append(price)
        if len(avg_10) > period:
            del avg_10[0]
        avg_value.append(np.mean(avg_10))

    zgpa: DataFrame = zgpa.assign(avg_10=pd.Series(avg_value, index=zgpa.index))
    return zgpa


def plot_SMA_data(SMA_data: DataFrame) -> None:
    plt.figure(figsize=(10, 6))
    plt.plot(SMA_data['Close'], lw=2, c='k',label='Close Price')
    plt.plot(SMA_data['avg_10'], '--', lw=5, c='b',label='Average 10')
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == '__main__':
    zgpa = get_SMA_data()
    plot_SMA_data(zgpa)
