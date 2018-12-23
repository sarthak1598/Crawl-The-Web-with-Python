

# This is basic script using iterative programming logic to save the extracted data from  the requested domain in the file in
# the hard drive as raw data and returns a content length in bytes

# Specific function used in scraping: 

# used basic file handling operation in python 
import requests
    url = raw_input("enter the web url")
    response = requests.get(url)
    
    response.raise_for_status()
    
    savefile = open('raw_data.txt', 'wb') # opened the new file to hold the extracted data 
    
    for chunk in res.iter_content(100000): # assumed data size in bytes to be loaded into the file
        savefile.write(chunk) # writing the data to the file 
        
    savefile.close() # closing the file
        
 # program ends 
        
        
