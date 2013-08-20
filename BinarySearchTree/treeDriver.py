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
myTree.addNode(12)
myTree.addNode(5)
myTree.addNode(1)
myTree.addNode(3)
myTree.addNode(9)
myTree.addNode(13)
myTree.addNode(10)
myTree.addNode(14)



 
myTree.printInOrder(myTree.root)

print ""




print ""
print "program ended"
