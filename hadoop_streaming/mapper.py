#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        """original code
	print "{0}\t{1}".format(store, cost)
	"""
	#for practice1
	#print "{0}\t{1}".format(item, cost)
	
	#for practice2
	#print "{0}\t{1}".format(store, cost)
	
	#for practice3
	print "{0}\t{1}".format(store, cost)

