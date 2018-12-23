
# this program/script is using requests and bs4 modules in python 
# This code is written to scrape a html content from the webpage passed into the code


import requests 
import sys
from bs4 import BeautifulSoup 
  
URL = raw_input("Please enter the web url here)

reqobject = requests.get(URL)  # performing the http get requst to the web server 
   
soup = BeautifulSoup(reqobject.content, 'html5lib') 

print(reqobject.status_code) # prints the HTTP response status code got by the web server 

# while reqobject.content : this consists of the raw html data.

print(reqobject.prettify())  # present the parsed tree from the response 

# program ends
