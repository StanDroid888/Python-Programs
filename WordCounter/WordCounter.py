#!/usr/bin/python
# WordCounter.py by Stanley Wong
import re
from WordClass import Word

# Array used to hold a line of text
wordInLines = []      

# Dictionary to hold Words
wordDictionary = {}

# Initialize lineCounter
lineCounter = 0

print "Stan's Python Word Counter"

# Read File
try:
	f = open('DataFile.txt')
	fileData = f.readlines()
	f.close()
except IOError as e:
	print "I/O error({0}): {1}".format(e.errno, e.strerror)

for line in fileData:

	line = line.lower()			 # format line to lower case
	line = re.sub('[!@#$.?,]', '', line)	 # remove punctuation
	wordInLines = line.split()		 # break line into words
	lineCounter=lineCounter+1

	for word in wordInLines:
	
		# store words into dictionary and update counter
		if wordDictionary.has_key(word):
			# word object exist and needs to be updated
			wordObject = wordDictionary[word]
			wordObject.wordCount = wordObject.wordCount + 1
			(wordObject.linesWhereAppears).append(lineCounter)
		else:
			# Add new word object to dictionary
			wordObject = Word(word, lineCounter)
			wordDictionary[word] = wordObject
	
# Print out results of the word counter
for key, value in wordDictionary.iteritems():
	print "\n-----------------------------------------------\n"
	print "Word:(", key, ") \nNumber of appearances:", value.wordCount, "\nLine(s) which word appears:",value.linesWhereAppears

print "\n-----------------------------------------------\n"

