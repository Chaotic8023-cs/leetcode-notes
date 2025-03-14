from typing import *


class Solution:
    """
    回溯（横向去重）：去重思路和40组合总和2还有90子集2一样。此题就是普通全排列加上重复元素，所以需要横向去重。此题可以提前排序然后用prev方法进行去横向去重。
    """
    def backtracking(self, state, nums, used, ans):
        if len(state) == len(nums):
            ans.append(state[:])
            return

        prev = None
        for i in range(len(nums)):
            if not used[i] and nums[i] != prev:  # 加上横向去重，和used一起用。也就是往深了走能用重复的1，但以第一个1开头的找完后下次开头就不能用1了！
                used[i] = True
                state.append(nums[i])
                self.backtracking(state, nums, used, ans)
                prev = state.pop()
                used[i] = False


    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [False] * len(nums)
        nums = sorted(nums)
        self.backtracking([], nums, used, ans)
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 2]
    print(sol.permuteUnique(nums))


