import copy
from collections import deque


class SimpleSudoku:
    def __init__(self):
        self.__matrix = []
        self.__appearances = [0]

    def set_matrix_and_appearances(self, matrix, app):
        self.__matrix = matrix
        self.__appearances = app

    def parse_sudoku_string(self, sudoku_string):
        lines = sudoku_string.split("\n")
        matrix = []
        for l in lines:
            matrix.append(l.split(" "))
            self.__appearances.append(0)
        self.__matrix = matrix
        self.validateSudoku()
        self.to_int_elements()
        return self

    def validateSudoku(self):
        line_count = len(self.__matrix)
        for line in self.__matrix:
            if len(line) != line_count:
                return False
            for elem in line:
                if elem != "_":
                    value = int(elem)
                    if value > line_count:
                        return False
                    self.__appearances[value] += 1
        return True



    def to_int_elements(self):
        for i in range(len(self.__matrix)):
            for j in range(len(self.__matrix)):
                if self.__matrix[i][j] != "_":
                    self.__matrix[i][j] = int(self.__matrix[i][j])

    def get_solution_set(self):
        solution = []
        for i in range(1, len(self.__matrix) + 1):
            for j in range(len(self.__matrix) - self.__appearances[i]):
                solution.append(i)
        return solution

    def validate_lines(self):
        for i in range(len(self.__matrix)):
            appearances_line = [0]
            appearances_column = [0]
            for j in range(len(self.__matrix)):
                appearances_line.append(1)
                appearances_column.append(1)
            for j in range(len(self.__matrix)):
                if self.__matrix[i][j] == "_":
                    return False
                if self.__matrix[j][i] == "_":
                    return False
                appearances_line[self.__matrix[i][j]] -= 1
                appearances_column[self.__matrix[j][i]] -= 1
            for k in appearances_line:
                if k != 0:
                    return False
            for k in appearances_column:
                if k != 0:
                    return False
        return True

    def set_solution(self, sol):
        soldeq = deque(sol)
        for i, item in enumerate(self.__matrix):
            for j, item2 in enumerate(self.__matrix):
                if self.__matrix[i][j] == "_":
                    self.__matrix[i][j] = soldeq.popleft()

    def validate_solution(self, sol):
        my_copy = SimpleSudoku()
        my_copy.set_matrix_and_appearances([row[:] for row in self.__matrix], list(self.__appearances))
        my_copy.set_solution(sol)
        if my_copy.validate_lines():
            return my_copy
        else:
            return None

    def __str__(self):
        res = ""
        for i in self.__matrix:
            res = res + str(i) + "\n"
        return res