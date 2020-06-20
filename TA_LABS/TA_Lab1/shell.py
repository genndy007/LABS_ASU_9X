from random import randint  # to generate random numbers
from datetime import datetime  # to compute algorithm running time

def shell_marcin_ciura(array, gaps):
    size = len(array)
    shifts = 0
    comparisons = 0
    for gap in gaps:
        for i in range(gap, size):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                comparisons += 1
                shifts += 1
                j -= gap
            comparisons += 1
            array[j] = temp
    return shifts, comparisons

def menu():
    print("Shell Sort (Marcin Ciura's sequence)\n"
          "This empirical sequence is good for sorting 4000 elements arrays")
    gaps = [1750, 701, 301, 132, 57, 23, 10, 4, 1]
    while input("Type 'exit' to exit: ") != 'exit':
        our_gaps = []
        array_type = input("What array you want to sort?:\n"
                           "1. Already sorted\n"
                           "2. Already backward sorted\n"
                           "3. Randomly sorted\n").strip()
        size = int(input("What size of array?: ").strip())
        while array_type != '1' and array_type != '2' and array_type != '3':
            print('Try again')
            array_type = input("What array you want to sort?:\n"
                               "1. Already sorted\n"
                               "2. Already backward sorted\n"
                               "3. Randomly sorted\n").strip()
            size = int(input("What size of array?: ").strip())
        if array_type == '1':
            array = [i for i in range(size)]
        if array_type == '2':
            array = [i for i in range(size, 0, -1)]
        if array_type == '3':
            array = [randint(0, size) for i in range(size)]
        for i in range(len(gaps)):
            if gaps[i] < size:
                our_gaps.append(gaps[i])
        start_time = datetime.now()
        shifts_comps = shell_marcin_ciura(array, our_gaps)
        print('Time:', datetime.now() - start_time)
        print('Shifts:', shifts_comps[0])
        print('Comparisons:', shifts_comps[1])

menu()
