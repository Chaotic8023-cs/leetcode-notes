from typing import *

"""
198打家劫舍的变种，变成环了。
所以就两种情况：
    1. 第一个偷最后一个不偷
    2. 第一个不偷最后一个偷
我们分别按普通的打家劫舍处理最后取最大的即可。
"""
class Solution:
    def rob(self, nums: List[int]) -> int:  # 0-index
        n = len(nums)
        if n <= 3:  # 3个及3一下只能偷1次
            return max(nums)
        # 两种情况：1. 第一个偷最后一个不偷 2. 第一个不偷最后一个偷；每种按普通的打家劫舍处理即可
        # 偷第一个，最后一个就不能偷（去掉最后一个）
        dp1 = [0] * (n - 1)
        dp1[0], dp1[1] = nums[0], max(nums[0], nums[1])
        # 不偷第一个，最后一个就可以偷（去掉第一个）
        dp2 = [0] * (n - 1)
        dp2[0], dp2[1] = nums[1], max(nums[1], nums[2])
        # 遍历
        for i in range(2, n - 1):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])
        for i in range(2, n - 1):
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i + 1])  # 因为去掉第一家了，所以这里dp[i]对应的就是nums[i + 1]
        # 取两着中大的那个
        return max(dp1[-1], dp2[-1])


# 
class Solution1:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)
        # dp数组初始化多一个（这样dp[1]就不用使用max），和普通打家劫舍一致
        dp1, dp2 = [0] * n, [0] * n
        # 偷第1家
        dp1[0], dp1[1] = 0, nums[0]  # 偷第1家时从第1家起步（下标0），此时dp2[i]对应nums[i - 1]
        for i in range(2, n):
            dp1[i] = max(dp1[i - 2] + nums[i - 1], dp1[i - 1])
        # 不偷1家
        dp2[0], dp2[1] = 0, nums[1]  # 不偷第1家时从第2家起步（下标1），此时dp2[i]对应nums[i]
        for i in range(2, n):
            dp2[i] = max(dp2[i - 2] + nums[i], dp2[i - 1])
        return max(dp1[n - 1], dp2[n - 1])







