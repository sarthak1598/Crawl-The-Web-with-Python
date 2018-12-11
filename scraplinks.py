
#code to extract the webpage links 

import bs4 
import requests

url = raw_input("Enter the name of site to extract out the url links : ")  #input from the user as the address/url of the web-page

r  = requests.get("http://" +url) # initialised the r object as to make a remote request with the web url 

edata = r.text

soup = BeautifulSoup(edata) 

for link in soup.find_all('a'):  # simply used for the pattern matching for extracting out the nessecory links.
    print(link.get('href'))  # prints all of the response .
