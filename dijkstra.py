graph = {}
graph["start"] = {}
graph["start"]["a"]=6;
graph["start"]["b"]=2;

graph["a"]={}
graph["a"]["fin"]=1;

graph["b"]= {}
graph["b"]["a"]=3
graph["b"]["fin"]=5

graph["fin"] = {}

costs={}
infinit = float("inf")
costs["a"]=6;
costs["b"] = 2
costs["fin"]=infinit

parents={}
parents["a"]="start"
parents["b"]="start"
parents["fin"]=None

processed = []

def find_lowst_cost_node(costs):
    nodes =costs.keys()
    lowest = float("inf")
    key = None;
    for n in nodes:
        if lowest > costs[n] and n not in processed:
            lowest = costs[n]
            key = n;
    return key
   
   

# print(find_lowst_cost_node(costs))
def find_best_path(graph,costs,parents):
    node = find_lowst_cost_node(costs)     
    while node is not None:
        cost = costs[node]
        neighbors=graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node;
        processed.append(node)
        node = find_lowst_cost_node(costs)
    return parents;
print(find_best_path(graph,costs,parents));
