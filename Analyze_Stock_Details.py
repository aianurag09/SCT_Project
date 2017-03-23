from yahoo_finance import Share
import time
from Neural_Network import NeuralNetwork

def normalizePrice(price, minimum, maximum):
	return ((2*price - (maximum + minimum)) / (maximum - minimum))

def denormalizePrice(price, minimum, maximum):
	return (((price*(maximum-minimum))/2) + (maximum + minimum))/2

def filterStock(Stock_prices):
	temp = {}
	Opening = []
	Low= []
	High = []
	Closing = []
	for Stock_price in Stock_prices:
		Closing.append(Stock_price['Close'])	
	temp['Close'] = Closing

	return temp

def fiveDayDivision(Closing,Days):

	temp = {}
	Average = []
	Minimum = []
	Maximum = []
	for i in range(Days-5):
		w = Closing[i:i+5]
		Average.append(float(sum(w))/len(w))
		Minimum.append(min(w))
		Maximum.append(max(w))
	temp['Average'] = Average
	temp['Maximum'] = Maximum
	temp['Minimum'] = Minimum
	return temp

def getTimeSeriesValues(Stock_prices,Days):
	temp = fiveDayDivision(Stock_prices,Days)
	movingAverages = temp['Average']
	maximums = temp['Maximum']
	minimums = temp['Minimum']
	returnData = []
	for i in range(0, len(movingAverages)):
		inputNode = [movingAverages[i], minimums[i], maximums[i]]
		price = normalizePrice(float(Stock_prices[len(movingAverages) - (i + 1)]), minimums[i], maximums[i])
		outputNode = [price]
		tempItem = [inputNode, outputNode]
		returnData.append(tempItem)

	return returnData

def getPredictionData(Stock_prices,Days):

	predictionData = getTimeSeriesValues(Stock_prices,Days)

	predictionData = predictionData[0][0]

	return predictionData

	

def getTrainingData(Stock_prices,Days):

	trainingData = getTimeSeriesValues(Stock_prices,Days)

	return trainingData

def AnalyzeCompany(Code):

	f = open('Analyzed_Stocks.csv','w')

	share = Share(Code)
	
	Dates =['2017-01-03','2017-01-04','2017-01-05','2017-01-06','2017-01-07','2017-01-08','2017-01-09','2017-01-10',
		'2017-01-11','2017-01-12','2017-01-13','2017-01-14','2017-01-15','2017-01-16','2017-01-17','2017-01-18','2017-01-19',
		'2017-01-20','2017-01-21','2017-01-22','2017-01-23','2017-01-24','2017-01-25','2017-01-26','2017-01-27','2017-01-28',
		'2017-01-29','2017-01-30','2017-01-31','2017-02-01','2017-02-02','2017-02-03','2017-02-04','2017-02-05','2017-02-06',
		'2017-02-07','2017-02-08','2017-02-09','2017-02-10','2017-02-11','2017-02-12','2017-02-13','2017-02-14','2017-02-15',
		'2017-02-16','2017-02-17','2017-02-18','2017-02-19','2017-02-20','2017-02-21','2017-02-22','2017-02-23','2017-02-24',
		'2017-02-25','2017-02-26','2017-02-27','2017-02-28','2017-03-01','2017-03-02',]

	for date in Dates:

		f = open('Analyzed_Stocks.csv','w')

		Stock_prices = share.get_historical('2016-12-02',date)

		Days = len(Stock_prices)

		closing = []

		for number,stock in enumerate(Stock_prices):
			if number % 5 == 4:
				closing.append(float(stock['Close'].encode('UTF8')))
				closing.append(closing[len(closing)-1])
				closing.append(closing[len(closing)-1])
			else:
				closing.append(float(stock['Close'].encode('UTF8')))

		#Dictionary 
		#Stock_price = filterStock(Stock_prices)

		#Stock_prices = Stock_price['Close']

		Stock_prices = closing

		network = NeuralNetwork(inputNodes = 3,hiddenNodes = 3,outputNodes = 1)

		trainingData = getTrainingData(Stock_prices,Days)

		network.train(trainingData)

		predictionData = getPredictionData(Stock_prices,Days)

		returnPrice = network.test(predictionData)

		predictedStockPrice = denormalizePrice(returnPrice, predictionData[1], predictionData[2])
		returnData = {}
		returnData['price'] = predictedStockPrice
		f.write(str(predictedStockPrice)+'\n')
		print returnData

	f.close()



if __name__ == '__main__':
	AnalyzeCompany('GOOG')
