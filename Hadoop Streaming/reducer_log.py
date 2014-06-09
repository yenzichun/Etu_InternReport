#!/usr/bin/python

import sys

hitCounter = 0
ipCounter = 0
oldPath = None
oldIp = None
path = None
popularHit = 0
popularPath = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    
    if len(data_mapped) != 1:
        # Something has gone wrong. Skip this line.
        continue
    #for practice1
    """
    thisPath = data_mapped
    #print thisPath
   #if thisPath == ['/assets/js/the-associates.js']:
    if oldPath and oldPath != thisPath:
	print "hitCount from ", oldPath, "is", hitCounter
	hitCounter = 0
    
    hitCounter += 1	
    oldPath = thisPath	
    
if oldPath != None:
    #for practice1
    print "hitCount from ",thisPath, "is", hitCounter
    """	
    #for practice2
    """
    thisIp = data_mapped
    if oldIp and oldIp != thisIp:
    	print "ip from ", oldIp, "is ", ipCounter
	ipCounter = 0
    ipCounter += 1
    oldIp = thisIp

if oldIp != None:
    print "ipCount from ",thisIp, "is", ipCounter
    """
    #for practice3    
    thisPath = data_mapped
    #print thisPath
    
    if thisPath == ['/assets/css/combined.css']:
       	hitCounter += 1
	path = thisPath
    """
    if oldPath and oldPath != thisPath:
	print "hitCount from ", oldPath, "is", hitCounter
	
	if int(hitCounter) > int(popularHit):
		popularHit = hitCounter
		popularPath = oldPath
	
	#popularHit = max(int(popularHit),int(hitCounter))
	hitCounter = 0
    """
    #hitCounter += 1	
    oldPath = thisPath
    #popularHit = hitCounter
    #popularPath = thisPath	
    
if oldPath != None:
    print "hitCount from ",path, "is", hitCounter
    #popularHit = max(int(popularHit),int(hitcounter))
    #print "the most popular website is: ", popularPath, "\nand the hitCount is: ", popularHit
