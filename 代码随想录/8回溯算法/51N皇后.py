from typing import *


class Solution:
    """
    回溯：典型用回溯算法解决的棋盘问题。我们按列进行从左到右的摆放（当然也可按按行，就是写法反过来而已，我们只记按列就可以），即先确定第1列放
    哪里，再确定第2列，最后就是第3和第4列。state如何表示呢？一共有4列，所以我们用一个数组表示，state[i]表示从左往右第i列的皇后摆在从下往上
    数的第几行。
    列如下面的棋盘：
    .Q..
    ...Q
    Q...
    ..Q.
    表示为：[1, 3, 0, 2]
    """
    def rotate_90_clockwise(self, matrix):
        """
        旋转90°：
        0. 原：
        [[1,2,3],
        [4,5,6],
        [7,8,9]]
        1. matrix[::-1]
        [[7,8,9],
        [4,5,6],
        [1,2,3]]
        2. zip(*matrix[::-1])
        zip([7,8,9], [4,5,6], [1,2,3])
        3. 最终：zip分别取每个arg的第1个元素，第2个元素，...
        [[7,4,1],
        [8,5,2],
        [9,6,3]]
        """
        return [list(row) for row in zip(*matrix[::-1])]

    def process_col_repr(self, state, n):
        ans = []
        for row in state:
            ans.append("." * row + "Q" + (n - row - 1) * ".")
        # 顺时针旋转90°
        ans = self.rotate_90_clockwise(ans)
        return [''.join(row) for row in ans]

    def get_next(self, state, n):
        # state第i个元素表示第i列的皇后摆在第state[i]行（列从左往右，行从下往上）
        if len(state) == 0:
            return list(range(n))
        invalid = set()  # 记录当前列不能放的位置
        curr_col = len(state)
        # 前面的所有Q都会影响当前列的位置
        for prev_q_col, prev_q_idx in enumerate(state):
            # 横向
            invalid.add(prev_q_idx)
            # 斜线
            diff = curr_col - prev_q_col
            invalid.add(prev_q_idx + diff)  # 右上
            invalid.add(prev_q_idx - diff)  # 右下
        return [i for i in range(n) if i not in invalid]

    def backtracking(self, state, n, ans):
        if len(state) == n:
            ans.append(self.process_col_repr(state, n))
            return
        for x in self.get_next(state, n):
            state.append(x)
            self.backtracking(state, n, ans)
            state.pop()

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        self.backtracking([], n, ans)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.solveNQueens(4))






