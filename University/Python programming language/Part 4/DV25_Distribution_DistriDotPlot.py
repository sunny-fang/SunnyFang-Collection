# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 08:59:13 2019

@author: user
"""

import matplotlib.patches as mpatches
# 匯入所需的函式及模組

# Prepare Data
df_raw = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")
# 將括號中的資料讀近來，並命名為df(已於DV_00中定義pd為pandas)
cyl_colors = {4:'tab:red', 5:'tab:green', 6:'tab:blue', 8:'tab:orange'}
df_raw['cyl_color'] = df_raw.cyl.map(cyl_colors)
# 創建一系列的顏色以使用

# Mean and Median city mileage by make
df = df_raw[['cty', 'manufacturer']].groupby('manufacturer').apply(lambda x: x.mean())
# 將資料按照變數manufacturer分類，並計算每組的平均數
df.sort_values('cty', ascending=False, inplace=True)
# 將資料按照變數cty的值作排序
df.reset_index(inplace=True)
# 還原索引，重新變回默認的索引
df_median = df_raw[['cty', 'manufacturer']].groupby('manufacturer').apply(lambda x: x.median())
# 將資料按照變數manufacturer分類，並計算每組的中位數，並令為df_median

# Draw horizontal lines
fig, ax = plt.subplots(figsize=(16,10), dpi= 80)
# 設定子圖的大小等資訊
ax.hlines(y=df.index, xmin=0, xmax=40, color='gray', alpha=0.5, linewidth=.5, linestyles='dashdot')
# 繪製水平線，並設定繪製線條的位置在y軸、顏色為灰色、線條寬度為0.5、線條樣式為虛線

# Draw the Dots
for i, make in enumerate(df.manufacturer):
    df_make = df_raw.loc[df_raw.manufacturer==make, :]
    ax.scatter(y=np.repeat(i, df_make.shape[0]), x='cty', data=df_make, s=75, edgecolors='gray', c='w', alpha=0.5)
    ax.scatter(y=i, x='cty', data=df_median.loc[df_median.index==make, :], s=75, c='firebrick')
# 依照變數manufacturer分類，於圖上畫點，並按照資料的集中度，繪製深淺不同的灰色圓圈，再於中位數的位置繪製紅色圓圈

# Annotate    
ax.text(33, 13, "$red \; dots \; are \; the \: median$", fontdict={'size':12}, color='firebrick')
# 於圖中右上角新增註解:red dots are the median，並設定字的顏色(磚紅色)及大小(12)

# Decorations
red_patch = plt.plot([],[], marker="o", ms=10, ls="", mec=None, color='firebrick', label="Median")
# 設定圖標，為一個紅色圓圈，標籤為Median，顏色為磚紅色
plt.legend(handles=red_patch)
# 繪製圖標
ax.set_title('Distribution of City Mileage by Make', fontdict={'size':22})
# 設定圖的標題及字型大小
ax.set_xlabel('Miles Per Gallon (City)', alpha=0.7)
# 設定x座標名稱及字的顏色深淺
ax.set_yticks(df.index)
ax.set_yticklabels(df.manufacturer.str.title(), fontdict={'horizontalalignment': 'right'}, alpha=0.7)
# 設定y座標為依據manufacturer分類，並設定位置及字的深淺(0.7)
ax.set_xlim(1, 40)
# 設定x座標的範圍
plt.xticks(alpha=0.7)
# 設定x座標的字的深淺(0.7)
plt.gca().spines["top"].set_visible(False)   
# 去除掉圖形的上邊框
plt.gca().spines["bottom"].set_visible(False)    
# 去除掉圖形的下邊框
plt.gca().spines["right"].set_visible(False)    
# 去除掉圖形的右邊框
plt.gca().spines["left"].set_visible(False)   
# 去除掉圖形的左邊框
plt.grid(axis='both', alpha=.4, linewidth=.1)
# 繪製網格，x、y軸都要畫，並設定顏色深淺(0.4)、寬度(0.1)
plt.show()
# 秀出圖形