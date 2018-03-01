from model.SimpleSudoku import SimpleSudoku


class Repository:
    def __init__(self):
        self.__path_to_files = "C:/Users/cpodariu/Workspace/AI/Lab01/data/"
        self.__sudoku = None
        self.__files = ["example1.txt", "example9x9.txt"]

    def read_sudoku_string(self, example):
        file_path = self.__files[example]
        file = open(self.__path_to_files + file_path)
        string = file.read()
        return string

    def get_sudoku(self, index):
        sudoku = SimpleSudoku().parse_sudoku_string(self.read_sudoku_string(index))
        return sudoku

    def get_sudoku_files(self):
        return self.__files

