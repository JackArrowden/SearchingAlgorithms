### UCS algorithm

def UCSRecursive(G, n, g, visited, priorityQueue, path):
    top = priorityQueue.pop(0)
    cur = top[1] # Get the top vertex
    curWeight = top[0] # Get the price of top vertex
        
    # If g is popped out of priority queue
    if g == cur:
        path.append(top)
        return True
    
    visited.append(cur) # Update list of visited vertice
        
    # If haven't found the path yet, continue searching
    for i in range(n): # Traverse backward so that the positions of elements will follow the alphabet order
        # A vertex can traverse to itself, we don't consider this case
        if i == cur:
            continue
        
        # If there is a vertex can be traversed
        if (i not in visited) and (G[cur][i] != 0):
            curLen = len(priorityQueue)
            found = False
            for j in range(curLen):
                if priorityQueue[j][1] == i: # If i is in the queue
                    found = True
                    if (G[cur][i] + curWeight < priorityQueue[j][0]):
                        priorityQueue[j][0] = G[cur][i] + curWeight # Update new weight
                        priorityQueue[j][2] = cur # update new previous vertex
                    break
            if (found == False): # If i is not in the queue
                priorityQueue.append([G[cur][i] + curWeight, i, cur])
                
            
    # Check priorityQueue
    if len(priorityQueue) == 0:
        return False
            
    # Call recursion
    while len(priorityQueue) != 0:
        priorityQueue.sort() # Sort queue
        
        if UCSRecursive(G, n, g, visited, priorityQueue, path) == True:
            if cur == path[0][2]: # If a vertex is the previous vertex of the top vertex in the path, add it to the top of path
                path.insert(0, top)
            return True
    
    # No path was found, return False
    return False

def UCS(G, s, g): # G is graph, s is start vertex, g is goal vertex
    visited = []
    priorityQueue = [[0, s, s]]
    path = [] # The path to the goal
    n = len(G) # Using the number of vertice as a parameter to reduce the number of time that calculate this number
    
    if UCSRecursive(G, n, g, visited, priorityQueue, path) == False:
        return [-1]
    
    return path