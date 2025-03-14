from typing import *


"""
滑动窗口（自己写的）：
维护一个滑动窗口[i,j]，每次以i为第一个元素，以前两个元素的差作为当前等差数列的差，进行搜索（右移j），每有符合的子数组且长度>=3则总数+1。
本循环找完后，下一个循环窗口起始位置i右移一格，重新开始搜索。
"""
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, 1  # 窗口的左右指针
        ans = 0
        while j < n:
            # 统计前两个元素的差作为当前等差数列的差
            diff = nums[j] - nums[i]
            j += 1
            # 统计以i起始的所有等差数列
            while j < n and nums[j] - nums[j - 1] == diff:
                j += 1
                if j - i >= 3:  # ans计数写在while里面，因为我们要统计所有子数组。例如[1,2,3,4], i = 0时，j=3（对应[1,2,3]）和j=4[1,2,3,4]都要统计！
                    ans += 1
            # 窗口起始点仅右移一格，因为我们要找所有的子数组，所以以i += 1作为一下个循环的第一个元素，j = i + 1为第二个元素！
            i += 1
            j = i + 1
        return ans






