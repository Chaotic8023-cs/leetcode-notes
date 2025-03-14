from typing import *


"""
1. dp数组下标含义：dp[i][j]表示以nums1中以i为结尾（包含），nums2中以j为结尾（包含）的最长重复子数组的长度
2. 递推公式：如果nums1[i] == nums2[j]，则说明分别以i和j结尾的重复子数组长度该+1了，但是上一个状态是什么呢？因为两个数组是绑定的，
    要回退就都回退，所以上一个状态就是dp[i - 1][j - 1]，即两个数组都回退一格的最长重复子数组的长度！
3. 初始化：因为我们定义的ij是以ij为结尾的，且递推公式要前一个状态，所以我们就需要初始化第一行和第一列
    1> 第一行dp[i][0]：表示nums1中以i为结尾和nums2中以第0个元素结尾的最长重复子数组，因为nums2的维度仅1个数字，所以我们只需要看
        nums1[i]是否和nums2[0]相等，相等则说明dp[i][0] = 1
    2> 第一列dp[0][j]：同理，遍历nums2看是否nums2[i]等于nums1[0]
4. 遍历顺序：
"""
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        # 初始化：第一行第一列
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if nums1[i] == nums2[0]:
                dp[i][0] = 1
        for j in range(n):
            if nums2[j] == nums1[0]:
                dp[0][j] = 1
        # 遍历
        for i in range(1, m):
            for j in range(1, n):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1  # 因为子数组是连续的，如果[i-1][j-1]两个字母不相等，则dp[i - 1][j - 1]为0，当前dp[i][j]就相当于从头起步了
                # 不用考虑nums1[i] != nums2[j]的情况，因为子数组是连续的，如果下标ij都不想等，那么以ij为结尾的最长长度一定为0
        # 最后要取全局的最大，因为我们不知道最长重复子数组的结尾分别在哪
        return max([i for sub in dp for i in sub])


if __name__ == '__main__':
    sol = Solution()
    nums1 = [1, 2, 3, 2, 8]
    nums2 = [5,6,1,4,7]
    print(sol.findLength(nums1, nums2))

