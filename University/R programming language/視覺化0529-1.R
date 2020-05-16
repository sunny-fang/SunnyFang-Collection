# tidyverse vs data.frame
# 主要差異有兩點，1.印出來的方式不一樣(tidyverse不會把頁面炸掉) 2.取部分資料時，用[['']]或$取都可以
library(tidyverse)
library(nycflights13)
data("flights")
head(flights)
f1 <- as.data.frame(flights) # 轉成data.frame型態
f1
flights
print(flights,width = Inf,n=20) # 印出所有變數，n為要看幾個樣本
# 取部分資料(以下兩種結果一樣)
f1$year
f1[,'year']
#####################################################################
table4a # 此表為一個tible，但1999、2000是年分(值)，不是變數
# 改為變數
t4a <- gather(table4a,`1999`,`2000`,key='year'
       ,value='cases') # key為把該變數名稱屬於哪種變數，value為資料代表什麼
t4a
#####################################################################
# 把上面的步驟串起來，run一次就好
t4b <- table4a %>%
  gather(`1999`,`2000`
         ,key='year',value='cases') %>%
  print(width=Inf,n=2)
#####################################################################
# 第一種髒的方式:變數其實是值(利用gather)
stocks <- tibble(
  time=as.Date('2008-01-01')+0:9,
  X=rnorm(10,0,1),
  Y=rnorm(10,0,2),
  Z=rnorm(10,0,4)
) # 隨機產生常態分配樣本，參數是樣本數、平均數、標準差
stocks
s1 <- stocks %>%
  gather(X,Y,Z,key="stock",value='price') %>% # 要合併的放前面(把xyz合併成stock)
  print(width=Inf,n=5)
# 有少數是正常的(此例為time是正常的)
s2 <- stocks %>%
  gather(X,Y,Z,key="stock",value="price",-time) %>% # 要合併的放前面(把xyz合併成stock)
  print(width=Inf,n=5)
#####################################################################
a1 <- read.csv("file:///C:/Users/user/Downloads/Toption2.csv",header = T) # 5直接於資料夾中點檔案複製，貼在""中即可
a11 <- as.tibble(a1) # 要記得改成tibble，如果是data.frame會有錯誤
a2 <- a11 %>%
  gather(colnames(a1)[3],colnames(a1)[4]
         ,key="交易類別",value="交易金額") %>%
  print(width=Inf,n=5)
#####################################################################
# 第二種髒的方式:值其實是變數(利用spread)
table2
spread(table2,key=type,value=count)
#####################################################################
# 第三種髒的方式:一格中有很多值，中間有特定符號分隔(利用separate)
table3
t1 <- table3 %>%
  separate(rate,into=c('cases','population')
           ,sep='/',convert=T) %>% # 把rate拆成'cases','population'，資料中是以/做分隔的，convert=T自動換成整數
  print()
#####################################################################
table3
# 切年份
t3 <- table3 %>%
  separate(year,into=c('cases','population'),sep=2) %>% # sep=2以兩個字元做切割(=-1即切最後一個字元)
  print()
# sep可以給兩個
t5 <- table3 %>%
  separate(year,into=c('cases','population','day'),sep=c(2,3)) %>% 
  print()






