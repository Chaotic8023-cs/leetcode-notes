from typing import *

"""
动态规划

1. dp数组下标含义：dp[i]表示前i个房间（包含i）最多能偷多少（1-index）
2. 递推公式：dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
    1. 当前房子i选择不偷，则前一个房子就可以偷，所以最大获得dp[i - 1]
    2. 则当前房子i选择偷，则前一个房子就不能偷，所以最大获得dp[i - 2] + nums[i - 1]
3. 初始化：dp[0] = nums[0], dp[1] = max(nums[0], nums[1])，因为前两个房间不能都偷！
4. 遍历顺序：正序遍历

也可以用1-index，但我们只记0-index即可
"""
class Solution:
    """
    0-index，记这个，最符合最先想到的思路
    """
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[n - 1]

    """
    1-index
    """
    def rob1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, n + 1):  # 1-index，所以nums里要-1
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp[n]




if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 1]
    print(sol.rob(nums))

