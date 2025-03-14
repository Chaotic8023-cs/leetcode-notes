from typing import *


class Solution:
    """
    回溯：和216组合的和3一样，除了此题中可以有重复的元素。但是如何避免重复的组合呢（例如[2,2,3]和[2,3,2]）?
    还是用组合的思想，我们只选后半部分。但是此题同一个元素能选多次，start_idx在下一层的时候不变就行，这样保证了当前
    元素能复选，且我们不会再选前面的元素（组合思想）
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(start_idx, curr_state, total, candidates, target, ans):
            if total > target:
                return
            if total == target:
                ans.append(curr_state[:])
                return
            for i in range(start_idx, len(candidates)):
                curr_state.append(candidates[i])
                total += candidates[i]
                backtracking(i, curr_state, total, candidates, target, ans)  # start_idx在下一层递归不变，所以就能复选当前元素
                total -= candidates[i]
                curr_state.pop()

        ans = []
        backtracking(0, [], 0, candidates, target, ans)
        return ans


class Solution1:
    """
    原始版本
    """
    def is_goal(self, state, target):
        return sum(state) == target

    def get_next(self, state, candidates, target):
        if len(state) == 0:
            return candidates
        possibles = candidates[candidates.index(state[-1]):]  # 能选当前元素（可重复上次选的），和它后面的，但不能选以前的
        diff = target - sum(state)
        if diff < 0:  # 和大于target就停止
            return []
        else:
            return [x for x in possibles if x <= diff]

    def backtracking(self, state, candidates, target, ans):
        if self.is_goal(state, target):
            ans.append(state[:])
            return
        for x in self.get_next(state, candidates, target):
            state.append(x)
            self.backtracking(state, candidates, target, ans)
            state.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.backtracking([], candidates, target, ans)
        return ans

