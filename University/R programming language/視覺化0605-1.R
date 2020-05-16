install.packages("tidyverse")
library(tidyverse)
mini_iris <- iris[c(1,51,101),]
newd <- mini_iris %>%
  gather(key=FlowerFE,value=measurement
         ,-Species) # -代表要留下的，其他都合併
################################################
# 以實價登陸資料庫為例
RE <- read.csv("file:///E:/A_LVR_LAND_A.CSV",header = T)
RE1 <- RE %>%
  separate(交易筆棟數
           ,sep=c(3,6) # 給兩個值切三份
           ,into=c('土地','建物','車位')) %>%
  separate(土地,sep=2,into=c('t土地','土地')) %>%
  separate(建物,sep=2,into=c('t建物','建物')) %>%
  separate(車位,sep=2,into=c('t車位','車位'))
# %>%目的為連在一起執行程式，就不用一值暫存資料
# 分割建築完成年月 法一
RE2 <- RE %>%
  separate(建築完成年月
           ,sep=c(-4)
           ,into=c('建築完成年','建築完成月')) %>%
  separate(建築完成月
           ,sep=c(-2)
           ,into=c('建築完成月','建築完成日'))
# 分割建築完成年月 法二
RE3 <- RE %>%
  separate(建築完成年月
           ,sep=c(-4,-2)
           ,into=c('建築完成年','建築完成月','建築完成日'))
###############################################
# 合併兩個變數
table5
t5 <- table5 %>%
  unite(newDate,century,year,sep='') # sep代表合併數值後中間要有啥符號
###############################################
install.packages("nycflights13")
library(nycflights13)
data(flights)
print(flights,width=Inf)
# 檢查是否有月份輸錯
barplot(table(flights$month),col=c(2,4))
# filter:選取觀察值
# 取出每年第一個月的第一天資料 法一
fm1 <- filter(flights,month==1,day==1)
table(fm1$month)
# 取出每年第一個月的第一天資料 法二
fm1a <- flights[flights$month==1
                &flights$day==1,]
# 上面是且，也可以或(,就是且)
fm2 <- filter(flights
              ,month==11 | month==12
              ,day==1)
table(fm2$day)
# 取出延誤低於半小時的 法一
fm3 <- filter(flights
              ,dep_delay<=30
              ,arr_delay<=30)
# 取出延誤低於半小時的 法二
fm3a <- filter(flights
              ,!dep_delay>30
              ,!arr_delay>30)
# RE2資料中，建築完成年>=100的資料佔總資料的比例
rate <- nrow(filter(RE2,建築完成年>=100))/nrow(RE2)
###############################################
view(mtcars)
arrange(mtcars,desc(mpg)) # 油耗由大到小排列，預設為遞減
arrange(mtcars,cyl,desc(disp)) # 先排列cyl，在排列disp
# select選取變數
f1 <- select(flights,year,month,day) # 取出flights中的這三個變數
f1b <- select(flights,year:day) # 取出year到day的變數
f1d <- select(flights,-(year:day)) # 加-號刪除變數
f1e <- select(flights,ends_with('delay')) # 以delay變數做結尾
f1f <- select(flights,-ends_with('delay')) 
f1g <- select(flights,starts_with('dep')) # 只取出dep開頭的變數
###############################################
# 刪除RE1中沒意義的變數
REa <- select(RE1,-starts_with('t'))
# 刪除車位為0的資料
REz <- filter(REa,車位!='0')
###############################################
print(flights,width=Inf)
colnames(flights)
# mutate轉換
m1 <- mutate(flights,gain=arr_delay-dep_delay)
m1a <- transmute(flights,arr_delay,gain=arr_delay-dep_delay) # 只留下新變數，transmute中，沒有等號的變數代表要留下
m1b <- mutate(flights,hours=air_time/60
              ,speed=distance/hours) # 剛產生的變數hours仍然可以用
# 將dep_time利用mutate轉成dep_hour、dep_min
m1c <- mutate(flights,dep_hour=dep_time%/%100
              ,dep_min=dep_time%%100) # %/%為商，%%為餘數
# 將價格的基準改為每坪
colnames(RE)
RE01 <- mutate(RE,單價每坪=單價每平方公尺*3.3058)
###############################################
# summarise看各種描述性統計量，且可分組
summarise(iris,n=n())
byg <- group_by(iris,Species) # 把iris按照種類分組
summarise(byg,n=n())
summarise(byg,n=n(),mean=mean(Sepal.Length)
          ,max=max(Sepal.Width))
###############################################
Sris <- group_by(iris,Species) %>%
  mutate(Sepal.ratio=Sepal.Length/Sepal.Width
         ,Petal.ratio=Petal.Length/Petal.Width) %>%
  summarise(Sepalm=mean(Sepal.ratio)
            ,Petalm=mean(Petal.ratio))
###############################################
# vs為引擎形式，am為自排手排
group_by(mtcars,vs,am) %>%
  summarise(mpgm=mean(mpg),mhp=mean(hp))




















