# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 16:34:13 2019

@author: user
"""

# Prepare Data
df_raw = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")
# 將括號中的檔案讀進來，並命名為df_raw(已於DV00中定義pd為pandas)
df = df_raw[['cty', 'manufacturer']].groupby('manufacturer').apply(lambda x: x.mean())
# 將資料依據manufacturer這個變數來分組，並計算每組的平均值
df.sort_values('cty', inplace=True)
# 按照變數cty的值做排序
df.reset_index(inplace=True)
# 還原索引，重新變為默認的索引

# Draw plot
import matplotlib.patches as patches
# 匯入模組，並命名為patches

fig, ax = plt.subplots(figsize=(16,10), facecolor='white', dpi= 80)
ax.vlines(x=df.index, ymin=0, ymax=df.cty, color='firebrick', alpha=0.7, linewidth=20)
# 設定長條圖的繪製方式以及顏色、大小、線的寬度等資訊

# Annotate Text
for i, cty in enumerate(df.cty):
    ax.text(i, cty+0.5, round(cty, 1), horizontalalignment='center')
# 設定每個柱子的數值、要取到小數點第一位，以及數字所在位置為柱子的中間


# Title, Label, Ticks and Ylim
ax.set_title('Bar Chart for Highway Mileage', fontdict={'size':22})
# 設定標題名稱及字型大小
ax.set(ylabel='Miles Per Gallon', ylim=(0, 30))
# 設定y座標軸之名稱及範圍
plt.xticks(df.index, df.manufacturer.str.upper(), rotation=60, horizontalalignment='right', fontsize=12)
# 設定x座標為manufacturer中的名稱，並設定字的旋轉角度(60度)及位置(柱子位於字的右邊)

# Add patches to color the X axis labels
p1 = patches.Rectangle((.57, -0.005), width=.33, height=.13, alpha=.1, facecolor='green', transform=fig.transFigure)
# 加上綠色長方形作為背景，並設定位置、大小等資訊
p2 = patches.Rectangle((.124, -0.005), width=.446, height=.13, alpha=.1, facecolor='red', transform=fig.transFigure)
# 加上紅色長方形作為背景，並設定位置、大小等資訊
fig.add_artist(p1)
fig.add_artist(p2)
plt.show()
# 於圖上加上前面所設定的p1、p2，在秀出圖形