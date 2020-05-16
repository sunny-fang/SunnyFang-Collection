setwd('D:\\研究所(2019.9.23)\\碩一上\\R讀書會\\project\\data\\air_Taichung\\csv')
library(tidyverse)

# 空汙資料
air_data107 <- read.csv('107年忠明站_20190315.csv',fileEncoding = "UCS-2LE")
air_data107_1 <- read.csv('107年忠明站_20190315.csv',fileEncoding = "UCS-2LE")

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

#row <- c('2015/11/27','沙鹿','PM2.5',0)
#air_data107_pm2.5 <- rbind(air_data107_pm2.5[1:330,], row, air_data107_pm2.5[331:nrow(air_data107_pm2.5), ])

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
# 日期 <- air_data107_pm10$日期
# max_10 <- cbind(日期,max_10)
# air_data107_pm2.5 <- merge(x = max_10, y = air_data107_pm2.5, by = "日期", all = TRUE)

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
air_data107_ZONG <- cbind(air_data107_pm2.5,max_o3)

##############################################################
air_data_ZONG <- rbind(air_data103_ZONG,air_data104_ZONG,air_data105_ZONG,
                     air_data106_ZONG,air_data107_ZONG)
write.csv(air_data_ZONG,file="D:\\研究所(2019.9.23)\\碩一上\\R讀書會\\project\\data\\air_Taichung\\csv\\air_data_ZONG.csv",row.names = FALSE)








