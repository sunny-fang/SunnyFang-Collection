# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 16:57:39 2019

@author: user
"""

# Import Data
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")
# 將括號中的資料讀近來，並命名為df(已於DV_00中定義pd為pandas)
# Prepare data
x_var = 'displ'
# 將資料中的displ設為x軸的變數
groupby_var = 'class'
# 將資料中的class變數命名為groupby_var
df_agg = df.loc[:, [x_var, groupby_var]].groupby(groupby_var)
# 將資料中的x_var透過groupby_var分類，並命名為df_agg
vals = [df[x_var].values.tolist() for i, df in df_agg]
# 將x_var轉換為列表，並命名為vals
# Draw
plt.figure(figsize=(16,9), dpi= 80)
#　設定圖的大小
colors = [plt.cm.Spectral(i/float(len(vals)-1)) for i in range(len(vals))]
#　設定每一個柱子會因為分類的不同而有不同顏色
n, bins, patches = plt.hist(vals, 30, stacked=True, density=False, color=colors[:len(vals)])
# 繪製長條圖，並設定寬度、顏色等資訊

# Decoration
plt.legend({group:col for group, col in zip(np.unique(df[groupby_var]).tolist(), colors[:len(vals)])})
# 一個柱子中再依據分類顯示不同的顏色
plt.title(f"Stacked Histogram of ${x_var}$ colored by ${groupby_var}$", fontsize=22)
# 設定圖的標題和文字大小
plt.xlabel(x_var)
# 設定ｘ座標為x_var
plt.ylabel("Frequency")
# 設定ｙ座標標題為Frequency
plt.ylim(0, 25)
# 設定ｙ座標軸的範圍為０－２５
plt.xticks(ticks=bins[::3], labels=[round(b,1) for b in bins[::3]])
# 設定ｘ座標的刻度線位置
plt.show()
# 秀出圖形