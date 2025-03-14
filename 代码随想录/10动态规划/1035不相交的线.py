from typing import *


"""
本题和#1143一模一样，只是表述不一样，完全一样的代码就可以ac。
最长公共子序列就是连续的相等的数字，因为连续所以不可能相交，所以两题一样！
"""
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        # 初始化
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if nums1[i] == nums2[0]:
                dp[i][0] = 1
            elif nums1[i] != nums2[0]:
                dp[i][0] = dp[i - 1][0]
        for j in range(n):
            if nums2[j] == nums1[0]:
                dp[0][j] = 1
            elif nums2[j] != nums1[0]:
                dp[0][j] = dp[0][j - 1]
        # 遍历
        for i in range(1, m):
            for j in range(1, n):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m - 1][n - 1]



