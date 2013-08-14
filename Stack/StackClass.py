##############################################
#
# Programmer: Stanley Wong
# File: StackClass.py
# Description: Python Dynamic Stack module. 
#              Requires NodeClass.py
#
##############################################
from NodeClass import Node

class Stack:
    
    def __init__(self):
        self.head = None
        self.count = 0
    
    def push(self, data):
        newNode = Node(data)
        self.count +=1
    
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        
        self.count -=1
        
        if self.count == 1:
            returnNode = Node(self.head.data)
        elif self.count > 1:
            returnNode = Node(self.head.data)
            self.head = self.head.next
        else:
            print "Stack is Empty!!"
            return
            
        return returnNode
        
            
    def printStack(self):

        print "Number of element: %d" % self.count
        print "Stack Contents"
        print "--------------"
        currentNode = self.head

        while(currentNode != None):
            print currentNode.data
            currentNode = currentNode.next
            
        
    