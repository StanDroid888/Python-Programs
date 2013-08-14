##############################################
#
# Programmer: Stanley Wong
# File: StackDriver.py
# Description: This program checks if a 
# string is a Palindrome. This module 
# requires StackClass.py.
#          
##############################################
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
            self.stringToCheck = string
            print "Checking string %s" % self.stringToCheck

            # Initialize return value to be True
            booleanValue = True

            # Fill the stack            
            for eachChar in self.stringToCheck:
                self.stringStack.push(eachChar)
            
            #print self.stringStack.printStack()
            for eachChar in self.stringToCheck:
                if eachChar != self.stringStack.pop():
                    booleanValue = False
		
	    # return boolean
            return booleanValue
