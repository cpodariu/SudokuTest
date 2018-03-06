from model.Problem import Problem
from model.SimpleSudoku import SimpleSudoku
from repository.Repository import Repository

r = Repository()
sudoku = r.get_sudoku(1)
problem = Problem(sudoku)
problem.test_bfs()
print(problem)