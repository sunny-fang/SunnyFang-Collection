# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:10:29 2019

@author: user
"""

import matplotlib as mpl
import calmap

# 安裝
# pip install calmap
#

# Import Data
df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/yahoo.csv", parse_dates=['date'])
df.set_index('date', inplace=True)

# Plot
plt.figure(figsize=(16,10), dpi= 80)
calmap.calendarplot(df['2014']['VIX.Close'], fig_kws={'figsize': (16,10)}, yearlabel_kws={'color':'black', 'fontsize':14}, subplot_kws={'title':'Yahoo Stock Prices'})
# calendarplot() 的輸入參數:依序為資料來源(df中的2014年，變數為VIX.Close)、圖的大小、年份座標的顏色和大小、圖的標題
plt.show()