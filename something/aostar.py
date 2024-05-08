graph = {}
heuristics = {}
start = None
parent = {}
status = {}
solution = {}

def apply_ao():
    ao_star(start, False)
    print("Final solution:", solution)

def neighbour(v):
    return graph.get(v, [])

def get_status(v):
    return status.get(v, 0)

def set_status(v, val):
    status[v] = val

def get_heur_val(n):
    return heuristics.get(n, 0)

def set_heur_val(n, value):
    heuristics[n] = value

def min_cost_node(v):
    minimum = 0
    cost_child = {}
    cost_child[minimum] = []
    flag = True
    for node_info_tuple_list in neighbour(v):
        cost = 0
        nodelist = []
        for c, weight in node_info_tuple_list:
            cost += get_heur_val(c) + weight
            nodelist.append(c)
        if flag:
            minimum = cost
            cost_child[minimum] = nodelist
            flag = False
        elif minimum > cost:
            minimum = cost
            cost_child[minimum] = nodelist
    return minimum, cost_child[minimum]

def ao_star(v, backtrack):
    print("Heuristic value:", heuristics)
    print("Solution:", solution)
    print("Processing node:", v)
    if get_status(v) >= 0:
        min_cost, child_nodelist = min_cost_node(v)
        set_heur_val(v, len(child_nodelist))
        solved = True
        for child_node in child_nodelist:
            parent[child_node] = v
            if get_status(child_node) != -1:
                solved &= False
        if solved:
            set_status(v, -1)
            solution[v] = child_nodelist
        if v != start:
            ao_star(parent[v], True)
    if not backtrack:
        if child_nodelist:
            for child_node in child_nodelist:
                set_status(child_node, 0)
                ao_star(child_node, False)

heuristics = {'A': 1, 'B': 6, 'C': 12, 'D': 10, 'E': 4, 'F': 4, 'G': 5, 'H': 7}
graph = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],
    'B': [[('G', 1)], [('H', 1)]],
    'D': [[('E', 1), ('F', 1)]]
}
start = 'A'

apply_ao()
