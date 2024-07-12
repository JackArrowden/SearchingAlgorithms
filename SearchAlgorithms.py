import NODE
import stackQueue

# BREADTH FIRST SEARCH
def BFS(problem):
    node = NODE.NODE(state = problem.Initial)
    if problem.IS_GOAL(node.state):
        return node
    
    frontier = stackQueue.FIFOQueue()
    frontier.push(node)
    reached = set({problem.Initial})
    
    while not frontier.is_empty():
        node = frontier.pop()
        
        for child in problem.EXPAND(node):
            s = child.state
            
            if problem.IS_GOAL(s):
                return child 
            
            if s not in reached:
                reached.add(s)
                frontier.push(child)
    return None

# BEST FIRST SEARCH
def BestFirstSearch(problem, f, earlyStop = False, dfsCheckCycle = False):
    node = NODE.NODE(state = problem.Initial)
    frontier = stackQueue.PriorityQueue()
    frontier.push([f(node), node])
    reached = {problem.Initial: node}
    
    while not frontier.is_empty():
        node = frontier.pop()[1]
        
        if problem.IS_GOAL(node.state):
            return node
        
        for child in problem.EXPAND(node):
            s = child.state
            
            if earlyStop and problem.IS_GOAL(s): # Early stop chekking
                return child 
            
            if dfsCheckCycle and problem.IS_CYCLE(child):
                continue
            
            if s not in reached or f(child) < f(reached[s]):
                reached[s] = child
                frontier.push([f(child), child])
    return None

# DEPTH FIRST SEARCH
def DFS(problem):
    return BestFirstSearch(problem, lambda node : -node.depth, earlyStop = True, dfsCheckCycle = True)

# UNIFORM COST SEARCH
def UCS(problem):
    return BestFirstSearch(problem, lambda node : node.cost)

# GREEDY BEST FIRST SEARCH
def GBFS(problem):
    return BestFirstSearch(problem, lambda node : problem.Heuristic[node.state], earlyStop = True)

# A*
def AStar(problem):
    return BestFirstSearch(problem, lambda node : node.cost + problem.Heuristic[node.state])

# DEPTH LIMITED SEARCH
def DLS(problem, l):
    frontier = stackQueue.LIFOQueue()
    frontier.push(NODE.NODE(problem.Initial))
    result = None
    
    while not frontier.is_empty():
        node = frontier.pop()
        
        if problem.IS_GOAL(node.state):
            return node
        
        if node.depth > l:
            result = 'cutoff'
            
        elif not problem.IS_CYCLE(node):
            for child in problem.EXPAND(node):
                frontier.push(child)
    return result

# ITERATIVE DEEPENING SEARCH
def IDS(problem):
    depth = 0
    while True:
        result = DLS(problem, depth)
        if result != 'cutoff':
            return result
        depth = depth + 1
        
# HILL CLIMBING
def HC(problem):
    current = NODE.NODE(problem.Initial)
    
    while True:
        neighbor = current
        for child in problem.EXPAND(current):
            if neighbor < child:
                neighbor = child
                
        if neighbor <= current:
            return current
        
        current = neighbor