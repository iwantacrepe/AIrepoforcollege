import heapq
import copy

heuristics = {'A': 1, 'B': 6, 'C': 12, 'D': 10, 'E': 4, 'F': 4, 'G': 5, 'H': 7}

graph = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],
    'B': [[('G', 1)], [('H', 1)]],
    'D': [[('E', 1), ('F', 1)]]
}

def ao_star(node, g):
    if node not in graph:
        return heuristics[node]

    min_cost = float('inf')
    for compound_action in graph[node]:
        cost = sum(ao_star(child, g+cost) for child, cost in compound_action)
        if cost < min_cost:
            min_cost = cost
            best_action = compound_action

    sol[node] = best_action
    return min_cost

sol = {}
start = 'A'
result_cost = ao_star(start, 0)

print(f"Best solution from {start} with cost {result_cost}")
print("Solution path:")
def print_solution(node):
    if node not in sol:
        print(node)
        return
    print(node, "->", end=" ")
    for child, _ in sol[node]:
        print_solution(child)

print_solution(start)
