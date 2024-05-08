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

def dls_solver(initial_state, limit, explored, parents):
    frontier = [(initial_state, None, 0)]  # Store state, parent state, and depth

    while frontier:
        current_state, parent, depth = frontier.pop()  # Use list as stack
        if tuple(current_state) in explored and depth > parents[tuple(current_state)]:
            continue
        
        explored.add(tuple(current_state))
        parents[tuple(current_state)] = parent

        if is_goal(current_state):
            # Reconstruct path back to the start
            path = []
            while current_state:
                path.append(current_state)
                current_state = parents[tuple(current_state)]
            path.reverse()
            return path

        if depth < limit:
            for move in reversed(get_possible_moves(current_state)):
                move_tuple = tuple(move)
                if move_tuple not in explored:
                    frontier.append((move, current_state, depth + 1))

    return None  # No solution found if nothing returned within limit

def iddfs_solver(initial_state):
    depth = 0
    while True:
        explored = set()
        parents = {tuple(initial_state): None}
        result = dls_solver(initial_state, depth, explored, parents)
        if result is not None:
            return (result,depth)
        depth += 1  # Increase the depth limit for the next iteration

initial_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
result,depth = iddfs_solver(initial_state)
print(f"Solution found at depth {depth}")

if result:
    for state in result:
        k = 0
        for num in state:
            print(num, end=' ')
            k += 1
            if k % 3 == 0:
                print()  # New line every three numbers
        print()  # Blank line between states
else:
    print("No solution found")
