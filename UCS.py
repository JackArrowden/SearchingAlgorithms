### UCS algorithm
import BestFirstSearch

def UCS(problem):
    return BestFirstSearch.BestFirstSearch(problem, lambda node : node.cost)