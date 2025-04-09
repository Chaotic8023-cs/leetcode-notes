from typing import *
from collections import *


"""
自己写的dp

1. dp数组下标含义：
dp[i]为一个字典，dp[i][x]表示以下标i为结尾的差为x的等差子序列长度-1（没有算这个等差子序列的首个元素），即差为x的等差子序列[..., nums[i]]的长度-1
    -1是因为等差子序列开头第一个没算上，例如：
        [1, 3, 5]中，i = 1，j = 0，此时nums[j]的字典全是0，所以我们先算diff = nums[i] - nums[j] = 2，然后更新
        nums[1][diff] = nums[0][diff] + 1，因为此时nums[0][diff]为0，但等差序列为[1, 3]，所以会更新为0 + 1 = 1
        但实际上长度为2，我们只需在每次更新ans的时候+1就行，dp中一直保留长度-1的定义就行！
        
2. 递推公式：
为了效率，每次更新字典中以某个x为差的等差数列长度的时候就更新一次ans。
因为最后求的时最长子序列，所以对于每个下标i，我们需要遍历i前面的所有下标j：
    1> 假设当前的等差子序列最后两个元素就是nums[j]和nums[i]，那么当前等差子序列的差就是
        diff = nums[i] - nums[j]
    2> 因为nums[j][diff]记录着以diff为差且以nums[j]结尾的等差子序列长度-1，给这个序列加上nums[i]后：
        dp[i][diff] = dp[j][diff] + 1
        此时dp[i][diff]表示：以i为结尾差为diff的等差子序列的长度-1
            注意：dp数组中记录的长度始终是真实子序列长度-1
    3> 更新ans
        ans = max(ans, dp[i][diff] + 1)
        由于dp中始终记录的是没算上第一个元素的子序列长度，所以更新ans时+1就行

3. 初始化：每个位置i用默认的defaultdict(int)即可，不需要初始化 
    defaultdict(int)默认返回0，所以就会不算上等差子序列的第一个元素，见上
4. 遍历顺序：正序遍历即可

"""
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        ans = 0
        for i in range(1, n):
            for j in range(i):
                # 当前的差
                diff = nums[i] - nums[j]
                """
                1. dp[j][diff]：以j为结尾diff为差的等差子序列长度-1
                2. 加上元素i：dp[i][diff] = dp[j][diff] + 1
                3. dp[i][diff]：以i为结尾diff为差的等差子序列长度-1
                    注意，dp数组中永远都是真实的等差子序列长度-1！
                """
                dp[i][diff] = dp[j][diff] + 1
                # 每次更新以diff为差的等差序列长度时，就更新一次ans
                ans = max(ans, dp[i][diff] + 1)
        return ans

    """
    其实defaultdict支持初始化乘默认返回1，如下
    这样dp[i][diff]就表示的时以i为结尾diff为差的等差子序列的真实长度了
    更新ans时就不用+1了！
    """
    def longestArithSeqLength1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(lambda: 1) for _ in range(n)]
        ans = 0
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[j][diff] + 1
                ans = max(ans, dp[i][diff])
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [9, 4, 7, 2, 10]
    print(sol.longestArithSeqLength(nums))






