from typing import *


"""
状压dp + 记忆化搜索：和 #473火柴拼正方形思路完全一致
只是这里改成了凑k次
"""
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def dfs(nums, status, cap, curr, rest, dp):
            if rest == 0:
                return True  # 必然 status == 0
            if dp[status] != 0:
                return dp[status] == 1
            ans = False
            for i in range(len(nums)):
                if status & (1 << i) != 0 and curr + nums[i] <= cap:
                    if curr + nums[i] == cap:
                        ans = dfs(nums, status ^ (1 << i), cap, 0, rest - 1, dp)
                    else:
                        ans = dfs(nums, status ^ (1 << i), cap, curr + nums[i], rest, dp)
                    if ans:
                        break
            dp[status] = 1 if ans else - 1
            return ans
                        
        n = len(nums)
        s = sum(nums)
        if s % k != 0:
            return False
        cap = s // k
        dp = [0] * (1 << n)
        return dfs(nums, (1 << n) - 1, cap, 0, k, dp)  # 需要凑k次



