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

def is_goal(state):
    return state == [2, 8, 1, 0, 4, 3, 7, 6, 5]

def ucs_solver(initial_state):
    frontier = [(0, initial_state, None)]  # (cost, state, parent)
    explored = set()
    parents = {tuple(initial_state): None}
    costs = {tuple(initial_state): 0}

    while frontier:
        cost, current_state, parent = heapq.heappop(frontier)
        if tuple(current_state) in explored:
            continue
        if is_goal(current_state):
            return current_state, parents, costs  # Return information needed for path reconstruction
        explored.add(tuple(current_state))
        parents[tuple(current_state)] = parent
        for move in get_possible_moves(current_state):
            move_tuple = tuple(move)
            move_cost = cost + 1
            if move_tuple not in explored or costs.get(move_tuple, float('inf')) > move_cost:
                heapq.heappush(frontier, (move_cost, move, current_state))
                parents[move_tuple] = current_state
                costs[move_tuple] = move_cost

    return None, None, None  # No solution found

def reconstruct_path(final_state, parents):
    path = []
    while final_state:
        path.append(final_state)
        final_state = parents[tuple(final_state)]
    path.reverse()
    return path

# Example Usage
initial_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
final_state, parents, costs = ucs_solver(initial_state)

if final_state:
    path = reconstruct_path(final_state, parents)
    for state in path:
        k = 0
        for num in state:
            print(num, end=' ')
            k += 1
            if k % 3 == 0:
                print()  # New line every three numbers
        print()  # Blank line between states
else:
    print("No solution found")
