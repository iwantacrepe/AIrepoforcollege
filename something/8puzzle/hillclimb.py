import copy

def calculate_heuristic(state):
    goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    misplaced = 0
    for i in range(9):
            if state[i] != goal_state[i] and state[i] != 0:
                misplaced += 1
    return misplaced

def is_goal(state):
    return state == [1, 2, 3, 8, 0, 4, 7, 6, 5]

def get_possible_moves(state):
    moves = []
    blank_index = state.index(0)
    row = blank_index // 3
    col = blank_index % 3

    def swap_tiles(i, j):
        new_state = copy.deepcopy(state)
        new_state[i], new_state[j] = new_state[j], new_state[i]
        return new_state

    if row > 0:  # Move up
        moves.append(swap_tiles(blank_index, blank_index - 3))
    if row < 2:  # Move down
        moves.append(swap_tiles(blank_index, blank_index + 3))
    if col > 0:  # Move left
        moves.append(swap_tiles(blank_index, blank_index - 1))
    if col < 2:  # Move right
        moves.append(swap_tiles(blank_index, blank_index + 1))

    return moves

def hill_climbing_solver(initial_state):
    current_state = initial_state
    path = [current_state]
    current_heuristic = calculate_heuristic(current_state)

    while True:
        next_moves = get_possible_moves(current_state)
        if not next_moves:
            break

        evaluated_moves = [(move, calculate_heuristic(move)) for move in next_moves]
        next_move, next_move_heuristic = min(evaluated_moves, key=lambda x: x[1])

        if next_move_heuristic >= current_heuristic:
            break

        current_state = next_move
        current_heuristic = next_move_heuristic
        path.append(current_state)

        if is_goal(current_state):
            break

    return path

# Example Usage
initial_state = [2, 0, 3, 1, 8, 4, 7, 6, 5]
goal= [1, 2, 3, 8, 0, 4, 7, 6, 5]
solution_path = hill_climbing_solver(initial_state)

if solution_path[-1] ==goal:
    for state in solution_path:
        for i in range(3):
            print(state[i * 3:i * 3 + 3])
        print()
else:
    print("No solution found")
