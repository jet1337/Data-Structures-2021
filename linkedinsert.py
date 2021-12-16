# Singly Linked List: Insert
# Function: Insert words in a linked list in sorted order
# Note: Had to use only a node class in node.py

"""
File: a5.py
Assignment 5

Define a length function.
Define a printStructure function.
Define an insert function.
Test the above functions and the Node class.
"""

from node import Node

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
    
def insert(newItem, head):
    """Inserts newNode at the correct position (ascending order) in
    the linked structure referred to by head.
    Returns a reference to the new structure."""
    probe = head
    newNode = Node(newItem)
    if head is None:                                                                            # EMPTY LIST
        head = newNode
        return head
    while True:
        if newNode.data.upper() < head.data.upper():                                            # COMPARE TO HEAD VALUE
            newNode.next = head
            head = newNode
            return head
        if probe.next is None:                                                                  # LAST ELEMENT OF LIST
            if probe.data.upper() <= newNode.data.upper():
                probe.next = newNode
                break
            if probe.data.upper() > newNode.data.upper():
                newNode.next = probe
                probe = newNode
                break
        else:                                                                                    # COMPARE BETWEEN 2 ELEMENTS
            if probe.data.upper() <= newNode.data.upper() and newNode.data.upper() <= probe.next.data.upper():
                newNode.next = probe.next
                probe.next = newNode
                break
            else:
                probe = probe.next
                continue
    return head

def printStructure(head):
    """Prints the items in the structure referred to by head."""
    probe = head
    while head is not None:
        if probe is None:
            break
        else:
            print(probe.data, end=" ")
            if probe.next is not None:
                probe = probe.next
            else:
                break
def main():
    """Gets words from the user and inserts in the
    structure referred to by head."""
    head = None
    while True:
        userInput = input('Please enter a word (or just hit enter to end): ')
        if userInput == '':
            break
        head = insert(userInput, head)
    print('The structure contains', length(head), 'items:', end=" ")
    printStructure(head)

if __name__ == "__main__": main()
