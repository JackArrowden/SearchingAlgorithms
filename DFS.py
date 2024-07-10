### Tree search DFS algorithm
import NODE
import stackQueue

def DFSRecursive(node, problem):
    for child in problem.EXPAND(node): # Early check
        if problem.IS_GOAL(child.state):
            return child
        
    for child in problem.EXPAND(node):
        s = child.state
        
        result = DFSRecursive(child, problem)
        if result != None:
            return result
    
    return None

def DFS(problem):
    if problem.Initial == problem.Goal:
        return NODE.NODE(problem.Goal)
    return DFSRecursive(NODE.NODE(problem.Initial), problem)