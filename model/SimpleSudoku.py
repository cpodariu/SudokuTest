import copy
import random
from collections import deque

from math import sqrt


class SimpleSudoku:
    def __init__(self):
        self.matrix = []
        self.appearances = [0]
        self.size = 0

    def get_size(self):
        return self.size

    def set_matrix_and_appearances(self, matrix, app):
        self.matrix = matrix
        self.appearances = app

    def parse_sudoku_string(self, sudoku_string):
        lines = sudoku_string.split("\n")
        matrix = []
        for l in lines:
            matrix.append(l.split(" "))
            self.appearances.append(0)
        self.matrix = matrix
        self.validateSudoku()
        self.to_int_elements()
        self.size = len(matrix)
        return self

    def validateSudoku(self):
        line_count = len(self.matrix)
        for line in self.matrix:
            if len(line) != line_count:
                return False
            for elem in line:
                if elem != "_":
                    value = int(elem)
                    if value > line_count:
                        return False
                    self.appearances[value] += 1
        return True

    def to_int_elements(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] != "_":
                    self.matrix[i][j] = int(self.matrix[i][j])

    def get_solution_set(self):
        solution = []
        for i in range(1, len(self.matrix) + 1):
            for j in range(len(self.matrix) - self.appearances[i]):
                solution.append(i)
        return solution

    def validate_lines(self):
        for i in range(len(self.matrix)):
            appearances_line = [0]
            appearances_column = [0]
            for j in range(len(self.matrix)):
                appearances_line.append(1)
                appearances_column.append(1)
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == "_":
                    return False
                if self.matrix[j][i] == "_":
                    return False
                appearances_line[self.matrix[i][j]] -= 1
                appearances_column[self.matrix[j][i]] -= 1
            for k in appearances_line:
                if k != 0:
                    return False
            for k in appearances_column:
                if k != 0:
                    return False
        return True

    def set_solution(self, sol):
        soldeq = deque(sol)
        for i, item in enumerate(self.matrix):
            for j, item2 in enumerate(self.matrix):
                if self.matrix[i][j] == "_":
                    self.matrix[i][j] = soldeq.popleft()

    def validate_sol_appearances(self, sol):
        app_copy = list(self.appearances)
        for i in sol:
            app_copy[i] += 1
            if app_copy[i] > self.get_size() + 1:
                return False
        return True

    def validate_solution(self, sol):
        app_copy = list(self.appearances)
        for i in sol:
            app_copy[i] += 1
            if app_copy[i] > self.get_size():
                return None
        my_copy = SimpleSudoku()
        my_copy.set_matrix_and_appearances([row[:] for row in self.matrix], list(self.appearances))
        my_copy.set_solution(sol)
        if my_copy.validate_lines():
            return my_copy
        else:
            return None

    def get_possible_solutions(self, x, y):
        sol_set = list(range(1, self.get_size() + 1))
        for i in range(self.get_size()):
            if self.matrix[x][i] in sol_set:
                sol_set.remove(self.matrix[x][i])
            if self.matrix[i][y] in sol_set:
                sol_set.remove(self.matrix[i][y])
        squares_count = int(sqrt(self.get_size()))
        starting_x = int(x/squares_count) * squares_count
        starting_y = int(y/squares_count) * squares_count
        for i in range(starting_x, starting_x + squares_count):
            for j in range(starting_y, starting_y + squares_count):
                if self.matrix[i][j] in sol_set:
                    sol_set.remove(self.matrix[i][j])
        random.shuffle(sol_set)
        return sol_set

    def __str__(self):
        res = ""
        for i in self.matrix:
            res = res + str(i) + "\n"
        return res


    def get_possible_solutions_per_point(self):
        while True:
            solutions = []
            for i in range(self.get_size()):
                for j in range(self.get_size()):
                    if self.matrix[i][j] == "_":
                        solutions.append(self.get_possible_solutions(i, j))
            base_solution = [x[0] for x in solutions]
            if self.validate_sol_appearances(base_solution):
                return solutions


def get_solution_from_possible_points_distribution(distrib):
    sol = []
    for i in distrib:
        sol.append(i[0])

    return sol
