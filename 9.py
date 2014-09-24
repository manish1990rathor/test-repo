#!/usr/bin/python
import re
print"hello world"
ahappy=0
acrook=0
asurprised=0
aneutral=0
asarcastic=0
asad=0
aangry=0
fh= open("content.txt","r")
while 1:
	line = fh.readline()
	c= line[:1]
	if c=="A":
		
		searchObj = re.search( r':[)]', line, re.M|re.I)
		if searchObj:
			print "A is happy: ", searchObj.group()
			ahappy=ahappy+1
		
		searchObj = re.search( r':P', line, re.M|re.I)
		if searchObj:
			print "A is sarcastic: ", searchObj.group()
			asarcastic=asarcastic+1
	
		searchObj = re.search( r':[(]', line, re.M|re.I)
		if searchObj:
			print "A is sad: ", searchObj.group()
			asad=asad+1
		
		searchObj = re.search( r':-o', line, re.M|re.I)
		if searchObj:
			print "A is surprised: ", searchObj.group()
			asurprised=asurprised+1
		
		searchObj = re.search( r'B-[)]', line, re.M|re.I)
		if searchObj:
			print "A is crook: ", searchObj.group()
			acrook=acrook+1
		
		searchObj = re.search( r':-/', line, re.M|re.I)
		if searchObj:
			print "A is neutral: ", searchObj.group()
			aneutarl=aneutral+1
		
		searchObj = re.search( r'x-[(]', line, re.M|re.I)
		if searchObj:
			print "A is angry: ", searchObj.group()
			aangry=aangry+1
		
		searchObj = re.search( r':D', line, re.M|re.I)
		if searchObj:
			print "A is happy: ", searchObj.group()
			ahappy=ahappy+1
		
		searchObj = re.search( r';[)];[)]', line, re.M|re.I)
		if searchObj:
			print "A is sarcastic: ", searchObj.group()
			asarcastic=asarcastic+1
		
		searchObj = re.search( r'O_O', line, re.M|re.I)
		if searchObj:
			print "A is surprised: ", searchObj.group()
			asurprised=asurprised+1
		
		searchObj = re.search( r';[)]', line, re.M|re.I)
		if searchObj:
			print "A is crook: ", searchObj.group()
			acrook=acrook+1
		
		searchObj = re.search( r'=_=', line, re.M|re.I)
		if searchObj:
			print "A is neutral: ", searchObj.group()
			aneutral=aneutarl+1
		
		searchObj = re.search( r'>_<', line, re.M|re.I)
		if searchObj:
			print "A is angry: ", searchObj.group()
			aangry=aangry+1		
		
#	print c
	
	if not line:
 	      break	
#	print line
print ahappy
print acrook
print asurprised
print aneutral
print asarcastic
print asad
print aangry
atotal=0
atotal=ahappy+acrook+asurprised+aneutral+asarcastic+asad+aangry
print "percentage of happy mood",(ahappy*100.0)/atotal
print "percentage of sad mood",(asad*100.0)/atotal
print "percentage of Sarcastic mood",(asarcastic*100.0)/atotal
print "percentage of Neutral mood",(aneutral*100.0)/atotal
print "percentage of angry mood",(aangry*100.0)/atotal
print "percentage of Surprised mood",(asurprised*100.0)/atotal
print "percentage of Crook mood",(acrook*100.0)/atotal



