class WithIndex:
    def __init__(self, iterable, start=0):
        self.iterable = iterable
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start in range(len(self.iterable)):
            result = (self.start, self.iterable[self.start])
            self.start += 1
        else:
            raise StopIteration
        return result


a=WithIndex([1,2,3,4,5])
print(list(a))