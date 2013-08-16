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