# Merge Sort
# Note: we couldn't use the short version
# Note 2: only coded the mergeSort function, rest was provided

"""
File: mergeSort.py

Recursive implementation of mergeSort
"""

import random
import time

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i+=1
            else:
                alist[k]=righthalf[j]
                j+=1
            k+=1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i+=1
            k+=1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j+=1
            k+=1

def shuffle(myList):
    for fromIndex in range(len(myList)):
        toIndex = random.randint(0,len(myList)-1)
        temp = myList[fromIndex]
        myList[fromIndex] = myList[toIndex]
        myList[toIndex] = temp

def main():
    listSize = 5                                        # CHANGE SIZE HERE TO TEST DIFFERENT INPUT SIZES

    print("mergeSort Timings")
    aList = list(range(listSize, 0, -1))
    print("\nBefore sorting list: ", end="")
    print(aList[0], aList[1], aList[2], '...', aList[-3], aList[-2], aList[-1])
    start = time.time()
    mergeSort(aList)
    end = time.time()
    print("sorted list:", end="")
    print(aList[0], aList[1], aList[2], '...', aList[-3], aList[-2], aList[-1])
    print("Time to sort", end - start, "seconds")

    print("\nBefore sorting list: ", end="")
    print(aList[0], aList[1], aList[2], '...', aList[-3], aList[-2], aList[-1])
    start = time.time()
    mergeSort(aList)
    end = time.time()
    print("sorted list:", end="")
    print(aList[0], aList[1], aList[2], '...', aList[-3], aList[-2], aList[-1])
    print("Time to sort", end - start, "seconds")

    aList = list(range(listSize, 0, -1))
    shuffle(aList)
    print("\nBefore sorting (random) list: ", end="")
    print(aList[0], aList[1], aList[2], '...', aList[-3], aList[-2], aList[-1])
    start = time.time()
    mergeSort(aList)
    end = time.time()
    print("sorted list:", end="")
    print(aList[0], aList[1], aList[2], '...', aList[-3], aList[-2], aList[-1])
    print("Time to sort", end - start, "seconds")

    aList = list(range(listSize, 0, -1))
    shuffle(aList)
    print("\nBefore sorting (random) list: ", end='')
    print(aList[0], aList[1], aList[2], '...', aList[-3], aList[-2], aList[-1])
    start = time.time()
    mergeSort(aList)
    end = time.time()
    print("sorted list:", end="")
    print(aList[0], aList[1], aList[2], '...', aList[-3], aList[-2], aList[-1])
    print("Time to sort", end - start, "seconds")

    input("Hit <Enter>-key to end")


if __name__ == "__main__": main()