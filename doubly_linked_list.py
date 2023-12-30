# %% Definitions
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
            new_node.prev = self.tail
            self.tail = new_node
        self._length += 1
        return self
    
    def prepend(self, value):
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._length += 1
        return self
    
    def pop_left(self):
        if not self._length:
            raise Exception("list is empty")
        head_old = self.head
        if self._length == 1:
            self.head = self.tail = None
        else:
            self.head = head_old.next
            self.head.prev = None
        self._length -= 1
        return head_old.value
    
    def pop_right(self):
        if not self._length:
            raise Exception("list is empty")
        tail_old = self.tail
        if self._length == 1:
            self.head = self.tail = None
        else:
            self.tail = tail_old.prev
            self.tail.next = None
            tail_old.prev = None
        self._length -= 1
        return 
    
    def remove(self, value):
        if not self._length:
            raise Exception("list is empty")
        if self.head.value is value:
            return self.pop_left()
        node_prev = self.head
        node = self.head.next
        while node.value is not value and node is not None:
            node_prev = node
            node = node.next
        if node is None:
            raise Exception("value not found")
        if node.next is None:
            return self.pop_right()
        node_prev.next = node.next
        node.next.prev = node_prev
        node.next = None
        node.prev = None
        self._length -= 1
        return node.value
    
    def reverse(self):
        # none, a, b, c, d
        l = None
        m = self.head
        while m is not None:
            r = m.next
            m.next = l
            l = m
            m = r
        self.head, self.tail = self.tail, self.head
        return self

        
# %% Scrips
x = DoublyLinkedList()
x.prepend(4)
x.prepend(3)
x.prepend(2)
x.prepend(1)
x.remove(2)

i = x.head
while i is not None:
    print(i.value)
    i = i.next
print()
i = x.tail
while i is not None:
    print(i.value)
    i = i.prev
