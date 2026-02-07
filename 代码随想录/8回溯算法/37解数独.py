from typing import *


class Solution:
    def backtracking(self, board, row, col, subr, spaces, idx):
        if idx == len(spaces):  # 最后一个位置（idx = len(spaces) - 1）填完了，再下一层才结束，所以这里要用 == len(spaces)！
            return True  # 填满了直接返回
        i, j = spaces[idx]
        for v in range(1, 10):
            if not row[i][v - 1] and not col[j][v - 1] and not subr[i // 3][j // 3][v - 1]:  # 如果v没用过
                board[i][j] = str(v)
                row[i][v - 1], col[j][v - 1], subr[i // 3][j // 3][v - 1] = True, True, True
                if self.backtracking(board, row, col, subr, spaces, idx + 1):
                    return True
                row[i][v - 1], col[j][v - 1], subr[i // 3][j // 3][v - 1] = False, False, False
                board[i][j] = "."  # 放回以回溯

    def solveSudoku(self, board: List[List[str]]) -> None:
        # 3个数组用来记录每行/每列/每个小块中对应的数字有没有被使用，用的是0-based index
        row = [[False] * 9 for _ in range(9)]  # row[i][v]代表第i行数字v+1已经用了
        col = [[False] * 9 for _ in range(9)]  # col[j][v]代表第j列数字v+1已经用了
        subr = [[[False] * 9 for _ in range(3)] for _ in range(3)]  # 3 * 3的小块，一共3行，每行3个小块：subr[r][c][v]表示第r行的第c个小块中数字v+1被用了
        # 先把board中已经有的填记录一下
        spaces = []  # 提前记录需要填数字的空位
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    v = int(board[i][j])
                    row[i][v - 1], col[j][v - 1], subr[i // 3][j // 3][v - 1] = True, True, True
                else:  # 空位
                    spaces.append((i, j))
        self.backtracking(board, row, col, subr, spaces, 0)


class Solution1:
    """
    回溯：会超时，尽管用的是数组去记录用没用过每个数字（空间换时间）。超时的原因是在backtracking中每次都扫描了整个board来找第一个空位，
    所以会超时。我们应该要提前找到所有空位，然后直接填空位即可！
    """
    def backtracking(self, board, row, col, subr):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    for v in range(1, 10):  # 1-9
                        if not row[i][v - 1] and not col[j][v - 1] and not subr[i // 3][j // 3][v - 1]:
                            board[i][j] = str(v)
                            row[i][v - 1], col[j][v - 1], subr[i // 3][j // 3][v - 1] = True, True, True
                            ans = self.backtracking(board, row, col, subr)
                            if ans:
                                return True  # 填满了立马return，这样到上一层也会直接return
                            board[i][j] = "."  # 放回以回溯
                            row[i][v - 1], col[j][v - 1], subr[i // 3][j // 3][v - 1] = False, False, False
                    return False  # board[i][j] 0-9都不能填，直接return False
        return True  # 这个其实就是解决找到答案的时候的情况(is_goal)，在最深层的那个递归棋盘填满了，上面的两个for就不会运行了，即得到了答案，直接返回True，这个一定得有

    def solveSudoku(self, board: List[List[str]]) -> None:
        # 3个数组用来记录每行/每列/每个小块中对应的数字有没有被使用，用的是0-based index
        row = [[False] * 9 for _ in range(9)]  # row[i][v]代表第i行数字v+1已经用了
        col = [[False] * 9 for _ in range(9)]  # col[j][v]代表第j列数字v+1已经用了
        subr = [[[False] * 9 for _ in range(3)] for _ in range(3)]  # 3 * 3的小块，一共3行，每行3个小块：subr[r][c][v]表示第r行的第c个小块中数字v+1被用了
        # 先把board中已经有的填记录一下
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    v = int(board[i][j])
                    row[i][v - 1], col[j][v - 1], subr[i // 3][j // 3][v - 1] = True, True, True
        self.backtracking(board, row, col, subr)


if __name__ == '__main__':
    sol = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                  [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                  ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                  [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                  [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    sol.solveSudoku(board)
    print(board)


