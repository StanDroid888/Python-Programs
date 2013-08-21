'''
Programmer: Stanley Wong
Description: Binary Search Tree Driver

'''
from treeNode import Node
from tree import BinarySearchTree

myTree = BinarySearchTree()

myTree.addNode(8)
myTree.addNode(4)
myTree.addNode(12)
myTree.addNode(2)
#myTree.addNode(12)
myTree.addNode(5)
myTree.addNode(1)
myTree.addNode(3)
myTree.addNode(9)
myTree.addNode(13)
myTree.addNode(10)
myTree.addNode(14)
myTree.addNode(8.5)
 
myTree.printInOrder(myTree.root)

print ""

myTree.deleteNode(9)

#===============================================================================
# myTree.deleteNode(1)
# myTree.deleteNode(14)
# myTree.deleteNode(10)
# myTree.deleteNode(3)
# myTree.deleteNode(9)
#===============================================================================


myTree.printInOrder(myTree.root)

print ""
print "program ended"
