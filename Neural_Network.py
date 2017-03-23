import math
from random import randint

def Initiate_Matrix(Rows,Columns):
	Matrix = []
	for i in range(Rows):
		Matrix.append([0.0]*Columns)
	return Matrix

def sigmoid(x):
	return math.tanh(x)

def dsigmoid(x):
	return 1.0 - x**2

class NeuralNetwork:
	
	def __init__(self,inputNodes,hiddenNodes,outputNodes):
		
		#To initiate the class variables 
		self.inputNodes = inputNodes + 1 #+1 for bias
		self.outputNodes = outputNodes
		self.hiddenNodes = hiddenNodes

		#To Activate the input nodes
		self.inputActivation = [1.0]*self.inputNodes
		self.hiddenActivation = [1.0]*self.hiddenNodes
		self.outputActivation = [1.0]*self.outputNodes

		#To initiate the weight matrix
		self.inputWeights = Initiate_Matrix(self.inputNodes,self.hiddenNodes)
		self.outputWeights = Initiate_Matrix(self.hiddenNodes,self.outputNodes)

		#Give Random weights
		for i in range(self.inputNodes):
			for j in range(self.hiddenNodes):
				self.inputWeights[i][j] = float(randint(-2,2))/10
		for i in range(self.hiddenNodes):
			for j in range(self.outputNodes):
				self.outputWeights[i][j] = float(randint(0,4))-2
				

		#weights for momentum
		self.ci = Initiate_Matrix(self.inputNodes, self.hiddenNodes)
		self.co = Initiate_Matrix(self.hiddenNodes, self.outputNodes)

	#Process of Updation of Nodes
	def Update(self,inputs):
		if len(inputs) != self.inputNodes - 1:
			print "No of inputs entered is wrong"

		#input Activation
		for i in range(self.inputNodes - 1):
			self.inputActivation[i] = inputs[i]
	
		#output Activation
		for j in range(self.hiddenNodes):
			sum = 0.0
			for i in range(self.inputNodes):
				sum = sum + self.inputActivation[i] * self.inputWeights[i][j]
				self.hiddenActivation[j] = sigmoid(sum)

		# output activations
		for k in range(self.outputNodes):
			sum = 0.0
			for j in range(self.hiddenNodes):
				sum = sum + self.hiddenActivation[j] * self.outputWeights[j][k]
				self.outputActivation[k] = sigmoid(sum)

		return self.outputActivation[:]

	def weights(self):
		print('Input weights:')
		for i in range(self.inputNodes):
			print(self.inputWeight[i])
		print()
		print('Output weights:')
		for j in range(self.hiddenNodes):
			print(self.outputWeight[j])

	def test(self, inputNodes):
		print inputNodes + '->' + self.Update(inputNodes)
		return self.Update(inputNodes)[0]


	def backPropagate(self, targets, N, M):
		if len(targets) != self.outputNodes:
    			raise ValueError('wrong number of target values')

		# calculate error terms for output
		output_deltas = [0.0] * self.outputNodes
		for k in range(self.outputNodes):
			error = targets[k]-self.outputActivation[k]
			output_deltas[k] = dsigmoid(self.outputActivation[k]) * error

		# calculate error terms for hidden
		hidden_deltas = [0.0] * self.hiddenNodes
		for j in range(self.hiddenNodes):
			error = 0.0
			for k in range(self.outputNodes):
				error = error + output_deltas[k]*self.outputWeights[j][k]
				hidden_deltas[j] = dsigmoid(self.hiddenActivation[j]) * error

		# update output weights
		for j in range(self.hiddenNodes):
			for k in range(self.outputNodes):
				change = output_deltas[k]*self.hiddenActivation[j]
				self.outputWeight[j][k] = self.outputWeights[j][k] + N*change + M*self.co[j][k]
				self.co[j][k] = change

		# update input weights
		for i in range(self.inputNodes):
			for j in range(self.hiddenNodes):
				change = hidden_deltas[j]*self.inputActivation[i]
				self.inputWeight[i][j] = self.inputWeights[i][j] + N*change + M*self.ci[i][j]
				self.ci[i][j] = change

		# calculate error
		error = 0.0
		for k in range(len(targets)):
			error = error + 0.5*(targets[k] - self.outputActivation[k])**2

		return error

	def train(self,patterns,iterations = 1000,N = 0.5,M =0.1):
	#N: Learning Rate M: Momentum factor
		for i in range(iterations):
			error = 0.0
			for p in patterns:
				inputs = p[0]
				targets = p[1]
				self.Update(inputs)
				error = error + self.backPropagate(targets,N,M)
		if i % 100 == 0:
			print('error %-.5f' % error)

if __name__ == "__main__":
	NeuralNetwork(3,3,1)
