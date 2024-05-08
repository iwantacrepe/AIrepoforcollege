#bfs
def isgoal(state):
    goal_state = (('A', None), ('B', 'A'), ('C', 'B'))
    return state == goal_state

def getchildren(state):
    children = []
    for i, (block, _) in enumerate(state):
        new_state = list(state)
        new_state[i] = (block, None)
        children.append(tuple(new_state))

        for j, (other_block, _) in enumerate(state):
            if i != j:
                new_state = list(state)
                new_state[i] = (block, other_block)
                new_state[j] = (other_block, None)
                children.append(tuple(new_state))
    return children

def solve(initial_state):
    queue = [initial_state]
    visited = set()

    while queue:
        state = queue.pop(0)
        visited.add(state)

        print("Current state:", state) 

        if isgoal(state):
            return state

        for child in getchildren(state):
            if child not in visited:
                queue.append(child)
                visited.add(child)

    return None 

initial_state = (('A', None), ('B', None), ('C', 'B'))


solution = solve(initial_state)

if solution:
    print("Solution found:", solution)
else:
    print("No solution found.")