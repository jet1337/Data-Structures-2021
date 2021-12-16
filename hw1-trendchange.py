# Trend Change
# Input: file with list of space-separated numbers
# Function: find the trend changes in a list (list goes from increasing to decreasing trends, vice versa)


def read():
    file = open("TestInputHW1.txt", "r")
    line = file.readline()
    values = []
    for value in line.split(' '):
        values.append(int(value))
    return values

def trend_change(list):
    for i in range(1, len(list)):
        if i == (len(list)-1):
            break
        if (list[i] < list[i-1] and list[i] < list[i+1]) or (list[i] > list[i-1] and list [i] > list[i+1]):
            print("Trend change points: " + str(list[i]) + " " + str(list[i+1]))

def main():
    list = read()
    trend_change(list)

if __name__ == "__main__": main()