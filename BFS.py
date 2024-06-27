### BFS algorithm

def BFSRecursive(G, n, g, visited, frontier, path):
    cur = frontier.pop()
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
    if len(frontier) == 0:
        return False
            
    # Call recursion
    while len(frontier) != 0:
        path.append(frontier[len(frontier) - 1])
        if BFSRecursive(G, n, g, visited, frontier, path) == True:
            return True
        path.pop()
    
    # No path was found, return False
    return False

def BFS(G, s, g): # G is graph, s is start vertex, g is goal vertex
    if s == g:
        return [g]
    
    visited = []
    frontier = [s]
    path = [s] # The path to the goal
    n = len(G) # Using the number of vertice as a parameter to reduce the number of time that calculate this number
    
    if BFSRecursive(G, n, g, visited, frontier, path) == False:
        return [-1]
    
    return path