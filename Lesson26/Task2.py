# O(log(n))
def fibonacci_search(some_list, value):
    first_index = 0
    second_index = 1
    old_index = 0
    while second_index < len(some_list):
        if some_list[first_index] <= value <= some_list[second_index]:
            if value < some_list[second_index] and value > some_list[first_index]:
                first_index += 1
                second_index -= 1
            else:
                if value == some_list[first_index]:
                    return first_index, True
                elif value == some_list[second_index]:
                    return second_index, True
        elif first_index == second_index != 1 or first_index > second_index:
            return False
        else:
            old_index = first_index
            first_index = second_index
            second_index = old_index + first_index
    return False

