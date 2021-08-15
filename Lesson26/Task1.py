# O(log(n))
def binary_search(some_list, value):
    if len(some_list)>1:
        if some_list[round(len(some_list)/2)] > value:
            return binary_search(some_list[:round(len(some_list)/2)], value)
        elif some_list[round(len(some_list)/2)] < value:
            return binary_search(some_list[round(len(some_list)/2):], value)
        elif some_list[round(len(some_list)/2)] == value:
            return True
    return some_list[0] == value