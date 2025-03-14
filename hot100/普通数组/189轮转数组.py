from sys import orig_argv
from typing import *


class Solution:
    """
    最简单的方法就是用extra space，下面数组的切片就是创建了额外空间
    """
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums[:] = nums[n - k:] + nums[:n - k]  # 向右轮转k位 = 后k个数 + 前n - k个数

    """
    原地解法（三次反转）：其实就是按上面的思路，先反转整个数组，再反转前k个，最后反转后n - k个。
    """
    def rotate1(self, nums: List[int], k: int) -> None:
        def reverse(nums, l, r):
            i, j = l, r
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j - 1
        n = len(nums)
        k %= n
        reverse(nums, 0, n - 1)  # 1. 反转整个数组
        reverse(nums, 0, k - 1)  # 2. 反转前k个
        reverse(nums, k, n - 1)     # 3. 反转后n - k个


if __name__ == '__main__':
    sol = Solution()
    nums = [-1]
    k = 2
    print(sol.rotate1(nums, k))






