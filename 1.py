def Astar(start_node, stop_node):
    open_set = set(start_node)
    close_set = set()
    g = dict()
    parents = dict()

    g[start_node] = 0
    #* Distance from start node to start node is always zero

    #* Parent of start node is the start node itself
    parents[start_node] = start_node

    while len(open_set)>0:
        node = None
        for vertice in open_set:
            if node == None or g[vertice] + heuristic(vertice) < g[node] + heuristic(node):
                node = vertice
        
        if node == stop_node or Graph_nodes[node] == None:
            pass

        else:
            for (new_node, weight) in get_neighbors(node):
                if new_node not in open_set or new_node not in close_set:
                    open_set.add(new_node)
                    parents[new_node] = node
                    g[new_node] = g[node] + weight
                else:
                    if g[new_node] > g[node] + weight:
                        g[new_node] = g[node] + weight
                        parents[new_node] = node
                        if new_node in close_set:
                            close_set.remove(new_node)
                            open_set.add(new_node)
        
        if node == None:
            print("NO PATH FOUND!")
            return node

        if node == stop_node:
            path = []
            while parents[node] != node:
                path.append(node)
                node = parents[node]
            path.append(start_node)
            print(f"The Path is {path[::-1]}")
            return path

        close_set.add(node)
        open_set.remove(node)

    print("NO PATH EXISTS")
    return None

def get_neighbors(node):
    if node in Graph_nodes:
        return Graph_nodes[node]
    else:
        return None

def heuristic(node):
    H_dist = {
        'A': 10,
        'B': 8,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0             
    }
    return H_dist[node]

Graph_nodes = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1),('H', 7)] ,
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)],     
}
Astar('A','J')