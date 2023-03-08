# Binary_Search_Tree_Python_Implementation

Implements a binary search tree with addition.
The tree contains Student objects. A student object contains first name, last name, red id, and GPA.
code implements the following patterns on your tree.
1. Internal iterator. The iterator accepts a lambda and evaluates the lambda on all of the elements in the
tree.
2. Strategy pattern to order the tree. You will implement three strategies. One to sort by Red Id. Another is
to sort by the last name and then by the first name if the two last names are equal. For the third strategy,
first round the GPA to the nearest integer. Then sort by rounded GPA and when equal use Red Id.
3. Null Object pattern to add a null node to your tree to eliminate the need to check for null references or
pointers in your tree.
4. Visitor pattern. Implement two visitors, One to count the number of null nodes. Another is to compute the
longest path in the tree and the average path length in the tree.
