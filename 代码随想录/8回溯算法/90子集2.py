from typing import *


class Solution:
    """
    回溯（有重复元素，需要横向去重）：和40组合总和2一样的解法，即nums有重复的元素。我们先将数组排序，并进行横向去重，即我们每次backtracking
    递归完成后，在partial state的同一个位置上的下一个possible value检查是否和前一个重复！
    """
    def backtracking(self, state, nums, start_idx, ans):
        ans.append(state[:])

        prev = None
        for i in range(start_idx, len(nums)):
            if nums[i] == prev:  # 横向去重，即搜索树中同一个分支往下的纵向不去重，而是不同分支去重，即partial state的同一个位置去重
                continue
            state.append(nums[i])
            self.backtracking(state, nums, i + 1, ans)
            prev = state.pop()


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)  # 横向去重需要排序！
        ans = []
        self.backtracking([], nums, 0, ans)
        return ans

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 2]
    print(sol.subsetsWithDup(nums))

