### A* algorithm

def AStar(G, h, s, g):
    if s == g:
        return [s]
    
    tmp = h[s]
    h[s] = 0
    
    stack = [[0, s]] # Behaves as a stack
    # Each element of the stack is followed by the structure: [<weight(cost)>, <vertex>]
    # This will help the sort function to sort easier
    
    n = len(G)
    prevNode = [-1] * n # Used for tracking the path returned and the cost to each vertex
    # -1 means vertex i wasn't been visited
    prevNode[s] = -2
    # -2 means vertex i is in the stack but has no parent
    
    while len(stack) != 0:
        stack.sort()
        head = stack.pop(0) # Get the vertex with lowest cost
        weight = head[0]
        cur = head[1]
        
        if cur == g:
            path = [g]
            while prevNode[cur] != -2: # Traverse back to node s
                path.insert(0, prevNode[cur])
                cur = prevNode[cur]
            h[s] = tmp
            return path
        
        for i in range(n):
            if G[cur][i] == 0:
                continue
            
            # If i was generated
            found = False
            for j in range(len(stack)):
                if stack[j][1] == i:
                    if G[cur][i] + weight - h[cur] + h[i] < stack[j][0]: # If the cost is smaller, update it
                        prevNode[i] = cur
                        stack[j][0] = G[cur][i] + weight - h[cur] + h[i]
                    found = True
                    break
            
            # If i wasn't been generated and wasn't been visited
            if not found and prevNode[i] == -1:
                stack.append([G[cur][i] + weight - h[cur] + h[i], i])
                prevNode[i] = cur
            
    h[s] = tmp
    return [-1]