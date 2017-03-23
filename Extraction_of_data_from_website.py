import urllib2
from bs4 import BeautifulSoup
from urllib import urlopen
import requests
from os import listdir
from os import path
from os.path import isfile, join

proxy = urllib2.ProxyHandler( {'http': '10.3.100.207:8080'} )
 
# Create an URL opener utilizing proxy
opener = urllib2.build_opener( proxy )
urllib2.install_opener( opener )
url = 'http://www.hyundai.com'
# Aquire data from URL
request = urllib2.Request( url )
response = urllib2.urlopen( request )

html = response.read
soup = BeautifulSoup(html)

print soup.pertify()

"""compdir = "/home/anurag1/SCT_Project/"

cfile = 'index.html'

with open(compdir + '/' + cfile, 'r') as myfile:
	data = myfile.read()

soup = BeautifulSoup(data)

data = soup.findAll(text=True)

print data"""


