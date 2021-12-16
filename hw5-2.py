# Singly linked list: Merge Sort
# Function: read a file into a linked list and merge sort it
# Note: uses node.py

"""
File: hw5-2.py
Assignment 5

Read linked list from file
Print List
Merge Sort List
Print Sorted List
"""

from node import Node

def read():
    file = open("hw5-2.txt", "r")
    line = file.readline()
    head = None
    for value in line.split(' '):
        if head is None:
            head = Node(int(value))
            probe = head
        else:
            probe.next = Node(int(value))
            probe = probe.next
    return head

def printStructure(head):
    """Prints the items in the structure referred to by head."""
    probe = head
    while probe is not None:
        print(probe.data, end=" ")
        probe = probe.next

def length(head):
    """Returns the number of items in the linked structure
    referred to by head."""
    probe = head
    count = 0
    if head is None:
        return 0
    else:
        while True:
            count += 1
            if probe.next is None:
                break
            else:
                probe = probe.next
                continue
    return count

def sorted_merge(left, right):
    """Sorts and merges left and right halves together"""
    head = None
    while left is not None and right is not None:
        if head is None:
            if left.data <= right.data:
                head = left
                left = left.next
            else:
                head = right
                right = right.next
            probe = head
        else:
            while left is not None and right is not None:
                if left.data <= right.data:
                    probe.next = left
                    left = left.next
                else:
                    probe.next = right
                    right = right.next
                probe = probe.next

    while left is not None:
        probe.next = left
        left = left.next
        probe = probe.next

    while right is not None:
        probe.next = right
        right = right.next
        probe = probe.next
    return head

def mid_finder(head, size):
    """Find the midpoint of the linked list"""
    if size > 1:
        mid = size // 2
        lefthalf = None
        righthalf = None
        left_temp = None
        count = 0
        if head is None or head.next is None:
            return head
        while head is not None:                                         # Find midpoint
            count += 1
            if count <= mid:
                if lefthalf is None:
                    lefthalf = head
                    left_temp = lefthalf
                    head = head.next
                    continue
                else:
                    left_temp.next = head
                    left_temp = left_temp.next
                    head = head.next
                    continue
            righthalf = left_temp.next                                  # Create right half
            left_temp.next = None                                       # Cut off left half
            break
        return (lefthalf, righthalf)

def merge_sort(head):
    if head is None or head.next is None:
        return head
    lefthalf, righthalf = mid_finder(head, length(head))                # Find mid
    lefthalf = merge_sort(lefthalf)                                     # Call merge_sort recursively
    righthalf = merge_sort(righthalf)
    return sorted_merge(lefthalf, righthalf)                            # Merge the Sorted Lists

def main():
    head = read()
    print("Unsorted")
    printStructure(head)
    head = merge_sort(head)
    print("\n\nSorted")
    printStructure(head)

if __name__ == "__main__": main()