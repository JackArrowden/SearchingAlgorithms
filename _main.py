import problem
import SearchAlgorithms

main = problem.Problem()
main.getProblem('./TestCases/input.txt')

main.findSolution(
    './TestCases/output.txt',
    SearchAlgorithms.BFS,
    SearchAlgorithms.DFS,
    SearchAlgorithms.UCS,
    SearchAlgorithms.IDS,
    SearchAlgorithms.GBFS,
    SearchAlgorithms.AStar,
    SearchAlgorithms.HC
)