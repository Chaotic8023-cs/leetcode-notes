# 137
from typing import *


class Solution:
    """
    位运算：
    因为每个数出现3次，除了单独的那个数，所以我们一个bit一个bit看（从右往左）：
        1. 如果所有数第i位上的bit之和能被3整除，说明单独的那个数的第i位为0（因为其它数都出现3次，它们加起来一定能被3整除）
        2. 如果所有数第i位上的bit之和不能被3整除，说明单独的那个数的第i位为1（重复3次的数加起来能被整除，加上这个1就不能了）
    所以我们根据这个一位一位看，如果不能整除则把这位上的1更新到ans上（用|=）
    需要注意的是，题中说可能出现负数，所以我们需要单独处理最左边的sign bit：
        如果在sign bit上不能被3整除，说明这个单独的数这位上是1，即负数
        负数表示为：1 + 2‘s complement（即sign bit加上原始的大小反转再加1）
        此时ans的后31位已经更新完了，真实的结果恰好就是后31位（2‘s complement）的大小减去2^31，即ans -= 1 << 31（硬记即可）

        例子：
        -5表示：5是00000000000000000000000000000101，
        2‘s complement先反转再+1，最后给前面加个sign bit就是11111111111111111111111111111011
        其中除去sign bit的数1111111111111111111111111111011的大小为2147483643
        最终的结果就是2147483643 - 2^31 = -5
    """
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            cnt = sum((num >> i) & 1 for num in nums)  # 所有num的当前bit之和
            if cnt % 3 != 0:
                if i != 31:  # not sign bit
                    ans |= 1 << i
                else:  # sign bit, account for negative value
                    ans -= 1 << 31
        return ans



