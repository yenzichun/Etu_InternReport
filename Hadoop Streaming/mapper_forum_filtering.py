#!/usr/bin/python
import sys
import csv

# To run this code on the actual data, please download the additional dataset.
# You can find instructions in the course materials (wiki) and in instructor comments.
# There are some things in this data file that are different from what you saw
# in Lesson 3. This dataset is more complicated, and closer to what you
# would see in the real world. It was generated by exporting data from
# a SQL database.
# Since the data in at least one of the fields (the body field) can include new lines,
# and all the fields are enclosed in double quotes,
# you should use a less naive way of processing the data file (instead of split(",")).
# We have provided sample code on how to use the csv module of Python.
# "line" in this case will be an array that contains all the fields
# similar to using split in the previous lesson.
###########################################################################
# In this exercise you are interested in the field "body" which is the 5th field.
# Find forum nodes where "body" contains only one sentence.
# We define sentence as a "body" that contains either none of the following
# 3 punctuation marks ".!?" , or only one of them as the last character in the body.
# You should not parse the HTML inside body, or pay attention to new lines.

for line in sys.stdin:

    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        
        body = line[4]
        def one_sentence():
            #print body
            ends = body.endswith("!") or body.endswith("?") or body.endswith(".")
            r_contains = max(body.rfind("?"), body.rfind("."), body.rfind("!"))
            max_contains = max(body.find("?"), body.find("."), body.find("!"))
            min_contains = min(body.find("?"), body.find("."), body.find("!"))
            if(ends==False and max_contains==-1):
                return True            
            #elif (ends==True and (max_contains==r_contains) and (min_contains<0) ):
            elif (ends ==True and (max_contains==r_contains) and (min_contains<0) ):
                return True
            else:
                return False
        #print body
	one_sentence()
        
        if(one_sentence()==True):
            writer.writerow(line)
	    #print(line)
	
