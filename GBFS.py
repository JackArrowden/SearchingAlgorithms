### GBFS algorithm
import BestFirstSearch

def GBFS(problem):
    return BestFirstSearch.BestFirstSearch(problem, lambda node : problem.Heuristic[node.state], earlyStop = True)