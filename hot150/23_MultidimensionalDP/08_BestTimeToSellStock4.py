# 188
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 * k] * n
        # 初始化
        for i in range(2 * k):
            if i % 2 == 0:
                # 持有
                dp[0][i] = -prices[0]
            else:
                # 不持有
                dp[0][i] = 0

        """
        解法同#123， 只是dp数组每天需要2k个：
        k = 0:      第一次持有
        k = 1:      第一次不持有
        k = 2:      第二次持有
        k = 3:      第二次不持有
        k = 4:      第三次持有
        ...
        k = 2k-1:   第k次持有
        k = 2k:     第k次不持有
        """
        for i in range(1, n):
            for j in range(2 * k):
                if j == 0:
                    # 第1次持有
                    # 1. 昨天还是第一次持有， 2. 昨天是还没操作，即初始值为0然后购买第一次
                    dp[i][j] = max(dp[i-1][j], -prices[i])
                elif j % 2 == 0:
                    # 第k次持有
                    # 1. 昨天还是第k次持有，2. 昨天是第k-1次不持有
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] - prices[i])
                else:
                    # 第k次不持有
                    # 1. 昨天还是第k次不持有，2. 昨天是第k次持有
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + prices[i])
        return dp[n-1][2*k-1]

    """
    因为当天只跟前一天有关，我们可以优化空间，只保存两天的数组即可，也就是dp数组两行2*k就够
    """


if __name__ == '__main__':
    k = 2
    prices = [3,2,6,5,0,3]
    sol = Solution()
    print(sol.maxProfit(k, prices))

