# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 16:25:20 2019

@author: user
"""

import numpy as np
import pandas as pd

# Prepare Data
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/economics.csv", parse_dates=['date']).head(100)
# 將括號中的檔案讀進來，並命名為df(已於DV00中定義pd為pandas)
x = np.arange(df.shape[0])
# 將x軸的座標值按照固定寬度來建立
y_returns = (df.psavert.diff().fillna(0)/df.psavert.shift(1)).fillna(0) * 100
# 設定y軸的值的算法

# Plot
plt.figure(figsize=(16,10), dpi= 80)
# 設定圖的大小
plt.fill_between(x[1:], y_returns[1:], 0, where=y_returns[1:] >= 0, facecolor='green', interpolate=True, alpha=0.7)
# 將y之值畫出來，大於0的話就塗綠色
plt.fill_between(x[1:], y_returns[1:], 0, where=y_returns[1:] <= 0, facecolor='red', interpolate=True, alpha=0.7)
# 將y之值畫出來，小於0的話就塗紅色

# Annotate
plt.annotate('Peak \n1975', xy=(94.0, 21.0), xytext=(88.0, 28),
             bbox=dict(boxstyle='square', fc='firebrick'),
             arrowprops=dict(facecolor='steelblue', shrink=0.05), fontsize=15, color='white')
# 於最高點作註解，並設定註解的位置、大小、顏色等


# Decorations
xtickvals = [str(m)[:3].upper()+"-"+str(y) for y,m in zip(df.date.dt.year, df.date.dt.month_name())]
plt.gca().set_xticks(x[::6])
plt.gca().set_xticklabels(xtickvals[::6], rotation=90, fontdict={'horizontalalignment': 'center', 'verticalalignment': 'center_baseline'})
# 設定x軸的座標為每六個月為一單位
plt.ylim(-35,35)
# 設定y座標軸的範圍
plt.xlim(1,100)
# 設定x座標軸的範圍
plt.title("Month Economics Return %", fontsize=22)
# 設定圖的名稱及字的大小
plt.ylabel('Monthly returns %')
# 設定y座標軸名稱
plt.grid(alpha=0.5)
# 設定背景框線和顏色深度
plt.show()
# 秀出圖形