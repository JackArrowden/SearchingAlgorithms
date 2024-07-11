### Class problem
import NODE

class Problem:
    def __init__(self, file = None, AdjMatrix = [], heuristic = [], initial = None, goal = None):
        self.AdjMatrix = AdjMatrix
        self.Heuristic = heuristic
        self.Initial = initial
        self.Goal = goal
        if file:
            self.getProblem(file)
    
    def printProblem(self):
        print("Adjacent matrix: ", self.AdjMatrix)
        print("Heuristic values: ", self.Heuristic)
        print("Start vertex: ", self.Initial)
        print("Goal vertex: ", self.Goal)
        
    def getProblem(self, file):
        try:
            curFile = open(file, 'r')
            numVertex = int(curFile.readline().strip())
            strArray = curFile.readline().strip().split()
            
            self.Initial = int(strArray[0])
            self.Goal = int(strArray[1])
            
            for i in range(numVertex):
                strArray = curFile.readline().strip().split()
                curRow = [int(num) for num in strArray]
                
                self.AdjMatrix.append(curRow)
                
            strArray = curFile.readline().strip().split()
            self.Heuristic = [int(num) for num in strArray]
            
        finally:
            curFile.close()
            
    def ACTION(self, state):
        numNodes = len(self.AdjMatrix)
        for i in range(numNodes):
            if self.AdjMatrix[state][i] > 0:
                yield i # Goes to vertex i
                
    def ACTION_COST(self, s, action, sCur):
        return self.AdjMatrix[s][sCur]
                
    def RESULT(self, state, action):
        return action # Return state i
    
    def IS_GOAL(self, state):
        if state == self.Goal:
            return True
        return False
    
    def EXPAND(self, node):
        s = node.state
        for action in self.ACTION(s):
            sCur = self.RESULT(s, action)
            cost = node.cost + self.ACTION_COST(s, action, sCur)
            yield NODE.NODE(sCur, parent = node, action = self.ACTION(action), cost = cost, depth = node.depth + 1)
    
    def getPath(self, node):
        if node == None:
            return None
        
        path = []
        while node:
            path.append(node.state)
            node = node.parent
        path.reverse()
        
        return path
    
    def IS_CYCLE(self, node):
        path = self.getPath(node)
        path.pop()
        
        if node.state in path:
            return True
        return False