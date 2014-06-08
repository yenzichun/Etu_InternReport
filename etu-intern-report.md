**Etu 實習進度報告**	{#welcome}
=====================

Hi, This is my *overall report* for my internship in **Etu** during these 5 months.

Also it's my very first time using `Markdown language` and `StackEdit` to produce documents, and I have to say, `StackEdit` helps me to organize my articles in a **rapid** and **well-organized** way. (Thanks **Jazz** for introducing me this powerful tool.)

Thanks for all the opportunities I've been given! :)

----
**Get familiar with EVA(Etu Virtual Appliance)**
--------
- use **EVA** to deploy a 1+2 node Hadoop environment rapidly.
- use web console on Etu Appliance
- help Effy & Judy to think of/correct wordings for EA 2.5

----

**Udacity: Intro to Hadoop & MapReduce (2/11~2/23)**
---------
- **Big Data Intro:**
    Understand the basic knowledge of big data. (4V: Velocity, Variaty, Volume, Veracity)

- **Hadoop, HDFS, and Mapreduce:**
    - what **hadoop** is ( an open sorce framework for processing big data)
    - the mechanism behind **HDFS** (_data block, duplication, and fault tolerant_)
    - the philosophy of  **Mapreduce** (_functional programming_, 符合交換率跟結合率的問題才適合用mapreduce解 -> 不需要一直迭代(iteration)結果的問題 )

- **Mapreduce Code:**
    - `Python` + `Hadoop Streaming` 
        - 使用 hadoop streaming 讓 user 可以用幾乎任何語言寫hadoop job
        - 
    - **Virtual machine:** Cloudera Quick VM
    - **core:** key-value
    - **flow:** mapper > shuffle & sort > reducer
    - **combiner:** 減少mapper & reducer間suffle的task loading
    (Note: 當拿 reducer用作 combiner 時，reducer 的 output & input type 須一致，因為 combiner 的 output 是 reducer 的 input)
    

- **Mapreduce Design Patterns**
    - **Prcatice:** analyse __*web-log data*__. ( Inverted index, url hits analysis)
    - A pattern is a **proven solution** to a **recurring problem** in a **specific context**
- **Referance:** Hadoop Definition Guide, Udacity online resource

----

**RHadoop: rmr2, rhdfs, rhbase (2/24~3/9) **
---------
- **Installing RHadoop package 安裝RHadoop**
    Briefly summary:
    1. Download the latest packages from [github][1]
    ex: [plyrmr-0.3.0][2], [rmr2-3.1.1][3], [rhdfs-1.0.8][4], and [rhbase-1.2.0][5]
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
 參考 [r-and-hadoop-整合初體驗][6] 文章，使用RHadoop計算股市累積移動平均(CMA)，得到一樣的錯誤結果。
![the incorrect result][7]

 檢查code以後，發現是因為[參考範例][8]中的 `map` function 程式碼有誤， 在 rmr package 中已經 handle input format 的整理，所以不需要自行split strings

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

- Reference: 
    - The [github][9] page of the RHadoop developer
    - RHadoop on [google forum][10]
    - [My post on RHadoop forum][11] : 我於RHadoop論壇上的發問

----

**Collaborative Filtering (3/10)**
---------
- study the algorithm of **_Collaborative Filtering_**.
    - similarity: calculate the corelation (distance) between two object.
- **_user-based_** and **_item-based_**
- problem field: Mostly using Collaborative Filtering for **_recommendation_**

----

**L1-D Hadoop 第一天 (3/13)**
---------
Learn the basic knowledge of **_hadoop ecosystem_**, and manage to use them practically.

**Sqoop**

 - Export _table schema_ from PostgreSQL to Hive

   > sqoop create-hive-table --connect jdbc:postgresql://etu-master/hive --username hive -P --table nyse_dividends --hive-table etu203.nyse_dividends
    
 - Export _data from_ PostgreSQL to Hive

	> sqoop import --connect jdbc:postgresql://etu-master/hive --username hive -P --table nyse_dividends --hive-import --hive-table etu203.nyse_dividends -m 1

 - arguments:

    > **--connect < jdbc-uri >:** 	Specify JDBC connect string
    > **--driver < class-name >:** 	Manually sprcify JDBC driver class to use
    > **--help:**					Print usage instructions
    > **--P:**						Read password from console
    > **--password < password >:**	Set authentication passeord
    > **--username < username >:**	Set authentication username
    > **--verbose:**				Print more information while working
    > **--table < table-name >:**	Table to read
    > **--target-dir < dir >:**		HDFS destination dir
    > **--hive-table:**			Specify target table name in Hive
    > **--hive-import:**			Specify sqoop target to Hive
    > **-m	< n >:**					Use n map tasks to import in parallel

**Pig:**

 - script language
 - 指令用法整理
 
 > $ pig

 讀取baseball資料, position的資料型態為bag, bat 的資料型態為map
 >	grunt>	players = LOAD 'baseball' USING PigStorage ('\t') AS ( name:chararray, team:chararray, position:bag{t:(p:chararray)},bat:map[]);
				
 將position攤平 並從map中取得平均打擊率
 >	grunt>	pos = FOREACH players GENERATE name, FLATTEN(position) as position, bat#'batting_average' as batAvg;

 濾掉沒有打擊率的紀錄
 >	grunt>	batters = FILTER pos BY batAvg IS NOT NULL;

 依打擊/守備位置 grouping
 >	grunt>	byPos = GROUP batters BY position;
 
 算出各打擊/守備位置的平均打擊率
 >	grunt>	battingAvg = FOREACH byPos GENERATE group, AVG(batters.batAvg);
 
 依平均打擊率做排序
 >	grunt>	team_batavg = ORDER battingAvg BY $1;
	grunt>	DUMP team_batavg;
	
 將position攤平
 >	grunt>	pos = FOREACH players GENERATE name, FLATTEN(position) as position;
 
 只列出捕手 filter
 >	grunt>	catchers = FILTER pos BY posotion == 'Catcher';


**Hive:** 

 - use **SQL-like** command to manipulate data
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
	

----

**L1-V Data Visualization(3/20)**
---------
use `QlikView` to visualize data.

----

**Project with WeatherRisk**
---------


----

**L1-H HBase - NoSQL (3/27)**
---------
- **key concept:** _Column Family_

----

**Udacity: Intro to Computer Science (4/16~4/28)**
---------
- **goal:** use _python_ to built a search engine.

----

**EHC 員工內部大賽**
---------
- **Environment:** CentOS 6.5 minimal
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
 
 3. 新增`jps`指令
 於`.bashrc`中加入`alias jps='/usr/java/jdk1.7.0_55/bin/bin/jps'`
 > [root@localhost ~] vi ~/.bashrc

 4. 從 `Bigtop` 安裝 hadoop component (hadoop, pig, hive, zookeeper, hbase)
 > [root@localhost ~] wget -O /etc/yum.repos.d/bigtop.repo http://www.apache.org/dist/bigtop/stable/repos/[centos5|centos6|fedora15|fedora16]/bigtop.repo
 > [root@localhost ~] yum install -y hadoop\* pig\* hive\* zookeeper\* hbase\*

- An **exciting moment**!!!

 ![enter image description here][12]
- **Referance:** [jazz vagrant-hadoop][13] on github

----

**Etu Training L1-M: MapReduce (4/24-5/6)**
---------
- Write mapreduce programs in **java**
- Know the difference between **new** and **old** API
- Use **Combiner**, **partitioner**, **toolrunner**, and **distrubuted cache**

認證題目:
「以新版的 MapReduce API 寫一個 M/R 程式，算出每天的成交量總合，並且使用 3 個 Reducer 將這三個交易日期範圍歸到同一個 Reducer 下。」

view the [code][14] on github

give arguents in command line:
`/opt/hadoopmr/bin/hadoop jar [.jar] -D mapred.reduce.tasks=5 [input on HDFS] [output directory]`

----

**Data Visualization via Collaborative Filtering (5/25)**
---------

study the [thesis][15] and try to write some R codes, using the _movielens_ as dataset

**some preliminary results: 一些初步的成果**

1. plot1: Users and the correspond ratings on specific items.
`> qplot(user_factor,item_factor, data = ratings_100, colour=pref, size=pref)`
![item_factor & user_factor][16]

2. plot2: A biplot using **PCA** (principal component analysis) method to express the similarity of movies and characteristics.
`> biplot(cfpca,choice=1:2)`
![pca_biplot][17]

3. plot3: Project the result of PCA on a 2D plane, presenting the coordinate of each movie.
`> ggplot(d,	aes(x=PC1,	y=PC2))	+  geom_point()	+	  geom_text(aes(label=id),            size=3,	vjust=-0.5)`
![item_based_projection][18]


----

**Event List**
---------

> - 2/20 Etu ALL-hands Monthly, Feb.
> - 3/15 SITCON 2014
> - 3/28 Etu ALL-hands Monthly, Mar.
> - 4/11~4/12 OSDC
> - 4/29 中研院 陳昇瑋 研究員演講
> - 4/30 Etu ALL-hands Monthly, Apr.
> - 5/28 Etu All-hands Monthly, May.

----

> Written with [StackEdit](https://stackedit.io/).


  [1]: https://github.com/RevolutionAnalytics/RHadoop/wiki/Downloads
  [2]: http://goo.gl/UhrcbF
  [3]: http://goo.gl/UpK2y9
  [4]: http://goo.gl/UpK2y9
  [5]: https://github.com/RevolutionAnalytics/rhbase/blob/master/build/rhbase_1.2.0.tar.gz?raw=true
  [6]: http://michaelhsu.tw/2013/05/01/r-and-hadoop-%E5%88%9D%E9%AB%94%E9%A9%97/
  [7]: http://i.imgur.com/JN1SV1c.png
  [8]: https://github.com/alexholmes/hadoop-book/blob/master/src/main/R/ch8/stock_cma_rmr.R
  [9]: https://github.com/RevolutionAnalytics/RHadoop
  [10]: https://groups.google.com/forum/?hl=zh-TW#!forum/rhadoop
  [11]: https://groups.google.com/forum/#!topic/rhadoop/S02_moZEsI4
  [12]: https://lh3.googleusercontent.com/7z0OTqBOoZSuvdVPYAZ7PgPC3_0pHAeLDzXZCGqrkoI=s500 "882109_10200805859548553_1933855539414159678_o.jpg"
  [13]: https://github.com/jazzwang/vagrant-hadoop/blob/master/bigtop-aws/ubuntu/provision.sh
  [14]: https://github.com/yenzichun/StockVolume
  [15]: http://hal.archives-ouvertes.fr/docs/00/67/33/30/PDF/visualCF.pdf
  [16]: https://lh6.googleusercontent.com/JwDvKdwbpmrezwIDYjQ1hbP8fkH_MWPOMzyZMNvP1dQ=s500 "item&user_biplot.jpeg"
  [17]: https://lh3.googleusercontent.com/_OIFCqtOg_rinSmKXrMdl0DLGF_UMjRdwxMo-mJVzHc=s500 "CFpca.jpeg"
  [18]: https://lh5.googleusercontent.com/d4KwdqEV_viL3FmbaRnT9tpsjc70HbN2npSjLrvKohs=s500 "item_based_projection.jpeg"