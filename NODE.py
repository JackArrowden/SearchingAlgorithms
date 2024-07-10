### Class NODE

class NODE:
    def __init__(self, state, parent = None, action = None, cost = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1
        # self.hValue = float('inf')