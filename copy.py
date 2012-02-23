import csv
from googlemaps import GoogleMaps

##fo = open('countries_excel.csv', 'wb')
##fo.write(data.replace('\x00', ''))
##fo.close()
import time
fo=open('project_excel.csv','wb')
csvWriter = csv.writer( fo )  #Defaults to the excel dialect
i=1;
import csv, sys
filename = 'countries_excel.csv'
with open(filename, 'rb') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            line=list()
            line=row
            #print row
            if not line:
                print
            else:
                great=list()
                countries=list()
                countries=line[0].split(',')
                for country in countries:
                    great.append(i)
                    great.append(row)
                    csvWriter.writerow(great)

            i=i+1
                   
                
    except csv.Error, e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))



