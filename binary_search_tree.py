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
        if not self.root:
            return False
        if value == self.root.value:
            return True
        node_now = self.root
        while value != node_now.value:
            if value < node_now.value:
                if not node_now.left:
                    break
                elif value == node_now.left.value:
                    return True
                node_now = node_now.left
            else:
                if not node_now.right:
                    break
                elif value == node_now.right.value:
                    return True
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
