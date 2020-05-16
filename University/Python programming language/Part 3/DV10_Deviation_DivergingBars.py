# Prepare Data
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mtcars.csv")
# 將括號中的檔案讀進來，並命名為df(已於DV00中定義pd為pandas)
x = df.loc[:, ['mpg']]
# 令x為mpg該行之資料
df['mpg_z'] = (x - x.mean())/x.std()
# 將x標準化，並命名為mpg_z
df['colors'] = ['red' if x < 0 else 'green' for x in df['mpg_z']]
# 標準化後為負值的使用紅色，標準化後為正職的使用綠色
df.sort_values('mpg_z', inplace=True)
# 按照mpg_z的值做排序
df.reset_index(inplace=True)
# 還原索引，重新變為默認的索引 

# Draw plot
plt.figure(figsize=(14,10), dpi= 80)
# 畫圖，設定圖的大小
plt.hlines(y=df.index, xmin=0, xmax=df.mpg_z, color=df.colors, alpha=0.4, linewidth=5)
# 畫水平線，並設定x軸之最大、最小值、線的寬度等
# Decorations
plt.gca().set(ylabel='$Model$', xlabel='$Mileage$')
# 設定圖的x、y座標軸名稱
plt.yticks(df.index, df.cars, fontsize=12)
# 設定y軸的資料來自於cars此行，並設定字型大小
plt.title('Diverging Bars of Car Mileage', fontdict={'size':20})
# 設定圖的標題名稱與字型大小
plt.grid(linestyle='--', alpha=20)
# 設定背景線條的形式
plt.show()
# 秀出圖形