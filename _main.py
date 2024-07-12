import DFS
import BFS
import GBFS
import UCS
import AStar
import IDS
import problem
import HC

main = problem.Problem()
main.getProblem('./testcase2.txt')
main.printProblem()

# print(main.getPath(BFS.BFS(main)))
# print(main.getPath(DFS.DFS(main)))
# print(main.getPath(UCS.UCS(main)))
# print(main.getPath(GBFS.GBFS(main)))
# print(main.getPath(AStar.AStar(main)))
# print(main.getPath(IDS.IDS(main)))

print(main.getPath(HC.HC(main))) ## Remember to check if reach goal