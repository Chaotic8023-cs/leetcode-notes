from typing import *


class Solution:
    """
    回溯：排列看顺序，即相同元素但不同顺序也算不同的一组。所以排列相当于纵向去重，我们每次只用看当前state没用过的数即可。
    """
    def backtracking(self, state, nums, ans):
        if len(state) == len(nums):
            ans.append(state[:])
            return

        for x in [i for i in nums if i not in state]:  # 排列看顺序，不同顺序算不同的，所以只要没选过就可以用（即纵向不用重复的元素）
            state.append(x)
            self.backtracking(state, nums, ans)
            state.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backtracking([], nums, ans)
        return ans


class Solution1:
    """
    回溯：用used数组记录用过的元素来达到纵向去重。
    """
    def backtracking(self, state, nums, ans, used):
        if len(state) == len(nums):
            ans.append(state[:])
            return

        for i in range(len(nums)):  # 排列看顺序，不同顺序算不同的，所以只要没选过就可以用（即纵向不用重复的元素）
            if not used[i]:
                used[i] = True  # 去下一层前标记当前元素已被用过
                state.append(nums[i])
                self.backtracking(state, nums, ans, used)
                state.pop()
                used[i] = False  # 从深层回来之后取消标记

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [False] * len(nums)
        self.backtracking([], nums, ans, used)
        return ans



