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
        if node.value == self.root.value:
            return self
        node_now = self.root
        while node_now.left != None or node_now.right != None:
            if node.value < node_now.value:
                if not node_now.left:
                    break
                node_now = node_now.left
            else :
                if not node_now.right:
                    break
                node_now = node_now.right
        if node.value < node_now.value:
            node_now.left = node
        else:
            node_now.right = node
        return self

# %%
btree = BinaryTree()
btree.insert(2)
btree.insert(3)
btree.insert(1)

btree.root.left.value
