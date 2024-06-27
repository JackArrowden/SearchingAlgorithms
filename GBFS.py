### GBFS algorithm

def GBFSRecursive(G, h, n, g, visited, frontier, path):
    cur = path[len(path) - 1]
    visited.append(cur)
    # Make sure to remove all occurences of "cur" from frontier
    while cur in frontier:
        frontier.remove(cur)
    
    # Check for early stopping
    for i in range(n):
        if G[cur][i] != 0 and i == g:
            return True
        
    # If haven't found the path yet, continue searching
    for i in range(n - 1, -1, -1): # Traverse backward so that the positions of elements will follow the alphabet order
        # A vertex can traverse to itself, we don't consider this case
        if i == cur:
            continue
        
        # If there is a vertex can be traversed
        if (i not in visited) and (G[cur][i] != 0):
            frontier.append(i)
            
    # Check frontier
    length = len(frontier)
    if length == 0:
        return False
            
    # Call recursion
    minHValue = h.index(max(h))
    while len(frontier) != 0:
        # Find the vertex that has the minimum heuristic value
        length = len(frontier)
        for i in range(length - 1, -1, -1):
            if (h[frontier[i]] < h[minHValue]):
                minHValue = frontier[i]
                
        # Start recursing
        path.append(minHValue)
        if GBFSRecursive(G, h, n, g, visited, frontier, path) == True:
            return True
        path.pop()
    
    # No path was found, return False
    return False

def GBFS(G, h, s, g): # G is graph, s is start vertex, g is goal vertex
    if s == g:
        return [g]
    
    visited = []
    frontier = [s]
    path = [s] # The path to the goal
    n = len(G) # Using the number of vertice as a parameter to reduce the number of time that calculate this number
    
    if GBFSRecursive(G, h, n, g, visited, frontier, path) == False:
        return [-1]
    
    return path