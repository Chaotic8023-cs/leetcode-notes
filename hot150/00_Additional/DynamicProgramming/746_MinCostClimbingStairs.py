# 746
from typing import *


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (1 + len(cost))
        """
        dp[i]表示到i台阶需要的cost（注意是到，而不是爬到楼顶，越过这阶台阶！）
        eg:
        idx: 0  1   2   3  4  5   6   7  8   9   10 END
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1] TOP
        dp = 0  0   0   1  2  2   3   3  4   4   5
        前两阶都需要0，因为我们可以从第0阶爬1步或两步到达！
        我们看爬到第6阶台阶需要多少，则有两种方法：
            1. 从第四阶爬两步：cost = dp[4] + cost[4]
            2. 从第五阶爬一步：cost = dp[5] + cost[5]
        即到前面两阶需要的cost加上前面两阶自己需要的cost
        这样以来dp里最后一个表示到末尾需要的cost，而不是爬到顶，即TOP
        同理，我们可以从第9阶爬两步，或第10阶爬一步，我们返回其中cost最小的即可！
        """
        for i in range(3, 1 + len(cost)):
            """
            这里我们从3开始，我们先看dp[i-2]即dp[1]
            对应的是cost[0]，两个index差1，所以是cost[i-3]
            """
            dp[i] = min(dp[i - 2] + cost[i - 3], dp[i - 1] + cost[i - 2])
        return min(dp[-2] + cost[-2], dp[-1] + cost[-1])

    """
    此题还可以把dp[0]直接看成到第1阶所需的cost，然后dp[-1]表示TOP，
    这样最后直接return dp[-1]即可！
    """
    def minCostClimbingStairs1(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        return dp[n]


if __name__ == '__main__':
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    sol = Solution()
    print(sol.minCostClimbingStairs(cost))
