# Palindrome Checker
# Function: Check for a palindrome sentence using a stack ADT

from stack import Stack

def isPalindrome(sentence):          
    """Returns True if sentence is a palindrome
    or False otherwise."""
    stk1 = Stack()                                              # Creates a stack called stk1
    stk2 = Stack()                                              # Creates a stack called stk2

    for i in range(0, len(sentence)):                           # push sentence to stk1 if a letter
        if sentence[i].isalpha():
            stk1.push(sentence[i])
            #print(stk1.size(), stk1.peek())
    for j in range(len(sentence) - 1, -1, -1):                  # push sentence backwards to stk2 if a letter
        if sentence[j].isalpha():
            stk2.push(sentence[j])
            #print(stk2.size(), stk2.peek())

    for k in range(stk1.size()):                                # compare stacks one pop at a time
        if stk1.peek() != stk2.peek():
            return False                                        # if it is ever not equal, not palindrome
        stk1.pop()
        stk2.pop()
    return True                                                 # if it makes it through loop, is palindrome

# *** Do not modify main() ***
def main():
    while True:
        sentence = input("Enter some text or just hit Enter to quit: ")
        if sentence == "":
            break
        elif isPalindrome(sentence):
            print("It's a palindrome.")
        else:
            print("It's not a palindrome.")

if __name__ == "__main__":main()
