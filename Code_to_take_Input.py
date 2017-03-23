sA	k for the operation to be done
import os,sys,subprocess


print "1.Stock Market Analysis\n2.To know the news related to the company and how positive is it to the company\n3.Fuzzy\n4.To know the details about tthe company\n"

while True:

	Operation = raw_input("Enter the operation to be done")

	#print type(Operation)

	if int(Operation) == 1 :
		#print "Analyze by Week,Month,Year"
		execfile('Extraction_of_Stock_Details.py')
		subprocess.call(['/usr/bin/Rscript','/home/anurag1/SCT_Project/Opening.R'])
	elif int(Operation) == 2 :
		execfile('Extraction_of_news.py')
	elif int(Operation) == 3 :
		execfile('Analysis_of_Companies.py')
	elif int(Operation) == 4 :
		#print the details and analysis
		print "1"
	else:
		print "Please enter the Correct input Value\n"
		continue
