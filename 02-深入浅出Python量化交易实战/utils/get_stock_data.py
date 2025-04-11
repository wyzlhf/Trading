import akshare as ak
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame


def get_stock_data_from_akshare(stock_code="601318", start_date='20200101', end_date='20200320') -> DataFrame:
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
    data: DataFrame = ak.stock_zh_a_hist(symbol="601318", period="daily", start_date=start_date, end_date=end_date,
                                         adjust="")
    # data: DataFrame = data[['日期', '最高', '最低', '开盘', '收盘', '成交量']]
    # print(data)

    zgpa: DataFrame = data[['日期', '最高', '最低', '开盘', '收盘', '成交量']]
    zgpa.columns = ['Date', 'High', 'Low', 'Open', 'Close', 'Volume']
    # zgpa.set_index('Date', inplace=True)
    # zgpa_signal = pd.DataFrame(index=zgpa.index)
    # zgpa_signal['price'] = zgpa['Close']
    # zgpa_signal['diff'] = zgpa_signal['price'].diff()
    # zgpa_signal = zgpa_signal.fillna(0.0)
    # zgpa_signal['signal'] = np.where(zgpa_signal['diff'] >= 0, 0, 1)
    # zgpa_signal['order'] = zgpa_signal['signal'].diff() * 100
    return zgpa


def load_and_save_stock_data_from_akshare(stock_code: str = '601318', start_date: str = '20170309',
                                          end_date: str = '20200305', out_file: str = '601318.pkl') -> DataFrame:
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
    try:
        df = pd.read_pickle(out_file)
        print('载入股票数据文件完毕')
    except FileNotFoundError:
        print('文件未找到，重新下载中……')
        df: DataFrame = ak.stock_zh_a_hist(symbol="601318", period="daily", start_date=start_date, end_date=end_date,
                                           adjust="")
        df: DataFrame = df[['日期', '最高', '最低', '开盘', '收盘', '成交量']]
        df.columns = ['Date', 'High', 'Low', 'Open', 'Close', 'Volume']
        df.set_index("Date", inplace=True)
        df.to_pickle(out_file)
        print('下载完成')
    return df


def get_money_flow(
        stock_code: str = '002458',
        # start_date: str = '20170309',
        # end_date: str = '20200418',
        market: str = 'sh'
) -> DataFrame:
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
    stock_individual_fund_flow_df = ak.stock_individual_fund_flow()
    df: DataFrame = pd.DataFrame(index=stock_individual_fund_flow_df.index)
    df['date'] = stock_individual_fund_flow_df['日期']
    df['sec_code'] = stock_code + '.sh'
    df['change_pct'] = stock_individual_fund_flow_df['涨跌幅']
    df['net_amount_main'] = stock_individual_fund_flow_df['主力净流入-净额']
    df['net_pct_main'] = stock_individual_fund_flow_df['主力净流入-净占比']
    return df


if __name__ == '__main__':
    df = get_money_flow()
    print(df)
