
from bs4 import BeautifulSoup
import requests
import urllib.request as urll
import os
from os.path import os
import html5lib
import codecs
import urllib.parse


count =28
index = 1
max_count = 500*count # number that you want download


imageDataDir = 'C:/Image_Dataset/bing_down/'
querySet = ['리트리버']

def get_soup(url,header):
    return BeautifulSoup(urll.urlopen(urll.Request(url,headers=header)))

if not os.path.isdir(imageDataDir):
    os.mkdir(imageDataDir)
    
for query in querySet:
    image_naming = query # image name
    query = query.split()
    tempDirName = '_'.join(query)
    query = '+'.join(query)
    isQueryKorean = False
        
    targetDir = imageDataDir+tempDirName
    
    try:
        if not os.path.isdir(targetDir):
            os.mkdir(targetDir)
    except:
        isQuerykorean = True
        image_naming = "temp"
        targetDir = imageDataDir+"temp"
        dirNum=0
        while(True):
            tempTargetDir = targetDir + str(dirNum)
            dirNum+=1
            if not os.path.isdir(tempTargetDir):
                targetDir = tempTargetDir
                os.mkdir(targetDir)
                break
            
index = 1 # init index

for i in range(int(max_count/count)):
    kencode = urllib.parse.quote_plus(query)
    url="http://www.bing.com/images/search?q="+kencode+"&first="+str(index)+"&count="+str(count)+"&FORM=HDRSC2"
    #url="http://www.bing.com/images/search?q="+query+"&first="+str(index)+"&count="+str(count)+"&FORM=HDRSC2"
    index = index+count
    print(url)
    #print(type(url))
    
    page = urll.urlopen(url).read()
    soup = BeautifulSoup(page, 'html5lib')
    
    for img_temp in soup.find_all("a","thumb"):
        img = img_temp.get('href')
        try:
            print(img)
            raw_img = urll.urlopen(img).read()
            cntr = len([i for i in os.listdir(targetDir) if image_naming in i])+1
            print(cntr)
            f = open(targetDir+"/"+image_naming+"_"+str(cntr)+".jpg",'wb')
            f.write(raw_img)
            f.close()
        except:
            print("fail to download")
            
            
    
                           

