from typing import *

"""
完全背包变种：求最小的物品数量
1. dp数组下标含义：dp[i][j]表示用前i个硬币找零j所需的最小硬币数
2. 递推公式：完全背包的max换成min
3. 初始化：全inf（为了取min），除了dp[0][0] = 0，因为使用0个硬币找0块钱相当于不用找，这个0也为同一行只用1个硬币找零做铺垫了（如dp[5] = dp[5-5] + 1 = 1）
4. 遍历顺序：2d正序遍历即可，注意完全背包选物品i时用的是dp[i]而不是dp[i-1]；1d也正序遍历，因为要复用！
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float('inf')] * (amount + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):  # 物品
            for j in range(amount + 1):  # 背包容量：由于此题我们全部初始化成inf，但第一列应当为0，所以背包容量从0开始遍历，我们统一记背包都从0开始遍历即可
                dp[i][j] = dp[i - 1][j]
                if j >= coins[i - 1]:
                    dp[i][j] = min(dp[i][j], dp[i][j - coins[i - 1]] + 1)  # 这里换成min了，因为我们要的是最小的个数
        return dp[n][amount] if dp[n][amount] < float('inf') else -1

    """
    1d版本
    """
    def coinChange_1d(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, n + 1):  # 物品
            for j in range(coins[i - 1], amount + 1):  # 背包容量
                dp[j] = min(dp[j], dp[j - coins[i - 1]] + 1)  # dp[j]：不选i，dp[j - coins[i - 1]] + 1：选i；正序遍历就能复选
        return dp[amount] if dp[amount] < float('inf') else -1


if __name__ == '__main__':
    sol = Solution()
    coins = [1, 2, 5]
    change = 11
    print(sol.coinChange(coins, change))





