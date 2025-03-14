# 189
from typing import *

"""
eg, [1,2,3,4,5,6,7], k=3
step 1: [7,6,5,4,3,2,1]
step 2: [5,6,7,4,3,2,1]
step 3: [5,6,7,1,2,3,4]
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(i, j):
            # 反转一个array[i:j]
            # 从两头开始每次进行调换
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j - 1

        n = len(nums)
        k %= n  # 求余一下: rotate大于len的次数等同于rotate k % len次
        reverse(0, n - 1)  # 先整个array反转
        reverse(0, k - 1)  # 再反转前k个
        reverse(k, n - 1)  # 再反转剩余(n-k)个

    # 方法二
    def rotate1(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]


if __name__ == '__main__':
    nums = [1]
    k = 0
    sol = Solution()
    sol.rotate1(nums, k)
    print(nums)
