# 136
from typing import *


class Solution:
    """
    位运算：
    异或XOR的性质：
        1. x XOR 0 = x：任何数和0异或是它本身
        2. x XOR x = 0：任何数和它自己异或是0
        3. a XOR b XOR c = c XOR b XOR a：异或有交换律
    所以我们直接把所有nums异或，根据交换律有两个的数都会抵消变为0，最后那个单独的数和0异或就是它自己
    """
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans

