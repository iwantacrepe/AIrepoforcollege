def is_goal(state):
    goal_state = (('A', None), ('B', 'A'), ('C', 'B'))
    return state == goal_state

def get_children(state):
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

def depth_limited_search(initial_state, limit):
    stack = [(initial_state, 0)]  # Stack stores tuples of (state, current depth)
    visited = set()

    while stack:
        state, depth = stack.pop()
        if depth > limit:
            continue  # Skip processing if the depth exceeds the limit

        visited.add(state)
        
        print("Current state:", state, "at depth:", depth)

        if is_goal(state):
            return state

        if depth < limit:  # Only add children to stack if within depth limit
            for child in get_children(state):
                if child not in visited:
                    stack.append((child, depth + 1))

    return None  

initial_state = (('A', None), ('B', None), ('C', 'B'))
depth_limit = 3  # Define a maximum depth limit

solution = depth_limited_search(initial_state, depth_limit)

if solution:
    print("Solution found:", solution)
else:
    print("No solution found.")
