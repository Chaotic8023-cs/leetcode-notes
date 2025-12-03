from typing import *

"""
解法：动态规划

含义：dp[i][j] = 以 arr[i] 和 arr[j] 为最后两个数的最长fib子序列长度
递推公式：arr[i] + arr[j] == arr[k] -> dp[j][k] = dp[i][j] + 1
初始化：因为fib子序列至少要3个数，所以不用初始化，全0即可
"""
class Solution:
    """
    naive版：三个for循环，注意要先定k，j才能定，因为j必须在中间！
    会超时！！！
    """
    def lenLongestFibSubseq_naive(self, arr: List[int]) -> int:
        """
        dp[i][j] = 以ij为最后两个数的最长fib序列长度
        arr[i] + arr[j] == arr[k] -> dp[j][k] = dp[i][j] + 1
        """
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        max_len = 0
        for i in range(n):
            for k in range(i + 2, n):
                for j in range(i + 1, k):
                    if arr[i] + arr[j] == arr[k]:
                        dp[j][k] = max(dp[j][k], dp[i][j] + 1)
                        max_len = max(max_len, dp[j][k])
        # 因为第一次找到长度3的fib子序列时，dp[j][k]更新成了1，少算前面两个（此时dp[i][j]是0），所以最后要+2
        return max_len + 2 if max_len != 0 else 0
    
    """
    改进：空间换时间，将第三层for循环换成哈希表

    将遍历找j改为直接通过arr[j]的值（arr[k] - arr[i]）来找j的下标，当找到的j下标在ik中间时，则满足条件。
    """
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        mapping = {v: k for k, v in enumerate(arr)}  # 记录 arr[i]: i 索引
        max_len = 0
        for i in range(n):
            for k in range(i + 2, n):
                if arr[k] - arr[i] in mapping:
                    j = mapping[arr[k] - arr[i]]
                    if j > i and j < k:
                        dp[j][k] = max(dp[j][k], dp[i][j] + 1)
                        max_len = max(max_len, dp[j][k])
        return max_len + 2 if max_len != 0 else 0




