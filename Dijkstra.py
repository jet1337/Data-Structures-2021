# Dijkstra's Shortest Path Algorithm
# Function: Find the shortest path in a graph from all nodes to the specified node
# Note: input is an adjacency matrix; assumes matrix is symmetrical


def read_matrix(input):                                                             # Read file into matrix
    file = open(input, "r")
    lines = file.readlines()
    a=[]
    for line in lines:
        b=[]
        for x in line.strip('\n').split(' '):
                b.append(int(x))
        a.append(b)
    return a


def dijkstra(matrix, dest):
    v = set()                                                                       # Set of visited vertexes
    distances = [2 ** 64] * len(matrix)                                             # 2**64 signifies infinity
    distances[dest] = 0                                                             # initialize distance 0 for source vertext
    current_v = 0
    while len(v) < len(matrix):
        mini = 2 ** 64 + 1
        for i in range(len(distances)):
            if i not in v:
                if distances[i] < mini:
                    mini = distances[i]
                    current_v = i
        v.add(current_v)                                                            # visit current v
        for j in range(len(matrix[current_v])):
            if matrix[current_v][j] == 0:
                continue
            else:                                                                   # choose shortest distance
                distances[j] = min(distances[j], distances[current_v] + matrix[current_v][j])
    for vert in range(len(distances)):
        print("The distance from vertex " + str(vert) + " to vertex " + str(dest) + " is " + str(distances[vert]))
    # print(distances)
    # print(v)


def main():
    #read matrix
    adjMat = read_matrix("adjMat.txt")
    #get destination vertex
    while True:
        dest_vertex = int(input("Enter the destination vertex (0 - 9): "))
        if dest_vertex not in range(len(adjMat)):
            print("Vertex not in graph - Enter valid vertex")
        else:
            break
    #call dijkstra on matrix and source
    dijkstra(adjMat, dest_vertex)

if __name__ == "__main__": main()