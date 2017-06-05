

# Takes a graph that is in the form of a dictionary, with the values as sets.


graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}



# Function tels if there exists a path - and gives it's found path
# Nodes must have unique names, entered as strings

def depth_first_search(graph, start, goal, visited=set()):

    next_nodes = graph[start]

    # breadth first
    # for node in next_nodes:
    #     recursive_depth(graph, node, end, visited)

    while min(next_nodes) in visited:

        next_nodes.remove(min(next_nodes))

    if len(next_nodes) > 0 :

        # Add the current node to visited
        visited.add(min(next_nodes))

        if min(next_nodes) == goal:
            return visited

        else:
            depth_first_search(graph, min(next_nodes), goal,)

    else:

        # not in list.
        return False




print(depth_first_search(graph=graph, start='A', goal='F'))

