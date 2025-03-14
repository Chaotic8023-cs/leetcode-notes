from typing import *
from math import inf


"""
买卖股票1：最多买卖1次
买卖股票2（本题）：买卖无限次
"""
class Solution:
    """
    最简单的做法：就是统计两两之间正利润即可（递增区间拆成两两之间的也行！）
    """
    def maxProfit(self, prices: List[int]) -> int:
        diff = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        return sum([d for d in diff if d > 0])

    """
    双指针（一般做法）：因为能买卖多次，其实就是找递增区间，用双指针找到所有递增区间然后求差即可。
    """
    def maxProfit1(self, prices: List[int]) -> int:
        i, j = 0, 1  # i是当前递增区间的头，j用来遍历找到尾部
        n = len(prices)
        profit = 0
        while j < n:
            while j < n and prices[j] >= prices[j - 1]:
                j += 1
            profit += prices[j - 1] - prices[i]  # 当前递增区间的利润
            # 继续找下一个递增区间
            i = j
            j += 1
        return profit

    """
    动态规划：
    此题较121基础版改变的是可以买卖多次了，所以唯一改的地方就是今天持有的状态中今天买入的情况：
        因为能买卖多次，所以今天买入还得加上昨天不持有状态能得到的最大利润。因为昨天不持有有可能已经买卖多次了，所以得把之前的利润加上！
    """
    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]  # [持有，不持有]
        dp[0][0], dp[0][1] = -prices[0], 0
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])  # 和121基础版本区别在这，如果今天买入还得加上昨天不持有的最大利润！
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        return max(dp[n - 1])  # 返回最后一天两种状态中的最大值




