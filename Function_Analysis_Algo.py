import numpy as np
import math

f = open('output.txt','rb')

i =0

row = []

for line in f:
	temp = []
	for j in range(len(line.split(','))):
		temp.append(int(line.split(',')[j]))
	row.append(temp)
	i = i+1

n = i-1
arr = np.zeros(7)
#no of dimensions of the data

for i in range(1,n):
	arr = np.array(row[i]) + arr

####Mean of the data
Mean = arr/n

####Calculation of variance
Varaiance = 0

for i in range(0,i):
	Row_matrix = np.array(row[i])
	Difference = np.subtract(Row_matrix,Mean)
	Difference_transpose = Difference.transpose()
	Varaiance = Varaiance + np.dot(Difference,Difference_transpose)
print Varaiance

Deviation = math.sqrt(int(Varaiance))

D = 7
L = 2

arr = np.zeros(D*L)

matrix = arr.reshape(7,2)

#phi is a D*D diagonal matrix
#matrix is the weight function
phi = np.diag([1,1,1])

def Guassian(row,a,Mean,Varaiance):
	Row_matrix = np.array(row[i])
	Difference = np.subtract(Row_matrix,Mean)
	Difference_transpose = Difference.transpose()
	Variation = np.dot(Difference,Difference_transpose)
	return (a*math.exp((-1)*Variation)/(Varaiance))

