from typing import *
from math import inf


class Solution:
    """
    常规做法（其实是贪心，取左边一个最小值右边一个最大值）：因为买入的那天一定是卖出的那天之前的最小值，所以只要维护一个最小值就行，然后每天看卖出是否能赚更多即可。
    此题记常规做法即可！
    """
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = inf   # 维护一个当前的最小值
        profit = 0
        for p in prices:
            curr_min = min(curr_min, p)
            profit = max(profit, p - curr_min)
        return profit

    """
    动态规划：此题没必要用动态规划，但为了后面的题做铺垫所以还是记录一下。真正解的化还是上面的贪心即可。
    1. dp数组下标含义：dp[i][0]表示第i天交易后持有股票能获得的最大利润，dp[i][1]表示第i天交易后不持有股票能获得的最大利润。
        注意，这里持有和不持有指的是当天最后的状态，如果当天买入了则当天就是持有；如果当天是不持有状态，那么可能还没买，
        也可能已经买卖过一次了！
    2. 递推公式：
        1. dp[i][0] = max(dp[i - 1][0], -prices[i])
            当天持有，那么：
                1 > 昨天就已经持有了，所以不变，即dp[i - 1][0]
                2 > 今天买入了，所以今天就持有了，即-prices[i]
                    注意，这里为什么不是昨天不持有加上今天买入呢？因为昨天不持有的状态可能已经买卖过一次了，但本题只能买卖一次，所以直接就是-prices[i]
        2. dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
            1 > 昨天就已经不持有了，所以不变，即dp[i - 1][1]
            2 > 今天卖出了，所以今天就不持有了，但今天能卖出昨天肯定是持有状态的（因为只能买卖一次），所以是昨天持有加上今天卖出，即dp[i - 1][0] + prices[i]
    3. 初始化：因为用的是0-index，所以第一天持有和不持有分别就就是-prices[0]和0
    4. 遍历顺序：正序遍历
    """
    def maxProfit_dp(self, prices: List[int]) -> int:
        n = len(prices)
        # 初始化
        dp = [[0, 0] for _ in range(n)]  # [持有，不持有]
        dp[0][0], dp[0][1] = -prices[0], 0
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], -prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        return max(dp[n - 1][0], dp[n - 1][1])




