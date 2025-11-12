from typing import *


"""
能复选的组合问题：因为当前元素能无限复选，所以start_idx就不+1，即直接传i
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(state, start_idx, curr_sum, ans):
            if curr_sum > target:
                return
            elif curr_sum == target:
                ans.append(state[:])
                return
            for i in range(start_idx, len(candidates)):
                state.append(candidates[i])
                curr_sum += candidates[i]
                backtracking(state, i, curr_sum, ans)  # 因为当前元素能无限复选，所以start_idx就不+1，即直接传i
                curr_sum -= candidates[i]
                state.pop()

        ans = []
        backtracking([], 0, 0, ans)
        return ans 



