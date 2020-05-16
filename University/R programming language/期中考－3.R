install.packages(c("corrplot", "GGally", "hexbin", "scatterplot3d", "Sleuth2"))
library(corrplot)
library(GGally)
library(hexbin)
library(scatterplot3d)
library(Sleuth2)
library(car)
library(plotrix)
library(ggplot2)
# 進階圖形
# 一、堆疊直方圖
histStack(Salaries$salary
          ,z=Salaries$rank
          ,legend.pos = "topright") # 解釋:薪水高的都是教授，沒有助理教授
histStack(diamonds$price
          ,z=diamonds$color
          ,legend.pos = "topright") # 解釋:低價時各種顏色的鑽石都有，高價時，透明顏色較少見
cq <- quantile(diamonds$carat)
cc <- cut(diamonds$carat
          ,cq,include.lowest = T)
levels(cc) <- c('L','M','H','SH') # 設定圖例的文字
histStack(diamonds$price
          ,z=cc
          ,legend.pos = "topright") # 解釋:越重的鑽石越貴
## 直方圖加上機率曲線
hist(diamonds$price
     ,col=3
     ,freq=F
     ,ylim = c(0,0.0005))
eq <- density(diamonds$price)
lines(eq,col=4,lwd=2)
# 二、盒形圖加入類別變數
palette(heat.colors(7))
boxplot(mtcars$mpg~mtcars$cyl # horizontal=T變橫向圖形，las=1讓字也變正的
        ,col=1:3
        ,main='mtcars Boxplot'
        ,horizontal=T
        ,las=1)
## 看兩個類別(利用*)
data("Salaries")
boxplot(Salaries$salary~Salaries$sex*Salaries$discipline
        ,col=1:7)
# 三、3d圓餅圖(explode = 0.1用來切割區塊間的寬度，radius調區塊大小，labelcex調字型大小)
allocation <- c(30,25,28,10,7)
sec <- c('Stock','Fore','Bonds','Gold','Cash')
pie3D(allocation,labels = sec
      ,explode = 0.05
      ,radius = 0.8
      ,labelcex = 1)
legend(locator(1)
       ,legend = sec
       ,fill=1:5
       ,cex=0.5
       ,ncol=2) # ncol設定圖例要分幾行

# 散佈圖矩陣
library(Sleuth2)
data("ex1713")
pairs(~Distinct+Attend+NonChurch+StrongPct
      ,data=ex1713
      ,pch=16
      ,col='deepskyblue'
      ,panel=panel.smooth
      ,upper.panel=NULL)
library(psych) 
library(GGally) # ggpairs可以處理類別資料
pairs.panels(ex1713)
ggpairs(Salaries)
scatterplotMatrix(~Distinct+Attend+NonChurch+StrongPct,data=ex1713)
scatterplotMatrix(~Distinct+Attend+NonChurch+StrongPct,data=ex1713
                  ,diagonal=list(method='histogram'))
# 3d圖
attach(ex1713)
scatterplot3d(Attend,NonChurch,StrongPct
              ,color=2,pch=16)




