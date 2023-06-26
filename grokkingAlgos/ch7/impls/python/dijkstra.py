# A hash map can be used to represent the edge weight between nodes
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["b"] = {}
graph["a"]["fin"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

infinity = float("inf")
costs = {"a": graph["start"]["a"],"b": graph["start"]["b"], "fin": infinity }
parents = {"a": "start", "b": "start", "fin": None}
processed = []

def find_lowest_cost_node(costs):
    min = None
    min_node = None
    for node in costs.keys():
        if node not in processed and min is None:
            min = costs[node]
            min_node = node
        elif node not in processed and costs[node] < min:
            min = costs[node]
            min_node = node
    return min_node

print("Before: costs, then parents:")
print(costs)
print(parents)
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
print("After: costs, then parents:")
print(costs)
print(parents)
