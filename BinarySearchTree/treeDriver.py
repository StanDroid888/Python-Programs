'''
Programmer: Stanley Wong
Description: Binary Search Tree Driver

'''
from treeNode import Node
from tree import BinarySearchTree

myTree = BinarySearchTree()

myTree.add(myTree.root,55)
myTree.add(myTree.root, 22)
myTree.add(myTree.root, 33)
myTree.add(myTree.root, 11)
myTree.add(myTree.root, 44)
myTree.add(myTree.root, 200)
myTree.add(myTree.root, 88)
myTree.add(myTree.root, 300)
myTree.add(myTree.root, 66)
myTree.add(myTree.root, 99)
myTree.add(myTree.root, 77)
myTree.add(myTree.root, 100)

myTree.printInOrder(myTree.root)

myTree.deleteNode(44)
myTree.deleteNode(33)
myTree.deleteNode(11)
myTree.deleteNode(77)

myTree.printInOrder(myTree.root)

print "program ended"
