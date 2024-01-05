# %% imports
from collections import deque

# %% definitions
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left: Node = None
        self.right: Node = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Node = None

    def insert(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
            return self
        node_now = self.root
        while value != node_now.value:
            if value < node_now.value:
                if not node_now.left:
                    node_now.left = node
                    break
                node_now = node_now.left
            else:
                if not node_now.right:
                    node_now.right = node
                    break
                node_now = node_now.right
        return self

    def contains(self, value):
        node_now = self.root
        while node_now:
            if value == node_now.value:
                return True
            if value < node_now.value:
                node_now = node_now.left
            else:
                node_now = node_now.right
        return False

    def remove(self, value, start=None, parent=None):
        current = start or self.root
        while current and current.value != value:
            parent = current
            if value < current.value:
                current = parent.left
            else:
                current = parent.right
        if not current:
            raise Exception("item not in the tree")
        if not current.left and not current.right:
            return self._remove_node_no_child(current, parent)
        if current.left and current.right:
            return self._remove_node_two_child(current)
        return self._remove_node_one_child(current, parent)

    def _remove_node_no_child(self, current, parent):
        if current == self.root:
            self.root = None
            return self
        if current == parent.left:
            parent.left = None
        if current == parent.right:
            parent.right = None
        return self

    def _remove_node_one_child(self, current, parent):
        if current == self.root:
            self.root = current.right if current.right else current.left
            return self
        if current == parent.left:
            parent.left = current.right if current.right else current.left
        else:
            parent.right = current.right if current.right else current.left
        return self

    def _remove_node_two_child(self, current):
        successor = self._get_successor(current)
        current.value = successor.value
        return self.remove(current.value, start=current.right, parent=current)

    @staticmethod
    def _get_successor(current):
        successor = current.right
        while successor and successor.left:
            successor = successor.left
        return successor
    
    def breath_first_traversal(self):
        if not self.root:
            raise Exception("tree is empty")
        queue = deque()
        queue.append(self.root)
        visited = []
        while queue:
            visited_node = queue.popleft()
            visited.append(visited_node.value)
            if visited_node.left:
                queue.append(visited_node.left)
            if visited_node.right:
                queue.append(visited_node.right)
        return visited

    def dft_pre_order_iterative(self):
        if not self.root:
            raise Exception("tree is empty")
        stack = deque()
        stack.append(self.root)
        visited = []
        while stack:
            visited_node = stack.pop()
            visited.append(visited_node.value)
            if visited_node.left:
                stack.append(visited_node.left)
            if visited_node.right:
                stack.append(visited_node.right)
        return visited


# %%
btree = BinarySearchTree()
btree.insert(2)
btree.insert(4)
btree.insert(1)
btree.insert(3)
btree.insert(5)

# btree.remove(4)
# btree.root.value
# btree.root.left.value
# btree.root.right.right
# btree.root.right.value
btree.dft_pre_order_iterative()
