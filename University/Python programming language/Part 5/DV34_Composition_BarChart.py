# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:41:01 2019

@author: user
"""

import random

# Import Data
df_raw = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")
# 將括號中的資料讀近來，並命名為df(已於DV_00中定義pd為pandas)

# Prepare Data
df = df_raw.groupby('manufacturer').size().reset_index(name='counts')
# 將資料依據manufacturer變數分類，並計算每個分類的資料個數
n = df['manufacturer'].unique().__len__()+1
# 計算變數manufacturer中不重複的資料點共有幾個，再加一並命名為n
all_colors = list(plt.cm.colors.cnames.keys())
# 選取顏色表並命名為all_colors
random.seed(100)
# 產生一個編號為100的隨機數列
c = random.choices(all_colors, k=n)
# 從all_colors中隨機選出n個顏色，並命名為c

# Plot Bars
plt.figure(figsize=(16,10), dpi= 80)
# 創建一個繪圖空間，並設定大小
plt.bar(df['manufacturer'], df['counts'], color=c, width=.5)
for i, val in enumerate(df['counts'].values):
    plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':12})
# 繪製長條圖

# Decoration
plt.gca().set_xticklabels(df['manufacturer'], rotation=60, horizontalalignment= 'right')
# 繪製圖的下標
plt.title("Number of Vehicles by Manaufacturers", fontsize=22)
# 繪製圖的標題，並設定字型大小
plt.ylabel('# Vehicles')
# 繪製y座標軸名稱
plt.ylim(0, 45)
# 設定y軸座標範圍
plt.show()
# 秀出圖形