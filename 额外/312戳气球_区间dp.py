from typing import *



"""
1. dp数组含义：dp[i][j] 表示 开区间 (i, j) 内（不包括 i 和 j）所有气球被戳破后可获得的最大金币
2. 初始化：默认为0即可
3. 状态转移：
    设 k 是 (i, j) 中  ！最后一个！  戳破的气球：
        dp[i][j] = max(dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j])
            - dp[i][k]：先戳 (i, k) 之间的所有气球
            - dp[k][j]：再戳 (k, j) 之间的所有气球
            - nums[i] * nums[k] * nums[j] 是 k 被最后戳破时的得分（因为两侧端点的气球还存在）
    即：对于排列[i, ..., k, ..., j]，开区间(i, j)上，我们假设下标k为最后一个被戳爆的气球，那么(i, j)上最高得分为
        k两侧的区间的最高得分，即dp[i][k]和dp[k][j]，加上最后被戳爆的气球k的得分，即nums[i] * nums[k] * nums[j]
        
补充：为什么区间长度 length 是 [2, n - 1]（注意，range(2, n)中n取不到）？
例如 nums = [3, 1, 5, 8]，在两端补了两个1后变成 [1, 3, 1, 5, 8, 1]，我们最后求的是开区间(0, n - 1)，此时n是6，包含了两端的1，所以开区间
包含了原nums的所有数！于是，最长的区间长度就是 n-1，因为left的起始位置是0，加上 n-1=5 后区间刚好就是最大的 (0, 5)，并没有越界！
"""
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]  # 首尾+1，方便处理越界
        n = len(nums)  # 这里n是首尾补1了后的长度
        dp = [[0] * n for _ in range(n)]
        # 遍历区间长度：指left + 多少能得到right。最短为2，即只有一个元素
        for length in range(2, n):
            # 遍历区间左端点
            for left in range(n - length):
                right = left + length  # 根据左端点及区间长度，得到右端点
                # 遍历最后一个戳破的位置k
                for k in range(left + 1, right):  # 戳气球的位置是开区间内部
                    score = dp[left][k] + nums[left] * nums[k] * nums[right] + dp[k][right]
                    dp[left][right] = max(dp[left][right], score)
        # 最终返回开区间(0, n - 1)，即区间内是所有气球，两个端点是补的1
        return dp[0][n - 1]






