A = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

B = ['Very_Low','Low','Moderate','High','Very_High']

global Membership_value_Very_High 
global Membership_value_High
global Membership_value_Moderate
global Membership_value_Low
global Membership_value_Very_High

f = open('Membership_Value_for_Importance.csv','w')
def Very_Low():
	Membership_value_Very_Low =[]
	for i in range(0,len(A)):
		if i >= 2:
			Membership_value_Very_Low.append(int(0))
			continue
		Membership_value_Very_Low.append(int(1))
	return Membership_value_Very_Low

def Low():
	Membership_value_Low = []
	for i in range(0,len(A)):
		if i <= 1 or i >=4:
			Membership_value_Low.append(int(0))
			continue
		Membership_value_Low.append(int(1))
	return Membership_value_Low

def Moderate():
	Membership_value_Moderate = []
	for i in range(0,len(A)):
		if i >= 6 or i <= 3:
			Membership_value_Moderate.append(int(0))
			continue
		Membership_value_Moderate.append(int(1))
	return Membership_value_Moderate

def High():
	Membership_value_High = []
	for i in range(0,len(A)):
		if i >= 8 or i<= 5:
			Membership_value_High.append(int(0))
			continue
		Membership_value_High.append(int(1))
	return Membership_value_High

def Very_High():
	Membership_value_Very_High =[]
	for i in range(0,len(A)):
		if i <=7:
			Membership_value_Very_High.append(int(0))
			continue	
		if i ==8:
			Membership_value_Very_High.append(float(0.5))			
		if i >= 9:
			Membership_value_Very_High.append(int(1))
	return Membership_value_Very_High


Membership_value_Very_Low = Very_Low()
Membership_value_Low = Low()
Membership_value_Moderate = Moderate()
Membership_value_High = High()
Membership_value_Very_High = Very_High()
for i in range(0,11):
	f.write(str(Membership_value_Very_Low[i])+','+str(Membership_value_Low[i])+','+str(Membership_value_Moderate[i])+','+str(Membership_value_High[i])+','+str(Membership_value_Very_High[i])+'\n')

f.close()
