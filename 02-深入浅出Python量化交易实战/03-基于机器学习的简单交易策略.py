from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame, Series
from sklearn.neighbors import KNeighborsClassifier

from utils.get_stock_data import load_and_save_stock_data_from_akshare
from sklearn.model_selection import train_test_split


def classification_tc(df: DataFrame) -> Tuple[DataFrame | Series, DataFrame | Series]:
    df['Open-Close'] = df['Close'] - df['Open']
    df['High-Low'] = df['High'] - df['Low']
    df['target'] = np.where(df['Close'].shift(-1) > df['Close'], 1, -1)
    df.dropna()
    X = df[['Open-Close', 'High-Low']]
    y = df['target']
    return X, y


def regression_tc(df: DataFrame) -> Tuple[DataFrame | Series, DataFrame | Series]:
    df['Open-Close'] = df['Close'] - df['Open']
    df['High-Low'] = df['High'] - df['Low']
    df['target'] = df['Close'].shift(-1) - df['Close']
    df.dropna()
    X = df[['Open-Close', 'High-Low']]
    y = df['target']
    return X, y


def cum_return(df: DataFrame, split_value: int) -> float:
    cum_return_num: float = df[split_value:]['Return'].cumsum() * 100
    return cum_return_num


def strategy_return(df: DataFrame, split_value: int) -> float:
    df['Strategy_Return'] = df['Return'] * df['Predict_Signal'].shift(1)
    cum_strategy_return: float = df[split_value:]['Strategy_Return'].cumsum() * 100
    return cum_strategy_return
def plot_chart(cum_retrun:float,cum_strategy_return:float,symbol:str)->None:
    plt.figure(figsize=(9,6))
    plt.plot(cum_retrun,'--',label=f'{symbol} Returns')
    plt.plot(cum_strategy_return,label='Strategy Returns')
    plt.legend()
    plt.show()

zgpa = load_and_save_stock_data_from_akshare()
X, y = classification_tc(zgpa)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8)
knn_clf = KNeighborsClassifier(n_neighbors=95)
knn_clf.fit(X_train, y_train)
print(knn_clf.score(X_train, y_train))
print(knn_clf.score(X_test, y_test))
zgpa['Predict_Signal'] = knn_clf.predict(X)
zgpa['Return'] = np.log(zgpa['Close'] / zgpa['Close'].shift(1))
print(zgpa)
cum_return_num=cum_return(zgpa,len(X_train))
cum_stragegy_return=strategy_return(zgpa,len(X_train))
plot_chart(cum_return_num,cum_stragegy_return,'zgpa')
