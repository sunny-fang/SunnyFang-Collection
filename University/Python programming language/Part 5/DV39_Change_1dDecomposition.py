# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:02:46 2019

@author: user
"""

from statsmodels.tsa.seasonal import seasonal_decompose
from dateutil.parser import parse

# statsmodels.tsa.stattools.ccf 用法:計算兩變數間的互相關函數
# statsmodels.tsa.stattools 其他統計常用的函數:
# 1. ACF : 時間序列中的自相關
# 2. PACF: 時間序列中的偏自相關

# Import Data
df = pd.read_csv('https://github.com/selva86/datasets/raw/master/AirPassengers.csv')
dates = pd.DatetimeIndex([parse(d).strftime('%Y-%m-01') for d in df['date']])
# 指定將输入的字串轉換為可變的時間數據
# 因為Pandas默認的數據讀取格式是‘YYYY-MM-DD HH:MM:SS’。如需要獲取的數據没有默認的格式，就要人工定義。
# 將資料集df中的變數date解析後，再格式化為"1949-01-01"的格式，並命名為dates
df.set_index(dates, inplace=True)

# Decompose 
result = seasonal_decompose(df['value'], model='multiplicative')
# 將value變數使用移動平均數法進行季節性分解

# Plot
plt.rcParams.update({'figure.figsize': (10,10)})
# 設置圖的大小等資訊
result.plot().suptitle('Time Series Decomposition of Air Passengers')
plt.show()
