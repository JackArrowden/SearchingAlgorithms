# Best First Search algorithm

import NODE
import stackQueue

def BestFirstSearch(problem, f, earlyStop = False):
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
            
            if s not in reached or f(child) < f(reached[s]):
                reached[s] = child
                frontier.push([f(child), child])
    return None