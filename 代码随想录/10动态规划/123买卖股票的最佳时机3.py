from typing import *
from math import inf


"""
买卖股票1：最多买卖1次
买卖股票2：买卖无限次
买卖股票3（本题）：最多买卖2次

1. dp数组下标含义：一下都是某种状态所能获得的最大利润
    1> dp[i][0]: 还没有进行操作（即还没有进行第一次买卖）
    2> dp[i][1]: 第一次持有（不一定是当天买，主要是第一次持有就算这个状态）
    3> dp[i][2]: 第一次不持有（不一定是当天卖，只要是在卖和第二次买入之前就算这个状态）
    4> dp[i][3]: 第二次持有
    5> dp[i][4]：第二次不持有
2. 递推公式：见代码
3. 初始化：根据直觉即可 -> dp[0][0], dp[0][1], dp[0][2], dp[0][3], dp[0][4] = 0, -prices[0], 0, -prices[0], 0
4. 遍历顺序：正序遍历

注意：dp[i][0]没进行操作的状态其实可以省略，因为：
    1. 不用递推：当天没进行操作的话前一天只能也是没进行操作，所以一直是0
    2. dp[i][1]虽然可以从dp[i][0]推过来，即当天买入，但因为是第一次买入，所以直接-prices[i]即可（因为dp[i][0]一直=0）
我们不省略是因为看着好看也好记！
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # 初始化
        dp = [[0, 0, 0, 0, 0] for _ in range(n)]
        dp[0][0], dp[0][1], dp[0][2], dp[0][3], dp[0][4] = 0, -prices[0], 0, -prices[0], 0  # 根据直觉初始化，比如第一次持有就是直接买，第一次不持有就是第一天买卖一次结果还是0；第二次同理，比如第二次不持有就是第一天买卖两次最后还是0
        # 遍历
        for i in range(1, n):
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])  # 1. 昨天就第一次持有；2. 今天第一次买入，昨天还没有进行操作 (实际上dp[i][0]没操作可以直接省略，因为一直是0！)
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])  # 1. 昨天就第一次不持有；2. 今天第一次卖出，昨天第一次持有
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])  # 1. 昨天就第二次持有；2. 今天第二次买入，昨天第一次不持有
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])  # 1. 昨天就第二次不持有；2. 今天第二次卖出，昨天第二次持有
        return max(dp[n - 1])  # 返回最后一天5中状态中的最大值



