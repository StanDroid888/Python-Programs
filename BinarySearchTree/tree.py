'''
Programmer: Stanley Wong
Module: BinarySearchTree
Description: Binary Search Tree Module

'''
from treeNode import Node

class BinarySearchTree(object):

    # Constructor
    def __init__(self):
        self.root = None
    
    # Inserts a Node on to the BST
    def add(self, currentNode, dataValue):
        # Check to see if tree is Empty
        if currentNode == None:
            self.root = Node(dataValue)
            print "Added Root Node %s" % str(dataValue)
        # Add a node onto the tree
        else:
            if dataValue > currentNode.data:
                if currentNode.right == None:
                    currentNode.right = Node(dataValue)
                    print "Added Node %s" % str(dataValue)
                else:
                    self.add(currentNode.right, dataValue)
            elif dataValue < currentNode.data:
                if currentNode.left == None:
                    currentNode.left = Node(dataValue)
                    print "Added Node %s" % str(dataValue)
                else:
                    self.add(currentNode.left, dataValue)
                    
    # Output the tree IN order
    def printInOrder(self, currentNode):
        if currentNode == None:
            return
        else:
            self.printInOrder(currentNode.left)
            print currentNode
            self.printInOrder(currentNode.right)
            
    # Output the tree PRE order
    def printPreOrder(self, currentNode):
        if currentNode == None:
            return
        else:
            print currentNode
            self.printInOrder(currentNode.left)
            self.printInOrder(currentNode.right)
            
    # Output the tree POST order
    def printPostOrder(self, currentNode):
        if currentNode == None:
            return
        else:
            self.printInOrder(currentNode.left)
            self.printInOrder(currentNode.right)
            print currentNode
            
    # Returns a boolean base on if an element is
    # in the Binary Search Tree
    def find(self, dataToFindValue):
        
        foundData = False
        currentNode = self.root
        
        while foundData == False:
            if currentNode.data == dataToFindValue:
                foundData = True
                break
            elif dataToFindValue > currentNode.data:
                currentNode = currentNode.right
            elif dataToFindValue < currentNode.data:
                currentNode = currentNode.left
            elif currentNode == None:
                foundData = False
                break
        
        # Return boolean     
        return foundData
    
    # Return the minimum value in the tree
    # starting at Node which was passed in
    # as the parameter.  
    def findMin(self, currentNode):
        
        while(currentNode.left != None): 
            currentNode = currentNode.left
            
        return currentNode.data
    
    
    # Returns the parent of the Node with 
    # the specified data value.
    def findParent(self, childDataValue):
        
        foundChild = False
        currentNode = self.root
        
        while foundChild == False:
            if currentNode.left.data == childDataValue or currentNode.right.data == childDataValue:
                foundChild = True
                break
            elif childDataValue > currentNode.data:
                currentNode = currentNode.right
            elif childDataValue < currentNode.data:
                currentNode = currentNode.left
            elif currentNode == None:
                print "error"
                break
        
        # Return boolean     
        return currentNode
        
    # Delete the Node from the Binary Search Tree
    # which has the specified value specified as an
    # argument. 
    def deleteNode(self, deleteValue):
        
        previousNode = currentNode = self.root
        
        # Request to Delete Node
        if self.root.data == deleteValue:
            
            ### TO DO: Fix deletion of Root
            print "Can't delete Root right now!!"
            return
            
        # Check if value is actually in 
        # the binary search tree.
        if (self.find(deleteValue)):
            
            # Find where the Node to be deleted is
            # located. 
            while currentNode.data != deleteValue:
                if deleteValue > currentNode.data:
                    previousNode = currentNode
                    currentNode = currentNode.right
                elif deleteValue < currentNode.data:
                    previousNode = currentNode
                    currentNode = currentNode.left
                else:
                    print "Error!!"
        
        # Now that the right spot has been found,
        # process the Node deletion.             
        print "Deleting...%s" % currentNode
     
        if currentNode.left == None and currentNode.right == None:
            
            # Delete Node with no children
            if previousNode.data > currentNode.data:
                previousNode.left = None
            else:
                previousNode.right = None  
                
        elif currentNode.left != None and currentNode.right == None:
            
            # Delete Node with only one child on the Left
            previousNode.left = currentNode.left

        elif currentNode.left == None and currentNode.right != None:
            
            # Delete Node with only one child on the Right
            previousNode.right = currentNode.right
            
        else:
            
            # Delete Node that has two children. 
            if previousNode.data > currentNode.data:
                currentNode.data = self.findMin(currentNode.right)
                self.findParent(currentNode.data).right = None
            else:
                currentNode.data = self.findMin(currentNode.right)
                self.findParent(currentNode.data).left = None