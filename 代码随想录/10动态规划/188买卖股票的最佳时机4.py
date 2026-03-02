from typing import *


"""
买卖股票1：最多买卖1次
买卖股票2：买卖无限次
买卖股票3：最多买卖2次
买卖股票4（本题）：最多买卖k次

本题就是买卖股票3的扩展，最多买卖两次我们需要1个无操作的状态加上2 * 2个持有和不持有的状态，所以最多买卖k次就要1 + 2 * k个状态。
然后for循环遍历时我们就两两一组进行更新即可。
"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * (2 * k + 1) for _ in range(n)]
        # 初始化（奇数为持有状态，偶数为不持有状态）
        for j in range(1, 2 * k + 1, 2):
            dp[0][j] = -prices[0]
        # 遍历
        for i in range(1, n):
            for j in range(1, 2 * k + 1, 2):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - prices[i])  # 第xxx次持有
                dp[i][j + 1] = max(dp[i - 1][j + 1], dp[i - 1][j] + prices[i])  # 第xxx次不持有
        # 返回最后一个维度的全部状态中的最大值
        return max(dp[n - 1])
    


# 省去第一个状态（什么都没做）的版本
class Solution1:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(2 * k)] for _ in range(n)]  # 0：第1次持有，1：第1次不持有，2：第2次持有，...
        for i in range(2 * k):
            if i % 2 == 0:
                dp[0][i] = -prices[0]
        for i in range(1, n):
            for j in range(2 * k):
                if j % 2 == 0:
                    dp[i][j] = max(dp[i - 1][j], -prices[i] if j == 0 else dp[i - 1][j - 1] - prices[i])  # 第一次持有时直接是 -prices[i]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + prices[i])
        return max(dp[n - 1])





