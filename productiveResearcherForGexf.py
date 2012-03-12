
import pprint, pickle
from operator import itemgetter
import operator
import math
from xml.dom.minidom import parse
import os

def printDict():
        global ArticleDict
	
        for key,value in ArticleDict.items():
                print(key + '::::::::::::')
                print(len(value))
                print(value.pop())

def readline(line):
	
	global writer
	global ArticleDict
	global CurrentIndex
	global CurrentID
	global CurrentCategoryList
	
	line = line.replace("\n","")
	
	if len(line.partition(" ")[0]) == 2:
		CurrentIndex = line.partition(" ")[0]

		
		
	if(CurrentIndex=='ID'):
		if CurrentCategoryList:
			CurrentCategoryList.remove('')
			ArticleDict[CurrentID]=CurrentCategoryList
			
		CurrentID =line[3:]
		CurrentCategoryList = list()
	
	if(CurrentIndex=='CA'):
		CurrentCategoryList.append(line[3:].lower().strip())



def readfile(filename):
	'''comfirm the file name '''
	inputfile=file(filename)
			
	while True:
		line = inputfile.readline()
		if len(line)==0:
			break
		else:
			readline(line)
			
	inputfile.close()
	

def MakeEachAuthorGexfFile(rank, authorName, listItem):
        f = open('list.txt', 'r')
        sequenceCA = {}
        sequence = 1
        listCA = {}

        while True:
                line = f.readline()
                if len(line)==0:
                        break
                else:
                        keys = line.split("\"")
                        listName = str(keys[1]).strip()
        ###### make a dictionary key: value = (CA name : # of article)
                        sequenceCA[sequence] = str(listName).lower()
                        listCA[str(listName).lower()] = 0
                        sequence += 1
        f.close()

        
        for item in listItem:
                if item in ArticleDict:                        
                        for ca in ArticleDict[item]:
                                if ca in listCA:
                                        listCA[ca] = listCA[ca] + 1

        ####make vec file for each key
        authorNameSep = authorName.split(",")
        #author = authorNameSep[0],"_",authorNameSep[1]
        filename = str(str(rank) + authorNameSep[0]+'_' + authorNameSep[1]+ '.gexf')
        new_file_name = 'test.gexf'
        doc = parse('test.gexf')
        nodes = doc.getElementsByTagName('viz:size')

        for key, value in sequenceCA.items():
            index = int(key) -1
            if listCA[value] == 0:
                nodes[index].setAttribute("value", "0")
            else:                       
                logValue = math.log10(listCA[value])
                nodes[index].setAttribute("value", str(logValue))
                #print sequenceCA[key], ':', str(logValue)
                
        xml_file = open(filename, "w")
        doc.writexml(xml_file, encoding="utf-8")
        xml_file.close()

        print filename, 'is done for', authorName
        
        f.close()        


############################
ArticleDict = {}

CurrentIndex = ''
CurrentID = ''
CurrentCategoryList = list()

inputfilename = 'in.txt'
readfile(inputfilename)


#for key, value in ArticleDict.items()[0:2]:
#        print key,':', value       


#########################
data1 = pickle.load(open('authorname-noderole.pck','rb'));
data2 = pickle.load(open('authornames-articleids.pck','rb'));


# get all authors from authorname-noderrole pck
AuthorsOnBoardDict={}

# for every author find out the dict items in authorname-articleids.pck
for key,value in data1.items():
        AuthorsOnBoardDict[key]= len(data2[key])


# sort author dictionary        
items = AuthorsOnBoardDict.items()
items.sort(key=operator.itemgetter(1),reverse=True)

# get the author candidates(top 10!)
authorCandidates_articles = {}
authorRank={}
i=1;

for key,value in items:
        if i>10:
                break
        authorRank[i]=key;
        authorCandidates_articles[key]=data2[key]
        i=i+1


for key, value in authorRank.items():
    authorName = authorRank[key]
    MakeEachAuthorGexfFile(key, authorRank[key], authorCandidates_articles[authorName])

############################

