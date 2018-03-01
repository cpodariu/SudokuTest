import copy

import time
from collections import deque


class Problem:
    def __init__(self, sudoku):
        self.__sudoku = sudoku
        self.__root = sudoku.get_solution_set()
        self.__result = None
        self.__method = ""
        self.__time = 0

    @staticmethod
    def bfs(sudoku, node):
        nodes = deque([node])
        k = 1
        while len(nodes) > 0:
            k = k + 1
            sol = nodes.popleft()
            if k % 100 == 0:
                print("k = " + str(k) + " " + str(sol))
            solution = sudoku.validate_solution(sol)
            if solution is not None:
                return solution
            if (len(nodes) < 1000000):
                for i in range(len(sol) - 1):
                    for j in range(i + 1, len(sol)):
                        if sol[i] < sol[j]:
                            node_copy = list(sol)
                            node_copy[i] = sol[j]
                            node_copy[j] = sol[i]
                            nodes.append(node_copy)
        return None

    def test_bfs(self):
        start = time.time()
        self.__result = self.bfs(self.__sudoku, self.__root)
        end = time.time()
        self.__time = end - start
        self.__method = "bfs"

    def __str__(self):
        res = ""
        res += "Sudoku:\n" + str(self.__sudoku) + "\n"
        res += "Solution:\n" + str(self.__result) + "\n"
        res += "Method:" + self.__method + "\n"
        res += "Execution time:\n" + self.__time.__str__() + "\n"
        return res