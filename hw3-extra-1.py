# Duplicates
# Function: in a list of numbers, find which have duplicates within the list

def read(infile):
    file = open(infile, "r")
    line = file.readline()
    values = []
    for value in line.split(' '):
        values.append(int(value))
    return values

def duplicates(list):                                           #   checks for duplicates in array
    d = []                                                      #   holds duplicate values
    for i in range(len(list)):                                  #   iterates through key values
        if list[i] in d:                                        #   check if the current item has already been found
            continue
        for j in range(len(list) - 1, i, -1):                   #   interates back to front to search (elements before [i] omitted)
            if (list[j] == list[i]):
                if list[i] not in d:                            #   prevents multiple duplicates from being stored ex. 7, 7, 7 => 7, 7
                    d.append(list[i])
                break                                           #   duplicate found, no need to look more
    return d

def main():                                                     #   main function
    #list1 = read("hw3-ExtraCredit.txt")
    list1 = [2, 99, 3, 5, 2, 3, 1, 7, 7, 9, 13, 15, 99, 96, 4, 1]   #   test input
    dupes = duplicates(list1)
    print("The duplicate numbers: ")
    print(*dupes, sep = " ")

main()                                                          #   Call main