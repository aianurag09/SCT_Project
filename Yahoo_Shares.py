from yahoo_finance import Share



share = Share('GOOG')

Stocks = share.get_historical('2017-01-02','2017-03-02')

Stocks.reverse()

closing = []
f = open('Stocks.csv','w')
for number,stock in enumerate(Stocks):
	if number % 5 == 4:
		f.write(stock['Close'].encode('UTF8')+'\n')
		f.write(closing[len(closing)-1]+'\n')
		f.write(closing[len(closing)-1]+'\n')
		closing.append(float(stock['Close'].encode('UTF8')))
		closing.append(closing[len(closing)-1])
		closing.append(closing[len(closing)-1])
	else:
		f.write(stock['Close'].encode('UTF8')+'\n')
		closing.append(float(stock['Close'].encode('UTF8')))
f.close()

print len(closing)
print closing
		



