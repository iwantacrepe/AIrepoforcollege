#dls
from collections import deque

def isgoal(state):
    return state == (('A', None), ('B', 'A'), ('C', 'B'))

def getchildren(state):
    children = []
    for i, (block, _) in enumerate(state):
        new_state = list(state)
        new_state[i] = (block, None)
        children.append(tuple(new_state))
    
        for j, (other_block, _) in enumerate(state):
            if i != j and other_block is not None:
                new_state = list(state)
                new_state[i] = (block, other_block)
                new_state[j] = (other_block, None)
                children.append(tuple(new_state))
    return children

def depth_limited_search(state, depth):
    if depth == 0:
        return None 

    if isgoal(state):
        return state  

    for child in getchildren(state):
        print("Current state at depth", depth, ":", child)
        solution = depth_limited_search(child, depth - 1)
        if solution:
            return solution  
    return None  

def solve(initial_state, max_depth):
    for depth in range(max_depth + 1):
        print("At depth", depth)
        solution = depth_limited_search(initial_state, depth)
        if solution:
            return solution
    return None  

initial_state = (('A', None), ('B', None), ('C', 'B'))
goal_state = (('A', None), ('B', 'A'), ('C', 'B'))
max_depth = 3

solution = solve(initial_state, max_depth)

if solution:
    print("Solution found:", solution)
else:
    print("No solution found within the maximum depth.")
