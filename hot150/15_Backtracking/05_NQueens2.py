# 52
from typing import *


class Solution:
    def __init__(self):
        self.ans = 0

    def totalNQueens(self, n: int) -> int:
        self.backtrack([], n)
        return self.ans

    def backtrack(self, partial, n):
        if self.is_valid(partial, n):
            self.ans += 1
        else:
            for i in self.get_poss(partial, n):
                partial.append(i)
                self.backtrack(partial, n)
                partial.pop()

    def is_valid(self, partial, n):
        return len(partial) == n

    """
    partial: [2, 0, 3, 1]
    len为board size，每个element代表这一列的Queen的row index
    如2表示第一列第3行的Queen
    """
    def get_poss(self, partial, n):
        all_possible_pos = [i for i in range(n)]
        # same rows from current queens
        not_possible_pos = [i for i in partial]
        # 考虑对角线，因为partial是一列一列的考虑
        # 所以只用考虑前面的Q的右边的diagonal的影响（即右上和右下）
        current_col_idx = len(partial)
        for q_col_idx, q_row_idx in enumerate(partial):
            # top right diagonal impact
            affected_row_idx_tr = q_row_idx-(current_col_idx-q_col_idx)
            # bottom right diagonal impact
            affected_row_idx_br = q_row_idx+(current_col_idx-q_col_idx)
            # check if the impacted row idx is within the board range
            if affected_row_idx_tr < n:
                not_possible_pos.append(affected_row_idx_tr)
            if affected_row_idx_br < n:
                not_possible_pos.append(affected_row_idx_br)
        # return the possible row indices
        return list(set(all_possible_pos) - set(not_possible_pos))


if __name__ == '__main__':
    n = 4
    sol = Solution()
    print(sol.totalNQueens(n))
