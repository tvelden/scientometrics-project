##import jsonpickle
##f=open('C:\Users\chitrita\Desktop\maps\our_project\pickle1.pck')
##json_str=f.read()
##obj = jsonpickle.encode(json_str)
##
##for k,v in obj:
##    
##    print obj
##    break
import pickle
import csv, sys
dict1 = pickle.load( open( "pickle1.pck", "rb" ) )


count=0
#print dict1
count1=list()
for k,v in dict1.iteritems():
    #print v
    #type(v)
    count1.append(len(v))
    count=count+1

count1.sort(reverse=True)
print"great"

new_count1=list()
for i in range(0,8):
    new_count1.append(count1[i])
    
new_dict=dict()
count2=0
for k,v in dict1.iteritems():
    if len(v) in new_count1:
        new_dict[k]=v
        count2=count2+1
    

print count2
first_list_ref=list()
for k, v in new_dict.iteritems():
    first_list_ref=v
    print len(v)
    break
    
print first_list_ref[0]


filename = 'list_ids.csv'
list_of_numbers=list()
count3=0
with open(filename, 'rb') as f:
   reader = csv.reader(f)
   for row in reader:
       count3=count3+1
       temp1=list()
       temp1=row[0].split('\n')
       #print temp1[0]
       if temp1[0] in first_list_ref:
           list_of_numbers.append(count3)
           

print "great"
fo=open('first_cluster.csv','wb')
csvWriter=csv.writer(fo)
print list_of_numbers[0]

fo1='cities_coordinates.csv'
with open(fo1, 'rb') as f:
   reader = csv.reader(f)
   for row in reader:
       if int(row[0]) in list_of_numbers:
           #print "entered"
           csvWriter.writerow(row)



##fo=open('final_eight_clusters.csv','wb')
##csvWriter = csv.writer( fo )  #Defaults to the excel dialect
##for k, v in new_dict.iteritems():
##    temp=list()
##    temp.append(k)
##    temp.append(v)
##    csvWriter.writerow(temp)


##i=0
##line1=list()
##fi='final_eight_clusters.csv'
##with open(fi, 'rb') as f:
##   reader = csv.reader(f)
##   for row in reader:
##       #print row[1]
##       print len(row[1])
##       line1.append(row[1])
##       i=i+1
##       #print len(row[1])
##       if i==7:
##           break
