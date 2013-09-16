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
        self.count = 0


    # Inserts a Node on to the BST
    # Iterative version
    def addIteratively(self, dataValue):
        
        currentNode = self.root
        locationFound = False
        
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
        
        # Increment Counter            
        self.count += 1
                        
    # Inserts a Node on to the BST
    # Recursive Version
    def addRecursively(self, currentNode, dataValue):
        
        # Check to see if tree is Empty
        if currentNode == None:
            self.root = Node(dataValue)
            print "Added Root Node %s" % str(dataValue)
            self.count += 1
        # Add a node onto the tree
        else:
            if dataValue > currentNode.data:
                if currentNode.right == None:
                    currentNode.right = Node(dataValue)
                    print "Added Node %s" % str(dataValue)
                    self.count += 1
                else:
                    self.addRecursively(currentNode.right, dataValue)
            elif dataValue < currentNode.data:
                if currentNode.left == None:
                    currentNode.left = Node(dataValue)
                    print "Added Node %s" % str(dataValue)
                    self.count += 1
                else:
                    self.addRecursively(currentNode.left, dataValue)
                    
    # Add wrapper
    def add(self, dataValue):
        
        # Check to see if Node is already on the Tree
        if self.find(dataValue) == True:
            print "CAN'T ADD DUPLICATE NODE ONTO TREE"
            return
               
        # Call implemented add Node method
        self.addRecursively(self.root, dataValue)
                    
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
        
        # Search for particular data value
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
        
        # Initialize Pointer/References
        previousNode = currentNode = self.root
        
        # Check for special case where
        # there is only the one Node on
        # the Binary Search Tree. 
        if self.count == 1:
            self.root = None
            self.count -= 1
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
        else:
            # The Node was not found on the Binary Search Tree
            print "ERROR: Attempt to DELETE a Node not on the Tree"
            return
        
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
            
            # Traverse to Node which will
            # be removed from the Binary Search Tree

            # Check if there is a need to traverse
            # to the Node to remove obsolete Node
            if currentNode.right.left != None:
                
                # Reset pointers/references
                # to sub-root will be the right Node of 
                # the value being deleted. 
                currentNode = previousNode = currentNode.right
                
                # Search until obsolete Node is reached
                while currentNode.left != None:
                    previousNode = currentNode
                    currentNode = currentNode.left
                    
                    # Obsolete Node found. Check to see 
                    # If obsolete Node has a right child,
                    # swap values of the right Node with the 
                    # obsolete Node. Afterwards, delete the 
                    # right Node.
                    if currentNode.right != None:
                        
                        # Check if the obsolete Node is a right 
                        # or left child. Then process deletion 
                        # accordingly. 
                        if previousNode.data < currentNode.data:
                            previousNode.right = currentNode.right
                            currentNode.right = None
                        else:
                            # Check if the obsolete Node is a right 
                            # or left child. Then process deletion 
                            # accordingly.
                            previousNode.left = currentNode.right
                            currentNode.right = None
                    # Obsolete Node has no right child, just delete.
                    else:
                        if previousNode.data <= currentNode.data:
                            previousNode.right = None
                        else:
                            previousNode.left = None
            # Already at obsolete Node location, 
            # just delete it.                 
            else:
                currentNode.right = None
                
        # Deletion of Node with only a LEFT child                
        elif currentNode.left != None and currentNode.right == None:
            if currentNode.data < previousNode.data:
                previousNode.left = currentNode.left
            else:
                previousNode.right = currentNode.left
        
        # Deletion of Node with only a RIGHT child 
        elif currentNode.left == None and currentNode.right != None:
            if currentNode.data < previousNode.data:
                previousNode.left = currentNode.right
            else:
                previousNode.right = currentNode.right
                
        # Decrement Counter 
        self.count -= 1