library(tidyverse)
library(zoo)
setwd('D:\\研究所(2019.9.23)\\碩一上\\R讀書會\\project\\data')
raw_data <- read.csv('台灣電力公司_過去電力供需資訊.csv', header = T, fileEncoding = 'UCS-2LE')
summary(is.na(raw_data))
raw_data[is.na(raw_data)] <- 0
colnames <- colnames(raw_data)
raw_data1 <- raw_data%>%
  separate(日期,sep=c(4,6),into=c('year','month','date'))
raw_data2 <- group_by(raw_data1,month)%>%
  lapply(raw_data1,mean)

zoo(raw_data1[, c('year')], raw_data1$month)

zoo(mydf[, c('a', 'b')], mydf$date)


class(colnames)















