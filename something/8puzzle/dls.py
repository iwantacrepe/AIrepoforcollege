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

    if row > 0:  # Move up
        moves.append(swap_tiles(state, blank_index, blank_index - 3))
    if row < 2:  # Move down
        moves.append(swap_tiles(state, blank_index, blank_index + 3))
    if col > 0:  # Move left
        moves.append(swap_tiles(state, blank_index, blank_index - 1))
    if col < 2:  # Move right
        moves.append(swap_tiles(state, blank_index, blank_index + 1))

    return moves

def is_goal(state):
    return state == [2, 8, 1, 0, 4, 3, 7, 6, 5]

def dls_solver(initial_state, limit):
    frontier = [(initial_state, None, 0)]  # Stack: state, parent, depth
    explored = {}
    parents = {tuple(initial_state): None}

    while frontier:
        current_state, parent, depth = frontier.pop()  # LIFO stack

        if tuple(current_state) in explored and explored[tuple(current_state)] <= depth:
            continue
        
        explored[tuple(current_state)] = depth
        parents[tuple(current_state)] = parent

        if is_goal(current_state):
            path = []
            while current_state:
                path.append(current_state)
                current_state = parents[tuple(current_state)]
            path.reverse()
            return path

        if depth < limit:
            for move in get_possible_moves(current_state):
                move_tuple = tuple(move)
                if move_tuple not in explored or explored[move_tuple] > depth + 1:
                    frontier.append((move, current_state, depth + 1))

    return None  # Return None if no solution found within the depth limit

initial_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
depth_limit = 9  # Set a limit for depth
result = dls_solver(initial_state, depth_limit)

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
