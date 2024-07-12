import problem
import SearchAlgorithms

main = problem.Problem()
main.getProblem('./input1.txt')

main.findSolution(
    './output1.txt',
    SearchAlgorithms.BFS,
    SearchAlgorithms.DFS,
    SearchAlgorithms.UCS,
    SearchAlgorithms.IDS,
    SearchAlgorithms.GBFS,
    SearchAlgorithms.AStar,
    SearchAlgorithms.HC
)