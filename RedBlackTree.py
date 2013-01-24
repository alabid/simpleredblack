"""
RedBlackTree.py
Contains an implementation of a red black tree

Properties of a Red black tree:
1. Every node is either red or black.
2. The root is black.
3. All leaves (NIL) are black.
4. Both children of every red node is black.
5. Every simple path from any given node to any of its
descendent leaves contains the same number of black
nodes.
"""
from TreeNode import *


class RBTree:
    #### constants
    VERIFY_RBTREE = True

    def __init__(self):
        pass

    # verifyproperties -
    # verifies that an instance of this
    #  RedBlackTree does fulfill the
    # conditions of a standard RedBlackTree
    def verifyProperties():
        if VERIFY_RBTREE:
            verifyProperty1(self.root)
            verifyProperty2(self.root)
            # Property 3 is implicit
            verifyProperty3(self.root)
            verifyProperty4(self.root)
            verifyProperty5(self.root)



