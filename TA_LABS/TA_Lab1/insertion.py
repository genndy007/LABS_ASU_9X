from datetime import datetime
from random import randint


def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i - 1, 0, -1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            else:
                break


array = [randint(0, 1000) for i in range(10000)]

start_time = datetime.now()

insertion_sort(array)

print(datetime.now() - start_time)



