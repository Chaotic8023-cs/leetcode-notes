from typing import *

"""
等效于01背包问题：
其实就是把石头分成两堆，这两堆和尽可能相似，也就是说这两堆的和尽可能等于一半，这样它们粉碎之后一定就剩了 total - 2 * sum。
所以我们这里capacity就是sum(stones) // 2，向下取整因为石头是根据小的那个进行抵消的。

这里算出来的能装的重量（dp[n][capacity]）也就是最后要抵消掉的那部分：因为capacity是整除2，向下取整，所以背包装的就是把重量较小的那部分
石头重量最大化，这样就最大化了一共抵消的2 * dp[n][capacity]的重量，使得剩下的重量最小
（背包装的石头重量 <= s // 2，所以它和剩下的石头进行抵消一定一共抵消2 * dp[n][capacity]的重量）。
"""
class Solution:
    # 1d版本背包，物品 = 背包容量 = stones
    def lastStoneWeightII(self, stones: List[int]) -> int:
        capacity = sum(stones) // 2  # 背包容量为一半，我们要尽可能的填满这一半
        dp = [0] * (capacity + 1)
        for i in range(len(stones)):  # 物品正序
            for j in range(capacity, stones[i] - 1, -1):  # 背包容量倒序
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        return sum(stones) - 2 * dp[capacity]

    # 2d版本背包
    def lastStoneWeightII1(self, stones: List[int]) -> int:
        capacity = sum(stones) // 2
        weight = value = stones
        n = len(stones)
        # 初始化：物品前面多加一行，也就是第一行是选0个物品，这样初始化就直接全0即可
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]
        # 遍历：第一个物品对应的是index 1，所以访问weight和value就得i-1
        for i in range(1, n + 1):
            for j in range(capacity + 1):
                if j < weight[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i - 1]] + value[i - 1])
        return sum(stones) - 2 * dp[n][capacity]




