# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:34:18 2019

@author: user
"""

# Import
df_raw = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")
# 將括號中的資料讀近來，並命名為df(已於DV_00中定義pd為pandas)

# Prepare Data
df = df_raw.groupby('class').size().reset_index(name='counts')
# 將資料依據class變數分類，並計算每個分類的資料個數

# Draw Plot
fig, ax = plt.subplots(figsize=(12, 7), subplot_kw=dict(aspect="equal"), dpi= 80)
# 繪製一個繪圖空間，並設定大小，子圖的x、y軸長度要相等，並設定每英吋為多少像素(80)

data = df['counts']
# 取出所計算的各分類個數，並命名為data
categories = df['class']
# 取出class變數，並命名為categories
explode = [0,0,0,0,0,0.1,0]
# 設定圓餅圖中每個分類之間的距離，第六個類別與其他類別之間距離較開，其他類別間則相連

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}% ({:d} )".format(pct, absolute)
# 設定一個函數，除了計算每個分類中的資料筆數，也計算出所佔的百分比

wedges, texts, autotexts = ax.pie(data, 
                                  autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"), 
                                  colors=plt.cm.Dark2.colors,
                                 startangle=140,
                                 explode=explode)
# 繪製圓餅圖，並設定資料來自於data、並根據所定義的函數(func)計算結果、圓餅中數字的顏色(白色)、色彩表來源、將圓餅圖自第一分類逆時針旋轉140度、每個類別間的距離依照上面所定義的explode

# Decoration
ax.legend(wedges, categories, title="Vehicle Class", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
# 繪製圖例，名稱為Vehicle Class，並設定圖例之位置
plt.setp(autotexts, size=10, weight=700)
# 設定圓餅圖中數字的大小、自體粗細程度(700)
ax.set_title("Class of Vehicles: Pie Chart")
# 設定圖的標題為Class of Vehicles: Pie Chart
plt.show()
# 秀出圖形