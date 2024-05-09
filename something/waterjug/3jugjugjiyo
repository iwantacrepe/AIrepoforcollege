def water_jug_problem(jug1_cap, jug2_cap, jug3_cap, target_amount):
    j1, j2, j3 = 0, 0, 0
    actions = [
        ("fill", 1), ("fill", 2), ("fill", 3),
        ("empty", 1), ("empty", 2), ("empty", 3),
        ("pour", 1, 2), ("pour", 2, 1), ("pour", 1, 3), ("pour", 3, 1), ("pour", 2, 3), ("pour", 3, 2)
    ]
    visited = set()
    queue = [(j1, j2, j3, [])]  # (j1, j2, j3) - current state; [] - actions list

    while queue:
        j1, j2, j3, seq = queue.pop(0)
        if (j1, j2, j3) not in visited:
            visited.add((j1, j2, j3))
            if j1 == target_amount or j2 == target_amount or j3 == target_amount:
                return seq

            for action in actions:
                if action[0] == "fill":
                    if action[1] == 1:
                        next_state = (jug1_cap, j2, j3)
                    elif action[1] == 2:
                        next_state = (j1, jug2_cap, j3)
                    else:
                        next_state = (j1, j2, jug3_cap)
                elif action[0] == "empty":
                    if action[1] == 1:
                        next_state = (0, j2, j3)
                    elif action[1] == 2:
                        next_state = (j1, 0, j3)
                    else:
                        next_state = (j1, j2, 0)
                else:  # "pour"
                    if action[1] == 1:
                        if action[2] == 2:
                            amount = min(j1, jug2_cap - j2)
                            next_state = (j1 - amount, j2 + amount, j3)
                        else:
                            amount = min(j1, jug3_cap - j3)
                            next_state = (j1 - amount, j2, j3 + amount)
                    elif action[1] == 2:
                        if action[2] == 1:
                            amount = min(j2, jug1_cap - j1)
                            next_state = (j1 + amount, j2 - amount, j3)
                        else:
                            amount = min(j2, jug3_cap - j3)
                            next_state = (j1, j2 - amount, j3 + amount)
                    else:  # From jug 3
                        if action[2] == 1:
                            amount = min(j3, jug1_cap - j1)
                            next_state = (j1 + amount, j2, j3 - amount)
                        else:
                            amount = min(j3, jug2_cap - j2)
                            next_state = (j1, j2 + amount, j3 - amount)
                
                if next_state not in visited:
                    next_seq = seq + [action]
                    queue.append((next_state[0], next_state[1], next_state[2], next_seq))

    return None

# Example usage
result = water_jug_problem(4, 3, 5, 2)
print(result)
