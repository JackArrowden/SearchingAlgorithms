### BFS algorithm

def BFS(G, s, g):
    if s == g:
        return [s]
    
    reached = [s]
    frontier = [s] # Behaves as a FIFO queue
    
    n = len(G)
    prevNode = [-1] * n # Used for tracking the path returned
    
    while len(frontier) != 0:
        cur = frontier.pop(0) # First in first out
        
        for i in range(n):
            if i in reached or G[cur][i] == 0:
                continue
            
            # Check if reach the goal: Early check
            if i == g:
                path = [cur, g]
                while prevNode[cur] != -1:
                    path.insert(0, prevNode[cur])
                    cur = prevNode[cur]
                return path
            
            # If not reach the goal
            if i not in reached:
                reached.append(i)
                frontier.append(i)
                prevNode[i] = cur
        
    return [-1]