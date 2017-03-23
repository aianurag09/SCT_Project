#from nlp_task import *
#use direct exporting of  variables
from Extraction_of_data_from_Linkedin_one_entry import *
from Extraction_of_text_of_Wiki import *
import nltk
Words_file = open('Sentiment_analysis_Words.txt','r')
Positive_Score_file = open('Sentiment_analysis_Positive.txt','r')
Negative_Score_file = open('Sentiment_analysis_Negative.txt','r')
positive_score_of_sentence = 0
negative_score_of_sentence = 0

Words = []

Positive_Score = []

Negative_Score = []

for line in Words_file:
	word = line.split('\n')
	Words.append(word[0])
for line in Positive_Score_file:
	word = line.split('\n')
	Positive_Score.append(word[0])
for line in Negative_Score_file:
	word = line.split('\n')
	Negative_Score.append(word[0])
#print temp['Description']
for words in nltk.word_tokenize(filtered_text):#temp['Description'].decode("utf-8")):
	try:
		index = Words.index(words)
		if index==0:
			try:
				words = wnl.emmatize(words,'a')
				words = words.lower()
				index = Words.index(words)
			except:
				pass
				continue
		positive_score_of_sentence= positive_score_of_sentence + float(Positive_Score[index])
		negative_score_of_sentence= negative_score_of_sentence + float(Negative_Score[index])
	except:
		pass
print positive_score_of_sentence
print negative_score_of_sentence
#temp['Description_Positive_Score'] = positive_score_of_sentence 
#temp['Description_Negative_Score'] = negative_score_of_sentence 


