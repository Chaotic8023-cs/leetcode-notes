from typing import *
from math import inf


"""
完全背包变种2：求装满背包最小物品数
dp[i][j]：用前i个硬币找j块钱最少的个数
递推公式：
    1. 不选当前第i个硬币：dp[i][j] = dp[i - 1][j]
    2. 选当前第i个硬币（当前背包容量j >= coins[i - 1]）：dp[i][j] = dp[i][j - coins[i - 1]] + 1
    我们取min
初始化：dp[0][0] = 0，找0块需要0个硬币，用来应对一开始背包容量只用1枚硬币的情况，比如找零2块，那么就是找0块需要0枚0块 + 1枚2块 = 1枚
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[inf] * (amount + 1) for _ in range(n + 1)]
        dp[0][0] = 0  # dp[0][0] = 0来应对找零1枚硬币的情况，比如找零2块，那么就是找0块需要0枚0块 + 1枚2块 = 1枚
        for i in range(1, n + 1):  # 物品从1开始
            for j in range(amount + 1):  # 背包容量从0开始
                dp[i][j] = dp[i - 1][j]  # 不选当前第i个硬币
                if j >= coins[i - 1]:  # 物品是1-index，所以访问coins要-1
                    dp[i][j] = min(dp[i][j], dp[i][j - coins[i - 1]] + 1)  # 选当前第i个硬币。能复选所以是dp[i][j - coins[i - 1]]而不是dp[i - 1][j - coins[i - 1]]
        return dp[n][amount] if dp[n][amount] < inf else -1


"""
补充1：#518零钱兑换2：完全背包变种1：求方法个数
dp[i][j]：用前i个硬币找j块钱有多少种方法（组合）
递推公式：因为变成方法个数了，所以不选和选变成累加了，即不选为dp[i][j] = dp[i - 1][j]；如果能选，则 += dp[i][j - coins[i - 1]]
遍历顺序：求组合方法个数就是常规的顺序，先物品后背包。
初始化：所有求方法个数一般初始化都是1，就像爬楼梯
"""
class Solution1:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        dp[0][0] = 1  # 求方法个数就类似爬楼梯，初始化时dp[0][0] = 1，因为：比如找2块的一种方法就是找0块的这1种 + 1枚2块，最后还算1种方法。因为算方法不加1，所以一开始就得初始化一个1。
        for i in range(1, n + 1):
            for j in range(amount + 1):
                dp[i][j] = dp[i - 1][j]  # 不选当前硬币i有多少种方法
                if j >= coins[i - 1]:  # 如果能选当前硬币i，则加上选硬币i的方法数。因为能复选，所以用dp[i][j - coins[i - 1]]
                    dp[i][j] += dp[i][j - coins[i - 1]]
        return dp[n][amount]  # 如果找不了，就得返回0，但初始化就是0，所以不用管



