# 圖的註解(點、線、文字)
data("iris")
plot(iris$Petal.Width,iris$Sepal.Width
     ,col=iris$Species
     ,pch=as.numeric(iris$Species))
# 一、點(cex為放大幾倍)
points(0.5,2.5,col=2,cex=2,pch=16)
## 取出油耗小於15的樣本，並於圖上點出
plot(mtcars$mpg,mtcars$hp
     ,pch=16
     ,col=4)
d1 <- mtcars[mtcars$mpg<15,] # 向量取法
points(d1$mpg,d1$hp
       ,col=2
       ,pch=16
       ,cex=2)
# 二、線(a:intercept、b:slope、h:horizontal line、v:vertical line)
?abline
abline(a=2.5,b=1,lwd=3,col=3)
abline(h=3)
abline(v=1.5)
# 三、網格
plot(mpg~hp,data = mtcars)
grid(col="darkblue"
     ,lwd=3
     ,lty=5)
# 三、文字
plot(iris$Sepal.Length,iris$Petal.Length
     ,col=iris$Species
     ,pch=as.numeric(iris$Species))
text(iris$Sepal.Length,iris$Petal.Length # text中的col需要as.numeric
     ,labels = iris$Species
     ,col=as.numeric(iris$Species)
     ,cex=0.6
     ,pos=3)
## 以奧林匹亞女子全能運動會資料為例
library(HSAUR3)
data("heptathlon")
View(heptathlon)
plot(hurdles~highjump,data = heptathlon)
nm <- row.names(heptathlon) # 取出第一行的資料
text(heptathlon$highjump,heptathlon$hurdles # 標註人名及國家名
     ,labels = nm
     ,cex=0.7
     ,pos=4)
text(heptathlon$highjump,heptathlon$hurdles # 標註highjump之數值
     ,labels = heptathlon$highjump
     ,pos=4
     ,cex=0.7
     ,col=5)
## 以UScrime為例
setwd("C:\\Users\\Administrator\\Desktop\\視覺化R\\資料檔")
usc <- read.table("USAcrime.txt",header = T)
plot(usc[,1],usc[,2]
     ,pch=16)
text(usc[,1],usc[,2] # 取出第一、二行的資料繪圖，[]中為列、行
     ,labels = row.names(usc)
     ,col=4
     ,cex=0.8
     ,pos=3)

# 迴歸(結合點、線)
m1 <- lm(mpg~hp,data = mtcars) # ~左右邊分別是y、x軸
abline(reg=m1,lwd=3,col=2) # 畫迴歸線(法一)
## 看迴歸係數
coef(m1)
abline(a=coef(m1)[1],b=coef(m1)[2] # 畫迴歸線(法二)
       ,lwd=2,col=7)
## 在迴歸線上畫出hp=200的點(利用data.frame&predict)
newd <- data.frame(hp=200)
p1 <- predict(m1,newdata = newd)
points(200,16.4532,col=4,cex=2,pch=16)












