class CustomIterableObj:
    def __init__(self, some_list):
        self.some_list = some_list

    def __getitem__(self, value):
        return self.some_list[value]


some_list = list(CustomIterableObj([1, 2, 3, 4, 5]))

for i in some_list:
    print(i)
