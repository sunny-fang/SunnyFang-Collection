setwd('D:\\研究所(2019.9.23)\\碩一上\\R讀書會\\project\\data\\air_Taichung\\csv')
#library(readxl)
#library(stringr)
library(tidyverse)
library(highcharter)
library(ggplot2)

# 空汙資料
air_data107 <- read.csv('107年西屯站_20190315.csv',fileEncoding = "UCS-2LE")
air_data107_1 <- read.csv('107年西屯站_20190315.csv',fileEncoding = "UCS-2LE")

for(i in c(4:27)){
  air_data107_1[,i] <- as.numeric(as.character(air_data107[,i]))
}
air_data107_1[is.na(air_data107_1)]=0

air_data107_pm2.5 <- air_data107_1[air_data107_1$測項=='PM2.5',]
for(i in c(4:27)){
  for(x in c(1:365)){
    if(air_data107_pm2.5[x,i]>250){
      air_data107_pm2.5[x,i] <- 0
    }
  }
}
max_2.5 <-  apply(air_data107_pm2.5[,4:27],1,max,na.rm=TRUE)
max_2.5 <- data.frame(max_2.5)
air_data107_pm2.5 <- cbind(air_data107_pm2.5[,1:3],max_2.5)

air_data107_pm10 <- air_data107_1[air_data107_1$測項=='PM10',]
for(i in c(4:27)){
  for(x in c(1:365)){
    if(air_data107_pm10[x,i]>250){
      air_data107_pm10[x,i] <- 0
    }
  }
}
max_10 = apply(air_data107_pm10[,4:27],1,max,na.rm=TRUE)
max_10 <- data.frame(max_10)
air_data107_pm2.5 <- cbind(air_data107_pm2.5,max_10)

air_data107_co <- air_data107_1[air_data107_1$測項=='CO',]
for(i in c(4:27)){
  for(x in c(1:365)){
    if(air_data107_co[x,i]>4){
      air_data107_co[x,i] <- 0
    }
  }
}
max_co = apply(air_data107_co[,4:27],1,max,na.rm=TRUE)
max_co <- data.frame(max_co)
air_data107_pm2.5 <- cbind(air_data107_pm2.5,max_co)

air_data107_no2 <- air_data107_1[air_data107_1$測項=='NO2',]
for(i in c(4:27)){
  for(x in c(1:365)){
    if(air_data107_no2[x,i]>250){
      air_data107_no2[x,i] <- 0
    }
  }
}
max_no2 = apply(air_data107_no2[,4:27],1,max,na.rm=TRUE)
max_no2 <- data.frame(max_no2)
air_data107_pm2.5 <- cbind(air_data107_pm2.5,max_no2)

air_data107_so2 <- air_data107_1[air_data107_1$測項=='NO2',]
for(i in c(4:27)){
  for(x in c(1:365)){
    if(air_data107_so2[x,i]>250){
      air_data107_so2[x,i] <- 0
    }
  }
}
max_so2 = apply(air_data107_so2[,4:27],1,max,na.rm=TRUE)
max_so2 <- data.frame(max_so2)
air_data107_pm2.5 <- cbind(air_data107_pm2.5,max_so2)

air_data107_o3 <- air_data107_1[air_data107_1$測項=='O3',]
for(i in c(4:27)){
  for(x in c(1:365)){
    if(air_data107_o3[x,i]>200){
      air_data107_o3[x,i] <- 0
    }
  }
}
max_o3 = apply(air_data107_o3[,4:27],1,max,na.rm=TRUE)
max_o3 <- data.frame(max_o3)
air_data107_pm2.5 <- cbind(air_data107_pm2.5,max_o3)

summary(air_data107_pm2.5)

highchart()%>%
  hc_title(text='六大空氣指標')%>%
  hc_xAxis(categories=air_data107_pm2.5$日期)%>%
  hc_add_series(name='PM2.5',data=air_data107_pm2.5$max_2.5)%>%
  hc_add_series(name='PM10',data=air_data107_pm2.5$max_10)%>%
  hc_add_series(name='CO',data=air_data107_pm2.5$max_co)%>%
  hc_add_series(name='NO2',data=air_data107_pm2.5$max_no2)%>%
  hc_add_series(name='SO2',data=air_data107_pm2.5$max_so2)%>%
  hc_add_series(name='O3',data=air_data107_pm2.5$max_o3)

air_data107_pm2.5_sep <- air_data107_pm2.5 %>%
  separate(日期
           ,sep=c(5,7) 
           ,into=c('year','month','date'))
aa <- group_by(air_data107_pm2.5_sep,month)%>%
  summarise(mPM2.5=mean(max_2.5),mPM10=mean(max_10))
highchart()%>%
  hc_title(text='Mean of PM2.5&PM10')%>%
  hc_xAxis(categories=aa$month)%>%
  hc_add_series(name='PM2.5',data=aa$mPM2.5)%>%
  hc_add_series(name='PM10',data=aa$mPM10)


############################################################
# 台中火力發電量
setwd('D:\\研究所(2019.9.23)\\碩一上\\R讀書會\\project\\data')
data <- read.csv('sum of supply by month.csv',header=T,fileEncoding = 'UCS-2LE')
data[is.na(data)] <- 0
sum_taichung_fire <- apply(data[,16:25],1,sum)
sum_taichung_fire <- data.frame(sum_taichung_fire)
data1 <- cbind(data[,c(16:25,71)],sum_taichung_fire)
highchart()%>%
  hc_title(text='台中火力發電總供應電量')%>%
  hc_xAxis(categories=data1$date)%>%
  hc_add_series(name='火力總供電量',data=data1$sum_taichung_fire)

highchart()%>%
  hc_title(text='台中火力發電供應電量')%>%
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

############################################################

