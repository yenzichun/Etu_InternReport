#!/usr/bin/python

import sys
oldKey = None
meanValue = 0
salesTotal = 0
saleCount = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped   

    if oldKey and oldKey != thisKey:
	meanValue = float(salesTotal)/saleCount
	#print salesTotal, saleCount
	print "weekday:", oldKey,"\t", "meanValue:", meanValue
	oldKey = thisKey
	oldSale = thisSale
	saleCount = 0
	salesTotal = 0
		
    oldKey = thisKey
    oldSale = thisSale

    salesTotal += float(thisSale)
    saleCount += 1


if oldKey != None:
    meanValue = float(salesTotal)/saleCount
    print "weekday:", thisKey,"\t", "meanValue:", meanValue
    #print salesTotal, saleCount
    #print "# of sales:", saleCount, "\t", "Total of Sales:", salesTotal
