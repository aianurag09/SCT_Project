from urllib import urlopen
from bs4 import BeautifulSoup
#from Extraction_of_data_from_Linkedin import Company_Details
#from Geography_codes import Cities
"""
	The Data is Extracted From linkedin and Stored in CSV Format

	The Data entries can also be checked by Statistics

	
"""

"""
	Import Data From Csv Format and store it in a list

	And Each entity can be accessed by the index

"""

"""
	Differenent Linguistic Variables

	Industry,Company_Size,City,CompanyWebsite NLP analysis
"""

"""Array of Dictionaries"""
########take care of 10000+
Company_Size = [110,1150,51200,201500,5011000,100015000,500110000,10000]

def Find_the_Index(Size):
	if(Size<=10): return 0
	if(Size<=50): return 1
	if(Size<=200): return 2
	if(Size<=500): return 3
	if(Size<=1000): return 4
	if(Size<=5000): return 5
	if(Size<=10000): return 6
	return 7

def Membership_Function_for_Company_Size(x):
	Size = x[:-11]
	peak = Find_the_Index(int(Size))
	for i in range(0,8):
		if i >= peak :
			Membership_value_Company_Size[i] = 1
		elif i == peak - 1 :
			Membership_value_Company_Size[i] = 0.75
		elif i == peak - 2 :
			Membership_value_Company_Size[i] = 0.5
		elif i == peak - 3 :
			Membership_value_Company_Size[i] = 0.25
		else :
			Membership_value_Company_Size[i] = 0

	return Membership_value_Company_Size

def Regex_Max_Match(a,b):
	b = b.split(',')[0]
	a = a.split(',')[0]
	b = b.lower()
	a = a.lower() 
	try:
		Words_of_a = a.split()
	except:
		pass
	try:
		Words_of_b = b.split()
	except:
		pass
	for word in Words_of_a:
		if word in Words_of_b:
			return 1
	return 0

#main function

Cities = [{'City':'Austin','State':'Texas'}]

State = raw_input('Enter the State where you want to Start a Company\n')
Cities_in_State  = []
Exclusively_cities = []

for i in range(0,len(Cities)):
	if Cities[i]['State'] == State :
		Cities_in_State.append(Cities[i])	
		Exclusively_cities.append(Cities[i]['City'])
print Cities_in_State
print Exclusively_cities

Compressed_Company_Details_by_State = []
#low
#max regex
for i in range(0,len(Company_Details)):
	if Regex_Max_Match(Exclusively_cities[0],Company_Details[i]['City'].replace('\"','').split(',')[0]) == 1:
		Compressed_Company_Details_by_State.append(Company_Details[i])
		print Company_Details[i]['Name']


print len(Compressed_Company_Details_by_State)


City = raw_input('Enter the Place where you want to Start a company\n')

Cities_to_be_Analysed = []
Exclusively_cities = []


for i in range(0,len(Cities_in_State)):
	if Cities_in_State[i]['City'].replace('\"','').split(',')[0] == City:
		Cities_to_be_Analysed.append(Cities[i])
print len(Cities_to_be_Analysed)

#Compress the companies to be analysed by city
Compressed_Company_Details_by_City = []
#Moderate
for i in range(0,len(Compressed_Company_Details_by_State)):
	if Compressed_Company_Details_by_State[i]['City'].replace('\"','').split(',')[0] == City:
		Compressed_Company_Details_by_City.append(Company_Details[i])
		print Compressed_Company_Details_by_State[i]['Name']
#print Cities_to_be_Analysed
#print Compressed_Company_Details_by_City
print len(Compressed_Company_Details_by_State)

#==========================================================================================================================

#important
Industry = raw_input('Enter the Industry in which your Company falls into\n')

#use while preparing GUI
""""browser.get('https://developer.linkedin.com/docs/reference/industry-codes#!')
Field_rows=browser.find_elements_by_xpath("//div[@class='resource-table-section header-row']/table/tbody/tr/td")

#To Extract only the 3rd column(Industry Column) in the above page

Industry = []
 
for i in range(3,444):
    if(i%3==2): 
	Industry.append(Field_rows[i].text)"""


Specialities = raw_input('Enter the Specialities\n')

Compressed_Company_Details_by_Specialities = []

Compressed_Company_Details_by_Industry = []

"""for i in range(0,len(Compressed_Company_Details_by_City)):
	if Specialities in Compressed_Company_Details_by_City[i]['Specialities']: 
		Compressed_Company_Details_by_Specialities.append(Compressed_Company_Details_by_City[i])
"""
for i in range(0,len(Compressed_Company_Details_by_City)):	
	if Industry in Compressed_Company_Details_by_City[i]['Industry'].replace('\"','') :
		Compressed_Company_Details_by_Industry.append(Compressed_Company_Details_by_City[i])
print len(Compressed_Company_Details_by_Industry)
#============================================================================================================================

company_Size = raw_input('Enter the Company Size of your company\n')

index = Find_the_Index(int(company_Size))


Compressed_Company_Details_by_Company_Size = []

for i in range(0,len(Compressed_Company_Details_by_Specialities)):
	try:
		float(Compressed_Company_Details_by_Industry[i]['Size'][:-10].replace('-',''))
	except Exception as e:
		print str(e)
		continue
	if float(Compressed_Company_Details_by_Industry[i]['Size'][:-10].replace('-','')) == float(Company_Size[index]) :
		Compressed_Company_Details_by_Company_Size.append(Compressed_Company_Details_by_Industry[i])
for i in range(0,len(Compressed_Company_Details_by_Industry)):
	try:
		float(Compressed_Company_Details_by_Industry[i]['Size'][:-10].replace('-',''))
	except Exception as e:
		print str(e)
		continue
	if float(Compressed_Company_Details_by_Industry[i]['Size'][:-10].replace('-','')) == float(Company_Size[index]) :
		if Compressed_Company_Details_by_Industry[i]['Name'] not in Compressed_Company_Details_Company_Size:
			Compressed_Company_Details_by_Company_Size.append(Compressed_Company_Details_by_Industry[i])
#=============================================================================================================================

print len(Compressed_Company_Details_by_State)
print len(Compressed_Company_Details_by_City)
print len(Compressed_Company_Details_by_Specialities)
print len(Compressed_Company_Details_by_Industry)
print len(Compressed_Company_Details_by_Company_Size)

time.sleep(100)

Companies_to_be_Analysed = []

print "The Names of the Companies which are to be Analysed are "

print len(Compressed_Company_Details_Company_Size)
#very_Important
for i in range(0,len(Compressed_Company_Details_Company_Size)):
	Companies_to_be_Analysed.append(Compressed_Company_Details_Company_Size[i]['Name'])
	print Compressed_Company_Details_Company_Size[i]['Name']

"""	print "The Stock Market Details of the Companies are as follows"

	execfile('Stock_Market_Analysis.py')

	print "The News of the Companies are as follows"
	
	execfile('Extraction_of_News.py')"""

####EXTRACTION COMPLETE AND ANALYSIS TO BE DONE


