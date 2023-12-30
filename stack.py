# %% Definitions
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self) -> None:
        self._top = None
        self._size = 0
        self._max_size = 10
    
    def push(self, value):
        if self._max_size == self._size:
            raise Exception("max size")
        node = Node(value)
        node.next = self._top
        self._top = node
        self._size += 1
        return self
    
    def pop(self):
        if not self._size:
            raise Exception("empty stack")
        top_old = self._top
        self._top = top_old.next
        top_old.next = None
        self._size -= 1
        return self

    def peek(self):
        return self._top
    
    def clear(self):
        self._top = None
        self._size = 0
        return self

# %%
bjir = Stack()
bjir.push('google')
bjir.push('twitter')
bjir.pop()
bjir.push('pixiv')
print(bjir.peek().value)
# bjir.clear()
# bjir.pop()

print(bjir._size)
i = bjir._top
while i != None:
    print(i.value)
    i = i.next