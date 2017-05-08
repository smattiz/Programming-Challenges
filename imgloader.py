# coding: utf-8 
import os
import urllib
import sys
import random
from bs4 import BeautifulSoup
import string
# This program accepts as argument exacalty one (1) web page. It will then proceed to download all images from the page into folder named after the page
# @Author Matti Keskiniemi /Smattiz
# Tää ohjelma pyytää argumenttina nettisivun, jolta ladata kuvia. Sivun saatuaan se lähtee lataamaan jokaisen kuvan sivun nimiseen kansioon
# @Version 1.0
#DISCLAIMER: I do not know if this works on all web pages, but it does on most of pages

#Make sure user gives you web page
if len(sys.argv)<1:
    print "ERROR! Web page not given. Please give us web page to start downloading"
    quit()
    
#open URL
try:
    print "Hello! We will begin downloading soon!"
    url=sys.argv[1]
    folder_name=url.split('/')[0]
except:
    print "Page not given! Shutting down..."
    
    
#Make folder named after URL
try:
    os.makedirs(folder_name)
except:
    extraseed=random.randrange(2892) #Just in case our folder exists. I Do trust that users usually don't download more than 2892 different copies of _precisely_ same page
    folder_name=(folder_name+'Copy'+ str(extraseed))
    os.makedirs(folder_name) 
    
#Get the page and make it parseable using BeautifulSoup
opened_page=urllib.urlopen('https://'+url)
html=opened_page.read()
parser = BeautifulSoup(html, 'html.parser')


for img_link in parser.find_all('img'):
    link=img_link['src'] #get src of img
    img_link=string.replace( link, '\\\\', '/' ) #Cool string manipulations to ensure link is fine
    img_link=string.replace(link,'\\','/')
    img_name=str(random.randrange(3319))+ ".jpg"
    file_path=os.getcwd()+'\\' +folder_name+ '\\' +img_name
    print file_path
    try:
        urllib.urlretrieve(link,file_path)
    except:
        new_link=url.split('/')[0]+'/' + link
        urllib.urlretrieve(new_link,file_path)
        print "Ropleemia haun kanssa..?"

print "Done!"