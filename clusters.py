import csv, sys
filename = 'id_Ref.csv'
flag=0
count1=list()
dict1=dict()
with open(filename, 'rU') as f:
   reader = csv.reader(x.replace('\0', '') for x in f)
   
   for row in reader:
       flag1=0
       id1=list()
       id1=row[0].split('\n')
       ref=list()
       ref=row[1].split('\n,')
       word=ref[len(ref)-1]
       word1=list()
       word1=word.split('\n')
       ref[len(ref)-1]=word1[0]

       if flag==0:
           dict1[id1[0]]=ref
           flag=1

       else:
           for key,value in dict1.iteritems():
               if id1[0] not in value:
                   flag1=0
               elif id1[0] in value:
                   flag1=1
                   #print ""
                   break
           if flag1==0:
               dict1[id1[0]]=ref
               
    


count=0
#print dict1
for k,v in dict1.iteritems():
    #print v
    count1.append(len(v))
    count=count+1

count1.sort(reverse=True)
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

fo=open('top_eight_clusters.csv','wb')
csvWriter = csv.writer( fo )  #Defaults to the excel dialect
for k, v in new_dict.iteritems():
    temp=list()
    temp.append(k)
    temp.append(v)
    csvWriter.writerow(temp)



