import sys, os
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib, urllib.request
import requests
import random
import time
from selenium.webdriver.common.keys import Keys
import numpy as np

###initial set

folder = "C:/Image_Dataset/naver_down/"
baseurl = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
webDriver = "./chromedriver.exe"
searchItem = "한예슬"
size = 2000

url = baseurl + urllib.parse.quote_plus(searchItem)
browser = webdriver.Chrome(webDriver)
time.sleep(0.5)
browser.get(url)
html = browser.page_source
time.sleep(0.5)

### get number of image for a page

soup_temp = BeautifulSoup(html,'html.parser')
img4page = len(soup_temp.findAll("img"))

### page down 

elem = browser.find_element_by_tag_name("body")
imgCnt =0
while imgCnt < size:
    elem.send_keys(Keys.PAGE_DOWN)
    rnd = random.random()
    print(imgCnt)
    time.sleep(rnd)
    imgCnt+=img4page
    
html = browser.page_source
soup = BeautifulSoup(html,'html.parser')
img = soup.findAll("img")

browser.find_elements_by_tag_name('img')

print(np.shape(img))
fileNum=0
srcURL=[]

for line in img:
    if str(line).find('class="_img') != -1 and str(line).find('http')!=-1:
        if str(line).find('data-source') != -1 and line['data-source'].find('http')!= -1:
            print(fileNum, " : ", line['data-source'])  
            srcURL.append(line['data-source'])
            fileNum+=1
        elif str(line).find('src') != -1 and line['src'].find('http')!=-1:
            print(fileNum, " : ", line['src'])  
            srcURL.append(line['src'])
            fileNum+=1
print(fileNum)      
      
### make folder and save picture in that directory

saveDir = folder+searchItem

try:
    if not(os.path.isdir(saveDir)):
        os.makedirs(os.path.join(saveDir))
except OSError as e:
    if e.errno != e.errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise

for i,src in zip(range(fileNum),srcURL):
    urllib.request.urlretrieve(src, saveDir+"/"+str(i)+".jpg")
    print(i,"/",fileNum-1,"saved")
    
    