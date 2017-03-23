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


browser = webdriver.Firefox();

Links = []

f = open('Revenue_Company_list.csv','w')

f1 = open('Company_Links.csv','w')

for i in range(1,101):
	browser.get('http://www.hoovers.com/company-information/company-search.html?nvcnt=76&sortDir=Descending&sort=SalesUS&maxitems=100&page='+str(i))
	Rows = browser.find_elements_by_xpath('//div[@class="clear data-table sortable-header dashed-table-tr alternate-rows"]/table/tbody/tr')
	for j in range(0,len(Rows)):
		tmp = {}
		Record = ''
		Column = Rows[j].find_elements_by_xpath('./td')
		for k in range(0,len(Column)):
			if k == 0:
				Links.append(Column[k].find_element_by_xpath('./a').get_attribute('href'))
				f1.write(str(Column[k].find_element_by_xpath('./a').get_attribute('href'))+'\n')
				Record = Record + Column[k].text.replace(',',' ') + ','
				tmp['Name'] = Column[k].text
			if k== 1:
				Record = Record + Column[k].text + ','
				tmp['Location'] = Column[k].text
			if k ==2:
				Record = Record + Column[k].text + '\n'
				tmp['Sales'] = Column[k].text
				continue
		f.write(Record)
		print tmp
	print i
f.close()


