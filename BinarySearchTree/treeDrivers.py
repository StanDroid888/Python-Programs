'''
Created on Aug 15, 2013

@author: Stanley Wong
'''
from treeNode import Node
from tree import BinarySearchTree

node3 = Node(3)

myTree = BinarySearchTree()

myTree.add(myTree.root,55)
myTree.add(myTree.root, 22)
myTree.add(myTree.root, 33)
myTree.add(myTree.root,11)
myTree.add(myTree.root, 44)
myTree.add(myTree.root, 88)

myTree.printInOrder(myTree.root)

print myTree.find(33)
print myTree.minNode(myTree.root)
#myTree.deleteNode(44)
myTree.deleteNode(22)

myTree.printInOrder(myTree.root)



print "program ended"