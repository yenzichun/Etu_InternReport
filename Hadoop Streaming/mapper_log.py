#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
for line in sys.stdin:
    data = line.strip().split(" ")
    #print len(data)
    
    if len(data) == 10:
	ip, id_client, usr_client, time, zone, method, path, protocol, status, object_size = data  #data is in array form	
    	#for practice1
	#print "{0}".format(path)

	#for practice2
	#print "{0}".format(ip)
	
	#for practice3
	print "{0}".format(path)
