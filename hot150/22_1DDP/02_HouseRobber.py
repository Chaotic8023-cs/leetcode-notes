# 198
from typing import *


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        # dp[i]代表到这个位置能抢到的钱 (即一共i+1个房子能抢到的钱)
        """
        因为隔一个才能抢，所以每当增加一个房子（当前为房子i），我们有两种方法：
            1. 不抢当前的房子：则最多抢的钱 = i-1个房子的钱
            2. 抢当前的房子：则不能抢i-1的房子，即最多抢的钱 = i-2个房子的钱 + 当前房子的钱
        我们选两个方法中钱多的！
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]  # 一个房子就只能抢它
        dp[1] = max(nums[0], nums[1])  # 两个房子可以抢一个，所以选钱多的
        for i in range(2, len(nums)):
            # 要么不抢当前房子，即钱=抢到前一个房子的钱
            # 要么抢当前房子，即钱=抢到上上个房子的钱 + 当前房子的钱
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]


if __name__ == '__main__':
    nums = [2, 7, 9, 3, 1]
    sol = Solution()
    print(sol.rob(nums))

