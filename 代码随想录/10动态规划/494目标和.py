from typing import *

"""
01背包变种：装满背包有多少种装法？(物品和背包容量都从0开始)

设前面应该添加+的子数组的和为p，前面应该添加-的子数组的和为n，则p + n = sum，p - n = target
把n = sum - p带入到后面的式子中我们就能得到p - (sum - p) = target，即p = (sum + target) / 2
因为sum和target固定，则p就能算出来，即应当为正数的子数组和确定。我们又知道p和n的子数组的和都应该为整数，
所以如果上式不能整除，即p算出来不是整数，则无法找到答案. 还有一种情况就是整个数组的和都比target的绝对值小，
说明全选+（或-）都不能凑成target，也无法找到答案。

所以问题就转化为背包容量为(sum + target) / 2的背包，装满它一共有多少种情况：
1. dp数组下标含义：dp[i][j]表示选前i个物品装满容量为j的背包一共有几种选择（注意，这里物品和背包容量都从0开始！）
2. 递推公式：dp[i][j] = dp[i - 1][j] + dp[i - 1][j - weight[i - 1]]（01背包+爬楼梯）
    和01背包类似，有两种选择，即选物品i和不选物品i，但这里dp数组含义是方法的数量，所以又和爬楼梯类似，方法为不选和选物品i的方法数之和：
        1. 不选物品i，则方法数等于不含物品i且容量不变的方法数，即dp[i - 1][j]
        2. 选物品i，则方法数等于不含物品i且容量小了物品i的重量的方法数，即dp[i - 1][j - weight[i - 1]]
    不选和选物品i的方法合起来就是最终的方法数。
3. 初始化：dp[0][0] = 1，没物品且背包容量为0有1种放法，为了满足递推公式而设置，硬记即可
4. 遍历顺序：和普通01背包一样，2d版本都正正序即可，1d版本物品正序背包容量倒序
"""
class Solution:
    # 1D版本，记这个
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if abs(target) > sum(nums):  # |target|比sum(nums)都大了，答案不存在
            return 0
        if (target + sum(nums)) % 2 == 1:  # 正数子数组的和（应当为整数）算出来不是整数，所以答案不存在
            return 0
        # 初始化
        capacity = (target + sum(nums)) // 2  # 背包容量就是正数之和，我们要看和为capacity一共有几种方法
        weight = nums
        dp = [0] * (capacity + 1)
        dp[0] = 1  # 不同于普通01背包！
        n = len(nums)
        for i in range(n):  # 物品：1d可以直接从第一个物品开始遍历，index变回普通01背包中常用的0开始
            for j in range(capacity, weight[i] - 1, -1):  # 背包容量：同普通01背包1d版本
                # 爬楼梯+01背包：不选选物品i：dp[j]个方法，选物品i：dp[j - weight[i]]个方法，最后方法总数就是选和不选的方法个数之和
                dp[j] = dp[j] + dp[j - weight[i]]
        return dp[capacity]


    # 2d版
    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        if abs(target) > sum(nums):  # |target|比sum(nums)都大了，答案不存在
            return 0
        if (target + sum(nums)) % 2 == 1:  # 正数子数组的和（应当为整数）算出来不是整数，所以答案不存在
            return 0
        # 初始化
        capacity = (target + sum(nums)) // 2  # 背包容量就是正数之和，我们要看和为capacity一共有几种方法
        weight = nums
        n = len(nums)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        # 遍历
        for i in range(1, n + 1):
            for j in range(capacity + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= weight[i - 1]:
                    dp[i][j] += dp[i - 1][j - weight[i - 1]]  # 求方法个数：不选和选的方法数之和
        return dp[n][capacity]



if __name__ == '__main__':
    sol = Solution()
    nums = [0,0,0,0,1]
    target = 1
    sol.findTargetSumWays(nums, target)


