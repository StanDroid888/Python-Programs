'''
Programmer: Stanley Wong
Description: Binary Search Tree Driver

'''
from treeNode import Node
from tree import BinarySearchTree

myTree = BinarySearchTree()

myTree.addNode(10)
myTree.addNode(7)
myTree.addNode(5)
myTree.addNode(3)
myTree.addNode(4)
myTree.addNode(1)
myTree.addNode(2)
myTree.addNode(8)
myTree.addNode(9)

myTree.addNode(13)
myTree.addNode(12)
myTree.addNode(16)
myTree.addNode(20)
myTree.addNode(18)
myTree.addNode(22)
myTree.addNode(19)
 
 
print "\nOriginal List"

myTree.printInOrder(myTree.root)

print ""

myTree.deleteNode(16)
myTree.deleteNode(9)
myTree.deleteNode(1)
myTree.deleteNode(2)



myTree.printInOrder(myTree.root)

print ""
print "program ended"
