# Hanoi Tower
# Function: Shows all the moves necessary to solve the Hanoi Tower puzzle
# Note: Adjust HanoiTower.txt to test towers of different amounts (can get lengthy)

def read(infile):
    file = open(infile, "r")
    lines = file.readlines()
    linesNew = [int(x) for x in lines]
    return linesNew

#   The recursive aspect of this problem is that once the largest disc N is on the end peg
#   the problem becomes the same problem but now with N - 1 discs
#   Pegs A, B, and C alternate between which is the start, end, and other peg

def hanoi(discs, start, end):
    key = {1:"A", 2:"B", 3:"C"}                                                         #   Map peg numbers to letters
    other = 6 - start - end                                                             #   Gets the peg not required for the move
    if discs == 1:                                                                      #   Base case, single disc
        print("Disc " + str(discs) + " moves from " + key[start] + " to " + key[end])
    else:
        hanoi(discs - 1, start, other)                                                  #   Get everything but bottom disc to 2nd peg
        print("Disc " + str(discs) + " moves from " + key[start] + " to " + key[end])   #   Prints the move of the largest disc to the 3rd peg
        hanoi(discs - 1, other, end)                                                    #   Move bottom disc to end peg



def main():                                                                             #   main function
    tower = read("HanoiTower.txt")
    #tower = [1,2,3]
    hanoi(len(tower),1,3)

main()                                                                                  #   Call main