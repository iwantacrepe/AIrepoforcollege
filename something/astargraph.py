import heapq

def a_star_algorithm(start, goal):
    graph = {
        'A': {'B': 6, 'D': 3},
        'B': {'A': 6, 'D': 2, 'E': 8},
        'C': {'E': 5, 'F': 7},
        'D': {'A': 3, 'B': 2, 'E': 7, 'F': 8},
        'E': {'B': 8, 'C': 5, 'D': 7, 'J': 10},
        'F': {'C': 7, 'D': 8, 'G': 6},
        'G': {'F': 6, 'H': 1, 'I': 8},
        'H': {'G': 1, 'I': 3},
        'I': {'G': 8, 'H': 3, 'J': 4},
        'J': {'E': 10, 'I': 4}
    }
    
    heuristics = {
        'A': 10, 'B': 6, 'C': 2, 'D': 10, 'E': 4, 'F': 4, 'G': 5, 'H': 7, 'I': 3, 'J': 0
    }
    
    # Priority queue: (estimated_cost, current_node, cost_so_far, path_taken)
    priority_queue = [(heuristics[start], start, 0, [start])]
    visited = set()
    
    while priority_queue:
        # Select the node with the smallest estimated cost
        est_cost, current_node, cost_so_far, path = heapq.heappop(priority_queue)
        
        if current_node in visited:
            continue
        visited.add(current_node)
        
        # Check if we have reached the goal
        if current_node == goal:
            return path, cost_so_far
        
        # Explore each neighbo
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                total_cost = cost_so_far + weight
                estimated_cost = total_cost + heuristics[neighbor]
                heapq.heappush(priority_queue, (estimated_cost, neighbor, total_cost, path + [neighbor]))
    
    return None

# Example usage
path, cost = a_star_algorithm('A', 'J')
print("Path:", path)
print("Cost:", cost)
