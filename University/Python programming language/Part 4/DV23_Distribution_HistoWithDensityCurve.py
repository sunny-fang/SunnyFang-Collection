# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 17:00:23 2019

@author: user
"""

# Import Data
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")
# 將括號中的資料讀近來，並命名為df(已於DV_00中定義pd為pandas)

# Draw Plot
plt.figure(figsize=(13,10), dpi= 80)
# 設定圖形的大小
sns.distplot(df.loc[df['class'] == 'compact', "cty"], color="dodgerblue", label="Compact", hist_kws={'alpha':.7}, kde_kws={'linewidth':3})
# 挑選出變數class為compact的資料，在利用篩選後資料的cty之值，繪製密度圖結合直方圖，並設定顏色(藍色)、柱子大小寬度、圖例等資訊
sns.distplot(df.loc[df['class'] == 'suv', "cty"], color="orange", label="SUV", hist_kws={'alpha':.7}, kde_kws={'linewidth':3})
# 挑選出變數class為suv的資料，在利用篩選後資料的cty之值，繪製密度圖結合直方圖，並設定顏色(橘色)、柱子大小寬度、圖例等資訊
sns.distplot(df.loc[df['class'] == 'minivan', "cty"], color="g", label="minivan", hist_kws={'alpha':.7}, kde_kws={'linewidth':3})
# 挑選出變數class為minivan的資料，在利用篩選後資料的cty之值，繪製密度圖結合直方圖，並設定顏色(綠色)、柱子大小寬度、圖例等資訊
plt.ylim(0, 0.35)
# 設定Y軸的範圍

# Decoration
plt.title('Density Plot of City Mileage by Vehicle Type', fontsize=22)
# 設定標題及字型大小
plt.legend()
# 繪製圖例
plt.show()
# 秀出圖形