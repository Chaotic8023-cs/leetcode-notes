from typing import *


"""
能复选的组合问题：因为当前元素能无限复选，所以start_idx就不+1，即直接传i
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(start_idx, state, ans, candidates, target):
            s = sum(state)
            if s > target:  # 剪枝：当前sum大于target直接返回
                return
            if s == target:
                ans.append(state[:])
                return
            for i in range(start_idx, len(candidates)):
                state.append(candidates[i])
                backtracking(i, state, ans, candidates, target)  # 因为当前元素能无限复选，所以start_idx就不+1，即直接传i
                state.pop()

        ans = []
        backtracking(0, [], ans, candidates, target)
        return ans




