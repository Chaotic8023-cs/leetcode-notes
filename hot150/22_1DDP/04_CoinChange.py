# 322
from typing import *


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount+1)
        dp[0] = 0  # 0快钱需要0个硬币（为了满足那种只需一个硬币就能找零的情况）
        """
        dp[i]代表找i快钱需要的最少硬币
        每次考虑dp[i]时，由于要最少零钱数，所以我们就考虑能否有比i小的加上
        一个硬币来找当前i快钱
        即对于每个硬币面值c，我们看i-c块钱最少需要多少个硬币，
        然后当前i块钱需要的硬币数就 = i-c块需要的 + 1 （这1个硬币就是就是c块， 和i-c加起来就是i块）
        在所有硬币面值里我们找出需要最少的，也就是i-c块找零需要最少的！
        """
        for i in range(1, amount+1):
            possible = []
            for c in coins:
                if i-c >= 0 and dp[i-c] != -1:
                    possible.append(dp[i-c] + 1)
            dp[i] = min(possible) if len(possible) > 0 else -1
            # dp[i] = min((dp[i-c] + 1 for c in coins if i-c >= 0 and dp[i-c] != -1), default=-1)
        return dp[-1]


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    sol = Solution()
    print(sol.coinChange(coins, amount))
