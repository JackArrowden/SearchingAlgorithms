### IDS algorithm
import NODE
import stackQueue

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

def IDS(problem):
    depth = 0
    while True:
        result = DLS(problem, depth)
        if result != 'cutoff':
            return result
        depth = depth + 1