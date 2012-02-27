import csv, sys
from collections import *
from numpy import *
filename = 'first_cluster.csv'
flag=0
count1=list()
dict1=dict()
fi=open('first_cluster_citiescount.csv','wb')
csvWriter=csv.writer(fi)
lat=list()
with open(filename, 'rb') as f:
   reader = csv.reader(f)
   for row in reader:
       #print row[2]
       lat.append(row[2])

cnt=Counter()
print len(lat)
for word in lat:
    cnt[word]+=1


with open(filename, 'rb') as f:
   reader = csv.reader(f)
   for row in reader:
       temp=list()
       temp=row
       temp.append(log(cnt[row[2]])+1)
       csvWriter.writerow(row)


      
    



