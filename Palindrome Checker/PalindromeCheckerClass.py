##############################################
#
# Programmer: Stanley Wong
# File: StackDriver.py
# Description: This program checks if a 
# string is a Palindrome. This module 
# requires StackClass.py.
#          
##############################################
import re
from StackClass import Stack

class PalindromeChecker:
    
	# Initializtion/Constructor
        def __init__(self):
            self.stringToCheck = None
            self.stringStack = Stack()
            self.isPalindrome = False
            
	# This method checks if a string (argument)
	# is a palindrome. The method returns a 
	# boolean.
        def checkString(self, string):
	
	    # Initialize return value to be True
            booleanValue = True

	    # Show string to be evaluated
            print "Checking string %s" % string
	    
            # Remove punctuations 
	    string = re.sub('[!@#$.?,]', '', string)	  

	    # Set the attribute
	    self.stringToCheck = string.lower()

            # Fill the stack            
            for eachChar in self.stringToCheck:
                self.stringStack.push(eachChar)
            
            #print self.stringStack.printStack()
            for eachChar in self.stringToCheck:
                if eachChar != self.stringStack.pop():
                    booleanValue = False
		
	    # return boolean
            return booleanValue
