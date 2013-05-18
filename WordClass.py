#!/usr/bin/python
class Word:
	
	wordCount = 0
	linesWhichAppears = []
	theWord = ""

	def __init__(self, wordString, lineNumber):
		self.theWord = wordString
            	self.wordCount = 1
	    	self.linesWhichAppears = [lineNumber]
	
