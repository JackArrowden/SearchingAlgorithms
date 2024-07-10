# import DFS
import BFS
# import GBFS
# import UCS
# import AStar
# import IDS
import problem

# print(BFS.BFS([[0,4,5,0,0],[4,0,2,5,6],[5,2,0,3,0],[0,5,3,0,1],[0,6,0,1,0]], 0, 3))
# print(IDS.DepthLimitedSearch([[0,4,5,0,0],[4,0,2,5,6],[5,2,0,3,0],[0,5,3,0,1],[0,6,0,1,0]], 0, 3))
# print(GBFS.GBFS([[0,4,5,0,0],[4,0,2,5,6],[5,2,0,3,0],[0,5,3,0,1],[0,6,0,1,0]], [8,5,3,0,1], 2, 4))
# print(AStar.AStar([[0,4,5,0,0],[4,0,2,5,6],[5,2,0,3,0],[0,5,3,0,1],[0,6,0,1,0]], [8,5,3,0,1], 0, 4))
# print(UCS.UCS([[0,4,5,0,0],[4,0,2,5,6],[5,2,0,3,0],[0,5,3,0,1],[0,6,0,1,0]], 0, 4))
main = problem.Problem()
# main.getProblem('./input.txt')
# main.getProblem('./testcase2.txt')
main.getProblem('./testcase3.txt')
main.printProblem()

print(main.getPath(BFS.BFS(main)))