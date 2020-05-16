# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 13:11:02 2019

@author: user
"""

import scipy.cluster.hierarchy as shc

# Import Data
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/USArrests.csv')

# Plot
plt.figure(figsize=(16, 10), dpi= 80)  
plt.title("USArrests Dendograms", fontsize=22)  
dend = shc.dendrogram(shc.linkage(df[['Murder', 'Assault', 'UrbanPop', 'Rape']], method='ward'), labels=df.State.values, color_threshold=100)
# 繪製樹狀結構圖，參數有:依照什麼來分群('Murder', 'Assault', 'UrbanPop', 'Rape')、計算距離之方法(ward)、x座標標籤為df中的State變數、當群之間的距離大於等於100時，連接節點的線都塗成藍色
# linkage() 的功能:依照該陣列來進行階層式分群
plt.xticks(fontsize=12)
plt.show()