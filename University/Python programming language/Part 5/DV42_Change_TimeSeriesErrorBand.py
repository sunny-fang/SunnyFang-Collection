# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:06:47 2019

@author: user
"""

from scipy.stats import sem

# Import Data
df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/user_orders_hourofday.csv")
df_mean = df.groupby('order_hour_of_day').quantity.mean()
# 將資料依據order_hour_of_day變數分類，再分別計算每個類別的平均數，並命名為df_mean
df_se = df.groupby('order_hour_of_day').quantity.apply(sem).mul(1.96)
# 將資料依據order_hour_of_day變數分類，再分別計算每個類別的標準差，將標準差乘以1.96倍後，命名為df_se

# Plot
plt.figure(figsize=(16,10), dpi= 80)
plt.ylabel("# Orders", fontsize=16)  
x = df_mean.index
plt.plot(x, df_mean, color="white", lw=2) 
plt.fill_between(x, df_mean - df_se, df_mean + df_se, color="#3F5D7D")  
# 繪製信賴區間，範圍為每一分類的df_mean加減df_se之區間，再設定顏色
# plt.fill_between用法:
# plt.fill_between(曲線之x座標, 曲線之上界, 曲線之下界, color="顏色編碼")

# Decorations
# Lighten borders
plt.gca().spines["top"].set_alpha(0)
plt.gca().spines["bottom"].set_alpha(1)
plt.gca().spines["right"].set_alpha(0)
plt.gca().spines["left"].set_alpha(1)
plt.xticks(x[::2], [str(d) for d in x[::2]] , fontsize=12)
plt.title("User Orders by Hour of Day (95% confidence)", fontsize=22)
plt.xlabel("Hour of Day")

s, e = plt.gca().get_xlim()
plt.xlim(s, e)

# Draw Horizontal Tick lines  
for y in range(8, 20, 2):    
    plt.hlines(y, xmin=s, xmax=e, colors='black', alpha=0.5, linestyles="--", lw=0.5)

plt.show()