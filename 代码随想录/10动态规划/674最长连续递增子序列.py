from typing import *


class Solution:
    """
    和#300最长递增子序列不同的是，本题是连续的子序列，即区间，所以方法就和股票的最佳买卖时机2中双指针一模一样，
    就是求单增区间，返回找到的单增区间中最大的长度即可。

    本题就记双指针常规做法就行，dp其实更简单！
    """
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 1
        i, j = 0, 1
        n = len(nums)
        while j < n:
            while j < n and nums[j] > nums[j - 1]:
                j += 1
            ans = max(ans, j - i)
            i = j
            j += 1
        return ans

    """
    动态规划：
    此题动规也很好想，和#300非连续一样，初始化默认最小长度就是1。因为是连续子序列，所以每个下标i之和前一个位置有关。
    1. dp数组下标含义：dp[i]表示以下标i为结尾（包含）的最长连续递增子序列的长度
    2. 递推公式：如果nums[i] > nums[i - 1]，说明当前元素可以加到以前一个元素为末尾的最长连续递增子序列中，即dp[i] = dp[i - 1] + 1
    3. 初始化：同#300，最小长度都为1
    4. 遍历顺序：正序即可
    """
    def findLengthOfLCIS_dp(self, nums: List[int]) -> int:
        n = len(nums)
        # 初始化
        dp = [1] * n
        # 遍历
        for i in range(1, n):
            if nums[i] > nums[i - 1]:  # 由于连续，只和前一个元素相关！
                dp[i] = dp[i - 1] + 1
        return max(dp)




