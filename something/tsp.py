from sys import maxsize
from itertools import permutations
V=4
def tsp(graph, s):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    min_cost = maxsize
    best_path = None

    for i in permutations(vertex):
        current_cost = 0
        k = s
        path = [k]  # Initialize path with starting city

        for j in i:
            current_cost += graph[k][j]
            k = j
            path.append(j)

        current_cost += graph[k][s]  # Add cost from last city back to starting city
        path.append(s)  # Complete the path

        if current_cost < min_cost:
            min_cost = current_cost
            best_path = path

    print("Minimum cost:", min_cost)
    print("Path taken:", best_path)

    return min_cost

graph = [[0, 10, 15, 20], 
         [10, 0, 35, 25], 
         [15, 35, 0, 30], 
         [20, 25, 30, 0]]
s = 0
print(tsp(graph, s))
