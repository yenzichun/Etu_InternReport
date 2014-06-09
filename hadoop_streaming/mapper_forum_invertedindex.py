#!/usr/bin/python
import sys
import csv
import re
from string import translate, maketrans, punctuation


for line in sys.stdin:
    
    reader = csv.reader(sys.stdin, delimiter='\t')

    for line in reader:
    	body = line[4]
	node = line[0]
    	
    	#myList2 = body.strip().replace('<',' ').replace('>',' ')....split(' ')
    	# .!?:;"()<>[]#$=-/
    	#myList2 = re.findall(r"[\w]+",body)
    	#myList2 = re.split('[ .!?:;()<>\[\]#$/=-]',body)
	#del_char = ['',' ','\n']
	#myList2 = [ele for ele in myList2 if ele not in del_char]
    	T = maketrans(punctuation, ' '*len(punctuation)).lower()	
    	myList2 = translate(body, T).split()
    	
	
    	for element in myList2:
	    
	    #print "%s\t%s\t%s" % (element,1,node)
	    print "%s\t%s" % (element,node)
	    #print "%s\t%s" % (node, element)
	
	
    	
	
    	
    #reader = csv.DictReader(sys.stdin, delimiter='\t')

    #writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    

    
    
    
    #writer.writerow(line)
    
	
