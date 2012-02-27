import pprint, pickle
from operator import itemgetter

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
	
def getSortedKey(dict):
        print "Dict length: ", len(dict)
        DictKeyCount = {}
        for key, value in data1.items():
                DictKeyCount[key] = len(data1[key])

        #for key, value in DictKeyCount.items():
        #        print key, ":", value

        #print sorted(DictKeyCount.values())

        s = sorted(DictKeyCount.items(), key=itemgetter(1))
        s.reverse()

        sortedListKey = []
        for a, b in s[0:8]:
                sortedListKey.append(a)

        return sortedListKey

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

#for key, value in sequenceCA.items():
#        print key, ':', value

pkl_file = open('area-articleIDs.pck', 'rb')

data1 = pickle.load(pkl_file)
pkl_file.close()
#pprint.pprint(data1)

listKey = getSortedKey(data1)



############################
ArticleDict = {}

CurrentIndex = ''
CurrentID = ''
CurrentCategoryList = list()

inputfilename = 'in.txt'
readfile(inputfilename)


#for key, value in ArticleDict.items()[0:2]:
#        print ArticleDict[key]        




############################
List8topic = []
for key in listKey: 
        List8topic.append(data1[key])

for a in List8topic:
        for item in a:
                if item in ArticleDict:                        
                        for ca in ArticleDict[item]:
                                if ca in listCA:
                                        listCA[ca] = listCA[ca] + 1
                                else:
                                        test += 1
                                        print ca

for key, value in listCA.items():
        print key + ":" + str(value)

#### make vec file                        
f = open('static.vec', 'w')

f.write("\n")
f.write("*Vertices " + str(sequence-1) + "\n")
count = 1

for key, value in sequenceCA.items():
    #getcontext().prec = 8
    #n = Decimal(listCA[value])/Decimal(totalarticle)
    #print n
    #f. write(str(n) + "\n")
    f.write(str(listCA[value]) + "\n")
    print str(listCA[value])
f.close()
                






