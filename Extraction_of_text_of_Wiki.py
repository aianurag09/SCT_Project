from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time

browser = webdriver.Firefox()

browser.get('http://www.google.com')

input = browser.find_element_by_xpath('//input[@class="gsfi"]')

input.send_keys('Hyundai Company Wikipedia')

input.send_keys(Keys.ENTER)

time.sleep(3)

browser.find_element_by_xpath('//h3/a').click()

time.sleep(10)

ptag = browser.find_elements_by_xpath('//p')

print len(ptag)

filtered_text = ''

for i in range(0,len(ptag)):
	filtered_text = filtered_text + ptag[i].text+' '

execfile('NLP_Analysis.py')
