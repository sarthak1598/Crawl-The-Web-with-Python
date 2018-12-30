
# This python code i used to write for analysing and customizing the csv(comma , seperated values) file ad directed by the requirement



import csv # csv library for manipulation of csv file 

import sys
 
file = open(sys.argv[1], ‘rb’)
reader = csv.reader(f)

for row in reader
print row
 
f.close()

#program ends
