library(tidyverse)
library(ggplot2)
setwd('D:\\研究所(2019.9.23)\\碩一上\\R讀書會\\project\\data')
data <- read.csv('Statistics on electricity consumption of residential and service industries and institutions in various counties and cities.csv',
                 header=T,fileEncoding = 'UCS-2LE')# 用UCS-2LE才讀得了
summary(is.na(data))
class(data)
data[2,]
new_data <- data%>% # 年月分開
  separate(日期,
             sep=c(4,5,7),
             into=c('year','zyear','month','zmonth'))
new_data <- select(new_data,-starts_with('z'))
#data_taipei <- as.data.frame(filter(data,縣市=='台北市'))
#select(data,'縣市')
#filter(data,縣市=='台北市')
#colnames(data_taipei) <- a
#class(data_taipei)
#a <- colnames(data)
#class(a)
####################################################################

# 用電佔比
data[323:2139,][12] <- data[323:2139,][12]*100
data_without_sum <- filter(data,縣市用電佔比...!=100)
win.graph()
data_without_sum %>% 
  ggplot(aes(x=data_without_sum$日期,y=data_without_sum$縣市用電佔比...,group=縣市,color=縣市)) +
  geom_line() + 
  geom_point() + 
  labs(x = "年月" , y = "用電佔比",title = "各縣市各月份用電佔比")+
  coord_cartesian(ylim = c(min(data_without_sum$縣市用電佔比), max(data_without_sum$縣市用電佔比)))+
  theme(plot.title = element_text(hjust = 0.5))+
  theme(axis.text.x = element_text(angle=65, vjust=0.6))
  
data_taipei[15:93,][12] <- data_taipei[15:93,][12]*100# 2018年開始，用電佔比改為百分比形式
summary(data_taipei[,12])
win.graph()
plot(data_taipei$日期,data_taipei$縣市用電佔比,pch=16)

new_data[323:2139,][12] <- new_data[323:2139,][12]*100
new_data_without_sum <- filter(new_data,縣市用電佔比...!=100)
win.graph()
data_without_sum %>% 
  ggplot(aes(x=data_without_sum$month,y=data_without_sum$縣市用電佔比,group=縣市,color=縣市)) +
  geom_line() + 
  geom_point() + 
  labs(x = "月份" , y = "用電佔比",title = "各縣市各月份用電佔比")+
  coord_cartesian(ylim = c(min(data_without_sum$縣市用電佔比), max(data_without_sum$縣市用電佔比)))+
  theme(plot.title = element_text(hjust = 0.5))

colnames(data)
####################################################################

## 各縣市平均用電佔比
aa <- 
  group_by(new_data_without_sum,縣市,month) %>%
  summarise(平均用電佔比=mean(縣市用電佔比...))
aa1 <- 
  group_by(aa,縣市) %>%
  summarise(平均用電佔比=mean(平均用電佔比))
order(aa1$平均用電佔比)

win.graph()
aa%>%
  ggplot(aes(x=month,y=平均用電佔比,group=縣市,color=縣市)) +
  geom_line() + 
  geom_point()
# draw 4 largest
data_largest <- filter(data_without_sum,縣市=='台北市'|縣市=='新北市'|縣市=='台中市'|
                         縣市=='高雄市')
bb <- 
  group_by(data_largest,縣市,month) %>%
  summarise(平均用電佔比=mean(縣市用電佔比...))

win.graph()
bb %>% 
  ggplot(aes(x=month,y=平均用電佔比,group=縣市,color=縣市)) +
  geom_line() + 
  geom_point() + 
  #coord_cartesian(ylim = c(min(data_largest$縣市用電佔比), max(data_largest$縣市用電佔比)))+
  theme(plot.title = element_text(hjust = 0.5))+
  theme(axis.text.x = element_text(angle=65, vjust=0.6))

# draw 3 opposite
data_opposite <- filter(data_without_sum,縣市=='台南市'|縣市=='桃園市'|縣市=='彰化縣')
bbo <- 
  group_by(data_opposite,縣市,日期) %>%
  summarise(平均用電佔比=mean(縣市用電佔比...))

win.graph()
bbo %>% 
  ggplot(aes(x=日期,y=平均用電佔比,group=縣市,color=縣市)) +
  geom_line() + 
  geom_point() + 
  #coord_cartesian(ylim = c(min(data_opposite$縣市用電佔比), max(data_opposite$縣市用電佔比)))+
  theme(plot.title = element_text(hjust = 0.5))+
  theme(axis.text.x = element_text(angle=65, vjust=0.6))

# only one city graph
colnames(data_without_sum)
data_nt <- as.data.frame(filter(data_without_sum,縣市=='新北市'))
win.graph()
data_nt%>%
  ggplot(aes(x=month,y=縣市用電佔比...,group=year,color=year))+
  geom_line()+
  geom_point()+
  labs(x = "month" , y = "用電佔比",title = "新北市各年月份用電佔比")+
  theme(plot.title = element_text(hjust = 0.5))
####################################################################

# 服務業用電量
colnames(data)
win.graph()
data %>% 
  ggplot(aes(x=data$日期,y=data$服務業部門售電量.度.,group=縣市,color=縣市)) +
  geom_line() + 
  geom_point() + 
  labs(x = "年月" , y = "服務業部門用電量",title = "各縣市各月份服務業部門用電量")+
  coord_cartesian(ylim = c(min(data_without_sum$服務業部門售電量.度.), max(data_without_sum$服務業部門售電量.度.)))+
  theme(plot.title = element_text(hjust = 0.5))+
  theme(axis.text.x = element_text(angle=65, vjust=0.6))
## largest 6
cc <- 
  group_by(new_data,縣市,month) %>%
  summarise(服務業部門用電量=mean(服務業部門售電量.度.))
table(cc)
cc1 <- 
  group_by(cc,縣市)%>%
  summarise(服務業部門用電量=mean(服務業部門用電量))
order(dd$服務業部門用電量)
data_largest <- filter(data,縣市=='台北市'|縣市=='新北市'|縣市=='台中市'|
                         縣市=='高雄市'|縣市=='桃園市'|縣市=='台南市')
win.graph()
data_largest %>% 
  ggplot(aes(x=data_largest$日期,y=data_largest$服務業部門售電量.度.,group=縣市,color=縣市)) +
  geom_line() + 
  geom_point() + 
  labs(x = "年月" , y = "服務業部門用電量",title = "各年月服務業部門用電量--前六高的縣市")+
  coord_cartesian(ylim = c(min(data_without_sum$服務業部門售電量.度.), max(data_without_sum$服務業部門售電量.度.)))+
  theme(plot.title = element_text(hjust = 0.5))+
  theme(axis.text.x = element_text(angle=65, vjust=0.6))
####################################################################

# 住宅用電量
colnames(data)
win.graph()
data %>% 
  ggplot(aes(x=data$日期,y=data$住宅部門售電量.度.,group=縣市,color=縣市)) +
  geom_line() + 
  geom_point() + 
  labs(x = "年月" , y = "住宅用電量",title = "各縣市各月份住宅用電量")+
  coord_cartesian(ylim = c(min(data_without_sum$住宅部門售電量.度.), max(data_without_sum$住宅部門售電量.度.)))+
  theme(plot.title = element_text(hjust = 0.5))+
  theme(axis.text.x = element_text(angle=65, vjust=0.6))























