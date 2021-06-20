class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front == None

    def en_queue(self, item):
        temp = Node(item)
        if not self.rear:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def de_queue(self):
        if self.is_empty():
            return
        temp = self.front
        self.front = temp.next
        if not self.front:
            self.rear = None