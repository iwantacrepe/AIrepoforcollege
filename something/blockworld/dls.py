import copy
def is_goal(state):
    goal_state = (('A', None), ('B', 'A'), ('C', 'B'))
    return state == goal_state

def get_children(state):
    children = []
    for i, (block, _) in enumerate(state):
        new_state = copy.deepcopy(state)
        new_state[i] = (block, None)
        children.append(tuple(new_state))
    
        for j, (other_block, other_base) in enumerate(state):
            if i != j and other_base is None:
                new_state = copy.deepcopy(state)
                new_state[i] = (block, other_block)
                children.append(tuple(new_state))
    return children

def depth_limited_search(state, depth):
    stack = [(state, None, 0)]  # Stack holds tuples of (state, parent state, current depth)
    explored = {}
    parents = {tuple(state): None}

    while stack:
        current_state, parent, current_depth = stack.pop()

        if tuple(current_state) in explored and explored[tuple(current_state)] <= current_depth:
            continue
        
        explored[tuple(current_state)] = current_depth
        parents[tuple(current_state)] = parent

        if is_goal(current_state):
            path = []
            step = current_state
            while step:
                path.append(step)
                step = parents[tuple(step)]
            path.reverse()
            return path

        if current_depth < depth:
            for child in get_children(current_state):
                child_tuple = tuple(child)
                if child_tuple not in explored or explored[child_tuple] > current_depth + 1:
                    stack.append((child, current_state, current_depth + 1))

    return None  # If no solution is found within the given depth

def solve(initial_state, max_depth):
    for depth in range(max_depth + 1):
        print("Searching at depth:", depth)
        solution = depth_limited_search(initial_state, depth)
        if solution:
            return solution
    return None

initial_state = (('A', None), ('B', None), ('C', 'B'))
max_depth = 3

solution = solve(initial_state, max_depth)

if solution:
    print("Solution found:")
    for state in solution:
        print(state)
else:
    print("No solution found within the maximum depth.")
