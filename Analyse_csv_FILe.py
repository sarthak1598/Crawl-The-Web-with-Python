
# This python code i used to write for analysing and customizing the csv(comma , seperated values) file ad directed by the requirement



import csv # csv library for manipulation of csv file 

import sys
 # opening the file object 
file = open(sys.argv[1], ‘rb’)
reader = csv.reader(file)  # initialised object 

for row in reader
print row   # printing the data 
 
f.close()

#program ends
