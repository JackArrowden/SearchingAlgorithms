### GBFS algorithm

def GBFS(G, h, s, g):
    if s == g:
        return [s]
    
    reached = [s]
    priorityQueue = [[h[s], s]] # Behaves as a priority queue
    
    n = len(G)
    prevNode = [-1] * n # Used for tracking the path returned
    
    while len(priorityQueue) != 0:
        priorityQueue.sort()
        cur = priorityQueue.pop(0)[1]
        
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
                priorityQueue.append([h[i], i])
                prevNode[i] = cur
        
    return [-1]