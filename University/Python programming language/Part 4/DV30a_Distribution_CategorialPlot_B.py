# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:17:11 2019

@author: user
"""

# Load Dataset
titanic = sns.load_dataset("titanic")
# 匯入seaborn中的資料集titanic，並命名為titanic

# Plot
sns.catplot(x="age", y="embark_town",
            hue="sex", col="class",
            data=titanic[titanic.embark_town.notnull()],
            orient="h", height=5, aspect=1, palette="tab10",
            kind="violin", dodge=True, cut=0, bw=.2)
# 繪製類別圖，並設定:x軸為age變數、y軸為embark_town變數、sex為分類變數、依據class分為數個欄位、資料來源為titanic、圖形為橫向的、每個面的高度為5、高度寬度的比為1、顏色來自於tab10、繪圖方式為小提琴圖