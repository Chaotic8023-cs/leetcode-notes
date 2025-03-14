# 122
from itertools import pairwise
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
            2. 昨天没持有股票，即当天买入了，即dp[i][0] = dp[i-1][1]-prices[i]
               和#121的区别就是可以多次买卖，所以昨天就算没有持有股票也可能已经获利了，
               所以是昨天不持有股票状态的利润减去今天买入的价格！
        我们取两种情况中最大的，即dp[i][0] = max(dp[i-1][0], -prices[i])
        dp[i][1]：有两种情况：
            1. 昨天就不持有股票，所以利润不变，即dp[i][1] = dp[i-1][1]
            2. 昨天持有股票，即当天卖出了，第dp[i][1] = dp[i-1][0] + prices[i]
               注音，昨天持有股票看的是dp[i-1][0]！
        我们取两种情况中最大的，即dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        这个和#121没有区别！因为：
            情况1: 昨天不持有股票，今天不持有股票，就算我们现在可以当天买了再卖，利润也不变，
                  所以还是dp[i][1] = dp[i-1][1]
            情况2: 昨天持有股票，今天不持有股票，只能是卖了，所以不变，还是昨天持有状态的利润
                  加上今天卖出获得的利润：dp[i-1][0] + prices[i]

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
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
        pprintdp(dp)
        return dp[n-1][1]

    # 解法2：贪心
    """
    从第二天开始，如果当天股价大于前一天股价，则在前一天买入，当天卖出，即可获得利润。
    如果当天股价小于前一天股价，则不买入，不卖出。也即是说，所有上涨交易日都做买卖，
    所有下跌交易日都不做买卖，最终获得的利润是最大的。
    """
    def maxProfit1(self, prices: List[int]) -> int:
        return sum(max(0, b - a) for a, b in pairwise(prices))


if __name__ == '__main__':
    prices = [7,6,4,3,1]
    sol = Solution()
    print(sol.maxProfit(prices))

