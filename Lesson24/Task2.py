class Deque:
    def __init__(self):
        self.items = []

    # O(1)
    def is_empty(self):
        return self.items == []

    # O(1)
    def add_front(self, item):
        self.items.append(item)

    # O(n)
    def add_rear(self, item):
        self.items.insert(0, item)

    # O(1)
    def remove_front(self):
        return self.items.pop()

    # O(n)
    def remove_rear(self):
        return self.items.pop(0)

    # O(n)
    def size(self):
        return len(self.items)

# def balance(some_str: str):
#     parentheses_left = 0
#     parentheses_right = 0
#     braces_left = 0
#     braces_right = 0
#     curly_brackets_left = 0
#     curly_brackets_right = 0
#     dq = Deque()
#
#     def check(checkeble, type):
#         if checkeble < 0:
#             raise Exception(f"not enough {type}")
#
#     for i in some_str:
#         dq.add_rear(i)
#
#     while not dq.is_empty():
#         if dq.size() == 1:
#             first = dq.remove_front()
#             lust = ""
#         else:
#             first = dq.remove_front()
#             lust = dq.remove_rear()
#         if first == "(":
#             parentheses_left += 1
#         elif first == ")":
#             parentheses_left -= 1
#             check(parentheses_left, "(")
#         if lust == ")":
#             parentheses_right += 1
#         elif lust == "(":
#             parentheses_right -= 1
#             check(parentheses_right, ")")
#         if first == "[":
#             braces_left += 1
#         elif first == "]":
#             braces_left -= 1
#             check(braces_left, "[")
#         if lust == "]":
#             braces_right += 1
#         elif lust =="[":
#             braces_right -= 1
#             check(braces_right, "]")
#         if first == "{":
#             curly_brackets_left += 1
#         elif first == "}":
#             curly_brackets_left -= 1
#             check(curly_brackets_left, "{")
#         if lust == "}":
#             curly_brackets_right += 1
#         elif lust == "{":
#             curly_brackets_right -= 1
#             check(curly_brackets_right, "}")
#     if parentheses_left < parentheses_right:
#         return f"')' {parentheses_right-parentheses_left} more than '('"
#     elif parentheses_right < parentheses_left:
#         return f"'(' {parentheses_left-parentheses_right} more than ')'"
#     if braces_left < braces_right:
#         return f"']' {braces_right - braces_left} more than '['"
#     elif braces_right < braces_left:
#         return f"'[' {braces_left - braces_right} more than ']'"
#     if curly_brackets_left < curly_brackets_right:
#         return '}' + str(curly_brackets_right - curly_brackets_left) + "more than '{'"


def new_balance(some_str: str):
    check_list = []
    new_list = []
    needed = ["{}", "[]", "()"]
    for i in some_str:
        if i in ["(", ")", "{", "}", "[", "]"]:
            check_list.append(i)
    check_str = "".join(check_list)
    flag = False
    while len(check_str) > 0 and not flag:
        flag = True
        for i in needed:
            if i in check_str:
                check_str = check_str.replace(i, "")
                flag = False
    if len(check_str) > 0:
        raise Exception("wrong balance")
    return "everything ok"

