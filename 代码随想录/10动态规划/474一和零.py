from typing import *


"""
01背包变种：多个维度的背包（即不同种类的容量）
1. dp数组下标含义：dp[i][j][k]表示选前i个元素，最多j个0和k个1的最大子集元素个数（也就是价值，此时单个物品价值为1）
2. 递推公式：dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - c1][k - c2] + 1)
    同普通01背包，只是此时weight变成两个维度了，所以只要当前的物品的其中一个“重量”超了对应的capacity维度，就不能选当前物品了
    3. 初始化：同普通01，此时物品有额外的选0个的维度所以全部初始化为0即可
4. 遍历顺序：正序遍历，同普通01背包
"""
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 两个不同的capacity
        capacity1, capacity2 = m, n
        # 初始化： 全0，同普通01背包，外加选0个物品的一行
        dp = [[[0] * (capacity2 + 1) for _ in range(capacity1 + 1)] for _ in range(len(strs) + 1)]
        # 遍历
        for i, s in enumerate(strs, 1):  # 从index 1开始，因为我们物品维度从0开始，所以第一个物品对应的就是index 1
            c1, c2 = s.count('0'), s.count('1')  # 两个不同的“重量”
            for j in range(capacity1 + 1):
                for k in range(capacity2 + 1):
                    dp[i][j][k] = dp[i - 1][j][k]  # 不选当前物品
                    if j >= c1 and k >= c2:  # 选当前物品，此时两个capacity的维度上都要减去当前物品在对应维度上的“重量”
                        # 因为我们要求最大的子集，所以value就设置为1，那么最后value最大也就是子集中元素最多
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - c1][k - c2] + 1)
        return dp[len(strs)][capacity1][capacity2]


    """
    不用enumerate的写法，i就用普通的index写法，从1开始。记这个即可。
    """
    def findMaxForm1(self, strs: List[str], m: int, n: int) -> int:
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs) + 1)]
        for i in range(1, len(strs) + 1):
            s = strs[i - 1]
            zeros, ones = s.count('0'), s.count('1')
            for j in range(m + 1):
                for k in range(n + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    if j >= zeros and k >= ones:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - zeros][k - ones] + 1)
        return dp[len(strs)][m][n]







