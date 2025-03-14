from typing import *


"""
1. dp数组下标含义：用1-index，dp[i]表示拆分数字i能得到的最大乘积
2. 递推公式：遍历j从1到i-1，因为要拆成>=2个数的和，所以有两种拆法：
    1. 直接拆成两个数：j和i-j，即最后的乘积为j * (i - j)
    2. j不拆，i-j拆，即最后的乘积为j * dp[i - j]（dp[i - j]即数字i-j拆分后最大的乘积）
3. 初始化：dp[2] = 1，2能拆成1+1，所以乘积为1。（dp[0]跳过因为我们用1-index，dp[1]无意义因为要拆分成>=2个数，所以也用不到）
4. 遍历顺序：每个地方需要前面的，所以正序遍历

优化补充：其实拆分的时候j从1遍历到(i // 2 + 1)就可以，因为是对称的，比如说5拆成2 + 3和3 + 2。这个优化可以不用记！
"""
class Solution:
    def integerBreak(self, n: int) -> int:
        # 按1-index算，dp[0]跳过，这样dp几就是数字几
        dp = [0] * (n + 1)
        dp[2] = 1  # 初始化：拆分2的最大乘积为1，即dp[2] = 1（dp[1]无意义，因为要拆分成>=2个数之和，1不能拆成两个）
        for i in range(3, n + 1):  # 从3开始拆分
            for j in range(1, i):
                # 1. 直接拆成两个：j * (i - j)，或拆成j和(i - j)的拆分（即dp[i - j]）
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])  # 注意，max中要有dp[i]，因为dp[i]一直在更新！
        return dp[n]





