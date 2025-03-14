from typing import *

"""
等效于01背包问题：
分割成两个子集和相等，其实就是一个容量为sum(nums) // 2的背包，把物品（数字）放进去，看能否刚好放满。
但我们如何判断是否放满呢？在背包问题中，最后求出来的是价值，那么此时我们可以把物品重量和价值都设为nums，
最后只需判断容量为sum(nums) // 2的背包的最大价值是否也是sum(nums) // 2即可！
"""
class Solution:
    # 2D版本
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:  # 和无法二分，则一定不能分割成2个等和数组
            return False
        capacity = sum(nums) // 2
        weight = value = nums
        n = len(nums)  # num_items
        # 初始化：和capacity一样，物品多加一个选0个物品的一行，这样初始化就可以直接全0，下面遍历就从第一个物品开始（对应index 1）
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]
        # 遍历：注意，此时第一个物品对应的时index 1，所以访问weight和value时i都要-1
        for i in range(1, n + 1):  # 物品
            for j in range(capacity + 1):  # 背包容量
                dp[i][j] = dp[i - 1][j]
                if j >= weight[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - weight[i - 1]] + value[i - 1])
        return dp[n][capacity] == capacity  # 看背包容量为capacity的最大价值是否恰好也是capacity，这样剩余没装的“物品”就也是和为capacity的

    # 1D版本滚动数组
    def canPartition1(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target_value = sum(nums) // 2
        dp = [0] * (target_value + 1)  # 只初始化dp[0] = 0，从第一个物品（0）开始遍历（相当于直接从2d中的第2行，即只选第一个物品的那行开始）
        n = len(nums)
        for i in range(n):
            for j in range(target_value, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        return dp[target_value] == target_value







