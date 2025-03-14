from typing import *


"""
买卖股票1：最多买卖1次
买卖股票2：买卖无限次
买卖股票3：最多买卖2次
买卖股票4：最多买卖k次

买卖股票含冷冻期：买卖无限次，但加入了冷冻期限制，即卖出一次后第二天不能买入
买卖股票含手续费：买卖无限次，但每次买入有一个统一的手续费

就是买卖股票2买入时加入手续费即可！
"""
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        # 初始化
        dp = [[0, 0] for _ in range(n)]
        dp[0][0], dp[0][1] = -prices[0] - fee, 0  # 和买卖股票2一样：[持有，不持有] (注意的是：第一天不持有状态还是0，因为是最大利润，所以还没操作利润为0最大，因为买入再卖出要亏一个手续费！)
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i] - fee)  # 唯一的区别就是今天买入时加上这个手续费
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        return max(dp[n - 1][0], dp[n - 1][1])