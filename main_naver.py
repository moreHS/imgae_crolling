from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import random
import os



webDriver = "./chromedriver.exe"
baseurl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
search_comand = '한예슬 사진'
url = baseurl + quote_plus(search_comand)
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
img = soup.find_all(class_='_img')
wantsize=2000

browser = webdriver.Chrome(webDriver)
time.sleep(0.5)
browser.get(url)
img4page = len(img)
elem = browser.find_element_by_tag_name("body")
imgCnt = img4page
while imgCnt < wantsize:
    elem.send_keys(Keys.PAGE_DOWN)
    rnd = random.random()
    print(imgCnt)
    time.sleep(rnd)
    imgCnt += 30

html = browser.page_source
soup = BeautifulSoup(html,'html.parser')
img = soup.find_all(class_='_img')
print(img[0])
print('Final_count = ' + str(len(img)))
fcnum = len(img)



save_dir = 'C:/Image_Dataset/naver_down/' + search_comand
try:
    if not(os.path.isdir(save_dir)):
        os.makedirs(os.path.join(save_dir))
except OSError as e:
    if e.errno != e.errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise
    
    
cnum = 1
for i in img:
    imgurl = i['src']
    with urlopen(imgurl) as f:
        with open(save_dir + '/img' + str(cnum) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    print(str(cnum) + '/' +str(fcnum))
    cnum += 1
    
    if cnum == fcnum:
        time.sleep(1)
        h.close()
        f.close()
    

