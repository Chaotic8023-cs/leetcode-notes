from typing import *


"""
动态规划：
dp[i]：以i为结尾（包含）的最长递增子序列的长度
递推公式：遍历所有i前面的下标j，如果nums[i] > nums[j]，则以j结尾的递增子序列就可以加上nums[i]。对于所有前面的位置j，我们取max。
初始化：一开始每个位置最长的递增子序列就是它自己，即长度 = 1
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)



"""
变种：返回最长的子序列本身
方法是dp中每个位置额外记录当前最长的子序列。为了优化，我们只记录每个位置的parent下标；同时，为了方便，我们将parent从dp中拆出来。
"""
class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [1] * n
        parent = [-1] * n  # parent[i]记录以i为结尾的最长的子序列中的上一个数的下标，也就是parent下标。初始时都是-1，代表到头了。
        max_len, max_idx = 0, 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:  # 只有以j结尾的最长子序列长度+1 > 当前以i结尾的最长子序列长度 时，才更新（由于普通版只需关心长度，所以用max就行，这里我们还得记录parent下标）
                        dp[i] = dp[j] + 1
                        parent[i] = j  # 更新parent下标
            # 在循环的时候就记录最长子序列的长度及其对应结尾的下标i，免得最后还得遍历查找
            # 注意：只能在把前面的位置j遍历完后更新max_len，因为遍历完j后以下标i为结尾的最长子序列才确定下来；同时，最长子序列可能出在任何下标i，所以每个i处都得判断一下（同普通版最后取全局的max）。
            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i

        # 最终从max_idx出发，也就是最长递增子序列的最后一个数字的下标，使用parent还原子序列本身
        ans = []
        curr = max_idx
        while curr != -1:
            ans.append(nums[curr])
            curr = parent[curr]
        return ans[::-1]

    # 简洁写法
    def lengthOfLIS1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1, -1] for _ in range(n)]  # dp[i] = [max_len, parent]
        max_len, max_idx = 1, 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = j
                if dp[i][0] > max_len:
                    max_len = dp[i][0]
                    max_idx = i
        ans = []
        curr = max_idx
        while curr != -1:
            ans.append(nums[curr])
            curr = dp[curr][1]
        return len(ans[::-1])







