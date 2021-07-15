class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, newdata):
        self.data = newdata
    def set_next(self, newnext):
        self.next = newnext
class UnorderedList:
    def __init__(self):
        self.head = None
    # O(1)
    def is_empty(self):
        return self.head is None
    # O(1)
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
    # O(n)
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count
    # O(n)
    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found
    # O(n)
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found or current is not None:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.setNext(current.get_next())

    def append(self, item):
        current = self.head
        previous = None
        temp = Node(item)
        if not current:
            temp = Node(item)
            self.head = temp
        else:
            while current is not None:
                previous = current
                current = current.get_next()
            previous.set_next(temp)

    def index(self, item):
        current = self.head
        found = False
        count = 0
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                count += 1
                current = current.get_next()
        return count

    def insert(self, pos, item):
        current = self.head
        previous = None
        count = 0
        while current is not None:
            if count == pos:
                item_node = Node(item)
                previous.set_next(item_node)
                item_node.set_next(current)
                break
            else:
                count = count + 1
                previous = current
                current = current.get_next()
        else:
            raise IndexError("this list is not that long")

    def pop(self, pos=None):
        current = self.head
        previous = None
        count = 0

        while current is not None:
            if pos == 0:
                self.head = current.get_next()
                return current.get_data()
            if count == pos:
                previous.set_next(current.get_next())
                return current.get_data()
            else:
                count = count + 1
                previous = current
                current = current.get_next()
                if not pos:
                    if current.get_next() is None:
                        previous.set_next(None)
                        return current.get_data()
        else:
            raise IndexError("position is out of range")

    def get_by_index(self, index):
        current = self.head
        count = 0
        while current is not None:
            if count == index:
                return current.get_data()
            else:
                current = current.get_next()
                count += 1
        else:
            raise IndexError("Index is out of range")

    def slice(self, start=0, end=None):
        counter = 0
        if not end:
            end = self.size() - 1
        current = self.head
        while current is not None:
            if counter >= end:
                break
            elif counter >= start:
                yield current.get_data()    #если нужно получить список из нодов тогда просто убрать get_data()
                current = current.get_next()    #есть ещё вариант с возвратом списка со значениями,  но мне чёт так захотелось сделать генератор
                counter += 1
            elif counter < start:
                counter += 1
                current = current.get_next()


unlist = UnorderedList()
unlist.append(1)
unlist.append(2)
unlist.append(3)
unlist.append(4)
unlist.append(5)
print(list(unlist.slice(1,3)))