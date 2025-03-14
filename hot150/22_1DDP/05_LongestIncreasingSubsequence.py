# 300
from typing import *


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] = longest subsequence end BY nums[i]
        # (nums[i] included at the end of the sequence)
        dp = [1] * (len(nums))
        """
        dp[i]表示 *包含* nums[i]的最长单增子序列
        当dp[i]表示包含他自己的序列长度，我们每次考虑dp[i]的时候，就可以去看它前面
        所有num，如果当前的nums[i]比某个大，说明nums[i]可以放在以那个数为结尾的
        最长单增子序列后面。所以我们在前面找所有比nums[i]小的，找出里面拥有子序列
        长度最长的，然后加1即可.
        
        注意：若仅表示到i的最长单增子列（即dp递增），到dp[i]的时候就无法确定前面到底
        那些属于最长的单增子序列， 也就没法拿当前的值去和序列最后一个比大小了！
        eg: 如果dp[i]表示到nums[i]的最长子序列长度（nums[i]不一定属于子序列）:
        1.
        nums: [4, 10, 4, 3, 8, 9]
          dp:  1,  2, 2, 2,
        我们看8的时候，前面的最长单增子列其实是[4, 10], 我们不知道这个子列到底包含
        哪些，所以没法和这个子列的末尾数字进行比较!
        """
        for i in range(1, len(nums)):
            j = i-1
            while j >= 0:
                if nums[i] > nums[j]:
                    # 如果在前面有比当前数小的num
                    # 则当前数可加到以这个num为结尾的subsequence后面
                    dp[i] = max(dp[i], dp[j]+1)
                j -= 1
        return max(dp)


if __name__ == '__main__':
    nums = [4, 10, 4, 3, 8, 9]
    sol = Solution()
    print(sol.lengthOfLIS(nums))
