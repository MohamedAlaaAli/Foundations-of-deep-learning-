def adjacency_matrix(edges, num_vertices):
    """
    Takes in a list of edges and the number of vertices in the graph and returns an adjacency matrix as a 2D array.

    Parameters:
        - edges: a list of tuples representing edges in the graph, where each tuple contains two vertices (strings or integers)
        - num_vertices: an integer representing the number of vertices in the graph

    Returns:
        - a 2D array representing the adjacency matrix of the graph
    """
    adj_mtrx = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
    for edge in edges:
        v1, v2 = edge
        adj_mtrx[v1][v2] = 1
        adj_mtrx[v2][v1] = 1
    return adj_mtrx

#print(adjacency_matrix([(1,2)], 5))

def adjacency_list(edges:list):
    """Takes a list of edges in a graph and returns an adjacency list

    Parameters:
        - edges : a list of tuples representing edges in the graph

    Returns:
        - an adjacency list of the graph

    """
    adj_lst = {}
    for edge in edges:
        v1, v2 = edge
        if v1 not in adj_lst:
            adj_lst[v1] = []
        adj_lst[v1].append(v2)
        if v2 not in adj_lst:
            adj_lst[v2] = []
        adj_lst[v2].append(v1)

    return adj_lst

#print(adjacency_list([(0, 1), (0, 2), (1, 2), (2, 3)]))

from collections import deque

def bfs(source:int, edges:dict, target=None, search=False):
    """A function that returns the breadth first traversal
    for each node in the graph that is reachable from the source node

    Parameters:
        source(int) : an integer representing the node to start traversal from
        edges(dict) : a dictionary where each key is a parent node and the values correspond to the childern
    """

    q = deque() # to keep track of the parent
    visited = set()
    q.append(source)
    visited.add(source)
    sort = [] #holds the bfs result

    while len(q) > 0 :
        curr = q.popleft()
        print(f"BFS visiting node {curr}")
        sort.append(curr)

        for child in edges[curr]:
            if child not in visited:
                q.append(child)
                visited.add(child)
    return sort

graph_2_vertices = list(range(6))
graph_2_edges = {
    0 : [1, 3],
    1 : [4],
    2 : [4, 5],
    3 : [1],
    4 : [3],
    5 : [5],
}
#_ = bfs(source=1,edges=graph_2_edges)

def dfs(source:int, vertices:list, edges:dict, visited=set(), topo=False):
    if visited is None:
        visited = set()
    try:
        visited.add(source)
        vertices.remove(source)
        print(f" dfs visiting node {source}")
        for child in graph_2_edges[source]:
            if child not in visited:
                dfs(source=child, vertices = vertices, edges=graph_2_edges, visited= visited)
        if len(vertices) != 0 :
            dfs(source = vertices[0], vertices=vertices, edges=graph_2_edges, visited= visited)
    except Exception:
        pass

#dfs(0, graph_2_vertices, graph_2_edges)

def rv_topo_srt(vertices, edges, srt=[],visited=None):
    if visited is None:
        visited = set()
    for node in vertices:
        if node not in visited:
            dfs(node, vertices, edges, visited, topo=True)






x=rv_topo_srt(graph_2_vertices, graph_2_edges)
print(x)

