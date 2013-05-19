#!/usr/bin/python
# WordClass.py by Stanley Wong
class Word:
	
	_wordCount = 0
	_linesWhichAppears = []
	_theWord = ""

	def __init__(self, wordString, lineNumber):
		self.theWord = wordString
            	self.wordCount = 1
	    	self.linesWhichAppears = [lineNumber]

	@property
	def wordCount(self):
		return self._wordCount

	@wordCount.setter
	def wordCount(self,wordCount):
		self._wordCount=wordCount

	@property
	def linesWhichAppears(self):
		return self._linesWhichAppears

	@linesWhichAppears.setter
	def linesWhichAppears(self,linesWhichAppears):
		self._linesWhichAppears = linesWhichAppears

	@property
	def theWord(self):
		return self._theWord

	@theWord.setter
	def theWord(self, theWord):
		self._theWord = theWord
