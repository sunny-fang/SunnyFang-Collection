# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 17:01:56 2019

@author: user
"""
import joypy
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import cm
# 匯入所需的函式、模組

#conda install -c anaconda msgpack-python

# 若沒有安裝joypy，先用系統執行anaconda prompt，然後輸入下面那行按enter
# pip install joypy

# Please use Line-14 to install "joypy" if necessary
# ==================

# ==================
#
# Import Data
mpg = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")
# 將括號中的資料讀近來，並命名為df(已於DV_00中定義pd為pandas)

# Draw Plot
plt.figure(figsize=(16,10), dpi= 80)
# 設定圖的大小等資訊
fig, axes = joypy.joyplot(mpg, column=['hwy', 'cty'], by="class", ylim='own', figsize=(14,10))
# 將資料依據變數class分類，在使用每個分類的市區里程、高速里程繪製不同顏色的密度圖

# Decoration
plt.title('Joy Plot of City and Highway Mileage by Class', fontsize=22)
# 設定圖的標題及字型大小
plt.show()
# 秀出圖形