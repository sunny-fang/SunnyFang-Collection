# 期中考第一題1.3
library(RColorBrewer)
c1 <- brewer.pal(5,"Reds") # 切成五份
t1 <- rep(1,5)
barplot(t1,col=c1)
q <- quantile(Price1,0:5/5)
p <- cut(Price1,q,include.lowest = T)
col1 <- brewer.pal(5,"Reds")[p] # 依據p來做顏色的切割
plot(TRE$GisX,TRE$GisY,pch=16,col=col1)
# 深淺調換(利用rev)
col2 <- rev(brewer.pal(5,"Reds"))[p]
plot(TRE$GisX,TRE$GisY,pch=16,col=col2)
