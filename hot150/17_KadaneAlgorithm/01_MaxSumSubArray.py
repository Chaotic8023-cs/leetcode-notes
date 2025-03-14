# 53
from typing import *


class Solution:
    # kadane's algorithm: 普通dp, O(n) time and space
    def maxSubArray(self, nums: List[int]) -> int:
        """
        dp[i]表示以dp[i]为结尾的最大subarray的sum，(包含dp[i]的max subarray sum)
        因为最终的最大subarray一定是以某个元素结尾的，所以我们这么设定
        那么递推公式就可以得出：
        如果dp[i-1]为正我们就要，为负我们就不要，即只要nums[i-1]
        这样确保max sum单增
        """
        # dp[0]为第一个元素为结尾的max subarray sum，即nums[0]
        dp = [nums[0]] + [0] * (len(nums)-1)
        for i in range(1, len(nums)):
            dp[i] = nums[i] + max(dp[i-1], 0)
        return max(dp)

    # kadane's algorithm: O(n) time, O(1) space
    def maxSubArray1(self, nums: List[int]) -> int:
        """
        cur_max即记录dp[i]
        每次更新cur_max的时候，更新前cur_max就是dp[i-1]，如果大于0我们就要，小于0就不要(取0)
        """
        ans = cur_max = nums[0]
        for x in nums[1:]:
            cur_max = max(cur_max, 0) + x  # 大于0就要，小于0就不要
            ans = max(ans, cur_max)
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(sol.maxSubArray(nums))
