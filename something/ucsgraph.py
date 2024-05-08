#ucs
import heapq
def ucs(graph, start, goal):
    pqueue = [(0, start)]  
    visited = set()
    
    while pqueue:
        (cost, node) = heapq.heappop(pqueue)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return cost

        for neighbor, edge_cost in graph.get(node, []):  
            heapq.heappush(pqueue, (cost + edge_cost , neighbor ))

graph = {
    's': [('a', 1), ('b', 5), ('c', 15)],
    'a': [('g', 10)],
    'b': [('g', 15)],
    'c': [('g', 5)]
}

result_cost = ucs(graph, 's', 'g')
if result_cost is not None:
    print(f"Found path with cost: {result_cost}")
else:
    print("No path found to the goal")
    
print(graph)