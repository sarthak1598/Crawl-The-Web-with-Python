
# python program to extract the inforrmation of the images using basic scripting and some image processing modules 
# module used  :: Python Pillow 

import requests 
from io import BytesIO
from PIL import Image 

url = raw_input("Please enter the full image url")
r = requests.get(url)

print("Status code:", r.status_code)
print(image.open(BytesIO(r.content))

print(image.size, image.format , image.mode) # extracting the basic image parameters 

path = "./image."+image.format # settingthe image path with respective extension format 

try:
    image.save(path,image.format)
except IOerror:
    print("Image can't save.")
    
# ends//;
