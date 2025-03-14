from typing import *


"""
运用XOR的性质，两个相同的数XOR会抵消变成0，所以我们把nums中所有数都XOR一下，出现两次的数就会全部抵消，最后就是出现1次的数和0进行XOR，也就是它本身。
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans




