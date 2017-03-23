from bs4 import BeautifulSoup
from urllib2 import urlopen
import nltk
import sys
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import PunktSentenceTokenizer 
from nltk import FreqDist,pos_tag
from nameparser.parser import HumanName
from nltk.tag.stanford import StanfordNERTagger
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
import re,os
import urllib
from os import listdir
from os import path
from os.path import isfile, join
from nltk.corpus import names
from nltk.corpus import wordnet as wn
from nltk.tag import RegexpTagger

"""cars = wn.synsets('car')
#print cars.hyponyms() #to print the category  

names = nltk.corpus.names
Names = names.fileids()
#print Names"""

def visible(element):
	if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
    		return False
	elif re.match('<!--.*-->', str(element.encode('utf-8'))):
		return False
	return True

compdir = "/home/anurag1/SCT_Project/"

files = [f for f in listdir(compdir) if isfile(join(compdir, f))]

wnl = WordNetLemmatizer()
Words_file = open('Sentiment_analysis_Words.txt','r')
Positive_Score_file = open('Sentiment_analysis_Positive.txt','r')
Negative_Score_file = open('Sentiment_analysis_Negative.txt','r')

ps = PorterStemmer()

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

tokenizer = RegexpTokenizer(r'\w+')


"""============================================================================================================================================="""


for cfile in files:
	if cfile[-5:] != '.html':
		continue
	with open(compdir + '/' + cfile, 'r') as myfile:
		data=myfile.read()
		
	soup = BeautifulSoup(data)

	data = soup.findAll(text=True)

	#for direct html use nltk.clean_html(html)

#	print nltk.clean_html(data)

	result = filter(visible, data)
		
	text = ''

	for word in result:
		if word== '\n':
			continue
		text = text + word
	
	print text

	tokenized_by_sentence = nltk.sent_tokenize(text)

	for sentence in tokenized_by_sentence:
		word_tokenized = tokenizer.tokenize(sentence)
		"""tagged = nltk.pos_tag(word_tokenized)
		flag = 0
		noun = ""
		adj = ""
		for tupple_pos in tagged:
			if(tupple_pos[1]=='NNP'): 
				noun = tupple_pos[0]
				break
			if(tupple_pos[1]=='NN'): 				
				noun = tupple_pos[0]
				break
		for tupple_pos in tagged:
			if(tupple_pos[1]=='JJR') : 				
				adj = tupple_pos[0]
				break
			if(tupple_pos[1]=='JJ'):
				adj = tupple_pos[0]
				break
			if(tupple_pos[1]=='JJS'):
				adj = tupple_pos[0]
				break
"""
#		positive_score_of_sentence = 0
#		negative_score_of_sentence = 0
		for words in nltk.word_tokenize(sentence):
			try:
				index = Words.index(words)
				if index==0:
					try:
						#words = wnl.emmatize(words,'a')
						words = words.lower()
						index = Words.index(words)
					except:
						pass
						print 2
				positive_score_of_sentence= positive_score_of_sentence + float(Positive_Score[index])
				negative_score_of_sentence= negative_score_of_sentence + float(Negative_Score[index])
			except:
				pass
		#print "%s\t\t%s\t\t%f\t%f" %(noun,adj,positive_score_of_sentence,negative_score_of_sentence)
	print positive_score_of_sentence
