from typing import *


"""
XOR：xor是不同为True，相同为False，所以把nums中所有数都XOR起来，两两相同的就会抵消全部变为False，即0，最后和那个单独出现一次的数进行XOR
后就是它本身。
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0  # False XOR 任何数 = 任何数它本身，所以ans初始化成False（0）不影响结果
        for num in nums:
            ans ^= num
        return ans




