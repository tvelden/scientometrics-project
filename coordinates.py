import csv
from googlemaps import GoogleMaps
gmaps=GoogleMaps(api_key='')
##fi = open('half_countries.csv', 'rb')
##data = fi.read()
##fi.close()
i=1
##fo = open('countries_excel.csv', 'wb')
##fo.write(data.replace('\x00', ''))
##fo.close()
import time
fo=open('final_coordinates.csv','wb')
csvWriter = csv.writer( fo )  #Defaults to the excel dialect

import csv, sys
filename = 'countries.csv'
with open(filename, 'rb') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            line=list()
            line=row
            print i
            
            if not line:
                print
            else:
                line=list()
                line=row[0].split(',')
                time.sleep(1)
                for country in line:
                    address=country
                    lat, lng=gmaps.address_to_latlng(address)
                    lat_list=list()
                    lat_list.append(i)
                    lat_list.append(row[0])
                    lat_list.append(lat)
                    lat_list.append(lng)
                    csvWriter.writerow(lat_list)
                    #print lat_list
            i=i+1
                
    except csv.Error, e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))



