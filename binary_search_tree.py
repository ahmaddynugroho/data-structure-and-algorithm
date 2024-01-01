#%% definitions
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left: Node = None
        self.right: Node = None


class BinaryTree:
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


# %%
btree = BinaryTree()
btree.insert(2)
btree.insert(3)
btree.insert(1)
btree.insert(4)

# btree.root.value
# btree.root.left.value
# btree.root.right.value
btree.contains(4)
