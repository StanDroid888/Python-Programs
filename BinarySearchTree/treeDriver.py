'''
Programmer: Stanley Wong
Description: Binary Search Tree Driver

'''
from treeNode import Node
from tree import BinarySearchTree

myTree = BinarySearchTree()

myTree.add(10)
myTree.add(7)
myTree.add(5)
myTree.add(3)
myTree.add(4)
myTree.add(1)
myTree.add(2)
myTree.add(8)
myTree.add(9)
 
myTree.add(13)
myTree.add(12)
myTree.add(16)
myTree.add(20)
myTree.add(18)
myTree.add(22)
myTree.add(19)
 
 
print "\nOriginal List"

myTree.printInOrder(myTree.root)
print "\ncount: %d" % myTree.count


print ""

myTree.deleteNode(16)
myTree.deleteNode(9)
myTree.deleteNode(1)
myTree.deleteNode(2)
myTree.deleteNode(7)
myTree.deleteNode(20)
myTree.deleteNode(10)

print "\nTree after Deletions"
myTree.printInOrder(myTree.root)
print "\ncount: %d" % myTree.count

print ""
print "program ended"
