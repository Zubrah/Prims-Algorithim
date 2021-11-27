#Prim's Implementation of the MST


INF = 9999999
# number of vertices in graph
Vertices = 5
# create a 2d array of size 5x5
# for adjacency matrix to represent graph
Graph = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]
# create a array to track selected vertex
# selected will become true otherwise false
choosen = [0, 0, 0, 0, 0]
# set number of edge to 0
no_edge = 0
# the number of egde in minimum spanning tree will be
# always less than(V - 1), where V is number of vertices in
# graph
# choose 0th vertex and make it true
choosen[0] = True
# print for edge and weight
print("Node(Edge) :  Weight\n")
while ( no_edge < Vertices - 1):
    # For every vertex in the set S, find the all adjacent vertices
    #, calculate the distance from the vertex selected at step 1.
    # if the vertex is already in the set S, discard it otherwise
    # choose another vertex nearest to selected vertex  at step 1.
    minimum = INF
    x = 0
    y = 0
    for i in range(Vertices):
        if choosen[i]:
            for j in range(Vertices):
                if ((not choosen[j]) and Graph[i][j]):  
                    # not in selected and there is an edge
                    if minimum > Graph[i][j]:
                        minimum = Graph[i][j]
                        x = i
                        y = j
    print(str(x) + "-" + str(y) +    ":" + str(Graph[x][y]))
    choosen[y] = True
    no_edge += 1