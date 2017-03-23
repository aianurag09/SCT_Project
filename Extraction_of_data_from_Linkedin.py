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
import subprocess
#from NLP_Analysis import *

#subprocess.call(['./nlp_analysis',text]) for nlp analysis 
#from file import *


def No_of_followers():
	Index = randint(0,8)
	if Index == 0:
		return randint(10000,12000)
	if Index == 1:
		return randint(12000,14000)
	if Index == 2:
		return randint(15000,18000)
	if Index == 3:
		return randint(18000,20000)
	if Index == 4:
		return randint(20000,23000)
	if Index == 5:
		return randint(21000,22000)
	if Index == 6:
		return randint(24000,25000)
	if Index == 7:
		return randint(10000,11000)
	if Index == 8:
		return randint(13000,14000)

Company_Details1 = []
Company_Details2 = []


f_name = open('Linkedin_Name.csv','r')
f_address = open('./linkedin/Linkedin_address.csv','r')
f_founded = open('Linkedin_Founded.csv','r')
f_people = open('./linkedin/Linkedin_People.csv','r')
f_city = open('Linkedin_City.csv','r')
f_industry = open('Linkedin_Industry.csv','r')
f_region = open('./linkedin/Linkedin_Region.csv','r')
f_country = open('./linkedin/Linkedin_Country.csv','r')
f_key_words = open('./linkedin/Linkedin_Key_Words.csv','r')
f_size = open('Linkedin_Size.csv','r')
f_description = open('./linkedin/Linkedin_Description.csv','r')
f_url = open('Linkedin_url.csv','r')
f_specialties = open('Linkedin_Specialties.csv','r')
f_followers = open('Linkedin_Followers.csv','r')
f_web = open('Linkedin_Website.csv','r')


count = 0

for line,line2,line4,line5,line8,line9,line12,line13 in zip(f_name,f_founded,f_city,f_industry,f_key_words,f_size,f_specialties,f_followers):
	temp = {}
	count = count + 1
	temp['Name'] = str(line.split('\n')[0])
	try:
		temp['Founded'] = int(line2.split('\n')[0])
	except:
		temp['Founded'] = 0
	temp['City'] = line4.split('\n')[0]
	temp['Industry'] = line5.split('\n')[0]
	Key_words = []
	for word in line8.split(','):
		Key_words.append(word)
	temp['Key_Words'] = Key_words
	temp['Size'] = line9.split('\n')[0]
	temp['Specialties'] = line12.split('\n')[0]
	try:
		temp['Followers'] = float(line13.split('\n')[0])
	except:
		temp['Followers'] = 0
	Company_Details1.append(temp)
	print count


count = 0

for line3,line1,line6,line10,line11,line14,line7 in zip(f_address,f_people,f_region,f_description,f_url,f_web,f_country):
	count = count + 1
	temp['Address'] = str(line1.split('\n')[0])
	People = []
	for Link in line3.split(','):
		People.append(Link)
	temp['People'] = People
	temp['Region'] = line6.split('\n')[0]
	#temp['Description'] = line10.split('\"')
	temp['Url'] = line11.split('\n')[0]
	temp['Website'] = line14.split('\n')[0]
	temp['Country'] = line7.split('\n')[0]
	Followers_Array = []
	Company_Details2.append(temp)
	print count

count = 0
Company_Details = []
for i in range(0,len(Company_Details1)):
	tmp = {}
	count = count + 1
	tmp['Name'] = Company_Details1[i]['Name']
	tmp['Founded'] = Company_Details1[i]['Founded']
	tmp['City'] = Company_Details1[i]['City']
	tmp['Industry'] = Company_Details1[i]['Industry']
	tmp['Key_Words'] = Company_Details1[i]['Key_Words'][:]
	tmp['Size'] = Company_Details1[i]['Size']
	tmp['Specialties'] = Company_Details1[i]['Specialties']
	tmp['Followers'] = Company_Details1[i]['Followers']
	tmp['Address'] = Company_Details2[i]['Address'] 
	tmp['People'] = Company_Details2[i]['People']
	tmp['Region'] = Company_Details2[i]['Region']
	#temp['Description'] = Company_Details2[i]['Description']
	tmp['Url'] = Company_Details2[i]['Url']
	tmp['Website'] = Company_Details2[i]['Website']
	tmp['Country'] = Company_Details2[i]['Country']
	"""for link in tmp['People']:
		Followers_Array.append(No_of_followers())
	tmp['People_Followers'] = Followers_Array"""
	Company_Details.append(tmp)
	print count



















	"""#print line
	temp = {}
	count = count + 1
	#print line
	Arrays = line.split('[')
	for index,array in enumerate(Arrays):
		if '_id' in array:
			continue
		Main_Array = array.split(']')
		if index == 1:
			temp['Key_Words'] = Main_Array[0]
		if index == 2:
			People = []
			People_Links = Main_Array[0].split(',')
			for link in People_Links:
				Link = link[1:-1]
				People.append(Link)
			temp['Related_People'] = People
	#print temp
	Entities = line.split('"')
	Description_entity = line.split('description')[1]
	Description_entity = Description_entity[3:]
	temp['Description'] = Description_entity.split('\",')[0]
	#os.sys('./NLP_Analysis.py')
#	execfile('NLP_Analysis.py')
#	subprocess.call(['./NLP_Analysis.py'],temp['Description'])
	#print positive_score_of_sentence
	#print negative_score_of_sentence
	List_of_selected_entities = line1.split('\n')[0].split(',')
	#print len(List_of_selected_entities)
	for index,entity_value in enumerate(List_of_selected_entities):
		if index == 0:
			temp['Followers'] = float(entity_value)
		if index == 1:
			temp['Name'] = entity_value
		if index == 2:
			temp['Country'] = entity_value
		if index == 3:
			temp['Industry'] = entity_value
		if index == 4:
			temp['Linkedin_Url'] = entity_value
		if index == 5:
			try:
				temp['Founded'] = float(entity_value)
			except Exception as e:
				print str(e)
				temp['Founded'] = ''
		if index == 6:
			temp['Employee_Size'] = entity_value[:-11]
		if index == 7:
			temp['City'] = entity_value
		if index == 8:
			temp['Website'] = entity_value
		if index == 9:
			temp['Specialities'] = entity_value
		if index == 10:
			temp['Region'] = entity_value
	#add linkedin id and then crawl and store as dataset
		browser.get(link)	
		time.sleep(4)
		try:
			Followers = browser.find_element_by_xpath('//section[@class="pv-profile-section artdeco-container-card pv-recent-activity-section ember-view"]/header/h3').text
			Followers_Array.append(int(Followers[:-10].replace(',','')))
		except:
			pass
	Company_Deatils.append(temp)
#	print temp
	print count
#	if count == :
#		break"""
	
