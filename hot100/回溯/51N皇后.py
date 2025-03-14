from typing import *


"""
经典回溯：
state：state[i] = x代表第i列的Q在第x行
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def get_next(state, n):
            possible = [i for i in range(n) if i not in state]  # 去掉横向
            illegal = set()  # 对角线（斜向，右上和右下方向）占用的位置不能选
            curr_col = len(state)
            for col, row in enumerate(state):  # 去掉斜向
                col_diff = curr_col - col
                illegal.add(row + col_diff)
                illegal.add(row - col_diff)
            return [i for i in possible if i not in illegal]

        def process_ans(state, n):
            # 先一列一列创建，然后在左旋90度即可
            ans = []
            for i in state:
                ans.append(list(i * '.' + 'Q' + (n - i - 1) * '.'))
            ans = [list(x) for x in zip(*ans)][::-1]  # 左旋90
            return [''.join(x) for x in ans]

        def backtracking(state, ans, n):
            if len(state) == n:
                ans.append(process_ans(state[:], n))
                return
            for i in get_next(state, n):
                state.append(i)
                backtracking(state, ans, n)
                state.pop()

        ans = []
        backtracking([], ans, n)
        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 4
    print(sol.solveNQueens(n))





