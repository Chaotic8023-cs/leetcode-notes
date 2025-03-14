from typing import *


"""
1. dp数组下标含义：dp[i]指以i为结尾（包含）的最长递增子序列的长度
2. 递推公式：对于i前面每个下标j，如果nums[i] > nums[j]，则当前的小标i就能加到子序列中，所以就是dp[j] + 1。我们取最大的那个值
3. 初始化：所有下标默认最短的就是1，因为它自己就算一个！
4. 遍历顺序：正序即可

注意，最后返回要取整个dp的max，因为dp数组含义时以i为结尾的，但最终最长的子序列不一定就包含数组最后一个元素，所以要取max(dp)！
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # 初始化
        dp = [1] * n  # 每个元素本身就是一个递增子序列，所以最短都是1！
        # 遍历
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)  # 因为我们要取前面所有下标中最大的那个+1，所以要一直取max！
        return max(dp)  # 最长的严格递增子序列的结尾不一定就是数组最后一个元素！



