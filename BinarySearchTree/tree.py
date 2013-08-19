'''
Created on Aug 16, 2013

@author: Stanley Wong
'''
from treeNode import Node

class BinarySearchTree(object):

    # Initalization/Constructor
    def __init__(self):
        self.root = None
    
    # Inserts a Node on to the BST
    def add(self, currentNode, data):
        # Check to see if tree is Empty
        if currentNode == None:
            self.root = Node(data)
            print "Added Root Node %s" % str(data)
        # Add a node onto the tree
        else:
            if data > currentNode.data:
                if currentNode.right == None:
                    currentNode.right = Node(data)
                    print "Added Node %s" % str(data)
                else:
                    self.add(currentNode.right,data)
            elif data < currentNode.data:
                if currentNode.left == None:
                    currentNode.left = Node(data)
                    print "Added Node %s" % str(data)
                else:
                    self.add(currentNode.left,data)
                    
    # Output the tree in order
    def printInOrder(self, currentNode):
        if currentNode == None:
            return
        else:
            self.printInOrder(currentNode.left)
            print currentNode
            self.printInOrder(currentNode.right)
            
    # Returns a boolean base on if an element is
    # in the BST
    def find(self, dataToFind):
        
        foundData = False
        currentNode = self.root
        
        while foundData == False:
            if currentNode.data == dataToFind:
                foundData = True
                break
            elif dataToFind > currentNode.data:
                currentNode = currentNode.right
            elif dataToFind < currentNode.data:
                currentNode = currentNode.left
            elif currentNode == None:
                foundData = False
                break
        
        # Return boolean     
        return foundData
    
    # Return the minium value in the tree
    # starting at Node which was passed in
    # as the parameter.  
    def minNode(self, currentNode):
        
        while(currentNode.left != None): 
            currentNode = currentNode.left
            
        return currentNode.data
    
    # Delete a node from Tree
    def deleteNode(self,valueToDelete):
        
        previousNode = currentNode = self.root
        
        # Check if value is actually in 
        # the binary search tree.
        if (self.find(valueToDelete)):
            
            while currentNode.data != valueToDelete:
                if valueToDelete > currentNode.data:
                    previousNode = currentNode
                    currentNode = currentNode.right
                elif valueToDelete < currentNode.data:
                    previousNode = currentNode
                    currentNode = currentNode.left
                else:
                    print "Error!!"
                    
        print "Deleting...%s" % currentNode
        
        if currentNode.left == None and currentNode.right == None:
            if previousNode.left > currentNode.data:
                previousNode.left = None
            else:
                previousNode.right = None
        else:
            currentNode.data = self.minNode(currentNode)