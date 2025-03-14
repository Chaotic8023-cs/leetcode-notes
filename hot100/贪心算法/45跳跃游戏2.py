from typing import *
from math import inf


class Solution:
    """
    贪心：我们不考虑每次跳几步，我们只管每次最远能跳到哪。假设第一次最远跳到下标2，然后我们遍历前两个位置后发现此时最远跳到5，那么其实说明
    第一次和第二次跳跃不管每次几步，总能两次跳到最远的下标5。所以我们只需要遍历nums一直更新当前最远能跳到哪，每次起跳的终点就是起跳时的curr_max，
    当达到curr_max时从curr_max起跳（其实真正的起跳位置可能是之前，我们只管最远跳多远），步数+1。

    基本思想是每次尽可能的往远跳，真正最少次数的起跳位置可能不是每次跳到最远，但我们按最远的算，因为总能跳到最远及之前的所有位置上。
    """
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jump = 0  # 起跳点
        curr_max = 0
        ans = 0
        for i in range(n - 1):  # 为什么是n-1不看最后一格，因为要是curr_max已经包含最后一格了，说明上一步就能直接跳到最后一格，在最后一格就不用再起跳了
            curr_max = max(curr_max, i + nums[i])
            if i == jump:  # 一开始从0起跳，下一次从上一次起跳时的curr_max处起跳
                ans += 1
                jump = curr_max
        return ans

    """
    动态规划：比较好想，但复杂度O(n^2)
    dp[i]表示跳到下标i最小的步数，我们遍历每个位置i，对于每个下标i我们遍历i前面的所有位置j，如果从j能跳到i，那么dp[i]就是跳到j的最小步数+1。
    """
    def jump1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [inf] * n
        dp[0] = 0
        for i in range(1, n):
            for j in range(i):  # 遍历前面的位置j，如果从j能跳到i，那么dp[i]就是跳到j的最小步数+1
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[n - 1]








