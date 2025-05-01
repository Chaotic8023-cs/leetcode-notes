from typing import *


"""
1. dp数组下标含义：dp[i]指以i为结尾（包含）的最长递增子序列的长度
2. 递推公式：对于i前面每个下标j，如果nums[i] > nums[j]，则当前的小标i就能加到子序列中，所以就是dp[j] + 1。我们取最大的那个值
3. 初始化：所有下标默认最短的就是1，因为它自己就算一个！
4. 遍历顺序：正序即可

注意，最后返回要取整个dp的max，因为dp数组含义时以i为结尾的，但最终最长的子序列不一定就包含数组最后一个元素，所以要取max(dp)！
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # 初始化
        dp = [1] * n  # 每个元素本身就是一个递增子序列，所以最短都是1！
        # 遍历
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)  # 因为我们要取前面所有下标中最大的那个+1，所以要一直取max！
        return max(dp)  # 最长的严格递增子序列的结尾不一定就是数组最后一个元素！

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



