def water_jug_problem(jug1_cap, jug2_cap, jug3_cap, jug4_cap, target_amount):
    j1, j2, j3, j4 = 0, 0, 0, 0
    actions = [
        ("fill", 1), ("fill", 2), ("fill", 3), ("fill", 4),
        ("empty", 1), ("empty", 2), ("empty", 3), ("empty", 4),
        ("pour", 1, 2), ("pour", 2, 1), ("pour", 1, 3), ("pour", 3, 1), ("pour", 1, 4), ("pour", 4, 1),
        ("pour", 2, 3), ("pour", 3, 2), ("pour", 2, 4), ("pour", 4, 2),
        ("pour", 3, 4), ("pour", 4, 3)
    ]
    visited = set()
    queue = [(j1, j2, j3, j4, [])]  # (j1, j2, j3, j4) - current state; [] - actions list

    while queue:
        j1, j2, j3, j4, seq = queue.pop(0)
        if (j1, j2, j3, j4) not in visited:
            visited.add((j1, j2, j3, j4))
            if j1 == target_amount or j2 == target_amount or j3 == target_amount or j4 == target_amount:
                return seq

            for action in actions:
                if action[0] == "fill":
                    if action[1] == 1:
                        next_state = (jug1_cap, j2, j3, j4)
                    elif action[1] == 2:
                        next_state = (j1, jug2_cap, j3, j4)
                    elif action[1] == 3:
                        next_state = (j1, j2, jug3_cap, j4)
                    else:
                        next_state = (j1, j2, j3, jug4_cap)
                elif action[0] == "empty":
                    if action[1] == 1:
                        next_state = (0, j2, j3, j4)
                    elif action[1] == 2:
                        next_state = (j1, 0, j3, j4)
                    elif action[1] == 3:
                        next_state = (j1, j2, 0, j4)
                    else:
                        next_state = (j1, j2, j3, 0)
                else:  # "pour"
                    src, dest = action[1], action[2]
                    jugs = [j1, j2, j3, j4]
                    amount = min(jugs[src-1], jug_caps[dest-1] - jugs[dest-1])
                    jugs[src-1] -= amount
                    jugs[dest-1] += amount
                    next_state = tuple(jugs)
                
                if next_state not in visited:
                    next_seq = seq + [action]
                    queue.append((*next_state, next_seq))

    return None

# Capacities of the jugs
jug_caps = [4, 3, 5, 7]

# Example usage
result = water_jug_problem(*jug_caps, target_amount=2)
print(result)
