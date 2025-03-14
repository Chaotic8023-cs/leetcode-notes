from typing import *


class Solution:
    """
    典型回溯：start_idx版本。start_idx记录了当前选择的起始位置，相当于get_next的逻辑，即每次只能选选过的数字的后半部分。
    按模板的看Solution1。
    """
    def backtracking(self, state, n, k, start_idx, ans):
        if len(state) == k:
            ans.append(state[:])
            return
        for i in range(start_idx, n):  # 当前的possible是 [start_idx, n)
            state.append(i + 1)  # 我们按0进行index，但是ans是从1起步，所以都+1
            self.backtracking(state, n, k, i + 1, ans)
            state.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.backtracking([], n, k, 0, ans)
        return ans


class Solution1:
    """
    典型回溯：需要注意的是组合不看顺序，即123和132是同一个组合。假设一共有5个数[1,2,3,4,5]，k=3，那么当partial为[1,3]时，我们只能选
    3后面的[4,5]，因为如果选2的话凑成[1,3,2]，就和前面选过的[1,2,3]重复了！
    """
    def is_goal(self, state, k):
        return len(state) == k

    def get_next(self, state, n):
        if len(state) == 0:
            return list(range(1, n + 1))
        return list(range(state[-1] + 1, n + 1))  # 组合能有重复，所以只能取当前有的数字的后面的那些数

    def backtracking(self, state, n, k, ans):
        if self.is_goal(state, k):
            ans.append(state[:])  # deep copy，因为state是变化的数组
            return
        for x in self.get_next(state, n):
            state.append(x)
            self.backtracking(state, n, k, ans)
            state.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.backtracking([], n, k, ans)
        return ans


class Solution2:
    """
    加上了剪枝优化，可以不记这个，记基础的就行。
    例如[1,2,3,4], k = 4，当state是[2]时，我们直到剩下的选择只有[3,4]，不可能凑成4个的组合，所以可以直接return。
    """
    def is_goal(self, state, k):
        return len(state) == k

    def get_next(self, state, n):
        if len(state) == 0:
            return list(range(1, n + 1))
        return list(range(state[-1] + 1, n + 1))  # 组合能有重复，所以只能取当前有的数字的后面的那些数

    def backtracking(self, state, n, k, ans):
        if self.is_goal(state, k):
            ans.append(state[:])  # deep copy，因为state是变化的数组
            return
        next_possibles = self.get_next(state, n)
        if len(next_possibles) == 0 or len(state) + len(range(next_possibles[0], n + 1)) < k:  # 剪枝
            return
        for x in next_possibles:
            state.append(x)
            self.backtracking(state, n, k, ans)
            state.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.backtracking([], n, k, ans)
        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 4
    k = 2
    print(sol.combine(n ,k))

