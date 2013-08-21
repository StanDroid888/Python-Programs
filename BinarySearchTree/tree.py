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
    # Iterative version
    def addNode(self, dataValue):
        
        currentNode = self.root
        locationFound = False
        
        # Check to see if Node is already on the Tree
        if self.find(dataValue) == True:
            print "CAN'T ADD DUPLICATE NODE ONTO TREE"
            return
        
        # Check to see if tree is Empty
        if currentNode == None:
            self.root = Node(dataValue)
            print "Added Root Node %s" % str(dataValue)
            locationFound = True
        else:
            while locationFound == False:
                if dataValue > currentNode.data:
                    if currentNode.right == None:
                        currentNode.right = Node(dataValue)
                        print "Added Node %s" % str(dataValue)
                        locationFound = True
                    else:
                        currentNode = currentNode.right
                elif dataValue < currentNode.data:
                    if currentNode.left == None:
                        currentNode.left = Node(dataValue)
                        print "Added Node %s" % str(dataValue)
                        locationFound = True
                    else:
                        currentNode = currentNode.left
    
    # Inserts a Node on to the BST
    # Recursive Version
    def addRecusively(self, currentNode, dataValue):
        
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
            print currentNode.data,
            self.printInOrder(currentNode.right)
            
    # Output the tree PRE order
    def printPreOrder(self, currentNode):
        if currentNode == None:
            return
        else:
            print currentNode.data,
            self.printInOrder(currentNode.left)
            self.printInOrder(currentNode.right)
            
    # Output the tree POST order
    def printPostOrder(self, currentNode):
        if currentNode == None:
            return
        else:
            self.printInOrder(currentNode.left)
            self.printInOrder(currentNode.right)
            print currentNode.data,
            
    # Returns a boolean base on if an element is
    # in the Binary Search Tree
    def find(self, dataToFindValue):
        
        foundData = False
        
        # If tree is empty, just return False
        if self.root != None:
            currentNode = self.root
        else:
            return False
        
        # Binary Tree is empty, 
        # so return False
        if self.root != None:
            while foundData == False:
                if currentNode == None:
                    return False
                elif currentNode.data == dataToFindValue:
                    return True 
                elif dataToFindValue > currentNode.data:
                    currentNode = currentNode.right
                elif dataToFindValue < currentNode.data:
                    currentNode = currentNode.left

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
            if previousNode.data < currentNode.data:
                previousNode.right = None
            else:
                previousNode.left = None
            
        elif currentNode.left != None and currentNode.right != None:
            
            # Delete Node with Two children
            # Need to fix
            currentNode.data = self.findMin(currentNode.right)
            
            currentNode = currentNode.right
            
            while currentNode.left != None:
                previousNode = currentNode
                currentNode = currentNode.left
            
            if currentNode.right != None:
                if previousNode.data < currentNode.data:
                    previousNode.right = currentNode.right
                else:
                    previousNode.left = currentNode.right
            else:
                previousNode.left = None
                                
        elif currentNode.left != None and currentNode.right == None:
            # Delete Node with Left child
            if currentNode.data < previousNode.data:
                previousNode.left = currentNode.left
            else:
                previousNode.right = currentNode.left
            
        elif currentNode.left == None and currentNode.right != None:
            # Delete Node with Right child
            if currentNode.data < previousNode.data:
                previousNode.left = currentNode.right
            else:
                previousNode.right = currentNode.right
