import DFS
import BFS
import GBFS
import UCS
import AStar
# import problem

# print(BFS.BFS([[0,4,5,0,0],[4,0,2,5,6],[5,2,0,3,0],[0,5,3,0,1],[0,6,0,1,0]], 0, 3))
# print(GBFS.GBFS([[0,4,5,0,0],[4,0,2,5,6],[5,2,0,3,0],[0,5,3,0,1],[0,6,0,1,0]], [8,5,3,0,1], 2, 4))
print(AStar.AStar([[0,4,5,0,0],[4,0,2,5,6],[5,2,0,3,0],[0,5,3,0,1],[0,6,0,1,0]], [8,5,3,0,1], 0, 4))
# print(UCS.UCS([[0,4,5,0,0],[4,0,2,5,6],[5,2,0,3,0],[0,5,3,0,1],[0,6,0,1,0]], 0, 4))
# main = problem.problem()
# main.getProblem('./input.txt')
# main.printProblem()