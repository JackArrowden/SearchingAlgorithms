### BFS algorithm

import NODE
import stackQueue

def BFS(problem):
    node = NODE.NODE(problem.Initial)
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