#讀入dataset
#con=file("/var/disk/a/user/etu/ratings.dat","r") #開啟檔案
#ratings_10k <- data.frame(a)
#a <- readLines(con,10000)
#a <- read.table(readLines(con,10000),quote="\"")
#a <- readLines(con,10000) #1表讀一列, 可一次讀取100列
#close(con) #關閉檔案

ratings <- read.table("/var/disk/a/user/etu/ratings.dat", quote="\"") #從vm的的disk上讀取檔案
ratings <- read.table(file.choose(), quote="\"") #從vm的的disk上讀取檔案

#建立data frame, 設定欄位名稱
ratings <- data.frame("user"=ratings$V1,"item"=ratings$V2,"pref"=ratings$V3)
ratings_20 <- ratings[1:20,]
#names(ratings)<-c("user","item","pref") 

#將data frame上傳到hdfs
ratings.hdfs = to.dfs(keyval(ratings$user, ratings))
from.dfs(ratings.hdfs)

#STEP 1 建立物品的伴隨矩陣
# 1) 依照user分組,得到所有物品出現的組合列表
ratings.mr<-mapreduce(
  ratings.hdfs, 
  map = function(k, v) {
    #keyval(k,v$item)
    rmr.str(keyval(k,v$item))
  }
  ,reduce=function(k,v){
    m<-merge(v,v)
    keyval(m$x,m$y)
  }
)
from.dfs(ratings.mr)

# 2) 對物品組合列表進行計數數字,建立物品的伴隨矩陣
system.time(
step2.mr<-mapreduce(
  ratings.mr,
  map = function(k, v) {
    d<-data.frame(k,v)
    d2<-ddply(d,.(k,v),count)
    #rm(d)
    #d3 <- subset(d2, d2$freq>1) #只把出現1次以上的留下
    #rm(d2)
    key<-d2$k
    val<-d2
    #key<-d3$k
    #val<-d3
    keyval(key,val)
  },
  #output="movie/data/step2.mr",
  #utput.format="text"
)
)
from.dfs(step2.mr)

# 2. 建立user對item的評分矩陣
train2.mr<-mapreduce(
  ratings.hdfs, 
  map = function(k, v) {
    #df<-v[which(v$user==3),]
    df<-v
    key<-df$item
    val<-data.frame(item=df$item,user=df$user,pref=df$pref)
    keyval(key,val)
  }
)
from.dfs(train2.mr)

#3. 合併伴隨矩陣跟評分矩陣
eq.hdfs<-equijoin(
  left.input=step2.mr, 
  right.input=train2.mr,
  map.left=function(k,v){
    keyval(k,v)
  },
  map.right=function(k,v){
    keyval(k,v)
  },
  outer = c("left")
)
from.dfs(eq.hdfs)

#4. 計算推薦結果列表
cal.mr<-mapreduce(
  input=eq.hdfs,
  map=function(k,v){
    val<-v
    na<-is.na(v$user.r)
    if(length(which(na))>0) val<-v[-which(is.na(v$user.r)),]
    keyval(val$k.l,val)
  }
  ,reduce=function(k,v){
    val<-ddply(v,.(k.l,v.l,user.r),summarize,v=freq.l*pref.r)
    keyval(val$k.l,val)
  }
)
from.dfs(cal.mr)

#5. 按照輸入格式得到推薦評分列表
result.mr<-mapreduce(
  input=cal.mr,
  #output="movie/data/ratings_100_result_top10",
  map=function(k,v){
    keyval(v$user.r,v)
  }
  ,reduce=function(k,v){
    val<-ddply(v,.(user.r,v.l),summarize,v=sum(v))
    val2<-val[order(val$v,decreasing=TRUE),]
    #val3 <- val2[1:10,]
    names(val2)<-c("user","item","pref")
    #names(val3)<-c("user","item","pref")
    keyval(val2$user,val2)
    #keyval(val3$user,val3)
  },
  #output.format = "text"
)
from.dfs(result.mr)