#!/usr/bin/python
# WordClass.py by Stanley Wong
class Word:
	
	def __init__(self, wordString, lineNumber):
		self.theWord = wordString
		self.wordCount = 1
		self.linesWhereAppears = [lineNumber]
				
	def wordCount(self):
		return self.wordCount

	def theWord(self):
		return self