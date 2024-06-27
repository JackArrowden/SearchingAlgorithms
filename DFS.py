### Tree search DFS algorithm

def DFSRecursive(G, n, cur, g, path):
    # Check for early stopping
    for i in range(n):
        if G[cur][i] != 0 and i == g:
            return True
        
    # If haven't found the path yet, continue searching
    for i in range(n):
        # A vertex can traverse to itself, we don't consider this case
        if i == cur:
            continue
        
        # If there is a vertex can be traversed
        if (i not in path) and (G[cur][i] != 0):
            path.append(i)
            if DFSRecursive(G, n, i, g, path) == True:
                return True
            path.pop()
            
    # No path was found, return False
    return False

def DFS(G, s, g): # G is graph, s is start vertex, g is goal vertex
    if s == g:
        return [g]
    
    path = [s] # The path to the goal
    n = len(G) # Using the number of vertice as a parameter to reduce the number of time that calculate this number
    
    if DFSRecursive(G, n, s, g, path) == False:
        return [-1]
    
    return path