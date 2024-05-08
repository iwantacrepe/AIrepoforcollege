import copy

def swap_tiles(state, i, j):
    new_state = copy.deepcopy(state)
    new_state[i], new_state[j] = new_state[j], new_state[i]
    return new_state

def get_possible_moves(state):
    moves = []
    blank_index = state.index(0)
    row = blank_index // 3
    col = blank_index % 3

    # Check for possible moves in each direction
    if row > 0:
        moves.append(swap_tiles(state, blank_index, blank_index - 3))
    if row < 2:
        moves.append(swap_tiles(state, blank_index, blank_index + 3))
    if col > 0:
        moves.append(swap_tiles(state, blank_index, blank_index - 1))
    if col < 2:
        moves.append(swap_tiles(state, blank_index, blank_index + 1))

    return moves

def is_goal(state):
    return state == [2, 8, 1, 0, 4, 3, 7, 6, 5]

def bfs_solver(initial_state):
    frontier = [(initial_state, None)]  # Store state and parent state
    explored = set()
    parents = {tuple(initial_state): None}

    while frontier:
        current_state, parent = frontier.pop()
        explored.add(tuple(current_state))

        if is_goal(current_state):
            return current_state, parents

        for move in get_possible_moves(current_state):
            if tuple(move) not in explored:
                frontier.append((move, current_state))
                parents[tuple(move)] = current_state

    return None  # No solution found

initial_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]  
result = bfs_solver(initial_state)

if result:
    current_state, parents = result
    path = []
    while current_state:
        path.append(current_state)
        current_state = parents[tuple(current_state)]
    path.reverse()
    
    k = 0
    for i in path:
        for j in i:
            if k < 3:
                print(j, end=' ')
                k += 1
            
            if k == 3:
                k = 0
                print()
        print()
else:
    print("No solution found")
