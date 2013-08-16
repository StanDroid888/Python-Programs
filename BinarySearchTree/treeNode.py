##############################################
#
# Programmer: Stanley Wong
# File: NodeClass.py
# Description: Python Node module to be used
#              with Stack module
#
##############################################
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
        return 'Data:%s' % self.data