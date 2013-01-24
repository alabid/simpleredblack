"""
Contains the implementation of a Node of a 
Red-Black tree
"""

### helper enum implementation ###
def enum(**enums):
    return type('Enum', (), enums)
##################################

COLOR = enum(RED=0, BLACK=1)

"""
Implementation of a node of a red-black tree
Can either be a red node or a black node
"""
class Node:
    def __init__(self, value, left, right, color, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color
        if self.left != None: self.left.parent = self
        if self.right != None: self.right.parent = self

    # returns the grand parent of this node
    def grandparent(self):
        assert(self.parent != None)
        assert(self.parent.parent != None)
        return self.parent.parent

    # returns the "sibling" of this node - the other child 
    # of the parent of this node
    def sibling(self):
        assert(self.parent != None)
        if self == self.parent.left: 
            return self.parent.right
        else:
            return self.parent.left

    # returns the "uncle" of a node - the "sibling" of its
    # parent
    def uncle(self):
        assert(self.parent != None)
        return self.parent.sibling()
