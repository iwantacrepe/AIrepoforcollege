def water_jug_problem(jug1_cap, jug2_cap, target_amount):    
    j1 = 0  
    j2 = 0  
    actions = [("fill", 1), ("fill", 2), ("empty", 1), ("empty", 2), ("pour", 1, 2), ("pour", 2, 1)]     
    visited = set()    
    queue = [(j1, j2, [])]  # (j1, j2) - current state of the system; [] - list of performed actions
    while queue:    # BFS loop, returns positive value if not empty
        j1, j2, seq = queue.pop(0) # j1 - 0, j2 - 0, sequence empty for first iteration
        if (j1, j2) not in visited:  #don't visit the same situation again
            visited.add((j1, j2))   #add j1, j2 in set
            if j1 == target_amount:  #target amount given in question
                return seq  #returns which action and amount present in the jugs 

            for i in actions:  #i is one tuple in the list actions
                if i [0] == "fill": # which action 
                    if i[1] == 1:  # on whom
                        next_state = (jug1_cap, j2)  
                    else:  
                        next_state = (j1, jug2_cap)  
                elif i[0] == "empty":  
                    if i[1] == 1:  
                        next_state = (0, j2)  
                    else:  
                        next_state = (j1, 0)  
                else:  #by default pour
                    if i[1] == 1:  
                        amount = min(j1, jug2_cap - j2)  
                        next_state = (j1 - amount, j2 + amount)  
                    else:  
                        amount = min(j2, jug1_cap - j1)  
                        next_state = (j1 + amount, j2 - amount)  
                 
                if next_state not in visited:  
                    next_seq = seq + [i] # adding the index 
                    queue.append((next_state[0], next_state[1], next_seq))     
    
    return None  
result = water_jug_problem(4, 3, 2)  
print(result)