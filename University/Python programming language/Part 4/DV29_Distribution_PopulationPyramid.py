# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:05:01 2019

@author: user
"""

# Read data
df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/email_campaign_funnel.csv")
# 將括號中的資料讀近來，並命名為df(已於DV_00中定義pd為pandas)

# Draw Plot
plt.figure(figsize=(13,10), dpi= 80)
# 創建一個繪圖空間，並設定大小
group_col = 'Gender'
# 將資料依據Gender變數分為兩個欄位，並命名為group_col
order_of_bars = df.Stage.unique()[::-1]
# 將變數Stage的順序倒過來
colors = [plt.cm.Spectral(i/float(len(df[group_col].unique())-1)) for i in range(len(df[group_col].unique()))]
# 建立一個新的色彩表，並依據group_col中欄位的個數取出顏色
for c, group in zip(colors, df[group_col].unique()):
    sns.barplot(x='Users', y='Stage', data=df.loc[df[group_col]==group, :], order=order_of_bars, color=c, label=group)
# 繪製barplot，並設定:x軸為資料中的Users變數、y軸為資料中的Stage變數、資料來自於group_col、顏色來自於c、圖例來自於分組的類別

# Decorations    
plt.xlabel("$Users$")
# 繪製x座標軸名稱
plt.ylabel("Stage of Purchase")
# 繪製y座標軸名稱
plt.yticks(fontsize=12)
# 設定y座標軸名稱字型大小
plt.title("Population Pyramid of the Marketing Funnel", fontsize=22)
# 繪製圖的標題並設定字型大小
plt.legend()
# 繪製圖例
plt.show()
# 秀出圖形