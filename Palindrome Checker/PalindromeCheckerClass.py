'''
Created on Aug 14, 2013

@author: Stanley Wong
'''
from StackClass import Stack

class PalindromeChecker:
    
        def __init__(self):
            self.stringToCheck = None
            self.stringStack = Stack()
            self.isPalindrome = False
            
        def checkWord(self, string):
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

            return booleanValue