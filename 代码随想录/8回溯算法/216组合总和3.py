from typing import *


class Solution:
    """
    回溯：就是组合加了一个目标和的条件，start_idx版本，记住这个简洁的即可
    也整一个candidates数组，和其他组合总和一致，方便记
    """
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [i + 1 for i in range(9)]

        def backtracking(state, start_idx, s, ans):
            if len(state) > k or s > n:
                return
            elif len(state) == k and s == n:
                ans.append(state[:])
                return
            for i in range(start_idx, len(candidates)):
                state.append(candidates[i])
                s += candidates[i]
                backtracking(state, i + 1, s, ans)
                s -= candidates[i]
                state.pop()
        
        ans = []
        backtracking([], 0, 0, ans)
        return ans


class Solution1:
    """
    回溯：原始版本
    """
    def is_goal(self, state, n, k):
        return len(state) == k and sum(state) == n  # 组合加了一个sum的条件

    def get_next(self, state, n, k):
        if len(state) == 0:
            return list(range(1, 10))  # 1 - 9
        possibles = list(range(state[-1] + 1, 10))  # 和组合一样，不能有重复的组合，所以只能选当前选过的最大数字的后半部分
        diff = n - sum(state)  # 距离目标和的差异
        if diff < 0:  # 当前和已经超了目标和
            return []
        else:  # 返回不超过或等于目标和的候选数字
            return [x for x in possibles if x <= diff]  #

    def backtracking(self, state, n, k, ans):
        if self.is_goal(state, n, k):
            ans.append(state[:])
        for x in self.get_next(state, n, k):
            state.append(x)
            self.backtracking(state, n, k, ans)
            state.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        self.backtracking([], n, k, ans)
        return ans


