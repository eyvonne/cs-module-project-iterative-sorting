# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        min = arr[i]
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i, len(arr)):
            if arr[j] < min:
                min = arr[j]
                smallest_index = j

        # TO-DO: swap
        # Your code here
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    switched = True

    while switched:
        switched = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                switched = True

    return arr


def insertion_sort(arr):
    '''I kinda stopped paying attenion in lecture and want to recreate this too'''

    for i in range(1, len(arr)):
        current = arr[i]
        j = i
        while j > 0:
            if current > arr[j-1]:
                arr.insert(j, current)
                del arr[i+1]
                break
            j -= 1

    return arr



def insertion_sort_books(arr_of_books):
    ''' this is just the code from lecture adapted for a list of numbers'''
    for i in range(1, len(arr_of_books)):
        curr_book = arr_of_books[i]
        j = i
        while j > 0 and curr_book < arr_of_books[j - 1]:
            arr_of_books[j], arr_of_books[j - 1] = arr_of_books[j - 1], arr_of_books[j]
            j -= 1

    return arr_of_books
# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):
    # Your code here

    return arr

import time
from random import randint

if __name__ == '__main__':
    benchmark = [randint(0,5000) for i in range(5000)]
    second_benchmark = benchmark.copy()
    selection = benchmark.copy()
    start_mine = time.time()
    insertion_sort(benchmark)
    end_mine = time.time()

    start_class = time.time()
    insertion_sort_books(second_benchmark)
    end_class = time.time()

    print(f'My Time: {end_mine-start_mine}')
    print(f'Class Time: {end_class-start_class}')

    start_selection = time.time()
    print(selection_sort(selection))
    end_selection = time.time()

    print(f'Selection Sort time: {end_selection-start_selection}')
