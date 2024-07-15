### Class problem
import NODE
import timeit
import tracemalloc

class Problem:
    def __init__(self, file = None, AdjMatrix = [], heuristic = [], initial = None, goal = None):
        self.AdjMatrix = AdjMatrix
        self.Heuristic = heuristic
        self.Initial = initial
        self.Goal = goal
        if file:
            self.getProblem(file)
        
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
          
    def findSolution(self, file, *algorithm):
        curFile = open(file, 'w')

        for algo in algorithm:
            if algo.__name__ == 'AStar':
                curFile.write("A*:\n")
            elif algo.__name__ == 'HC':
                curFile.write("Hill Climbing:\n")
            else:
                curFile.write(algo.__name__ + ":\n")
            
            tracemalloc.start()
            start = timeit.default_timer()
            
            result = algo(self)
            
            end = timeit.default_timer()
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            executionTime = end - start
            
            curFile.write(self.pathToString(result) + '\n')
            curFile.write(f"Time: {executionTime:.7f} seconds" + '\n')
            curFile.write(f"Memory: {current / 1024:.2f} KB" + '\n\n')
            
        curFile.close()
        return
            
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
    
    def pathToString(self, node):
        if node == None or node.state != self.Goal:
            return "Path: -1"
            
        path = self.getPath(node)
        n = len(path)
        
        string = "Path: "
        for i in range(n - 1):
            string += str(path[i]) + " -> "
            
        return string + str(path[n - 1])