import csv, sys
from collections import *
import urllib
import re
from operator import itemgetter
import operator
import itertools


filename = open('C:\Users\Sneha\Desktop\me.txt','rb')
while 1:
    data=filename.readline()
    data=data.split("   ",",")
    print data
    data=re.findall("(\"[0-9]*\")",data)
    if len(data)>0:
     print data
