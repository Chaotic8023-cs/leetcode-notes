# 121
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        min_buy = prices[0]
        max_profit = 0
        for i in range(1, n):
            max_profit = max(max_profit, prices[i] - min_buy)
            """
            min_buy should be updated after max_profit,
            since stock cannot be sold on the same day of buying.
            However, first updating min_buy still works, as buying and
            selling at same day produce 0 profit, the updated minimum
            will still be used afterwards!
            """
            min_buy = min(min_buy, prices[i])
        return max_profit

    # 动态规划
    def maxProfit1(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        """
        含义：
        dp[i][0]：第i天状态为持有股票的最大利润
        dp[i][1]：第i天状态为不持有股票的最大利润
        注意：表示的是状态，第i天持有和不持有只是当天的状态，和当天买卖没关系。
        例如，第三天持有并不代表是第三天买入的，可能是前面几天买的。
        
        状态转移：
        根据前一天(i-1)的状态推断今天(i)的状态
        dp[i][0]：有两种情况：
            1. 昨天就持有股票，所以利润不变，即dp[i][0] = dp[i-1][0]
            2. 昨天没持有股票，即当天买入了，即dp[i][0] = -prices[i]
               因为买了，且只能买一次（买时不可能已有利润），所以直接就是-prices[i]
        我们取两种情况中最大的，即dp[i][0] = max(dp[i-1][0], -prices[i])
        dp[i][1]：有两种情况：
            1. 昨天就不持有股票，所以利润不变，即dp[i][1] = dp[i-1][1]
            2. 昨天持有股票，即当天卖出了，第dp[i][1] = dp[i-1][0] + prices[i]
               注音，昨天持有股票看的是dp[i-1][0]！
        我们取两种情况中最大的，即dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        
        初始化：
        看第一天，dp[0][0]为持有状态，即买入了，利润就是-prices[0]
        dp[0][1]为不持有状态，即无交易发生，利润为0
        
        遍历顺序：
        从第2天开始顺序遍历，我们要的最大利润即为最后一天的两种情况的最大值：
        max(dp[end][0], dp[end][1])
        由于我们不可能在持有股票的情况下赚取最大利润，所以不持有情况肯定比持有的利润大，
        即直接返回dp[end][1]就可以了。
        """
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
        pprintdp(dp)
        return dp[n-1][1]


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    sol = Solution()
    print(sol.maxProfit(prices))
    print(sol.maxProfit1(prices))

