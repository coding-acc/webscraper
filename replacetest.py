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
        print(link.get_attribute("href"))
    time.sleep(2)
    b.close()
    return linkstr

def repplacelinks(linknames):
     with open("code/index.html", "r", encoding="utf-8") as tofile:
        file = tofile.read()
        tofile.close()
        print(type(file))
        for k in linknames:
            s = k.replace("https://www.classcentral.com", "")
            print (s+"   --this will be searched for in string")
            namefilethis=""
            if (k==currenturl):
                namefilethis="index"
            else:
                
                filename = k[len(currenturl):]
                parts = re.split('/', filename)
                namefilethis = parts[len(parts)-1]
            
            if (namefilethis==""):
                namefilethis = parts[len(parts)-2]

            print(namefilethis +"  :--This is the file name ")
            #file.replace("href=\""+k,"href=\""+namefilethis)
            #for f in file:
                  #newfile.append(f.replace(k, "href=\""+namefilethis+"\""))
        
        
        newfile= file.replace("\"https://www.classcentral.com/report/author/","\"https://coding-acc.github.io/")
        newfile= newfile.replace("\"https://www.classcentral.com/collection/","\"https://coding-acc.github.io/")
        newfile= newfile.replace("\"https://www.classcentral.com/report/","\"https://coding-acc.github.io/")
        newfile= newfile.replace("\"https://www.classcentral.com/provider/","\"https://coding-acc.github.io/")
        newfile= newfile.replace("\"https://www.classcentral.com/institution/","\"https://coding-acc.github.io/")
        newfile= newfile.replace("\"https://www.classcentral.com/university/","\"https://coding-acc.github.io/")
        newfile= newfile.replace("\"https://www.classcentral.com/subject/","\"https://coding-acc.github.io/")
        newfile= newfile.replace("\"https://www.classcentral.com/help/","\"https://coding-acc.github.io/")
        newfile= newfile.replace("\"https://www.classcentral.com/course/","\"https://coding-acc.github.io/")
        newfile= newfile.replace("\"https://www.classcentral.com/","\"https://coding-acc.github.io/")
        newfile= newfile.replace("\"/subject","\"")
        newfile= newfile.replace("\"/report/author","\"")
        newfile= newfile.replace("\"/course","\"")
        newfile= newfile.replace("\"/university","\"")
        newfile= newfile.replace("\"/institution","\"")
        newfile= newfile.replace("\"/provider","\"")
        newfile= newfile.replace("\"/collection","\"")
        print(newfile)
        with open("code/index.html","w",encoding="utf-8") as ovrwritefile:
            ovrwritefile.write(newfile)     
        #for n in newfile:
         #   print(n)


repplacelinks(getlinks(currenturl))
#getlinks(currenturl)
