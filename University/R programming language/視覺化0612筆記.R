install.packages("tidyverse")
library(tidyverse)
data(mpg)
view(mpg)
# ggplot2:用文法方式畫圖
# ggplot(data=mpg)是產生一個繪圖框
# 散佈圖用+geom_point,aes為aesthetic
ggplot(data=mpg)+
  geom_point(mapping = aes(x=displ,y=hwy))
# 連續變數後面要加stat='identity'，特別是bar一定要加
ggplot(data=mpg)+
  geom_bar(mapping = aes(x=class,y=hwy)
           ,stat='identity')
# 傳統畫散佈圖
plot(mtcars$wt,mtcars$mpg)
# ggplot2畫法
ggplot(data=mtcars)+
  geom_point(aes(x=wt,y=mpg))
# 線形圖lineplot
data("pressure") # 溫度與壓力的關係
view(pressure)
ggplot(data=pressure)+
  geom_line(aes(x=temperature,y=pressure))
###################################################
# color=class:不同類別用不同顏色顯示
ggplot(data=mpg)+
  geom_point(mapping = aes(x=displ
                           ,y=hwy
                           ,color=class))
# size=class:不同類別用不同大小顯示
ggplot(data=mpg)+
  geom_point(mapping = aes(x=displ
                           ,y=hwy
                           ,size=class))
# alpha=class:不同類別用不同透明度顯示
ggplot(data=mpg)+
  geom_point(mapping = aes(x=displ
                           ,y=hwy
                           ,alpha=class))
# shape=class:不同類別用不同透明度形狀顯示
ggplot(data=mpg)+
  geom_point(mapping = aes(x=displ
                           ,y=hwy
                           ,shape=class)) # 但系統形狀不夠多
# 調整系統可以提供的形狀至10個
ggplot(data=mpg)+
  geom_point(mapping = aes(x=displ
                           ,y=hwy
                           ,shape=class)) +
  scale_shape_manual(values = 0:10) 
###################################################
# aes指定資料對應到圖形上的資訊，參數若放在aes外面，則為單一設定，無對應到資料
# 因此下面這個無法執行
ggplot(data=mpg)+
  geom_point(mapping = aes(x=displ
                           ,y=hwy
                           ),color=class) # 因為class在aes外無法對應
ggplot(data=mpg)+
  geom_point(mapping = aes(x=displ
                           ,y=hwy
                           ),color='red')
ggplot(data=mpg)+
  geom_point(mapping = aes(x=displ
                           ,y=hwy)
             ,size=3,color=5)
ggplot(data=mpg)+
  geom_point(mapping = aes(x=displ
                           ,y=hwy)
             ,size=3,color='darkblue')
###################################################
data("BOD")
view(BOD)
# 傳統畫法，兩變數皆為量的變數
barplot(BOD$demand,names.arg = BOD$Time)
# ggplot2畫法
ggplot(data = BOD)+
  geom_bar(aes(x=Time,y=demand),stat = 'identity')
###################################################
view(mtcars)
# 傳統
barplot(table(mtcars$cyl)) # 要先統計cyl個數才能畫
# ggplot2
ggplot(data = mtcars)+
  geom_bar(aes(x=factor(cyl))) # 把cyl變類別變數
###################################################
data("diamonds")
view(diamonds)
# 傳統
barplot(table(diamonds$color))
# ggplot2 法一
t1 <- table(diamonds$color)
t1a = unname(t1) # 取值
t1b = names(t1) # 取名稱
t2 = data.frame(name=t1b,freq=t1a)
ggplot(data = t2)+
  geom_bar(aes(x=name,y=freq.Freq)
           ,stat = 'identity')
# ggplot法二
ggplot(data = diamonds)+
  geom_bar(aes(x=color))
###################################################
# 傳統
hist(mtcars$mpg)
hist(mtcars$mpg,breaks = 10)
# ggplot2
ggplot(data = mtcars)+
  geom_histogram(aes(x=mpg),bins = 10)
###################################################
# 傳統
boxplot(diamonds$price)
boxplot(price~color,data=diamonds)
boxplot(hwy~cyl+class,data=mpg) # 不同類別組合的盒型圖
# ggplot2
ggplot(data=diamonds)+
  geom_boxplot(aes(x=color,y=price))
ggplot(data=mpg)+
  geom_boxplot(aes(x=interaction(class,cyl)
                   ,y=hwy)) # 不同類別組合的盒型圖ggplot法
###################################################
ggplot(data=mpg)+
  geom_point(aes(x=displ,y=hwy))
# 畫平滑線
ggplot(data=mpg)+
  geom_smooth(aes(x=displ,y=hwy))
# 可以把圖形疊一起
ggplot(data=mpg)+
  geom_smooth(aes(x=displ,y=hwy))+
  geom_point(aes(x=displ,y=hwy))
###################################################
# 只用部分資料畫平滑線
ggplot(data=mpg,aes(x=displ,y=hwy))+
  geom_point()+
  geom_smooth(data = filter(mpg,class=='subcompact'))
###################################################
# 兩座位的畫紅點、加大
ggplot(data = mpg,aes(x=displ,y=hwy))+
  geom_point()+
  geom_point(data = filter(mpg,class=='2seater'),color='red'
             ,size=4)+
  geom_smooth(data = filter(mpg
                            ,class=='compact'),se=F) # se=F讓灰色區間消失
###################################################
# 一個類別一個散佈圖(用一個變數來切)
ggplot(data=mpg)+
  geom_point(aes(x=displ,y=hwy))+
  facet_wrap(~class)
# 以兩個變數做切割
ggplot(data=mpg)+
  geom_point(aes(x=displ,y=hwy))+
  facet_wrap(drv~cyl)
###################################################
# 長條圖變化
ggplot(data=mpg)+
  geom_bar(aes(x=class,y=hwy,fill=class) # 長條圖要填顏色要加fill=
           ,stat = 'identity')+
  scale_fill_brewer() # 加上預設調色盤
ggplot(data=mpg)+
  geom_bar(aes(x=class,y=hwy,fill=class)
           ,stat = 'identity')+
  scale_fill_brewer(palette='Set3') # 自己設定調色盤(ppt裡面有調色盤整理)
# 散佈圖變化
ggplot(data=mpg)+
  geom_point(aes(x=displ,y=hwy,color=class))+
  scale_colour_brewer(palette = 'Set1')
# 練習
ggplot(data=diamonds)+
  geom_bar(aes(x=color,y=price,fill=color)
           ,stat = 'identity')+
  scale_fill_brewer(palette='Spectral')
###################################################
install.packages("gcookbook")
library(gcookbook)
cabbage_exp
ggplot(cabbage_exp
       ,aes(x=Date,y=Weight,fill=Cultivar))+
  geom_bar(stat = 'identity') # 若是類別變數，會把顏色疊一起
# 把顏色分開 
ggplot(cabbage_exp
       ,aes(x=Date,y=Weight,fill=Cultivar))+
  geom_bar(stat = 'identity',position = 'dodge')
###################################################
# width設定寬度
ggplot(pg_mean,aes(x=group,y=weight))+
  geom_bar(stat = 'identity',width = 0.5)
###################################################
# 長條圖加入數字
ggplot(cabbage_exp
       ,aes(x=interaction(Date,Cultivar)
       ,y=Weight))+
  geom_bar(stat = 'identity')+
  geom_text(aes(label=Weight),vjust=1.5 # vjust調整數字的位置
            ,color='white')





  
  
























