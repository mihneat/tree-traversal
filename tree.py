from node import Node
import unittest


class Tree:
    """ Tree class for binary tree """

    def __init__(self):
        """ Constructor for Tree class """
        self.root = None

    def getRoot(self):
        """ Method for get root of the tree """
        return self.root

    def add(self, data):
        """ Method for add data to the tree """
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        """Method for add data to the tree

        Args:
            data (int): data to add

        Returns:
            None
        """
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        """Method for find data in the tree

        Args:
            data (int): data to find

        Returns:
            Node: node with data
        """
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        if data == node.data:
            return node
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)

    def deleteTree(self):
        """ Method for deleting a tree object

        Args:
            None

        Returns:
            None
        """
        self.root = None

    def printTree(self):
        """ Method for printing the data contained within the tree

        Args:
            None

        Returns:
            None
        """
        if self.root is not None:
            self._printInorderTree(self.root)

    def _printInorderTree(self, node):
        """ Inner helper method for printing the tree inorder

        Args:
            node (Node): the node to begin the traversal from

        Returns:
            None
        """
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ')
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        """ Inner helper method for printing the tree preorder

        Args:
            node (Node): the node to begin the traversal from

        Returns:
            None
        """
        if node is not None:
            print(str(node.data) + ' ')
            self._printPreorderTree(node.left)
            self._printPreorderTree(node.right)

    def _printPostorderTree(self, node):
        """ Inner helper method for printing the tree postorder

        Args:
            node (Node): the node to begin the traversal from

        Returns:
            None
        """
        if node is not None:
            self._printPostorderTree(node.left)
            self._printPostorderTree(node.right)
            print(str(node.data) + ' ')

class TestTree(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        self.tree.add(3)
        self.tree.add(4)
        self.tree.add(0)
        self.tree.add(8)
        self.tree.add(2)

    def test__find(self):
        foundNode = self.tree._find(4, self.tree.root)
        self.assertEqual(foundNode.data, 4)
        self.assertIsNotNone(foundNode)
        
        notFoundNode = self.tree._find(9, self.tree.root)
        self.assertIsNone(notFoundNode)
