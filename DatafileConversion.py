#!/usr/bin/python
# Filename: DocfileConversion.py

import sys
import csv




# the index order is : ID- CI- SO- TI- BI- AU- AF- CT- CO- RF

def initDict():
	global ArticleDict
	ArticleDict = { 'ID' : '',
		             'CI': '',
		             'SO': '',
		             'TI': '',
		             'BI': '',
		             'AU': '',
		             'AF': '',
		             'CT': '',
		             'CO': '',
		             'RF': '',
		 			 'CA':''}


def print_dict(Adict):
    """ 
    print dictionary
    """ 
    for key,value in Adict.items():
        print(key + ':' + value)


def readline(line):
	
	global writer
	global ArticleDict
	global CurrentIndex
	
	if(CurrentIndex=='AU'):
		line = line.replace(",","")
	
	if len(line.partition(" ")[0]) == 2:
		CurrentIndex = line.partition(" ")[0]
		if(CurrentIndex=='AU'):
			line = line.replace(",","")
		#print"CurrentIndex:"+CurrentIndex
		if len(line.partition(" ")[0]) == 2:
			CurrentIndex = line.partition(" ")[0]
			#print"CurrentIndex:"+CurrentIndex

			if CurrentIndex == "ID":
			#	print_dict(ArticleDict)
				if ArticleDict['ID']!='':
					writer.writerow([ArticleDict['ID'],ArticleDict['CI'],ArticleDict['SO'],ArticleDict['TI'],ArticleDict['BI'],ArticleDict['AU'],ArticleDict['AF'],ArticleDict['CT'],ArticleDict['CO'],ArticleDict['RF'],ArticleDict['CA']])
									
				initDict()
			#	ArticleDict['ID']= line.partition(" ")[2]

			if len(ArticleDict[CurrentIndex])<1:
				ArticleDict[CurrentIndex]= line[3:]	
			else:
				ArticleDict[CurrentIndex]=ArticleDict[CurrentIndex]+','+line[3:]

			

	else:
			#print 'CurrentIndex: '+CurrentIndex,
		#	print "ArticleDict["+CurrentIndex+"]:"+ArticleDict[CurrentIndex]
		if line.isspace():
			pass
		else:
			ArticleDict[CurrentIndex]=ArticleDict[CurrentIndex]+','+line
#		print "ArticleDict["+CurrentIndex+"]after :"+ArticleDict[CurrentIndex]

		

			
#	if len(line.partition(" ")[0]) == 2:
#	       CurrentIndex = len(line.partition(" ")[0]
#	
#	if CurrentIndex == 'ID':
#		Article.clear()
#		Article['ID']= line.partition(" ")[2]
#		print Article['ID'],
	
	


def readfile(filename):
	'''comfirm the file name '''
	inputfile=file(filename)
	outputfilename=filename.partition(".")[0]+".csv"
	
	outputfile = file(outputfilename,'w')
	outputfile.close()
	
	global writer
	
	print 'Start reading the file: %s, please wait for a second...'%filename

	writer.writerow(["ID","CI","SO","TI","BI","AU","AF","CT","CO","RF","CA"])
	
	# the index order is : ID- CI- SO- TI- BI- AU- AF- CT- CO- RF	
	
	while True:
		line = inputfile.readline()
		if len(line)==0:
			break
		else:
			readline(line)
			

	inputfile.close()
	print 'Finish!!! Cheers!The out put file is:------>'+outputfilename,
	
# Script starts

	
argvlength = len(sys.argv)
print 'argv len is %d'%argvlength

ArticleDict = { 'ID' : '',
	             'CI': '',
	             'SO': '',
	             'TI': '',
	             'BI': '',
	             'AU': '',
	             'AF': '',
	             'CT': '',
	             'CO': '',
	             'RF': '',
	 			 'CA':''}

CurrentIndex = ''


if  sys.argv[1].endswith('.txt'):
	print 'input is ok, the arg is %s'%sys.argv[1]
	inputfilename = sys.argv[1]
	writer = csv.writer(open(inputfilename.partition(".")[0]+".csv","w"))
	readfile(inputfilename)
	
else: 
		print 'input is not correct',
		sys.exit()