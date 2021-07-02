class Stack:
    def __init__(self):
        self.items = []

    # O(1)
    def is_empty(self):
        return self.items == []

    # O(1)
    def push(self, item):
        self.items.append(item)

    # O(1)
    def pop(self):
        return self.items.pop()

    # O(1)
    def peek(self):
        return self.items[-1]

    # O(n)
    def size(self):
        return len(self.items)

    def get_from_stack(self, item):
        try:
            return self.items[self.items.index(item)]
        except ValueError:
            raise ValueError("there is no such item in this stack")

s =Stack()

for i in [1, 2, 3, 4, 5, 6]:
    s.push(i)

print(s.get_from_stack(7))