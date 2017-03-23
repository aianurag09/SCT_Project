from yahoo_finance import Share

share = Share('GOOG')

Stocks = Share.get_historical('2017-01-02','2017-03-01')

Dates =['2017-01-02','2017-01-03','2017-01-04','2017-01-05','2017-01-06','2017-01-07','2017-01-08','2017-01-09','2017-01-10',
	'2017-01-11','2017-01-12','2017-01-13','2017-01-14','2017-01-15','2017-01-16','2017-01-17','2017-01-18','2017-01-19',
	'2017-01-20','2017-01-21','2017-01-22','2017-01-23','2017-01-24','2017-01-25','2017-01-26','2017-01-27','2017-01-28',
	'2017-01-29','2017-01-30','2017-01-31','2017-02-02','2017-02-03','2017-02-04','2017-02-05','2017-02-06','2017-02-07',
	'2017-02-08','2017-02-09','2017-02-10','2017-02-11','2017-02-12','2017-02-13','2017-02-14','2017-02-15','2017-02-16',
	'2017-02-17','2017-02-18','2017-02-19','2017-02-20','2017-02-21','2017-02-22','2017-02-23','2017-02-24','2017-02-25',
	'2017-02-26','2017-02-27','2017-02-28','2017-03-01']

Stocks.reverse()

f = open('Closing.csv','w')

for stock in Stocks:
	f.write(stock['Close'].encode('UTF8')+',')
	
f.close()

