# Matrix Multiplication
# Function: Dot product of 2 matrices

def read_matrix(input):                         #   Read file
    file = open(input, "r")
    lines = file.readlines()
    a=[]
    for line in lines:
        b=[]
        for x in line.strip('\n').split(' '):
            b.append(int(x))
        a.append(b)
    return a

def mat_sum(m1, m2):
    matrix3 = []
    for i in range(len(m1)):                    #   Loop: Matrix index
        list = []
        for j in range(len(m1)):                #   Loop: List index within matrix
            list.append(m1[i][j] + m2[i][j])    #   Append summed values
        matrix3.append(list)                    #   Append summed value list
    print("The final result is:")
    for m in range(len(matrix3)):               #   Print the final matrix (5x5 assumed)
        print(*matrix3[m], sep=" ")



def main():
    matrix1 = read_matrix("hw2-m1.txt")                 #   Assign Matrix values
    matrix2 = read_matrix("hw2-m2.txt")
    #matrix1 = [[1,2,0,3,4],[2,4,1,1,0],[3,0,5,6,1],[1,2,6,0,1],[4,1,1,0,0]]    #   Test Matrices
    #matrix2 = [[2,0,4,0,1],[2,2,1,0,5],[0,0,1,0,3],[2,1,0,4,1],[0,0,4,0,1]]
    right_size = True
    for i in range(max(len(matrix1), len(matrix2))):                            #   Check for proper dimensions
        if (len(matrix1) * len(matrix1[i]) != 25 or len(matrix2) * len(matrix2[i]) != 25):
            right_size = False
            break
    if right_size is False:
        print("Error: Matrix Dimensions Must Match")
    else:
        mat_sum(matrix1, matrix2)                           #   Add matrices


main()                                                  # Call Main function