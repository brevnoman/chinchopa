from typing import List, Tuple


# We assume that all lists passed to functions are same length N
# answers
# 1 - n^2
# 2 - 1
# 3 - log(n)
# 4 - n
# 5 - n^2
# 6 - n
def question1(first_list: List[int], second_list: List[int]) -> List[int]: #n^2
    res: List[int] = []
    for el_first_list in first_list:
        if el_second_list in second_list:
            res.append(el_first_list)
    return res


def question2(n: int) -> int: #1
    for _ in range(10):
        n **= 3
    return n


def question3(first_list: List[int], second_list: List[int]) -> List[int]: #log(n)
    temp: List[int] = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if second_list == check:
                flag = True
                break
        if not flag:
            temp.append(second_list)
    return temp


def question4(input_list: List[int]) -> int:    #n
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res


def question5(n: int) -> List[Tuple[int, int]]: #n^2
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res


def question6(n: int) -> int: #n
    while n > 1:
        n /= 2
    return n
