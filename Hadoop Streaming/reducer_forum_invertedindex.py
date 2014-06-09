#!/usr/bin/python

import sys
oldWord = None
wordCount = 0
wordIndex = []

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    #print len(data_mapped)
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    
    #for practice3    
    thisWord, thisIndex = data_mapped
    #print thisWord,thisIndex
    #print thisWord
    if oldWord and oldWord != thisWord:
	wordIndex.sort()
	print oldWord, "is", wordCount, " index:",wordIndex
	wordCount = 0
	wordIndex = []
	oldWord = thisWord
	
    wordCount += 1
    #for thisIndex in wordIndex:
    if int(thisIndex) not in wordIndex:
    	wordIndex.append(int(thisIndex))
	#wordIndex.sort()
    #wordIndex.append(thisIndex)
    oldWord = thisWord
    
if oldWord != None:
    print thisWord, "is", wordCount, " index:",wordIndex
