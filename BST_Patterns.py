
from visitor import Visitor
from abc import ABC, abstractmethod
from nullobject import bst_null
from visitable import Visitable
from visitor_class import Visitor1

class Strategy(ABC):
    """Strategy interface"""

    @abstractmethod
    def insert(self,key,value):
        """Each strategy class will provide its own implementation using this function."""
        pass

class Student():
    def __init__(self, redid=None,firstname="",lastname="", gpa=None):
        self.redid = redid
        self.firstname = firstname
        self.lastname = lastname
        self.gpa = gpa

class Node(Visitable):
    def __init__(self, key=None):
        self.left = None
        self.right = None
        self.val = key

    def accept(self, visitor: Visitor) -> None:
        visitor.longest_path(self)

class StudentNodes(Strategy):
    """Strategy class to insert the student details as node in the Binary search tree based on redid"""
    def insert(self,root,key):
        #Null object check for Binary search tree
        if bst_null.null_check(root):
            root = Node()
            root.val = key
            print(root.val.redid, root.val.firstname, root.val.lastname, root.val.gpa, " \tData for student object in BST")
            return root
        else:
            if root.val.redid < key.redid:
                root.right = self.insert(root.right,key)
            else:
                root.left = self.insert(root.left,key)
        return root
class StudentOrderByName:
    """Strategy Class to insert the student object in the binary search tree based on lastname and then by firstname if two lastnames are equal """
    def insert(self,root,key):
        # Null object check for Binary search tree
        if bst_null.null_check(root):
            root = Node()
            root.val=key
            print(root.val.redid, root.val.firstname, root.val.lastname, root.val.gpa)
            return root
        else:
            if root.val.lastname < key.lastname:
                root.right = self.insert(root.right,key)
            elif root.val.lastname == key.lastname:
                if root.val.firstname < key.firstname:
                    root.right= self.insert(root.right, key)
                else:
                    root.left= self.insert(root.left, key)
            else:
                root.left = self.insert(root.left, key)
        return root
class StudentOrderByGPA:
    """Strategy Class to insert the student object in the binary search tree based on rounded GPA and redid of GPA is equal"""
    def insert(self,root,key):
        if bst_null.null_check(root):
            root = Node()
            root.val = key
            print(root.val.redid, root.val.firstname, root.val.lastname, root.val.gpa)
            return root
        else:
            if round(root.val.gpa) < round(key.gpa):
                root.right = self.insert(root.right,key)
            elif root.val.gpa == key.gpa:
                if root.val.redid < key.redid:
                    root.right=self.insert(root.right,key)
                else:
                    root.left=self.insert(root.left,key)
            else:
                root.left = self.insert(root.left,key)
        return root

class SortStudentByRedid():
   """Inorder function with internal iterator for printing the elements of node in a Binary """
   def inorder_traversal(self,root):
      if root:
          self.inorder_traversal(root.left)
          print(root.val.gpa,":Inorder Order on GPA")
          self.inorder_traversal(root.right)
          ls = []
          ls.append(root.val.redid)
          ls1=(lambda x:x ,ls)

class Inserttree:
    """Context class for strategy"""
    def __init__(self, condition_check):
        self._condition_check = condition_check

    def insert_tree(self, root,key):
        return self._condition_check.insert(root,key)



node_object=Node()
root=None

""" Use a particular strategy pattern based on user input"""
strategy_pattern = input("Enter the strategy to be called \n 1.Insert by Redid \n 2.Insert by name \n 3.Insert by gpa\n")
if  strategy_pattern == '1':
    student_insert = StudentNodes()
    inserted_node=Inserttree(student_insert)

elif strategy_pattern== '2':
    student_name=StudentOrderByName()
    inserted_node = Inserttree(student_name)

else :
    student_gpa = StudentOrderByGPA()
    inserted_node=Inserttree(student_gpa)

"""Details of Students to be inserted """
root = inserted_node.insert_tree(root, Student(1,'John',"Carl",2.5))
root = inserted_node.insert_tree(root, Student(2,'Shweta',"S",2.9))
root = inserted_node.insert_tree(root, Student(3, 'Max', "Carver",4))
root = inserted_node.insert_tree(root, Student(4,'Alla',"Hoffman",3.8))


"""Visitor  for the longest path and average path length in the tree"""
visitor1 = Visitor1()
longest_path_tree=visitor1.longest_path(root)
average_path_count=visitor1.average_path(root)
print("\nAverage path count is\t",round(average_path_count))
n = len(longest_path_tree)
print('length of longest path is ',n,'and the path is\t')
print(longest_path_tree[n - 1], end = "")
for i in range(n - 2, -1, -1):
        print(" ->", longest_path_tree[i], end = "")

"""Count number of null nodes visitor"""
single_nodes=visitor1.single_node_count(root)
leaf_nodes=visitor1.leaf_count(root)
total_null_nodes=single_nodes+leaf_nodes
print("\ntotal null nodes",total_null_nodes)
a=SortStudentByRedid()
a.inorder_traversal(root)



