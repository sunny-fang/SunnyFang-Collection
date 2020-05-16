# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 16:59:39 2019

@author: user
"""

# Import Data
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")
# 將括號中的資料讀近來，並命名為df(已於DV_00中定義pd為pandas)

# Draw Plot
plt.figure(figsize=(16,10), dpi= 80)
sns.kdeplot(df.loc[df['cyl'] == 4, "cty"], shade=True, color="g", label="Cyl=4", alpha=.7)
# 挑選出變數cyl的值等於4的資料，在利用篩選後資料的cty的數值，繪製核密度估計圖，並設定顏色(綠色)等資訊
sns.kdeplot(df.loc[df['cyl'] == 5, "cty"], shade=True, color="deeppink", label="Cyl=5", alpha=.7)
# 挑選出變數cyl的值等於5的資料，在利用篩選後資料的cty的數值，繪製核密度估計圖，並設定顏色(粉紅色)等資訊
sns.kdeplot(df.loc[df['cyl'] == 6, "cty"], shade=True, color="dodgerblue", label="Cyl=6", alpha=.7)
# 挑選出變數cyl的值等於6的資料，在利用篩選後資料的cty的數值，繪製核密度估計圖，並設定顏色(藍色)等資訊
sns.kdeplot(df.loc[df['cyl'] == 8, "cty"], shade=True, color="orange", label="Cyl=8", alpha=.7)
# 挑選出變數cyl的值等於8的資料，在利用篩選後資料的cty的數值，繪製核密度估計圖，並設定顏色(橘色)等資訊

# Decoration
plt.title('Density Plot of City Mileage by n_Cylinders', fontsize=22)
# 設定圖的標題及字型大小
plt.legend()
# 繪製圖例
plt.show()
# 秀出圖形