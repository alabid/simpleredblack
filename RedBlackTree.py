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

This code is mostly a port of the one at 
en.literateprograms.org/Red-black_tree_(Java)
"""
from TreeNode import *
from VerifyRBTree import *

class RedBlackTree:
    def __init__(self):
        self.root = None
        
    # looks for a node with a certain value
    # returns the node if found; else returns
    # None; useful later for other operations
    # like insert and delete
    def lookup(self, value):
        node = self.root

        while node != None:
            if value == node.value:
                return node
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return node

    # printhelper
    # helper function for print that does the
    # real job putting indentation where
    # necessary
    def printhelper(self, node, indent):
        INDENT_STEP = 4

        if node == None:
            print "<empty tree>",
            return
        if node.right != None:
            self.printhelper(node.right, indent + INDENT_STEP)
        for i in range(0, indent):
            print " ",
        if node.color == COLOR.BLACK:
            print node.key
        else:
            print "<" + node.key + ">"
        if node.left != None:
            self.printhelper(node.left, indent + INDENT_STEP)
    
    def simpleinorderprinthelper(self, node):
        if node != None:
            self.simpleinorderprinthelper(node.left)
            print node.value,
            self.simpleinorderprinthelper(node.right)
            
    def simpleinorderprint(self, node):
        print "{",
        self.simpleinorderprinthelper(node)
        print "}"
            
    # printTree-
    # very useful print function
    def printTree(self):
        self.simpleinorderprint(self.root)
        print
        # self.printhelper(self.root, 0)
    
    ####### rotations #########
    # both insertion and deletion rely on a 
    # fundamental operation for reducing
    # tree height called a rotation.
    # a rotation locally changes the structure
    # of the tree without changing the in-order
    # order of the sequence of values it stores
    
    def rotateleft(self, node):
        r = node.right
        self.replacenode(node, r)
        node.right = r.left
        if r.left != None:
            r.left.parent = node
        r.left = node
        node.parent = r

    def rotateright(self, node):
        l = node.left
        self.replacenode(node,l)
        node.left = l.right
        if l.right != None:
            l.right.parent = node
        l.right = node
        node.parent = l

    # helper function that cuts a node away from
    # its parent, substituting a new node
    # (or None) in its place.
    # It simplifies consistent updating
    # of parent and child pointers.
    def replacenode(self, oldnode, newnode):
        if oldnode.parent == None:
            self.root = newnode
        else:
            if oldnode == oldnode.parent.left:
                oldnode.parent.left = newnode
            else:
                oldnode.parent.right = newnode

        if newnode != None:
            newnode.parent = oldnode.parent

    ############################


    # contains -
    # checks if this tree contains
    # a node with value val
    def contains(self, val):
        return self.lookup(val) != None 

    # maximumnode -
    # helper fo find the last non-leaf
    def maximumnode(self, node):
        assert(node != None)
        while node.right != None:
            node = node.right
        return node


    # delete -
    # deletes the node with value val 
    # from the red black tree
    def delete(self, val):
        node = self.lookup(val)
        
        if node == None:
            return
        if node.left != None and node.right != None:
            # copy value from predecessor and then delete
            # it instead
            pred = self.maximumnode(node.left)
            node.value = pred.value
            node = pred

        assert(node.left == None or node.right == None)
        child = node.left if node.right == None else node.right

        if node.right == None:
            node.child = node.left
        else:
            node.child = node.right
            
        if nodecolor(node) == COLOR.BLACK:
            node.color = nodecolor(child)
            self.deletecase1(node)
            
        self.replacenode(node, child)

        if nodecolor(self.root) == COLOR.RED: 
            self.root.color = COLOR.BLACK
        verifyProperties(self.root)

    # deletecase1 -
    # node becomes the root node
    def deletecase1(self, node):
        if node.parent == None:
            return
        else:
            self.deletecase2(node)

    # deletecase2 -
    # node has a red sibling
    # exchange colors of the parent and sibling, then
    # rotate about the parent so that the sibling
    # becomes the parent of its former parent
    def deletecase2(self, node):
        if nodecolor(node.sibling()) == COLOR.RED:
            node.parent.color = COLOR.RED
            node.sibling().color = COLOR.BLACK
            if node == node.parent.left:
                self.rotateleft(node.parent)
            else:
                self.rotateright(node.parent)
        self.deletecase3(node)

    # deletecase3 -
    # node's parent, sibling, and sibling's children
    # are black. Paint the sibling red.
    # Now all paths passing through node's parent
    # have one less black node than before the deletion,
    # so we must recursively run this procedure from case
    # 1 on node's parent
    def deletecase3(self, node):
        if nodecolor(node.parent) == COLOR.BLACK and \
                         nodecolor(node.sibling()) == COLOR.BLACK and \
                         nodecolor(node.sibling().left) == COLOR.BLACK and \
                         nodecolor(node.sibling().right) == COLOR.BLACK:
            node.sibling().color = COLOR.RED
            self.deletecase1(node.parent)
        else:
            self.deletecase4(node)

    # deletecase4 -
    # node's sibling and sibling's children are black
    # but its parent is red. Exchange the color
    # of its sibling and parent; this restores the
    # red black tree properties
    def deletecase4(self, node):
        if nodecolor(node.parent) == COLOR.RED and \
                nodecolor(node.sibling()) == COLOR.BLACK and \
                nodecolor(node.sibling().left) == COLOR.BLACK and \
                nodecolor(node.sibling().right) == COLOR.BLACK:
            node.sibling().color = COLOR.RED
            node.parent.color = COLOR.BLACK
        else:
            self.deletecase5(node)

    # deletecase5 -
    # node's sibling S is black, S's left child is red
    # S's right child is black, and node is the left
    # child of its parent. Exchange the colors of S
    # and its left sibling and rotate right at S
    # handle the mirror condition
    def deletecase5(self, node):
        if node == node.parent.left and \
                nodecolor(node.sibling()) == COLOR.BLACK and \
                nodecolor(node.sibling().left) == COLOR.RED and \
                nodecolor(node.sibling().right) == COLOR.BLACK:
            node.sibling().color = COLOR.RED
            node.sibling().left.color = COLOR.BLACK
            self.rotateright(node.sibling())
        elif node == node.parent.right and \
                nodecolor(node.sibling()) == COLOR.BLACK and \
                nodecolor(node.sibling().right) == COLOR.RED and \
                nodecolor(node.sibling().left) == COLOR.BLACK:
            node.sibling().color = COLOR.RED
            node.sibling().right.color = COLOR.BLACK
            self.rotateleft(node.sibling())

        self.deletecase6(node)

    # deletecase6 -
    # there are two analogous cases:
    # first, node's sibling S is black, S's
    # right child is red, and node is the
    # left child of its parent. Exchange
    # the color of node's parent and sibling.
    # Make S's right child black, then rotate 
    # at node's parent
    # Handle the mirror case analogously
    def deletecase6(self, node):
        node.sibling().color = nodecolor(node.parent)
        node.parent.color = COLOR.BLACK
        if node == node.parent.left:
            assert(nodecolor(node.sibling().right) == COLOR.RED)
            node.sibling().right.color = COLOR.BLACK
            self.rotateleft(node.parent)
        else:
            assert(nodecolor(node.sibling().left) == COLOR.RED)
            node.sibling().left.color = COLOR.BLACK
            self.rotateright(node.parent)
        

    # insert -
    # inserts a new node with value, val
    def insert(self, val):
        newnode = Node(val, None, None, COLOR.RED)

        if self.root == None:
            self.root = newnode
        else:
            node = self.root
            while True:
                if val == node.value:
                    return
                elif val < node.value:
                    if node.left == None:
                        node.left = newnode
                        break
                    else:
                        node = node.left
                else:
                    if node.right == None:
                        node.right = newnode
                        break
                    else:
                        node = node.right
            newnode.parent = node

        self.insertcase1(newnode)
        verifyProperties(self.root)

    # insertcase1 -
    # the node inserted is the root node
    def insertcase1(self, node):
        if node.parent == None:
            node.color = COLOR.BLACK
        else:
            self.insertcase2(node)
    
    # insertcase2 -
    # the node inserted has a black parent
    # all properties still satisfied
    def insertcase2(self, node):
        if nodecolor(node.parent) == COLOR.BLACK:
            return
        else:
            self.insertcase3(node)
            
    # insertcase3 -
    # handle the case where both the parent and 
    # uncle of the new node are both red
    # then recolor both to black
    # and then recolor the grandparent
    # of this node to red.
    # Then recursively try to make any structural
    # fixes.
    def insertcase3(self, node):
        if nodecolor(node.uncle()) == COLOR.RED:
            node.parent.color = COLOR.BLACK
            node.uncle().color = COLOR.BLACK
            node.grandparent().color = COLOR.RED
            self.insertcase1(node.grandparent())
        else:
            self.insertcase4(node)

    # insertcase4 -
    # so uncle of the new node is black
    # if the new node is the right child of 
    # its parent and the parent is the left
    # child of the grandparent, rotate the
    # new node left about its parent
    # Handle mirror case too.
    def insertcase4(self, node):
        if node == node.parent.right and \
                node.parent == node.grandparent().left:
            self.rotateleft(node.parent)
            node = node.left
        elif node == node.parent.left and \
                node.parent == node.grandparent().right:
            self.rotateright(node.parent)
            node = node.right
        self.insertcase5(node)
        
    # insertcase5 -
    # final case: the new node is the left child
    # of its parent and the parent is the left
    # child of the grandparent. Rotate right about
    # grand parent. Handle mirror case too.
    def insertcase5(self, node):
        node.parent.color = COLOR.BLACK
        node.grandparent().color = COLOR.RED
        if node == node.parent.left and \
                node.parent == node.grandparent().left:
            self.rotateright(node.grandparent())
        else:
            assert(node == node.parent.right and \
                       node.parent == node.grandparent().right)
            self.rotateleft(node.grandparent())

