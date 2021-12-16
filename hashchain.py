# Hash Chain
# Function: Create a hash chain based on user input and print the contents of the hash chain

import hashlib

def H(k):                                                                              # Hash Function
    kb = str.encode(k)
    return hashlib.sha256(kb).hexdigest()

class Node:                                                                            # Nodes
    def __init__(self, hash=None):
        self.hash = hash
        self.next = None

class LinkedList:                                                                      # Linked List
    def __init__(self):
        self.head = None


def main():
    while True:                                                                        # Get user input
        length = input("Enter the length of your hash chain: ")
        if length.isnumeric():
            length = int(length)
            break
        else:
            print("Enter a valid number\n")
    k = input("Enter your seed value: ")
    hash_chain = LinkedList()                                                          # Create Linked List
    hash_chain.head = Node(H(k))                                                       # Initialize head node
    probe = hash_chain.head

    for i in range(length - 1, 0, -1):                                                 # Create the hash chain
        probe.next = Node(H(probe.hash))
        probe = probe.next
    probe = hash_chain.head
    node = 1
    
    while(probe):                                                                      # Print hash chain
        print("Node", node, ": ", probe.hash)
        probe = probe.next
        node += 1

if __name__ == "__main__": main()