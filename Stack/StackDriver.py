##############################################
#
# Programmer: Stanley Wong
# File: StackDriver.py
# Description: Python Stack Driver
#
##############################################
from StackClass import Stack

myStack = Stack()

myStack.push(22)
myStack.push(33)
myStack.push(44)
myStack.pop()
myStack.push(99)
myStack.push(55)
myStack.push(88)
myStack.pop()
myStack.push(77)
myStack.push(11)
myStack.pop()
myStack.push(88)

myStack.printStack()