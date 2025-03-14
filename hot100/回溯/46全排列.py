from typing import *


"""
用used数组纵向去重：排列看顺序，123和321是两种不同的，所以就是当前没选的就都可以选，即用一个used进行纵向去重即可。
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(state, ans, nums, used):
            if len(state) == len(nums):
                ans.append(state[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    state.append(nums[i])
                    used[i] = True
                    backtracking(state, ans, nums, used)
                    used[i] = False
                    state.pop()

        ans = []
        used = [False] * len(nums)
        backtracking([], ans, nums, used)
        return ans








