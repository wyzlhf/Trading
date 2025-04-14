import numpy as np
import pandas as pd
from pandas import DataFrame

from utils.get_data import get_google_daily_data_from_akshare

goog_data: DataFrame = get_google_daily_data_from_akshare()
goog_data_signal: DataFrame = pd.DataFrame(index=goog_data.index)
goog_data_signal['price'] = goog_data['Close']
goog_data_signal['daily_difference'] = goog_data_signal['price'].diff()
goog_data_signal['signal']=np.where(goog_data_signal['daily_difference']>0,1,0)
print(goog_data_signal.head())
