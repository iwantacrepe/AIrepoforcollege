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
    goal_state = [2, 8, 1, 0, 4, 3, 7, 6, 5]
    return sum(1 for i, tile in enumerate(state) if tile != goal_state[i] and tile != 0)

def is_goal(state):
    return state == [2, 8, 1, 0, 4, 3, 7, 6, 5]

def astar_solver(initial_state):
    costs = {tuple(initial_state): 0}
    frontier = [(heuristic(initial_state), initial_state)]
    explored = set()

    while frontier:
        _, current_state = heapq.heappop(frontier)
        if tuple(current_state) in explored:
            continue
        explored.add(tuple(current_state))

        if is_goal(current_state):
            return current_state, costs

        for move in get_possible_moves(current_state):
            move_tuple = tuple(move)
            cost = costs[tuple(current_state)] + 1  # Assume each move has a cost of 1
            f_score = cost + heuristic(move)

            if move_tuple not in explored or cost < costs.get(move_tuple, float('inf')):
                heapq.heappush(frontier, (f_score, move))
                costs[move_tuple] = cost

    return None  # No solution found

# Example usage
initial_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
result = astar_solver(initial_state)

if result:
    solution_state, costs = result
    print("Solution found:", solution_state)
    print("Total cost to solve:", costs[tuple(solution_state)])
else:
    print("No solution found")
