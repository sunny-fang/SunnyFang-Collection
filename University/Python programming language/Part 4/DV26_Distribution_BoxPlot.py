# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:01:03 2019

@author: user
"""

# Import Data
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")
# 將括號中的資料讀近來，並命名為df(已於DV_00中定義pd為pandas)

# Draw Plot
plt.figure(figsize=(13,10), dpi= 80)
# 創建一個繪圖空間，並設定大小
sns.boxplot(x='class', y='hwy', data=df, notch=False)
# 繪製盒形圖，並設定x軸為資料中的class變數，y軸為資料中的hwy變數

# Add N Obs inside boxplot (optional)
def add_n_obs(df,group_col,y):
    medians_dict = {grp[0]:grp[1][y].median() for grp in df.groupby(group_col)}
    xticklabels = [x.get_text() for x in plt.gca().get_xticklabels()]
    n_obs = df.groupby(group_col)[y].size().values
    for (x, xticklabel), n_ob in zip(enumerate(xticklabels), n_obs):
        plt.text(x, medians_dict[xticklabel]*1.01, "#obs : "+str(n_ob), horizontalalignment='center', fontdict={'size':14}, color='white')
# 由於可能會扭曲一組中框的大小，因此於框中再加入觀察值個數的計算
# 定義一個新的函式叫做add_n_obs，目的為計算每個框中的觀察查值數量，並顯示於框中

add_n_obs(df,group_col='class',y='hwy')   
#  透過class變數分類，分別計算hwy變數之觀察值數量

# Decoration
plt.title('Box Plot of Highway Mileage by Vehicle Class', fontsize=22)
# 繪製圖的標題並設定字型大小
plt.ylim(10, 40)
# 繪製y軸範圍
plt.show()
# 秀出圖形