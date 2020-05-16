# 讀資料
# 1.複製路徑，斜線都加一條 2.read.table，有變數名稱加header = T
setwd("C:\\Users\\Administrator\\Desktop\\視覺化R\\資料檔")
usc <- read.table("USAcrime.txt",header = T)

# 載package要記得library
library(car)
library(ggplot2)
data(mtcars)
data(Salaries)

# 敘述統計量
mean(mtcars$mpg)
median(mtcars$mpg)
quantile(mtcars$mpg,c(0.1,0.5)) # 分位數
range(mtcars$mpg) # 最大最小值
var(mtcars$mpg)
sd(mtcars$mpg)

# 次數分配表
t1 <- table(Salaries$rank)
t1a <- addmargins(t1)
t1p <- prop.table(t1a) # 改成比例形式
round(t1p,4) # 算到小數點第4位
SRG <- table(Salaries$rank,Salaries$discipline)　# 雙變數次數分配表
s1 <- prop.table(SRG,1) # 1為列總合=1，2為行總合為1


# 各種圖形描繪(high level plot)
# 一、長條圖(適合類別資料)
plot(Salaries$rank)
barplot(mtcars$gear) # 資料為數值型態，硬畫長條圖
gear_f <- as.factor(mtcars$gear) #　將變數轉換為類別型態
plot(gear_f
     ,main="Gear's Barplot"
     ,col=c(1,2,3))
barplot(rep(1,5),col=1:8) # rep為要幾行
# 二、圓餅圖
t2 <- table(mtcars$gear)
pie(t2,main="Gear's Pieplot"
    ,col=2:5)
# 三、直方圖(labels=T為顯示每條之次數)
hist(mtcars$mpg
     ,main="mpg Histogram"
     ,labels=T
     ,ylim=c(0,20)
     ,col=1:5)
# 四、盒形圖
boxplot(mtcars$mpg
        ,main="mpg Boxplot"
        ,col=3)
# 五、散佈圖(as.numeric為轉成數值型態，alpha.f為透明度)
plot(mtcars$mpg,mtcars$hp
     ,pch=16
     ,col=adjustcolor(as.numeric(mtcars$gear),alpha.f = 0.5))
plot(Salaries$salary,Salaries$yrs.service
     ,col=Salaries$rank
     ,pch=as.numeric(Salaries$rank)) # pch要as.numeric
# 六、折線圖:plot中加type=(l、o、b)
# 使圖例的樣式和線條一致，利用lty
data("airquality")
plot(airquality$Wind
     ,type="l"
     ,lty=1
     ,ylim=c(0,100))
lines(airquality$Temp # 加折線圖(為low level plot)
      ,type="l"
      ,lty=2
      ,col=2)
legend(locator(1)
       ,legend = c("Wind","Temp")
       ,lty=1:2
       ,col=1:2)

# 畫面分割
r1 <- layout(rbind(c(1,2,3),c(1,4,3)))

# 顏色的選擇
palette()
palette(heat.colors(n=20))
palette("default")

# low level plot(pch為點的樣式)
plot(Salaries$salary,Salaries$yrs.service
     ,col=Salaries$rank
     ,pch=as.numeric(Salaries$rank))
legend("topright"
       ,legend=levels(Salaries$rank) # levels需為類別型態
       ,col=1:3
       ,pch=1:3)

# 切割資料(cut)
q <- quantile(mtcars$wt)
wtc <- cut(mtcars$wt,q
           ,include.lowest = T) # 左開右閉區間
table(wtc) # 看有無分割完整
levels(wtc) <- c("L","M","H","SH")
plot(mtcars$mpg,mtcars$hp
     ,col=wtc
     ,pch=as.numeric(wtc)
     ,main="mtcars"
     ,xlab="mpg"
     ,ylab="hp"
     ,ylim=c(40,400))
legend(locator(1)
       ,legend = levels(wtc)
       ,col=1:4
       ,pch=1:4)

