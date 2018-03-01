from model.Problem import Problem
from model.SimpleSudoku import SimpleSudoku
from repository.Repository import Repository

r = Repository()
sudoku = r.get_sudoku(1)
p = Problem(sudoku)
print(p)
p.test_bfs()
print(p)
