def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def quick_sort(array=[12,4,5,6,7,3,1,15]):
    less = []
    equal = []
    greater = []
    pivot = array[0]
    for x in array:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        elif x > pivot:
            greater.append(x)
    if len(array) > 4:
        return quick_sort(less) + equal + quick_sort(greater)
    elif 1 < len(array) <= 4:
        return insertionSort(less) + equal + insertionSort(greater)
    elif len(array) == 1:
        return array

print(quick_sort())