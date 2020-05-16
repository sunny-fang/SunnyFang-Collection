# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 16:15:57 2019

@author: user
"""

# Prepare Data
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mtcars.csv")
# 將括號中的檔案讀進來，並命名為df(已於DV00中定義pd為pandas)
x = df.loc[:, ['mpg']]
# 令x為mpg該行之資料
df['mpg_z'] = (x - x.mean())/x.std()
# 將x標準化，並命名為mpg_z
df['colors'] = 'black'
# 設定點和線的顏色
# color fiat differently
df.loc[df.cars == 'Fiat X1-9', 'colors'] = 'darkorange'
# 將Fiat X1-9此型號的點設為橘色的
df.sort_values('mpg_z', inplace=True)
# 按照mpg_z的值做排序
df.reset_index(inplace=True)
# 還原索引，重新變為默認的索引 


# Draw plot
import matplotlib.patches as patches
# 匯入模組，並命名為patches
plt.figure(figsize=(14,16), dpi= 50)
#設定圖的大小
plt.hlines(y=df.index, xmin=0, xmax=df.mpg_z, color=df.colors, alpha=0.4, linewidth=1)
# 畫水平線，並設定x軸之最大、最小值、線的寬度等
plt.scatter(df.mpg_z, df.index, color=df.colors, s=[600 if x == 'Fiat X1-9' else 300 for x in df.cars], alpha=0.6)
# 畫點，並且設定型號為Fiat X1-9的點較大
plt.yticks(df.index, df.cars)
# 設定y軸的資料來自於cars此行
plt.xticks(fontsize=12)
# 設定x軸的數字大小

# Annotate
plt.annotate('Mercedes Models', xy=(0.0, 11.0), xytext=(1.0, 11), xycoords='data', 
            fontsize=15, ha='center', va='center',
            bbox=dict(boxstyle='square', fc='firebrick'),
            arrowprops=dict(arrowstyle='-[, widthB=2.0, lengthB=1.5', lw=2.0, color='steelblue'), color='white')
# 將Mercedes Models的車特別標示出來

# Add Patches
p1 = patches.Rectangle((-2.0, -1), width=0.3, height=3, alpha=.2, facecolor='red')
# 設定一個座標位於(-2.0, -1)的框，並設定框的大小、顏色
p2 = patches.Rectangle((1.5, 27), width=.8, height=5, alpha=.2, facecolor='green')
# 設定一個座標位於(-2.0, -1)的框，並設定框的大小、顏色
plt.gca().add_patch(p1)
# 將上面設定的p1框畫出來
plt.gca().add_patch(p2)
# 將上面設定的p2框畫出來


# Decorate
plt.title('Diverging Bars of Car Mileage', fontdict={'size':20})
# 設定圖的標題名稱與字型大小
plt.grid(linestyle='--', alpha=0.5)
# 設定背景線條的形式
plt.show()
# 秀出圖形