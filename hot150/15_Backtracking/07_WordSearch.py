# 79
from typing import *


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    found = self.backtrack([(i, j)], word, board)
                    if found:
                        return True
        return False

    def is_goal(self, partial, word):
        return len(partial) == len(word)

    def get_poss(self, partial, word, board):
        x_len, y_len = len(board), len(board[0])
        x, y = partial[-1]  # current coordinates
        neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        # 先去除超出便捷的，然后去除走过的，最后保证neighbour是下个需要的字母
        # 这样保证路径一定按word走，不会走多余的！
        available = [(x, y) for x, y in neighbours
                     if 0 <= x < x_len and 0 <= y < y_len
                     and (x, y) not in partial
                     and board[x][y] == word[len(partial)]]
        # 用filter会超时，所以用了list comprehension
        return available

    def backtrack(self, partial, word, board):
        if self.is_goal(partial, word):
            return True
        else:
            for i in self.get_poss(partial, word, board):
                partial.append(i)
                found = self.backtrack(partial, word, board)
                if found:
                    return True
                partial.pop()
            return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    sol = Solution()
    print(sol.exist(board, word))
