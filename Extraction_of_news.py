import os, json, time, socket, random,sys
from random import randint
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.proxy import *
from email.mime.text import MIMEText
from subprocess import Popen, PIPE
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from pyvirtualdisplay import Display
from xvfbwrapper import Xvfb
import sys

vdisplay = Xvfb()
vdisplay.start()


browser = webdriver.Firefox()

#browser.get('http://www.google.com')

Links = []
News  = []
Company_List = []

f = open('Linkedin_Name.csv','r')

for line in f:
	Company_List.append(line.split('\n')[0])
#f1 = open('News_15454.csv','w')
#f2 = open('News_Links_15454.csv','w')

for no,company in enumerate(Company_List):
	if(no<15454):
		continue
	url = 'https://www.google.co.in/?gfe_rd=cr&ei=rEWfWPWcA-Ps8AedvJKIBQ&gws_rd=ssl#q=' + company + '&tbm=nws'
	browser.get(url)
	time.sleep(4)
	links = browser.find_elements_by_xpath('//a[@class="l _HId"]')
	f1.write(str(len(links))+',\n')
	f2.write(str(len(links))+',\n')
	for link in links:
		Links.append(link.get_attribute('href'))
		News.append(link.text)
		f2.write(str(link.get_attribute('href'))+',\n')
		f1.write(str(link.text.encode('UTF8'))+',\n')
	print no
vdisplay.stop()
Display.stop()


"""for i in range(0,len(Links)):
	browser.get(Links[0])
	time.sleep(5)
	divtag = browser.find_elements_by_xpath('//div')
	News_text  = ' '
	for j in range(0,len(divtag)):
		News_text = News_text + divtag[i].text + ' '
	break

print News[0]
print News_text"""
	
		



