from visitor import Visitor


class Visitor1(Visitor):
    """Visitor  to count the number of null nodes and  to compute the longest path in the tree and the average path length in the tree."""
    def longest_path(self, root) -> None:

        if (root == None):
            return []
        rightvect = self.longest_path(root.right)
        leftvect = self.longest_path(root.left)
        if (len(leftvect) > len(rightvect)):
            leftvect.append(root.val.redid)
        else:
            rightvect.append(root.val.redid)
        if len(leftvect) > len(rightvect):
            return leftvect
        return rightvect

    def average_path(self,root):
        if (root == None):
            return 0
        rightvect = self.average_path(root.right)
        leftvect = self.average_path(root.left)
        return (rightvect+leftvect/2) +1


    def single_node_count(self, root) -> None:
        single_child_nodes = []

        if not root:
            return
        if not root.left and root.right:
            single_child_nodes.append(root)
        elif root.left and not root.right:
            single_child_nodes.append(root)
        self.single_node_count(root.left)
        self.single_node_count(root.right)
        return len(single_child_nodes)

    def leaf_count(self, root) -> None:
        if root is None:
            return 0

        if (root.left is None and root.right is None):
            return 1
        else:
            return self.leaf_count(root.left) + self.leaf_count(root.right)*2



