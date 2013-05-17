#!/usr/bin/python
# WordCounter.py by Stanley Wong
import fileinput
import re

# Array used to hold a line of text
wordInLines = []      

# Dictionary to hold Words
wordDictionary = {}

print "Stan's Python Word Counter"

# Read File
f = open('DataFile.txt')
lines = f.readlines()
f.close()

for line in lines:

	line = line.lower()			 # format line to lowercase
	line = re.sub('[!@#$.?,]', '', line)	 # remove punctuations
	wordInLines = line.split()		 # break line into words

	for word in wordInLines:
	
		# store words into dictionary and update counter
		if wordDictionary.has_key(word):		
			wordDictionary[word] = wordDictionary[word]+1
		else:
			wordDictionary[word] = 1
	
# Print out results of the word counter
for key, value in wordDictionary.iteritems():
	print "\n---------------------------\n"
	print "Word:(", key, ") \nNumber of appearaces:", value

