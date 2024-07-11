### A* algorithm
import BestFirstSearch

def AStar(problem):
    return BestFirstSearch.BestFirstSearch(problem, lambda node : node.cost + problem.Heuristic[node.state])