import copy

import time
from collections import deque
from queue import PriorityQueue

from model import SimpleSudoku


class Problem:
    def __init__(self, sudoku):
        self.__sudoku = sudoku
        self.solution_matrix = sudoku.get_possible_solutions_per_point()
        self.__root = [0 for i in self.solution_matrix]
        self.__result = None
        self.__method = ""
        self.__time = 0

    def get_solution(self, sol):
        sol = [self.solution_matrix[i][sol[i]] for i, k in enumerate(sol)]
        return sol

    def pruning_function(self, elem, sol):
        # return True
        app = list(self.__sudoku.appearances)
        for i in range(0, elem):
            app[self.solution_matrix[i][sol[i]]] += 1
            if app[self.solution_matrix[i][sol[i]]] > self.__sudoku.get_size():
                return False
        return True

    def get_heuristic(self, elem, sol):
        app = list(self.__sudoku.appearances)
        for k, i in enumerate(sol):
            app[self.solution_matrix[k][i]] += 1
        diff = 0
        for i in app:
            diff += abs(9 - i)
        return diff


    def bfs(self, sudoku, node):
        checked = 0
        stop = False
        nodes = deque([(0, node)])
        while len(nodes) > 0:
            level, sol = nodes.popleft()
            if checked % 100000 == 0:
                print(str(checked) + " | queue length: " + str(len(nodes)))
            checked += 1
            if len(nodes) > 10000000:
                stop = True
            solution = sudoku.validate_solution(self.get_solution(sol))
            if solution is not None:
                return solution
            if stop is False:
                for i in range(level, len(sol)):
                    sol_copy = list(sol)
                    if len(self.solution_matrix[i]) > sol[i] + 1:
                        sol_copy[i] += 1
                        if self.pruning_function(i, sol_copy):
                            nodes.append((i, sol_copy))
        return None

    def gbfs(self, sudoku, node):
        checked = 0
        stop = False
        nodes = PriorityQueue()
        nodes.put((0, (0, node)))
        while not nodes.empty():
            a, b = nodes.get()
            level, sol = b
            if checked % 100000 == 0:
                print(str(checked) + " | queue length: " + str(nodes.qsize()))
            checked += 1
            if nodes.qsize() > 10000000:
                stop = True
            solution = sudoku.validate_solution(self.get_solution(sol))
            if solution is not None:
                return solution
            if stop is False:
                for i in range(level, len(sol)):
                    sol_copy = list(sol)
                    if len(self.solution_matrix[i]) > sol[i] + 1:
                        sol_copy[i] += 1
                        if self.pruning_function(i, sol_copy):
                            nodes.put((self.get_heuristic(i, sol_copy), (i, sol_copy)))
        return None

    def test_bfs(self):
        start = time.time()
        self.__result = self.bfs(self.__sudoku, self.__root)
        end = time.time()
        self.__time = end - start
        self.__method = "bfs"

    def test_gbfs(self):
        start = time.time()
        self.__result = self.gbfs(self.__sudoku, self.__root)
        end = time.time()
        self.__time = end - start
        self.__method = "gbfs"

    def __str__(self):
        res = ""
        res += "Sudoku:\n" + str(self.__sudoku) + "\n"
        res += "Solution:\n" + str(self.__result) + "\n"
        res += "Method:" + self.__method + "\n"
        res += "Execution time:\n" + self.__time.__str__() + "\n"
        return res