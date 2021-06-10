from typing import Union, List


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


def reverse(symbs: Union[List[Union[int, str]], str, int]) -> str:
    stack_obj= Stack()

    def for_list(symbs):
        for i in symbs:
            stack_obj.push(i)
        result_sting = ""
        while not stack_obj.is_empty():
            if stack_obj.size() > 1:
                result_sting = result_sting + str(stack_obj.pop()) + ","
            else:
                result_sting = result_sting + str(stack_obj.pop())
        return result_sting

    def for_str(symbs):
        symbs = list(symbs)
        return for_list(symbs)

    def for_int(symbs):
        symbs = list(str(symbs))
        return for_list(symbs)

    if type(symbs) is list:
        return for_list(symbs)
    elif type(symbs) is str:
        return for_str(symbs)
    elif type(symbs) is int:
        return for_int(symbs)


assert reverse(123456) == "6,5,4,3,2,1"
assert reverse("123456") == "6,5,4,3,2,1"
assert reverse([1,2,3,4,5,6]) == "6,5,4,3,2,1"
