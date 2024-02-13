# the graph
graph = {}


# the hash teble for start
graph["start"] = {}
graph["start"]["a"] = 36
graph["start"]["b"] = 13


# the hash teble for a
graph["a"] = {}
graph["a"]["f"] = 83
graph["a"]["i"] = 76


# the hash teble for b
graph["b"] = {}
graph["b"]["c"] = 80


# the hash teble for c
graph["c"] = {}
graph["c"]["d"] = 10


# the hash teble for d
graph["d"] = {}
graph["d"]["fin"] = 166

# the hash teble for j
graph["j"] = {}
graph["j"]["h"] = 50

# the hash teble for f
graph["f"] = {}
graph["f"]["j"] = 26

# the hash teble for i
graph["i"] = {}
graph["i"]["g"] = 40

# the hash teble for g
graph["g"] = {}
graph["g"]["fin"] = 107

# the hash teble for h
graph["h"] = {}
graph["h"]["fin"] = 75

# the hash teble for fin
graph["fin"] = {}

# hash table for costs
infinity = float("inf")
costs = {}
costs["a"] = 36
costs["b"] = 13
costs["c"] = infinity
costs["d"] = infinity
costs["i"] = infinity
costs["f"] = infinity
costs["j"] = infinity
costs["g"] = infinity
costs["h"] = infinity
costs["fin"] = infinity

# hash table for parents
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = infinity
parents["d"] = infinity
parents["i"] = infinity
parents["f"] = infinity
parents["j"] = infinity
parents["g"] = infinity
parents["h"] = infinity
parents["fin"] = infinity

# the array for processing all nodes
processed = []


# this function for find lowest costs node
def find_lowest_costs_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# main app
node = find_lowest_costs_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_costs_node(costs)

# cost for finish
print(f"{costs["fin"]}m")
