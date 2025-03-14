# 80
from typing import *


"""
可以扩展至相同的数字最多保留k个:
因为最多出现k次， 则nums中前k个可以直接保留。
对于后面的数字，与已保留的倒数第k个比较，不同则留下，相同则跳过
因为是sorted，所以只用看倒数第k个，之间的要么相同要么不同，
因为最多保留k个，所以最坏情况就是倒数k个全都相同！

如果当前的数都等于保留的倒数第k个了，就说明中间的也一定都是这个数，
即已经出现了k次了，需要跳过。
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        # 因为最多保留两个，如果当前的数等于保留的部分的倒数第二个的话，
        # 中间那个一定也是这个数，因为nums是sorted
        for num in nums:
            if k < 2 or num != nums[k-2]:
                nums[k] = num
                k += 1
        return k


if __name__ == '__main__':
    nums = [1, 2, 2]
    sol = Solution()
    print(sol.removeDuplicates(nums))
    print(nums)
