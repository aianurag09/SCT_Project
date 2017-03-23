from bs4 import BeautifulSoup
import string
import urllib
from selenium import webdriver
import time

Alphabets = list(string.ascii_uppercase)

Base_url = ['http://www.advfn.com/nyse/newyorkstockexchange.asp?companies=','http://www.advfn.com/nasdaq/nasdaq.asp?companies=','http://www.advfn.com/amex/americanstockexchange.asp?companies=']
Codes = []
Names = []
driver = webdriver.Firefox()
for base_url in Base_url:
	for letter in Alphabets:
		time.sleep(2)
		url = base_url + letter
		driver.get(url)
		rows = driver.find_elements_by_xpath('//table/tbody/tr')
		for row in rows:
			column = row.find_elements_by_xpath('.//td')
			if(len(column) == 3):
				Codes.append(column[1].text)
				Names.append(column[0].text)

f = open('Stock_Codes.csv','w')
for i in range(0,len(Codes)):
	f.write(Codes[i]+','+Names[i]+'\n')
print Codes
"""for letter in Alphabets:
	url = Base_url + letter
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page)
	rows = soup.find('tbody').findAll('tr')
	for row in rows:
		columns = row.findAll('td')
		print columns
"""
