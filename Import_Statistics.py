f = open('Statistics.json','r')

Statistics_Overall = []
Cities = []
Industries = []
for line_number,line in enumerate(f):
	Statistics = line.decode("utf-8")
	Entries = Statistics.split(',')
	temp = {}
	Industry = []
	temp_Industry = {}
	for index,entry in enumerate(Entries):
		if '_id' in entry:
			continue
		if index == 1:
			Cities.append(entry.split(':')[1])
			temp[entry.split(':')[0]] = entry.split(':')[1]
			continue
		if len(entry.split(':')) == 3:
			Industry.append(entry.split(':')[0].replace('\\u0026',''))
			if line_number == 0:
				Industries.append(entry.split(':')[0].replace('\\u0026',''))
			if index != 10:
				temp[Industry[(index-10)%8-1]] = temp_Industry
				temp_Industry = {}
			temp_Industry[entry.split(':')[1][1:]] = int(entry.split(':')[2])
		else:
			if '}' in entry.split(':')[1]:
				temp_Industry[entry.split(':')[0]] = int(entry.split(':')[1][:-1].replace('}',''))
			else:
				temp_Industry[entry.split(':')[0]] = int(entry.split(':')[1])
	print line_number
	Statistics_Overall.append(temp)



	#print temp['Think Tanks']
	#break
#print len(Statistics)
#print len(Cities)
#print len(Industries)
#		print index
#	print line_number
#	print temp
