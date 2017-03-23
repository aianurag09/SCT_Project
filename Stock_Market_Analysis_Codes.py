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
try:

	share = Share(Code)

	Stocks = share.get_historical(Start_Date,End_Date)

	Opening = []

	Closing = []

	Low = []

	High = []

	Volumes = []

	f = open('Stock_Details.csv','w')

	for i in range(0,len(Stocks)):
		f.write(Stocks[i]['Open']+','+Stocks[i]['Close']+','+Stocks[i]['Low']+','+Stocks[i]['High']+','+Stocks[i]['Volume']+'\n')	
except:
	pass
