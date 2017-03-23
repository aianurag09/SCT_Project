###  DONE WITH NEWS ANALYSIS

global Very_High,High,Moderate,Low,Very_Low,Positive_Score,Negative_Score,Answer

Very_High = [0.8,1]
High = [0.6,0.9]
Moderate = [0.4,0.7]
Low = [0.2,0.5]
Very_Low = [0,0.3]
Answer = list() 


def Interval_Airthemetic(Score):
	w1 = Very_High
	w2 = High
	w3 = Moderate
	w4 = Low
	w5 = Very_Low
	v1 = Score[0]
	v2 = Score[1]
	v3 = Score[2]
	v4 = Score[3]
	v5 = Score[4]
	minimum = 1
	maximum = 0
	for a in v1:
		for b in v2:
			for c in v3:
				for d in v4:
					for e in v5:
						for f in w1:
							for g in w2:
								for h in w3:
									for i in w4:
										for j in w5:
											e = (a*f + b*g + c*h + d*i + e*j)/(f+g+h+i+j)
											minimum = min(minimum,e)
											maximum = max(maximum,e)
	Answer.append(minimum)
	Answer.append(maximum)
	return Answer  
Score = []
for i in range(0,10):
	if i == 0 or i == 1: 	
		Positive_Score = 0.2 
		Negative_Score = 0.3 
		if i == 1:
			Score.append([Positive_Score,Negative_Score])
			Positive_Score = 0
			Negative_Score = 0
	if i == 2 or i == 3: 	
		Positive_Score = 0.4
		Negative_Score = 0.8
		if i == 3:
			Score.append([Positive_Score,Negative_Score])
			Positive_Score = 0
			Negative_Score = 0
	if i == 4 or i == 5: 	
		Positive_Score = 0.2
		Negative_Score = 0.9
		if i == 5:
			Score.append([Positive_Score,Negative_Score])
			Positive_Score = 0
			Negative_Score = 0
	if i == 6 or i == 7: 	
		Positive_Score = 0.6
		Negative_Score = 1
		if i == 7:
			Score.append([Positive_Score,Negative_Score])
			Positive_Score = 0
			Negative_Score = 0
	if i == 8 or i == 9: 	
		Positive_Score = 0.4
		Negative_Score = 0.7
		if i == 9:
			Score.append([Positive_Score,Negative_Score])
			Positive_Score = 0
			Negative_Score = 0
print Interval_Airthemetic(Score)
	
