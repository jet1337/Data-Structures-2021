# Quick Sort
# Note: Coded quickSort, quickSortHelper, and partition; rest were provided

"""
File: quickSort.py

Recursive implementation of quickSort
"""

import random
import time

def quickSort(aList):
    quickSortHelper(aList, 0, len(aList) - 1)

def quickSortHelper(aList, left, right):
    if left < right:
        pivotLocation = partition(aList, left, right)
        quickSortHelper(aList, left, pivotLocation - 1)
        quickSortHelper(aList, pivotLocation + 1, right)

def partition(aList, left, right):
    # Find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = aList[middle]
    aList[middle] = aList[right]
    aList[right] = pivot
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        if aList[index] < pivot:
            temp = aList[index]
            aList[index] = aList[boundary]
            aList[boundary] = temp
            boundary += 1
    # Exchange the pivot item and the boundary item
    temp = aList[boundary]
    aList[boundary] = aList[right]
    aList[right] = temp
    return boundary

def shuffle(myList):
    for fromIndex in range(len(myList)):
        toIndex = random.randint(0,len(myList)-1)
        temp = myList[fromIndex]
        myList[fromIndex] = myList[toIndex]
        myList[toIndex] = temp

def main():
    listSize = 5

    print("quickSort Timings")
    aList = list(range(listSize, 0, -1))
    print("\nBefore sorting list: ", end="")
    print(aList[0], aList[1], aList[2], '...', aList[-3], aList[-2], aList[-1])
    start = time.time()
    quickSort(aList)
    end = time.time()
    print("sorted list:", end="")
    print(aList[0], aList[1], aList[2], '...', aList[-3], aList[-2], aList[-1])
    print("Time to sort", end - start, "seconds")

    print("\nBefore sorting list: ", end="")
    print(aList[0], aList[1], aList[2], '...', aList[-3], aList[-2], aList[-1])
    start = time.time()
    quickSort(aList)
    end = time.time()
    print("sorted list:", end="")
    print(aList[0], aList[1], aList[2], '...', aList[-3], aList[-2], aList[-1])
    print("Time to sort", end - start, "seconds")

    aList = list(range(listSize, 0, -1))
    shuffle(aList)
    print("\nBefore sorting (random) list: ", end="")
    print(aList[0], aList[1], aList[2], '...', aList[-3], aList[-2], aList[-1])
    start = time.time()
    quickSort(aList)
    end = time.time()
    print("sorted list:", end="")
    print(aList[0], aList[1], aList[2], '...', aList[-3], aList[-2], aList[-1])
    print("Time to sort", end - start, "seconds")

    aList = list(range(listSize, 0, -1))
    shuffle(aList)
    print("\nBefore sorting (random) list: ", end='')
    print(aList[0], aList[1], aList[2], '...', aList[-3], aList[-2], aList[-1])
    start = time.time()
    quickSort(aList)
    end = time.time()
    print("sorted list:", end="")
    print(aList[0], aList[1], aList[2], '...', aList[-3], aList[-2], aList[-1])
    print("Time to sort", end - start, "seconds")

    input("Hit <Enter>-key to end")


if __name__ == "__main__": main()
