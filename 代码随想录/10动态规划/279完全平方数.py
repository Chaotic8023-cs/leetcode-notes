from typing import *
from math import inf

"""
和322零钱兑换完全一样，只是候选物品需要自己求出来，都是完全背包求最小物品个数！
"""
class Solution:
    def numSquares(self, n: int) -> int:
        i = 1
        while i ** 2 <= n:  # 统计符合条件的物品（完全平方数）的个数
            i += 1
        num_items, capacity = i - 1, n  # 此时i平方是第一个比n大的，所以候选物品是[1,i - 1]
        dp = [inf] * (capacity + 1)  # 求最少数量则初始化为inf
        dp[0] = 0  # 求最小数量dp[0] = 0
        for i in range(1, num_items + 1):  # 一共num_items个数，刚好从1开始，所以每个i就是候选数本身，可以直接用!
            for j in range(i ** 2, capacity + 1):  # 1d时正序 -> 可以复选
                dp[j] = min(dp[j], dp[j - i ** 2] + 1)
        return dp[capacity]

    """
    2d
    """
    def numSquares_2d(self, n: int) -> int:
        # 统计符合条件的物品（完全平方数）的个数
        i = 1
        while i ** 2 <= n:  # 此时i平方是第一个比n大的，所以候选物品是[1,i - 1]
            i += 1
        num_items, capacity = i - 1, n
        dp = [[inf] * (capacity + 1) for _ in range(num_items + 1)]  # 求最小物品个数全部初始化为inf
        dp[0][0] = 0  # 求最小物品个数dp[0][0] = 0
        for i in range(1, num_items + 1):  # 一共num_items个数，刚好从1开始，所以每个i就是候选数本身，可以直接用!
            for j in range(capacity + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= i ** 2:  # 此时容量能容下当前数的平方
                    dp[i][j] = min(dp[i][j], dp[i][j - i ** 2] + 1)  # 注意完全背包用dp[i]（能复选！）！
        return dp[num_items][capacity]


if __name__ == '__main__':
    sol = Solution()
    n = 13
    print(sol.numSquares_2d(n))



