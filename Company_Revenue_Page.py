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

f = open('Company_Links.csv','r')

for line in f:
	