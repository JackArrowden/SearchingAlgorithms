### Tree search DFS algorithm
import BestFirstSearch

def DFS(problem):
    return BestFirstSearch.BestFirstSearch(problem, lambda node : -node.depth, earlyStop = True)