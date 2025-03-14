from typing import *

"""
完全背包变种：和494目标和的思想一样，只是把遍历背包容量改成正序了，因为可以复用（一看到硬币数量不限则时完全背包）
要记住的就是求方法个数则初始化dp[0] = 1

注意：这里和纯完全背包求最大value不一样，这里是求方法的个数（不同组合），所以只能先物品后背包，我们统一记先物品后背包即可。
如果本题换成先背包后物品则求的是不同排列(见377组合总和4)!
原因：先物品的话，我们就是每次看所有背包容量下单个硬币怎么放，所以是先看1再看2，不会出现2在1的前面，所以就是组合；
    先背包的话，每个容量所有硬币都会考虑一边，所以就会出现12或21，即有顺序了，就是排列！
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        dp[0][0] = 1  # 求方法个数则dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(amount + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= coins[i - 1]:
                    dp[i][j] += dp[i][j - coins[i - 1]]  # 完全背包中要复选，所以选当前物品则用dp[i]；同时求方法个数则是不选和选的个数之和
        return dp[n][amount]

    def change_1d(self, amount: int, coins: List[int]) -> int:
        # 初始化
        dp = [0] * (amount + 1)
        dp[0] = 1  # 求方法个数则dp[0] = 1
        n = len(coins)
        # 遍历
        for i in range(n):  # 物品
            for j in range(coins[i], amount + 1):  # 背包容量：正序（可以复用）
                dp[j] = dp[j] + dp[j - coins[i]]  # dp[j]：不选当前的硬币; dp[j - coins[i]]：选当前的硬币
        return dp[amount]



