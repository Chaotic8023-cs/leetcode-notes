# 36
from typing import *


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def transpose(matrix):
            res = []
            for i in range(len(matrix)):
                r = []
                for j in range(len(matrix)):
                    r.append(matrix[j][i])
                res.append(r)
            return res

        def valid_row(row):
            hm = set()
            for c in row:
                if c != '.' and c in hm:
                    return False
                hm.add(c)
            return True

        def valid_subboard(subboard):
            hm = set()
            for row in subboard:
                for c in row:
                    if c != '.' and c in hm:
                        return False
                    hm.add(c)
            return True

        def valid_board(board):
            res = True
            for i in range(len(board) // 3):
                for j in range(len(board) // 3):
                    subboard = [row[j * 3:j * 3 + 3] for row in board[i * 3:i * 3 + 3]]
                    res = res and valid_subboard(subboard)
            return res

        return (all([valid_row(row) for row in board])
                and all([valid_row(row) for row in transpose(board)])
                and valid_board(board))

    # 1次遍历
    def isValidSudoku1(self, board: List[List[str]]) -> bool:
        # 用三个boolean matrix来替代hashmap
        # row[i][num] = True代表第i行num已经出现过了
        row = [[False] * 9 for _ in range(9)]
        col = [[False] * 9 for _ in range(9)]
        sub = [[False] * 9 for _ in range(9)]  # sub[k]为第k个3*3的submatrix
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == '.':
                    continue
                num = int(c) - 1  # accommodating for index in boolean array, so -1
                """
                相当于把sudoku分成9块，并合成一个list, 其中每个index代表一个submatrix
                [0, 1, 2]
                [3, 4, 5] -> [0, 1, 2, 3, 4, 5, 6, 7, 8]
                [6, 7, 8]
                """
                k = i // 3 * 3 + j // 3
                if row[i][num] or col[j][num] or sub[k][num]:
                    return False
                row[i][num] = True
                col[j][num] = True
                sub[k][num] = True
        return True


if __name__ == '__main__':
    board = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
             [".", "4", ".", "3", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", "3", ".", ".", "1"],
             ["8", ".", ".", ".", ".", ".", ".", "2", "."],
             [".", ".", "2", ".", "7", ".", ".", ".", "."],
             [".", "1", "5", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", "2", ".", ".", "."],
             [".", "2", ".", "9", ".", ".", ".", ".", "."],
             [".", ".", "4", ".", ".", ".", ".", ".", "."]]
    sol = Solution()
    print(sol.isValidSudoku1(board))
