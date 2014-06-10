**Etu 實習進度報告**
=====================

Hi, This is my *overall report* for my internship in **Etu** during these 4 months.

Also it's my very first time using `Markdown language` and `StackEdit` to produce documents, and I have to say, `StackEdit` helps me to organize my articles in a **rapid** and **well-organized** way. (Thanks **Jazz** for introducing me this powerful tool.)

**Table of Context:**

[TOC]

----
**Get familiar with EVA (Etu Virtual Appliance) (2/10~2/12)**
--------
- use **EVA** to deploy a 1+2 node Hadoop environment rapidly.
- use web console on Etu Appliance
- help Effy & Judy to think of/correct wordings for EA 2.5

----

**Udacity: Intro to Hadoop & MapReduce (2/11~2/23)**
---------
於 Udacity 網站上課學習 Hadoop & MapReduce 最基本的觀念。

- **Big Data Intro:**
    Understand the basic knowledge of big data. (4V: Velocity, Variaty, Volume, Veracity)

- **Hadoop, HDFS, and Mapreduce:**
    - what **hadoop** is ( an open sorce framework for processing big data)
    - the mechanism behind **HDFS** ( _data block, duplication, and fault tolerant_)
    - the philosophy of  **Mapreduce** ( _functional programming_)
    
        > hadoop 適合拿來解符合交換率跟結合率的問題 -> 不需要一直迭代(iteration)結果的問題
 
- **Mapreduce Code:**
    - `Python` + `Hadoop Streaming` 
        - 使用 hadoop streaming 讓 user 可以用幾乎任何語言寫 hadoop job
        
         `~ hadoop jar [path/to/.jar] -mapper [mapper_file] -reducer [reducer_file] -file [mapper_file] -file [reducer_file] -input [input_file] -output [output_directory]`

        - 在實際執行 hadoop job 前，可以先用小資料測試。 Pipeline in `terminal`:
        
         `~ cat testfile | ./mapper.py | sort | ./reducer.py`
        
        - or you can also set alias in `~/.bashrc` ex:
            > run_mapreduce(){
                hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mrl-cdh4.1.1.jar -mapper \$1 -reducer \$2 -file \$1 -file \$2 -input \$3 -output \$4
            }
            
            > alias hs = run_mapreduce

    - **Virtual machine:** Cloudera Quick VM
    - **Core:** key-value
    - **Flow:** mapper > shuffle & sort > reducer
    - **Combiner:** 減少 mapper & reducer 間 suffle 的 task loading
     ( Note: 當拿 reducer 用作 combiner 時，reducer 的 output & input type 須一致，因為 combiner 的 output 是 reducer 的 input)
    

- **Mapreduce Design Patterns**
    - **Prcatice:** analyse __*web-log data*__. ( Filtering, Inverted index, URL hits analysis)
    - A pattern is a **proven solution** to a **recurring problem** in a **specific context**
    - view the python code on my [github][1]
- **Referance:** Hadoop Definition Guide, Udacity online resource

- **感想:**

 透過在 Udacity 上完整學完5個章節的課程，讓我快速對寫 hadoop 程式的核心-- **map-reduce** 的計算邏輯有了初步的掌握。`hadoop streaming` 讓 user 可以用幾乎任何的程式語言撰寫 mapreduce 程式，我覺得以 python 寫 code 的好處是非常直覺，可以專注在演算邏輯上。透過 cloudera 提供的 quick VM 以及 python，讓完全沒有碰過 hadoop 的我對 hadoop HDFS 以及 map reduce 有了初步的認識。

----

**RHadoop: rmr2, rhdfs, rhbase (2/24~3/9)**
---------
- **Installing RHadoop package 安裝RHadoop**
    Briefly summary:
    1. Download the latest packages from [github][2]
    
     ex: [plyrmr-0.3.0][3], [rmr2-3.1.1][4], [rhdfs-1.0.8][5], and [rhbase-1.2.0][6]

    2. Install the required packages and related dependency in R console:
    
     `> install.packages( c('rJava', 'RJSONIO', 'itertools', 'digest', 'Rcpp','httr','functional','devtools', 'stringr', 'reshape2'))`
     
    3. Export environment variable:
    
     `~ export HADOOP_CMD=/usr/bin/hadoop` (my setting)
     
     `~ export HADOOP_STREAMING=/usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar` (my setting)

    4. Install rmr package
    
     `> sudo R CMD INSTALL rmr2_2.0.1.tar.gz `
     
    5. Set System environment in R console: 
    
     `Sys.setenv("HADOOP_HOME"="/opt/hadoopmr")` (my setting)
     
     `Sys.setenv("HADOOP_CMD"="/opt/hadoopmr/bin/hadoop")` (my setting)
     
     `Sys.setenv("HADOOP_STREAMING"="/opt/hadoopmr/hadoop-streaming-2.0.0-mr1-cdh4.0.1.jar")` (my setting)
     
    6. Install rhdfs package:
    
     `> sudo R CMD INSTALL rhdfs_1.0.5.tar.gz`
     
    7. Load the packages: ( be sure to run `hdfs.init()` everytime)
    
     `library(rmr2)`
     
     `library(rhdfs)`
     
     `hdfs.init()`
     
    8. Reference: 
        - http://www.meetup.com/Learning-Machine-Learning-by-Example/pages/Installing_R_and_RHadoop/
        - http://cos.name/2013/03/rhadoop2-rhadoop/

- **Problem Solving:**
 
 參考 [r-and-hadoop-整合初體驗][7] 文章，使用RHadoop計算股市累積移動平均(CMA)，得到一樣的錯誤結果。

 ![the incorrect result][8]

 檢查code以後，發現是因為[參考範例][9]中的 `map` function 程式碼有誤， 在 rmr package 中已經 handle input format 的整理，所以不需要自行split strings

 >  map <- function(k,v) {
 >      fields <- unlist(strsplit(v, ","))
 >      keyval(fields[1], mean(as.double(c(fields[3], fields[6]))))
 >  }
 
 只要將程式碼改為
 > map <- function(k,v) {
 >      keyval(v[,1], (v[,3]+v[,6])/2)
 > }

 即可得到預期的正確結果。
 > $key
 > \[1] GOOG GOOG GOOG GOOG AAPL AAPL AAPL AAPL AAPL GOOG
Levels: AAPL GOOG

 >$val
 \[1] 689.030 466.795 428.875 200.055  88.315 197.055  85.045  73.565  64.035 314.960

 **NOTE**: The result wasn't as sorted as it supposed to be, because I didn't use `reduce` function.
 
- view the code on [my github][10] 

- **Reference:** 
    - The [github][11] page of the RHadoop developer
    - RHadoop on [google forum][12]
    - [My post on RHadoop forum][13] : 我於RHadoop論壇上的發問

- **心得:**

 原本以為 **R + Hadoop** 會是一個必殺武器，只要安裝了套件就可以將 R 強大的繪圖以及統計引擎直接 implement 到hadoop上，不過實際接觸之後才知道不是這麼一回事...

 RHadoop 為一個R的套件，由三個子套件 `rhdfs` , `rmr`, `rhbase` 組成，其底層以 `hadoop streaming` 的方式為 R 提供了一個與 hadoop 串接的接口。
 
 RHadoop 的優點是，cover 掉原先需要 java developer 需要自己控制的 driver code ，讓 user 可以直接從 R 的 console 端設計 map-reduce 程式，以及存取 HDFS 跟 HBASE。
 
 在 R 裡面寫 map reduce 有多簡單? 舉最經典的 `word count` 為例：
 
  > mapper = function(k,v) {
    keyval(k,1) 
  }
  
  > reducer = function(word, counts){
    keyval(word, sum(counts))
  }
  
  > mapreduce(
    input = "word_count_data", #指定input data
    output = "word_count_result", #指定output 資料夾
    input.format = make.input.format("text", sep = " "), #切割input的方式
	output.format = "text",
    map = mapper,
    reduce = reducer
	)

 原先用 java 需要寫上百行的程式碼現在簡簡單單搞定。
 
 一言以蔽之，`RHadoop`「**讓寫 R 的人也可以在 Hadoop 上開發 R 程式**」，不過思考程式演算邏輯時，概念上仍然要遵守 map reduce 的設計模式。
 
 在研究Rhadoop的過程中，剛好也有機會參與某公司的 case 討論，而開始研究如何將線性以及指數迴歸問題拆解為 map reduce 的型式。找了許多資料，也做了諸多嘗試，雖然從結果來看算是並沒有成功實作出來，不過從問題的本質來看，指數迴歸模型本來就不適合用 hadoop 的 framework 來解。這也再次印證了所謂 **「 hadoop 並非萬靈丹」** 的真理。
 
 RHadoop 是一個尚未發展成熟的工具，所以在實際部屬和使用 RHadoop 的過程中，也中了不少招，像是看別人的範例 run 的好好的，不過自己卻怎麼試也跑不出來，最後才發現別人的 code 用的是尚未更新的版本，而新版卻早已經大幅更改了參數語法。我的解惑方法之一是直接到 package developer 的論壇上請教問題，能夠直接和所有在使用 RHadoop 的 developer 交流是一個很棒的經驗！


----

**Collaborative Filtering 演算法研究 (3/10~4/18)**
---------

相較於指數迴歸問題，**協同過濾 ( CF, Collaborative Filtering )** 便是一個經過驗證，適合用 hadoop 的演算法，甚至在 hadoop ecosystem 上還有專門做 machine learing 的 `mahout` 函式庫！

1. Study Collaborative Filtering from **mahout examples** using Java 學習協同過濾演算法

 - view my code on [github][14]

2. 練習以 `R + Hadoop` 實作協同過濾演算法，為這一階段最主要的課題。

- study the algorithm of **_Collaborative Filtering_**.
    - similarity: calculate the corelation (distance) between two object.
- **_user-based_** and **_item-based_**
- problem field: Mostly using Collaborative Filtering for **_recommendation_**

- view my code on [github][15]

**感想:**
 
 **協同過濾演算法** 是一種機器學習 ( Machine Learning) 的技巧，常用來做商品的推薦，最經典的例子就是亞馬遜網路書店 ( Amazon.com )：顧客選擇一本自己感興趣的書籍，馬上會在底下看到一行「Customer Who Bought This Item Also Bought」，以「對同一本書有興趣的讀者在某種程度上興趣相近」為前提下進行推薦，創造出了經典的電子商務模式。
 
 以我個人而言，除了學習協同過濾的演算法之外，同時也要專注在如何「以 Hadoop 進行協同過濾的計算」。直接找 mahout 的範例練習，幫助我快速上手，不過因為自己程式功力還不夠，光學習演算法的精神並了解程式的演算邏輯就幾乎花掉我所有時間，所以一直沒有機會實際拿 ER 的資料直接放在 EVA 上面來玩，這是有點可惜的地方。
 
 在練習用 `RHadoop` 實作協同過濾演算法時，我使用 movielens 的資料集，來實作 item-based 的推薦。用 RHadoop 的好處是，我可以專注理解處理資料，而無須理會底層 hadoop 框架的控制，這不僅增進我的 R 能力，也讓我更了解協同過濾。
 
 有件事值得一提，CF & mahout 的作法係將稀疏的資料矩陣降維，並計算出一個「分數」，然後依照分數高低來判斷 user & item 之間的相似程度，然而問題是，**「我們對算出來的結果該多有信心？」** 、 **「如何知道結果是否 make sence?」**，基於這樣的想法，才會有接下來 **「Data Visualization via Collaborative Filtering」** 的研究。

----

**Etu Training L1-D: Hadoop 第一天 (3/13)**
---------
Learn the basic knowledge of **_hadoop ecosystem_**, and manage to use them practically.

**Sqoop**

 - Export _table schema_ from PostgreSQL to Hive

   > sqoop create-hive-table --connect jdbc:postgresql://etu-master/hive --username hive -P --table nyse_dividends --hive-table etu203.nyse_dividends
    
 - Export _data from_ PostgreSQL to Hive

	> sqoop import --connect jdbc:postgresql://etu-master/hive --username hive -P --table nyse_dividends --hive-import --hive-table etu203.nyse_dividends -m 1

 - for further info please view the note on [my github][16]

**Pig:**

 - **Data flow** language
 - 以 **map** 結構定義 data schema

 >	grunt>	players = LOAD 'baseball' USING PigStorage ('\t') AS ( name:chararray, team:chararray, position:bag{t:(p:chararray)},bat:map[]);
				
 FLATTEN function
 >	grunt>	pos = FOREACH players GENERATE name, FLATTEN(position) as position, bat#'batting_average' as batAvg;

 GROUP BY function
 >	grunt>	byPos = GROUP batters BY position;
 
 - for further info please view the note on [my github][17]

**Hive:** 

- use as **Data warehouse**
- **SQL-like** command to manipulate data
- 例題:用hive讀取nyse_daily的交易資料 統計2009-01-01到2009-06-30有成交量的股票, 
用股票類別做分類再用成交量的總合作排序

	>hive>	SELECT symbol, sum(volume) as sum FROM nyse_daily
					WHERE tdate >= "2009-01-01" AND tdate <= "2009-06-30"
					GROUP BY symbol
					SORT BY sum DESC;
					
	>hive>	select symbol, sum(volume) from nyse_daily
					where tdate >= "2009-01-01" and tdate <= "2009-06-30"
					group by symbol;
					
	>hive> 	select symbol, volume from nyse_daily
					where volume>1000000 limit 10;
	
 - for further info please view the note on [my github][18]

----

**Etu Trainng L1-V: Data Visualization(3/20)**
---------
use `QlikView` to visualize data.
Honestly, despite learning a new fancy visualization tools, nothing really special... :P

----

**Etu Training L1-H: HBase - NoSQL (3/27)**
---------
- **CAP理論:** It's impossible for a web service to provide the following 3 guarantees
    - **C** onsistency  ( 交易處理 )
    - **A** vailability ( 能很快讀到data )
    - **P** artition tolerance ( 某個node掛掉仍然能正常服務 )
- **HBASE:** **C** onsistency + **P** artition tolerance
- Type of **NoSQL** DB:
    - key-value: 社群網路
    - In-memory: 加速網路遊戲
    - Document: 存 XML 
    - Graphic: Tree 結構、交友
- **key concept:** _Column Family_: Qualifier
    - ex: (個人資料 family: 身高)、(個人資料 family: 體重)
- RDBMS 看資料的方式: Column per Row
- HBASE 看資料的方式: Row per Column

----

**Udacity: Intro to Computer Science (4/16~4/28)**
---------
fowllow the course and improve **_python_** skill
目前進展到chapter 3

----

**EHC 員工內部大賽 (4/22)**
---------
- 和`喬巴`一起參加 EHC 的員工內部競賽，在有限的時間內部屬 hadoop 以及其 component
- **Testing Environment:** CentOS 6.5 minimal
- **環境設定筆記:**

 1. 安裝`wget`
 > [root@localhost ~] yum install wget

 2. 安裝 oracle java jdk
 > [root@localhost ~] wget --no-cookies 
--no-check-certificate 
--header "Cookie: oraclelicense=accept-securebackup-cookie" 
"http://download.oracle.com/otn-pub/java/jdk/7u55-b13/jdk-7u55-linux-x64.rpm"
-O jdk-7u55-linux-x64.rpm
 > [root@localhost ~] yum install jdk-7u55-linux-x64.rpm
 
 3. 新增`jps`指令， 於`.bashrc`中加入`alias jps='/usr/java/jdk1.7.0_55/bin/bin/jps'`
 > [root@localhost ~] vi ~/.bashrc

 4. 從 `Bigtop` 安裝 hadoop component (hadoop, pig, hive, zookeeper, hbase)
 > [root@localhost ~] wget -O /etc/yum.repos.d/bigtop.repo http://www.apache.org/dist/bigtop/stable/repos/[centos5|centos6|fedora15|fedora16]/bigtop.repo
 > [root@localhost ~] yum install -y hadoop\* pig\* hive\* zookeeper\* hbase\*

- An **exciting moment**!!!

 ![enter image description here][19]
- **Referance:** [jazz vagrant-hadoop][20] on github

----

**Etu Training L1-M: MapReduce (4/24-5/6)**
---------
- Write mapreduce programs in **java**
- Know the difference between **new** and **old** API
- Use **Combiner**, **partitioner**, **toolrunner**, and **distrubuted cache**

認證題目:
「以新版的 MapReduce API 寫一個 M/R 程式，算出每天的成交量總合，並且使用 3 個 Reducer 將這三個交易日期範圍歸到同一個 Reducer 下。」

view the code on [my github][21]

give arguents in command line:

`/opt/hadoopmr/bin/hadoop jar [.jar] -D mapred.reduce.tasks=5 [input on HDFS] [output directory]`

----

**Data Visualization via Collaborative Filtering (5/25)**
---------

study [this paper][22] and try to write some R codes, using the _movielens_ as test dataset

**some preliminary results: 一些初步的成果**

1. plot1: Users and the correspond ratings on specific items.

  `> qplot(user_factor,item_factor, data = ratings_100, colour=pref, size=pref)`

 ![item_factor & user_factor][23]

2. plot2: A biplot using **PCA** (principal component analysis) method to express the similarity of movies and characteristics.
 
  `> biplot(cfpca,choice=1:2)`

 ![pca_biplot][24]

3. plot3: Project the result of PCA on a 2D plane, presenting the coordinate of each movie.

 `> ggplot(d,	aes(x=PC1,	y=PC2))	+  geom_point()	+	  geom_text(aes(label=id),            size=3,	vjust=-0.5)`

 ![item_based_projection][25]


----

**Summary**
--------

----

**Event List**
---------

 - 2/20 Etu ALL-hands Monthly, Feb.
 - 3/15 SITCON 2014
 - 3/28 Etu ALL-hands Monthly, Mar.
 - 4/11~4/12 OSDC
 - 4/22 Etu EHC 員工內部大賽
 - 4/29 中研院 陳昇瑋 研究員演講
 - 4/30 Etu ALL-hands Monthly, Apr.
 - 5/28 Etu All-hands Monthly, May.

----

> Written with [StackEdit](https://stackedit.io/).


  [1]: https://github.com/yenzichun/Etu_InternReport/tree/master/hadoop_streaming
  [2]: https://github.com/RevolutionAnalytics/RHadoop/wiki/Downloads
  [3]: http://goo.gl/UhrcbF
  [4]: http://goo.gl/UpK2y9
  [5]: http://goo.gl/UpK2y9
  [6]: https://github.com/RevolutionAnalytics/rhbase/blob/master/build/rhbase_1.2.0.tar.gz?raw=true
  [7]: http://michaelhsu.tw/2013/05/01/r-and-hadoop-%E5%88%9D%E9%AB%94%E9%A9%97/
  [8]: http://i.imgur.com/JN1SV1c.png
  [9]: https://github.com/alexholmes/hadoop-book/blob/master/src/main/R/ch8/stock_cma_rmr.R
  [10]: https://github.com/yenzichun/Etu_InternReport/tree/master/RHadoop
  [11]: https://github.com/RevolutionAnalytics/RHadoop
  [12]: https://groups.google.com/forum/?hl=zh-TW#!forum/rhadoop
  [13]: https://groups.google.com/forum/#!topic/rhadoop/S02_moZEsI4
  [14]: https://github.com/yenzichun/Etu_InternReport/tree/master/MahoutPractice
  [15]: https://github.com/yenzichun/Etu_InternReport/blob/master/RHadoop/Collaborative_Filtering.R
  [16]: https://github.com/yenzichun/Etu_InternReport/blob/master/Sqoop,%20Pig%20and%20Hive/sqoop.txt
  [17]: https://github.com/yenzichun/Etu_InternReport/blob/master/Sqoop,%20Pig%20and%20Hive/pig.txt
  [18]: https://github.com/yenzichun/Etu_InternReport/blob/master/Sqoop,%20Pig%20and%20Hive/hive.txt
  [19]: https://lh3.googleusercontent.com/7z0OTqBOoZSuvdVPYAZ7PgPC3_0pHAeLDzXZCGqrkoI=s500 "882109_10200805859548553_1933855539414159678_o.jpg"
  [20]: https://github.com/jazzwang/vagrant-hadoop/blob/master/bigtop-aws/ubuntu/provision.sh
  [21]: https://github.com/yenzichun/StockVolume
  [22]: http://hal.archives-ouvertes.fr/docs/00/67/33/30/PDF/visualCF.pdf
  [23]: https://lh6.googleusercontent.com/JwDvKdwbpmrezwIDYjQ1hbP8fkH_MWPOMzyZMNvP1dQ=s500 "item&user_biplot.jpeg"
  [24]: https://lh3.googleusercontent.com/_OIFCqtOg_rinSmKXrMdl0DLGF_UMjRdwxMo-mJVzHc=s500 "CFpca.jpeg"
  [25]: https://lh5.googleusercontent.com/d4KwdqEV_viL3FmbaRnT9tpsjc70HbN2npSjLrvKohs=s500 "item_based_projection.jpeg"