"""
RedBlackTreeTests.py
Contains various tests to test
basic functionality of the red black tree
"""
from RedBlackTree import *


class RedBlackTreeTests:
    def __init__(self, testalgo=False):
        self.testalgorithms = testalgo
        
        self.rb = RedBlackTree()

    def run(self):
        if self.testalgorithms:
            self.rb.printTree() # should be empty
            for num in [5,10,7,6, 7, 8]:
                self.rb.insert(num)

            self.rb.printTree() # should now have [5,6,7,8,10]
            

            # should print "7 is in the list"
            if self.rb.contains(7):
                print "7 is in the list"
            else:
                print "7 is not in the list"
                
            # should print "-10 not in the list"
            if self.rb.contains(-10):
                print "-10 is in the list"
            else:
                print "-10 not in the list"
                
            # should print [5,6,7,8,10]                    
            self.rb.printTree()

            # should delete 7. 
            self.rb.delete(7)

            # should print "7 has been succesfully deleted"
            if not self.rb.contains(7):
                print "7 has been succesfully deleted"
        
            # should print [5,6,8,10]
            self.rb.printTree()

            # should delete 5
            self.rb.delete(5)
            self.rb.delete(20)

            # should print [6,8,10]
            self.rb.printTree()

            # should delete 8
            self.rb.delete(100)
            self.rb.delete(5)
            self.rb.delete(8)

            # should print [6,10]
            self.rb.printTree()

            # should delete [6, 10]
            self.rb.delete(6)
            self.rb.delete(8)
            self.rb.delete(10)
            self.rb.delete(-1)

            # should print [] (empty)
            self.rb.printTree()

            # should print False
            print self.rb.contains(8)


if __name__ == "__main__":
    RedBlackTreeTests(True).run()
