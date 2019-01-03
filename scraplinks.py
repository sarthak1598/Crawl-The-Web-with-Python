
# code to extract the webpage links and other information 

import bs4 
import requests

import urllib
url = raw_input("Enter the name of site to extract out the url links : ")  #input from the user as the address/url of the web-page

r  = requests.get("http://" +url) # initialised the r object as to make a remote request with the web url 

edata = r.text

soup = BeautifulSoup(edata) 

for link in soup.find_all('a'):  # simply used for the pattern matching for extracting out the nessecory links.
    print(link.get('href'))  # prints all of the response .
    
 # adding the code for extracting the divisions of the html webpage whose url is passed into the funtion

ht= urllib.urlopen(url)
html_page = ht.read()

b_object = BeautifulSoup(html_page)

data = b_object.find('div', id ='notice')  # finding div tags in html page 
print (data)

# ends 
