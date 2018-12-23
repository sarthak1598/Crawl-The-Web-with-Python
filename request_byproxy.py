
# This script can be used to make a http request with the web server using free proxies 

# This method can be usefull in the case when the request is to be made on restriced site . 

# As it will request through proxy on behalf of scraper 

# imported requests module
import requests

url = raw_input("Please enter the url of the webpage")
# defining the freely available proxy servers list to be use by the script.

proxies = {
    "http": 'http://209.50.52.162:9050', 
    "https": 'http://209.50.52.162:9050'
}
response = requests.get(url,proxies=proxies) # proxy request to server 

print(response.json()) # printing the http response data in json format to test. 

# program ends
