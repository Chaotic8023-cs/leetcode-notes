from typing import *


"""
由于重复数都出现3次，那么我们从右往左1位1位看，所有数的当前位之和能否被3整除：
    1. 能整除：说明多出来的那个数当前位上是0
    2. 不能整除：说明多出来的那个数当前位上是1
因为python中二进制下int都是2's complement，所以对于最左边的第32位sign bit要单独处理，我们直接硬记ans -= 1 << 31即可。

例子：
如果多出来的数是-5，那么它的二进制（2's complement）表示就是：11111111111111111111111111111011（32位）
在遍历到sign bit之前，我们ans累计到了后31位，也就是1111111111111111111111111111011，即2147483643，
我们看最后1位是1，也就是说单独的这个数是负数，那么我们就 ans -= 1 << 31就刚好变为-5，即在十进制下操作：2147483643 - 2147483648 = -5。
这个操作可以硬记。
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        # 从右往左每次看多出来的那个数第i位是1还是0
        for i in range(32):
            count = sum((num >> i) & 1 for num in nums)  # 统计所有数当前位之和
            if count % 3 != 0:  # 如果不能被3整除，说明多出来的那个数此位上是1
                if i != 31:  # 如果不是sign bit，则给ans对应位上赋上1（当前是从右往左数第i位）
                    ans += 1 << i
                else:  # 当前是从右往左第32位，即sign bit，因为int都是用2‘s complement存储的，此时sign bit是1，说明多出来的这个数是负数。
                    ans -= 1 << 31  # 此时ans是原数2's complement除去sign bit后剩余的部分，它是反转再+1的结果（即非常大的正数），所以我们要调整回去得到真正的负数
        return ans

    # 非位运算方法：nums中所有出现的数的和的三倍 - nums本身的和，就是那个只出现一次的数的两倍
    def singleNumber1(self, nums: List[int]) -> int:
        return (sum(set(nums)) * 3 - sum(nums)) // 2


if __name__ == '__main__':
    sol = Solution()
    nums = [7, 7, 7, -5, 6, 6, 6]
    print(sol.singleNumber(nums))


