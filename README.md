
SimpleRedBlack
==============

An implementation of a red black tree in python
 for my "Probabilistic Data Structures" class.

This implementation was made mostly to compare
and contrast the running times of a balanced
binary search tree (such as a red black tree)
and a skip list. 

Both the skip list and the red black tree
implementation carry out the following
operations:
* contains(x) -> returns True if the data
structure contains x. Else returns False
* insert(x) -> inserts x into the data
structure
* delete(x) -> delete x from the data
structure

But the amortized running times of these
operations differ. This difference will
be detailed in my upcoming report based
on measure tests on these data
structures.