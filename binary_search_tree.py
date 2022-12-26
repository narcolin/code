from queue_array import Queue


class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self):  # Returns empty BST
        self.root = None

    def is_empty(self):  # returns True if tree is empty, else False
        return self.root is None

    def search(self, key):  # returns True if key is in a node of the tree, else False
        tree = self.root
        while tree is not None:
            if key > tree.key:
                tree = tree.right
            elif key == tree.key:
                return True
            else:
                tree = tree.left
        return False

    def insert(self, key, data=None):  # inserts new node w/ key and data
        # If an item with the given key is already in the BST,
        # the data in the tree will be replaced with the new data
        tree = self.root
        if tree is None:
            node = TreeNode(key, data)
            node.key = key
            node.data = data
            self.root = node
            return
        while tree is not None:
            if key > tree.key:
                if tree.right:
                    tree = tree.right
                else:
                    tree.right = TreeNode(key, data)
                    return
            elif key < tree.key:
                if tree.left:
                    tree = tree.left
                else:
                    tree.left = TreeNode(key, data)
                    return
            elif tree.key == key:
                tree.data = data
                return

    def find_min(self):  # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        tree = self.root
        if tree is None:
            return None
        while tree.left is not None:
            tree = tree.left
        return tree.key, tree.data

    def find_max(self):  # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        tree = self.root
        if tree is None:
            return None
        while tree.right is not None:
            tree = tree.right
        return (tree.key, tree.data)

    def tree_height(self):  # return the height of the tree
        # returns None if tree is empty
        tree = self.root
        height = self.tree_height_helper(tree) - 1
        if height < 0:
            return None
        else:
            return height
    def tree_height_helper(self, tree):
        if tree is None:
            return 0
        left_height = self.tree_height_helper(tree.left)
        right_height = self.tree_height_helper(tree.right)
        height = max(left_height, right_height) + 1
        return height

    def inorder_list(self):  # return Python list of BST keys representing in-order traversal of BST
        return self.inorder_list_helper(self.root, [])

    def inorder_list_helper(self, tree, li):
        if tree is None:
            return []
        self.inorder_list_helper(tree.left, li)
        li.append(tree.key)
        self.inorder_list_helper(tree.right, li)
        return li

    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        return self.preorder_list_helper(self.root, [])

    def preorder_list_helper(self, tree, li):
        if tree is None:
            return []
        li.append(tree.key)
        self.preorder_list_helper(tree.left, li)
        self.preorder_list_helper(tree.right, li)
        return li

    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000)  # Don't change this!
        tree = self.root
        if not tree:
            return []
        li = []
        q.enqueue(tree)
        while not q.is_empty():
            tree = q.dequeue()
            li.append(tree.key)
            if tree.left is not None:
                q.enqueue(tree.left)
            elif tree.right is not None:
                q.enqueue(tree.right)
        return li
