'''
Created on Aug 16, 2013

@author: Stanley Wong
'''
from treeNode import Node

class BinarySearchTree(object):

    def __init__(self):
        self.root = None
      
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
                    
    def printInOrder(self, currentNode):
        if currentNode == None:
            return
        else:
            self.printInOrder(currentNode.left)
            print currentNode
            self.printInOrder(currentNode.right)
