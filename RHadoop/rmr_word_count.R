#my1mapper
#R-like
small.ints = 1:10
sapply(small.ints, function(x) x^2)
#mr_equivalent
small.ints = to.dfs(1:1000)
mapreduce(
  input = small.ints,
  map = function(k,v) cbind(v, v*2)
  )
from.dfs("/tmp/RtmpxvmpVk/filec31559c11d5")
from.dfs(small.ints)

#my1reducer
#R-like
groups = rbinom(32, n = 50, prob = 0.4)
tapply(groups, groups, length)
#mr_equivalent
groups = to.dfs(groups)
from.dfs(
  mapreduce(
    input = groups, 
    map = function(., v) keyval(v, 1), 
    reduce = function(k, vv) keyval(k, length(vv))
    )
)

#word_count
library(rmr2)
wordcount = function(){
  wc.map = function(k,v) {
    keyval(k,1)
  }
  wc.reduce = function(word, counts){
    keyval(word, sum(counts))
  }
  mapreduce(
    input = "word_count_data",
    output = "word_count_result",
    input.format = make.input.format("text", sep = " "),
	output.format = "text",
    map = wc.map,
    reduce = wc.reduce
	)
}

wordcount()


#old version
wordcount = 
  function(
    input, 
    output = NULL, 
    pattern = " "){
    wc.map = 
      function(., lines) {
        keyval(
          unlist(
            strsplit(
              x = lines,
              split = pattern)),
          1)}
    wc.reduce =
      function(word, counts ) {
        keyval(word, sum(counts))}
    mapreduce(
      input = groups,
      output = output,
      input.format = "text",
      map = wc.map,
      reduce = wc.reduce,
      combine = T)}





