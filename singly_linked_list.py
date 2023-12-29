# %% Definitions
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def append(self, value):
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._length += 1
        return self

# %% Scrips
x = SinglyLinkedList()
x.append(4)
x.append(2)
x.append(3)
x.append(1)

# %% Tests
x.head.next.next.next.value