#!/usr/bin/python
# Filename: MakeVecFile.py

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

while True:
    line = f.readline()
    if len(line) == 0:
        break
    else:
        if len(line.partition(" ")[0]) == 2:
            CurrentIndex = line.partition(" ")[0]
            #print CurrentIndex
            if CurrentIndex == 'CA':
                #print str(line.partition(" ")[2]).strip()
                field = str(line.partition(" ")[2]).strip()
                listCA[field.lower()] = listCA[field.lower()] + 1
f.close()
#for key, value in listCA.items():
#    print key + ":" + str(value)

#### make vec file

f = open('static.vec', 'w')

f.write("\n")
f.write("*Vertices " + str(sequence-1) + "\n")
count = 1
for key, value in sequenceCA.items():
    print listCA[value]
    f.write(str(listCA[value]) + "\n")
f.close()
