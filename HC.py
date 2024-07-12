### Hill climbing algorithm
import NODE

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