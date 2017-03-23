from yahoo_finance import Share

f = open('Company_codes.csv','r')
f1 = open('Stock_Codes.csv','r')

Codes = []

Names = []

for line_number,line in enumerate(f):
	try:
		Codes.append(line.split('\n')[0].split('\t')[0])
		Names.append(line.split('\n')[0].split('\t')[1])
	except:
		pass
for line_number,line in enumerate(f1):
	try:
		Codes.append(line.split('\n')[0].split(',')[0])
		Names.append(line.split('\n')[0].split(',')[1])
	except:
		pass

#print len(Codes)
Flag_for_Company_Code = raw_input('Enter\n1.If you know the code of the company\n2.If you want to know the code of the company\n')
if int(Flag_for_Company_Code) == 1 :
	while True:
		Code = raw_input('Enter the Code of The company\t')
		if Code not in Codes:
			print "The code Entered is not correct or not in our Database"
			Flag = raw_input('If you want to retry press 4 or press 1 to search by name')
			if int(Flag) == 4:
				continue
			else:
				print "1"
				#func
		if Code in Codes:
			index = Codes.index(Code)
			print Names[index]
			break
#function for search by company	
#try for max regex match	
else:
	while True:
		Company_name = raw_input('Enter the name of the company\t')
		if Company_name not in Names:
			print "The Name Entered is not correct or not in our Database"
			Flag = raw_input('If you want to retry press 4 or press 1 to search by name')
			if int(Flag) == 4:
				continue
			if int(Flag) == 1:
				break	
share = Share(Code)

Start_Date = raw_input('Enter the Start Date in YYYY/MM/DD')

End_Date = raw_input('Enter the End Date in YYYY/MM/DD')

Stocks = share.get_historical(Start_Date,End_Date)

Opening = []

Closing = []

Low = []

High = []

Volumes = []

f = open('Stock_Details.csv','w')

for i in range(0,len(Stocks)):
	f.write(Stocks[i]['Open']+','+Stocks[i]['Close']+','+Stocks[i]['Low']+','+Stocks[i]['High']+','+Stocks[i]['Volume']+'\n')	
"""	Opening.append(Stocks[i]['Open'])
	Closing.append(Stocks[i]['Close'])
	Low.append(Stock[i]['Low'])
	High.append(Stock[i]['High'])
	Volumes.append(Stock[i]['Volume'])
"""


