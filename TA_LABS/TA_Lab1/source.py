from random import randint
from datetime import datetime

def shell_sort(array, n):
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2
    return array


def shell_marzin_ziur(array, gaps):
    size = len(array)
    for gap in gaps:
        for i in range(gap, size):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp


gaps = [1750, 701, 301, 132, 57, 23, 10, 4, 1]

array_sorted = [i for i in range(4000)]
array_reverse_sorted = [i for i in range(4000, 0, -1)]
array_medium = [randint(0, 4000) for i in range(4000)]

start_time_medium = datetime.now()
shell_marzin_ziur(array_medium, gaps)
print("Sorted!")