# rmarkdown:https://knowlab.wordpress.com/2016/12/05/%E4%BB%A5-r-markdown-%E8%BC%95%E9%AC%86%E7%B7%A8%E8%BC%AF%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90%E5%A0%B1%E5%91%8A%EF%BC%88%E4%B8%8A%EF%BC%89/
library(ggplot2)
library(highcharter)
library(lattice)
library(tidyverse)
setwd('D:\\研究所(2019.9.23)\\碩一上\\R讀書會\\project\\data')
data <- read.csv('sum of supply by month.csv',header=T,fileEncoding = 'UCS-2LE')
data[is.na(data)] <- 0
select(data,starts_with('核二'))
win.graph()
highchart()%>%
  hc_title(text='核能供應')%>%
  hc_xAxis(categories=data$date)%>%
  hc_add_series(name='新北核2-1',data=data$'核二1萬瓩',color='#3D4490')%>%
  hc_add_series(name='新北核2-2',data=data$'核二2萬瓩',color='#5994FF')%>%
  hc_add_series(name='屏東核3-1',data=data$核三1,color='#FF5126')%>%
  hc_add_series(name='屏東核3-2',data=data$核三2,color='#FD9A28')

c <- highchart()%>%
  hc_title(text='台中火力供應')%>%
  hc_xAxis(categories=data$date)%>%
  hc_add_series(name='台中1',data=data$'台中1')%>%
  hc_add_series(name='台中2',data=data$'台中2')%>%
  hc_add_series(name='台中3',data=data$'台中3')%>%
  hc_add_series(name='台中4',data=data$'台中4')%>%
  hc_add_series(name='台中5',data=data$'台中5')%>%
  hc_add_series(name='台中6',data=data$'台中6')%>%
  hc_add_series(name='台中7',data=data$'台中7')%>%
  hc_add_series(name='台中8',data=data$'台中8')%>%
  hc_add_series(name='台中9',data=data$'台中9')%>%
  hc_add_series(name='台中10',data=data$'台中10')
c

#############################################################
data_require <- read.csv('Statistics on electricity consumption of residential and service industries and institutions in various counties and cities.csv',header = T,fileEncoding = 'UCS-2LE')
require_sum <- data_require[data_require$縣市=='合計',]
require_sum1 <- require_sum[1:21,]

require_sum1 <- rev(require_sum1$日期)

require_sum1[order(require_sum1$日期),]

d <- highchart()%>%
  hc_title(text='高雄火力供應')%>%
  hc_xAxis(categories=data$date)%>%
  hc_add_series(name='興達1',data=data['興達1'])%>%
  hc_add_series(name='興達2',data=data['興達2'])%>%
  hc_add_series(name='興達3',data=data['興達3'])%>%
  hc_add_series(name='興達4',data=data['興達4'])%>%
  hc_add_series(name='大林1',data=data['大林1'])%>%
  hc_add_series(name='大林2',data=data['大林2'])
d
highchart()%>%
  hc_title(text='高雄火力供應')%>%
  hc_xAxis(categories=data$date)%>%
  hc_add_series(name='興達1',data=data$興達1)%>%
  hc_add_series(name='興達2',data=data$興達2)%>%
  hc_add_series(name='興達3',data=data$興達3)%>%
  hc_add_series(name='興達4',data=data$興達4)%>%
  hc_add_series(name='大林1',data=data$大林1)%>%
  hc_add_series(name='大林2',data=data$大林2)

highchart()%>%
  hc_title(text='總供給量(MW)')%>%
  hc_xAxis(categories=new_data$date)%>%
  hc_add_series(name='總供電量',data=new_data$sum,color = '#155FCF')


setwd('D:\\研究所(2019.9.23)\\碩一上\\R讀書會\\project\\data\\usage')
data_usage <- read.csv('Usage.csv')
colnames(data_usage)
group_by(data_usage,年月份)%>%
  summarise(mean=mean(X25綜合.電力合計.售電度數.當月.))
sum_usage <- aggregate(data_usage$X25綜合.電力合計.售電度數.當月.,by=list(data_usage$年月份),FUN=sum)
class(sum_usage)






