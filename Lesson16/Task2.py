class CustomRange:
    def __init__(self, begin=0, end=None, step=1):
        self.counter = self.__condition2(begin, end)
        self.end = self.__condition1(begin, end)
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        return_value = self.counter
        if self.counter < self.end:
            self.counter += self.step
        else:
            raise StopIteration
        return return_value

    def __condition1(self, begin, end):
        if end is None:
            return begin
        else:
            return end

    def __condition2(self, begin, end):
        if end is None:
            return 0
        else:
            return begin



c = CustomRange

print(list(c(0,10)))
print(list(c(10)))
print(list(c(0,10,2)))