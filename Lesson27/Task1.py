def bobble_sort_both_directions(a):
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
            if a[end-i] < a[end-i-1]:
                a[end-i], a[end-i-1] = a[end-i-1], a[end-i]
                swapped = True
