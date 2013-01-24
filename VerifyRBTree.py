"""
VerifyRBTree.py
Contains functions that verify that a given
Red Black tree fulfills the properties of
a standard red black tree.
The 5 properties of the red black tree
are described below.
"""
from TreeNode import *

#### constants
VERIFY_RBTREE = True
####

# helper function to return
# the color of a node (if it's
# defined for that specific node)
# or else return BLACK (the node
# must be a leaf)
def nodecolor(node):
    if node == None: return COLOR.BLACK
    else: return node.color
    

# verifyProperties-
# verifies the 5 properties of 
# a red black tree
def verifyProperties(node):
    if VERIFY_RBTREE:
        verifyProperty1(node)
        verifyProperty2(node)
        # Property 3 is implicit
        verifyProperty4(node)
        verifyProperty5(node)

# property 1: every node is either
# red or black
def verifyProperty1(node):
    assert(nodecolor(node) == COLOR.RED \
               or nodecolor(node) == COLOR.BLACK)
    if node == None: return
    verifyProperty1(node.left)
    verifyProperty1(node.right)

# property 2: verify that the root is black
def verifyProperty2(node):
    assert(nodecolor(node) == COLOR.BLACK)

# property 3 is already verified by
# the function nodecolor
# since we make every leave black

# property 4: every red node has two
# children and both are black
def verifyProperty4(node):
    if nodecolor(node) == COLOR.RED:
        assert(nodecolor(node.left) == COLOR.BLACK)
        assert(nodecolor(node.right) == COLOR.BLACK)
        assert(nodecolor(node.parent) == COLOR.BLACK)

    if node == None: return
    verifyProperty4(node.left)
    verifyProperty4(node.right)

# verifyProperty5Helper
# helper function used by verifyProperty5
# to verify property 5
# blackcount --> the current count of black nodes along this path
# pathblackcount --> != -1: the count of black nodes from every node to a leaf
#                    == -1: just beginning traversal
def verifyProperty5Helper(node, blackcount, pathblackcount):
    if nodecolor(node) == COLOR.BLACK:
        blackcount += 1
    # reached a leaf
    if node == None:
        if pathblackcount == -1:
            # first path to the a leaf encountered
            pathblackcount = blackcount
        else:
            # have already encountered at least one path to a leaf
            assert(pathblackcount == blackcount)
        return pathblackcount

    pathblackcount = verifyProperty5Helper(node.left, blackcount, pathblackcount)
    # using pathblackcount (from left subtree), verify that every path in the
    # right subtree also contains paths of same length from the node to a leaf
    pathblackcount = verifyProperty5Helper(node.right, blackcount, pathblackcount)
    
    return pathblackcount

# property 5:every simple path from a node
# to any of its descendant leaves contains
# the same number of black nodes
def verifyProperty5(node):
    # no. of black nodes encountered is 0
    # the pathBlackCount is -1
    verifyProperty5Helper(node, 0, -1)


    


