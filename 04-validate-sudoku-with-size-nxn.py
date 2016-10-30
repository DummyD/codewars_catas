# https://www.codewars.com/kata/validate-sudoku-with-size-nxn/python


from math import sqrt


class Sudoku(object):
    def __init__(self, board):
        self.board = board

    def check_col(self, x):
        for i in range(len(self.board)):
            if set(self.board[i]) != x:
                return False
        return True

    def check_row(self, x):
        for i in range(len(self.board[0])):
            if set([self.board[j][i] for j in range(len(self.board))]) != x:
                return False
        return True

    def check_boxes(self, box, x):
        if set([self.board[m][n] for m in range(box[0], box[0] + 3) for n in range(box[1], box[1] + 3)]) != x:
            return False
        return True

    def is_valid(self):
        if len(set([len(x) for x in self.board])) != 1:
            return False
        x = set(self.board[0])
        if not self.check_col(x) or not self.check_row(x):
            return False
        boxes = [[i, i + int(sqrt(len(self.board)))] for i in range(0, len(self.board), int(sqrt(len(self.board))))]
        for n in range(len(boxes) - 1):
            if not self.check_boxes(boxes[n], x):
                return False
        return True
