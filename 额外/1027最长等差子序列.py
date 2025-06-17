from typing import *
from collections import *


"""
自己写的dp

1. dp数组下标含义：
dp[i]为一个字典，dp[i][x]表示以下标i为结尾的差为x的等差子序列长度-1（没有算这个等差子序列的首个元素），即差为x的等差子序列[..., nums[i]]的长度-1
    -1是因为等差子序列开头第一个没算上，例如：
        [1, 3, 5]中，i = 1，j = 0，此时nums[j]的字典全是0，所以我们先算diff = nums[i] - nums[j] = 2，然后更新
        nums[1][diff] = nums[0][diff] + 1，因为此时nums[0][diff]为0，但等差序列为[1, 3]，所以会更新为0 + 1 = 1
        但实际上长度为2，我们只需最后返回ans + 1即可。
        
2. 递推公式：
为了效率，每次更新字典中以某个x为差的等差数列长度的时候就更新一次ans。
因为最后求的时最长子序列，所以对于每个下标i，我们需要遍历i前面的所有下标j：
    1> 假设当前的等差子序列最后两个元素就是nums[j]和nums[i]，那么当前等差子序列的差就是
        diff = nums[i] - nums[j]
    2> 因为nums[j][diff]记录着以diff为差且以nums[j]结尾的等差子序列长度-1，给这个序列加上nums[i]后，使用和最长递增子序列一样的套路：
        dp[i][diff] = max(dp[i][diff], dp[j][diff] + 1)
        此时dp[i][diff]表示：以i为结尾差为diff的等差子序列的长度-1
            注意：dp数组中记录的长度始终是真实子序列长度-1
    3> 更新ans
        ans = max(ans, dp[i][diff])
    注意：由于dp中始终记录的是没算上第一个元素的子序列长度，所以只需最终返回时加上1即可

3. 初始化：每个位置i用默认的defaultdict(int)即可，不需要初始化 
    defaultdict(int)默认返回0，所以就会不算上等差子序列的第一个元素，见上
4. 遍历顺序：正序遍历即可

补充：其实在更新dp[i][diff]时，可以直接用：dp[i][diff] = dp[j][diff] + 1，而不用max，因为i是从前往后遍历的，j < i，因此对于一个i，
j从0遍历到i时每次diff都不一样，也就是说只会第一次给 dp[i][diff] 赋值，不会存在 dp[i][diff] 被赋值两次的情况，所以不同于最长递增子序列，
这里不用max恰好能work。但是为了方便记忆，还是记和最长递增子序列一样的方式，即取max。
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
                同最长递增子序列的思想：
                    dp[i][diff]：以i为结尾差为diff的等差子序列的最大长度 = max(dp[i][diff], dp[j][diff] + 1)
                    注意，因为 defaultdict 初始化为0，所以等差序列开头的一个数字没算上，所以dp数组中永远都是真实的等差子序列长度-1！
                """
                dp[i][diff] = max(dp[i][diff], dp[j][diff] + 1)
                # 每次更新以diff为差的等差序列长度时，就更新一次ans，这样最后直接就能返回最长的序列长度，不用再遍历了
                ans = max(ans, dp[i][diff])
        return ans + 1  # 由于没算序列开头，所以最后+1

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
                dp[i][diff] = max(dp[i][diff], dp[j][diff] + 1)  # 其实因为遍历j时每次diff都不一样，所以dp[i][diff]只会被更新一次，所以这里直接写成 dp[i][diff] = dp[j][diff] + 1 也可以！
                ans = max(ans, dp[i][diff])
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [9, 4, 7, 2, 10]
    print(sol.longestArithSeqLength(nums))






