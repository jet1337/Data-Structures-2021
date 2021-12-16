# Max/Min in an array
# Input: file with list of space-separated numbers
# Function: find the min and max within the list


def read():
    file = open("TestInputHW1.txt", "r")
    line = file.readline()
    values = []
    for value in line.split(' '):
        values.append(int(value))
    return values

def min_max(list):
    big = list[0]
    small = list[0]
    for i in range(1, len(list)):
        if list[i] > big:
            big = list[i]
        if list[i] < small:
            small = list[i]
    print("Maximum element: " + str(big) + "\n")
    print("Minimum element: " + str(small))

def main():
    list1 = read()
    #list1 = [1,6,9,2,60]
    min_max(list1)

if __name__ == "__main__": main()