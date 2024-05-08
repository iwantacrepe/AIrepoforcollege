#dfs
from collections import deque

def isgoal(state, ):
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

def solve(initial_state,):
    stack = [initial_state]
    visited = set()

    while stack:
        state = stack.pop()
        visited.add(state)
        
        print("Current state:", state)

        if isgoal(state,):
            return state

        for child in getchildren(state):
            if child not in visited:
                stack.append(child)

    return None  

initial_state = (('A', None), ('B', None), ('C', 'B'))
goal_state = (('A', None), ('B', 'A'), ('C', 'B'))

solution = solve(initial_state)

if solution:
    print("Solution found:", solution)
else:
    print("No solution found.")
