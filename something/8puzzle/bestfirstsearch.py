import copy
import heapq

def swap_tiles(state, i, j):
    new_state = copy.deepcopy(state)
    new_state[i], new_state[j] = new_state[j], new_state[i]
    return new_state

def get_possible_moves(state):
    moves = []
    blank_index = state.index(0)
    row = blank_index // 3
    col = blank_index % 3

    if row > 0:
        moves.append(swap_tiles(state, blank_index, blank_index - 3))
    if row < 2:
        moves.append(swap_tiles(state, blank_index, blank_index + 3))
    if col > 0:
        moves.append(swap_tiles(state, blank_index, blank_index - 1))
    if col < 2:
        moves.append(swap_tiles(state, blank_index, blank_index + 1))

    return moves

def heuristic(state):
    goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    misplaced = 0
    for i in range(9):
            if state[i] != goal_state[i] and state[i] != 0:
                misplaced += 1
    return misplaced

def is_goal(state):
    goal_state = [2, 8, 1, 0, 4, 3, 7, 6, 5]
    return state == goal_state

def best_first_search_solver(initial_state):
    priority_queue = [(heuristic(initial_state), initial_state)]
    explored = set()
    parents = {tuple(initial_state): None}

    while priority_queue:
        _, current_state = heapq.heappop(priority_queue)
        explored.add(tuple(current_state))

        if is_goal(current_state):
            return current_state, parents

        for move in get_possible_moves(current_state):
            if tuple(move) not in explored:
                heapq.heappush(priority_queue, (heuristic(move), move))
                parents[tuple(move)] = current_state

    return None  # No solution found

# Example usage
initial_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
result = best_first_search_solver(initial_state)

if result:
    current_state, parents = result
    path = []
    while current_state:
        path.append(current_state)
        current_state = parents[tuple(current_state)]
    path.reverse()

    # Printing the result as a 3x3 grid
    k = 0
    for i in path:
        for j in i:
            if k < 3:
                print(j, end=' ')
                k += 1
            
            if k == 3:
                k = 0
                print()
        print()  # Print a newline for better separation between states
else:
    print("No solution found")
