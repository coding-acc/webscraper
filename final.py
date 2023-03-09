from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import JavascriptException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import re
import os.path

myoptions = webdriver.ChromeOptions()
myoptions.add_argument('user-data-dir=C:/Users/kamee/Documents/User Data')
myoptions.add_argument('profile-directory=Profile 1')
#myoptions.add_argument('--blink-settings=imagesEnabled=false')


def savehtml(name, html):
    name="code/"+name+".html"
    print(name)
    if (os.path.exists(name)):
        print("file already exists")
    else:
        with open(name, "w", encoding="utf-8") as tofile:
            tofile.write(html)
            tofile.close()

def translate(url=[]):
    d = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=myoptions)
    for k in url:
        namefilethis=""
        if (k==currenturl):
            namefilethis="index"
        else:
            s=k
            filename = s[len(currenturl):]
            parts = re.split('/', filename)
            namefilethis = parts[len(parts)-1]
        
        if (namefilethis==""):
            namefilethis = parts[len(parts)-2]
        print(namefilethis +"  :--This is the file name ")
    
        d.get(k)
        time.sleep(3)
        d.refresh() 
        time.sleep(4)
        d.refresh()
        time.sleep(3)
        total_page_height = d.execute_script("return document.body.scrollHeight")
        #browser_window_height = d.get_window_size(windowHandle='current')['height']
        #current_position = d.execute_script('return window.pageYOffset')
        #while total_page_height - current_position > browser_window_height+100:
            #d.execute_script(f"window.scrollTo({current_position}, {browser_window_height + current_position});")
            #current_position = d.execute_script('return window.pageYOffset')
            #time.sleep(1)
        
        current_pos = d.execute_script("return window.pageYOffset + window.innerHeight")
        windowsizec = d.get_window_size(windowHandle='current')['height']

        while current_pos+windowsizec<total_page_height:
            d.execute_script(f"window.scrollTo({current_pos}, {windowsizec+current_pos})")
            current_pos = d.execute_script("return window.pageYOffset + window.innerHeight")
            time.sleep(1)
        
        time.sleep(4)
        dom = d.page_source
        
        savehtml(namefilethis, dom)
        time.sleep(2)
    





#get links---------------------------------

currenturl = 'https://www.classcentral.com/'
def getlinks(website):
    b = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    b.get(website)
    mainelem = b.find_element(By.TAG_NAME, 'main')

    links = mainelem.find_elements(By.TAG_NAME, "a")
    cnt=len(links)
    print(cnt)
    linkstr=[]
    linkstr.append(currenturl)
    for link in links:
        linkstr.append(link.get_attribute("href"))
        #print(link.get_attribute("href"))
    time.sleep(2)
    b.close()
    return linkstr
    

for j in getlinks(currenturl):
    print(j)


#translate(currenturl)
#for y in linkstr:

translate(getlinks(currenturl))
#d.close()
#end get links----------------------------




#get all links, translate and then save to text file?

