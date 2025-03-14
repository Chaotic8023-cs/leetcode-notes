# 26
from typing import *


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0  # number of unique nums
        for i in range(len(nums)):
            if k == 0 or nums[i] != nums[k-1]:  # see an unique num
                # since sorted, so only need to check if current num
                # is a duplicate of the previous unique num at num[k-1]
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    sol = Solution()
    print(sol.removeDuplicates(nums))
    print(nums)
