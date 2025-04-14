import pandas as pd
import akshare as ak


def get_google_daily_data_from_akshare(symbol: str = 'GOOG', start_date: str = '2014-01-01',
                                       end_date='2018-01-01') -> pd.DataFrame:
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
    google_data: pd.DataFrame = ak.stock_us_daily(symbol=symbol, adjust="")
    google_data = google_data.rename(columns=lambda x: x.title())
    google_data.set_index('Date', inplace=True)
    return google_data


if __name__ == '__main__':
    google_data = get_google_daily_data_from_akshare()
    print(google_data.head())
