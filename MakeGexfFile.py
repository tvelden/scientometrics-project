import pprint, pickle
from xml.dom.minidom import parse
import os
import math


#########################################
#### readfile to get the list of CA
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
        #print listName
        ###### make a dictionary key: value = (CA name : # of article)
        sequenceCA[sequence] = str(listName).lower()
        listCA[str(listName).lower()] = 0
        sequence += 1
f.close()

#for key, value in listCA.items():
#    print key + ":" + str(value)

#for key, value in sequenceCA.items():
#    print str(key) + ":" + value

####### read in.txt to save the # of article to each CA
f = open('in.txt', 'r')
totalarticle = 0
while True:
    line = f.readline()
    if len(line) == 0:
        break
    else:
        if len(line.partition(" ")[0]) == 2:
            CurrentIndex = line.partition(" ")[0]
            if CurrentIndex == 'ID':
                totalarticle += 1
            #print CurrentIndex
            if CurrentIndex == 'CA':
                #print str(line.partition(" ")[2]).strip()
                field = str(line.partition(" ")[2]).strip()
                if field.lower() in listCA:
                    listCA[field.lower()] = listCA[field.lower()] + 1
f.close()
#for key, value in listCA.items():
#    print key + ":" + str(value)



# create a backup of original file
new_file_name = 'test.gexf'
old_file_name = new_file_name + "~"
#os.rename(new_file_name, old_file_name)
# change text value of element
doc = parse('test.gexf')
nodes = doc.getElementsByTagName('viz:size')



for key, value in sequenceCA.items():
    index = int(key) -1
    if listCA[value] == 0:
        nodes[index].setAttribute("value", "0")
    else:                       
        logValue = math.log10(listCA[value])
        nodes[index].setAttribute("value", str(logValue))
        print sequenceCA[key], ':', str(logValue)



#nodes[0].setAttribute("value","100.0")
#print nodes[0].getAttribute("value") 
#node[0].firstChild.nodeValue = 'bar'


# persist changes to new file
xml_file = open('field1.gexf', "w")
doc.writexml(xml_file, encoding="utf-8")
xml_file.close()






##########################################################################################





