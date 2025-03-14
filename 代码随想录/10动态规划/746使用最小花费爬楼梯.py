from typing import *


"""
动态规划：
注意此题到达楼梯顶要越过最后一阶楼梯！
1. dp数组下标含义：dp[i] = 到达第i阶楼梯需要的最小花费
2. 递推公式：dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
    到达第i层有两种选择：
        1. 从i-2层出发一次走2步：dp[i - 2] + cost[i - 2]
        2. 从i-1层出发一次走1步：dp[i - 1] + cost[i - 1]
    我们要求最小值所以取min
3. 初始化：因为一开始可以从i=0和i=1出发，且dp数组下标的含义为到达，所以一开始0和1就是到达的，所以dp[0] = 0, dp[1] = 0，
    这样dp[2]就会取min(dp[0] + cost[0], dp[1] + cost[1])，符合题意
4. 遍历顺序：正序遍历
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)  # 初始化：dp[0] = 0, dp[1] = 0
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        return dp[n]







