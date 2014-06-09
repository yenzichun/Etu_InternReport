#!/usr/bin/python

import sys

salesTotal = 0
biggerSales = 0
oldKey = None
oldSale = 0 # for practice2
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
        """
	print oldKey, "\t", salesTotal
        oldKey = thisKey;
	salesTotal = 0
	"""
	"""
	# for practice2
	print oldKey, "\t", biggerSales
	oldKey = thisKey;
	oldSale = 0
	biggerSales = 0
        """
	
		
    oldKey = thisKey
    oldSale = thisSale    

    #salesTotal += float(thisSale)
    """
    #for practice2
    biggerSales = max(float(thisSale),float(biggerSales))
    """
    """
    if thisSale > biggerSales :
	#print "ts is" ,thisSale,"bs is",biggerSales
	biggerSales = thisSale
	#print "after update: now thisSale is",thisSale,"biggerSales is",biggerSales
    else:
    	#print "at this time thisSale is",thisSale,"biggerSales is",biggerSales 
	#print "no change"
	biggerSales = oldSale
    """
    #for practice3
    salesTotal += float(thisSale)
    saleCount += 1


if oldKey != None:
    """
    print oldKey, "\t", salesTotal
    """
    """
    #for practice2
    #print "here outside the loop, now thisSale is",thisSale,"biggerSales is",biggerSales
    if oldSale > biggerSales:
    	biggerSales = oldSale
    print oldKey, "\t", biggerSales
    """
    #for practice3
    print "# of sales:", saleCount, "\t", "Total of Sales:", salesTotal
