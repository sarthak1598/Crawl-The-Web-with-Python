

# python program for scraping/downloading the images from the webpage using dedicated modules of web scraping.

 import requests
 from bs4 import BeautifulSoup
 import sys
 
 import urlparse 

 pageurl = raw_input("Please enter the web page url)

   try: 
		pageresp = requests.get(pageurl)
        parse = BeautifulSoup(pageresp.text)
		
	 	imagetags = parse.find_all('img')
	   
	    images = [url.get('src') for url in imagetags ] 
		
	except:
			print("error occured")
			sys.exit(1)
			
	
	if not images:
		print("No images found")
		sys.exit(1)
		
		
	# finally downloading the images to the system 
	
	for url in imges:
		req = requests.get(url)
		file = open('downloading/%s' % url.split('/')[-1],'w') # opening the file for writing/saveing the content 
		
		file.write(req.content)
		
		file.close()
		
		print('downloaded %s' Z% url)
	
	# end //