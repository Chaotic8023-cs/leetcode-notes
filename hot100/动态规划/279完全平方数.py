from typing import *
from math import inf


"""
同#322零钱对换：完全背包变种2:求最少物品个数
这题物品需要自己生成：n的大小就是背包容量，那么所有i ^ 2 <= n的数就是能选的物品
"""
class Solution:
    def numSquares(self, n: int) -> int:
        # 生成所有 <= n的平方数作为候选物品
        i = 1
        num_items = 0
        while i ** 2 <= n:
            num_items += 1
            i += 1
        # 然后按常规完全背包求物品个数做
        dp = [[inf] * (n + 1) for _ in range(num_items + 1)]
        dp[0][0] = 0  # 求最小物品数初始化为0
        for i in range(1, num_items + 1):  # 遍历物品：这时候物品就是i，因为符合条件的数就是[1, num_items]，它们的平方小于n
            for j in range(n + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= i ** 2:
                    dp[i][j] = min(dp[i][j], dp[i][j - i ** 2] + 1)  # 注意，每个i放进背包是要平方的，因为是它们的平方相加！
        return dp[num_items][n]


if __name__ == '__main__':
    sol = Solution()
    n = 1
    print(sol.numSquares(n))



