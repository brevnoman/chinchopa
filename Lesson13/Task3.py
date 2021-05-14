def choose_func(nums: list, func1, func2):
    for num in nums:
        if num < 0:
            return func2(nums)
    else:
        return func1(nums)


def square_nums(nums):
    return [num**2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num >= 0]




nums1=[1, 2, 3, 4, 5]
nums2=[1, -2, 3, -4, 5]

a=choose_func(nums1, square_nums, remove_negatives)
b=choose_func(nums2, square_nums, remove_negatives)


print(a)
print(b)