class CustomRange:
    def __init__(self, begin=0, end=None, step=1):
        self.counter = begin
        self.end = end
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


c = CustomRange(0, 10)

print(list(c))
