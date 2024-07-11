### Class NODE

class NODE:
    def __init__(self, state, parent = None, action = None, cost = 0, depth = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.depth = depth
        if parent:
            self.depth = parent.depth + 1
        # self.hValue = float('inf')
        
    def __lt__(self, other): # Operator overloading: operator <
        return self.state < other.state