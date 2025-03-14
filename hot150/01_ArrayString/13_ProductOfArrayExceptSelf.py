# 238
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    # myver
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp1 = [nums[0]] + [0] * (n-1)
        dp2 = [0] * (n-1) + [nums[-1]]
        ans = [0] * n
        """
        dp1[i]记录从左到i的元素乘积，dp2[i]记录从右到i的元素乘积
        遮样ans[i]就等于它的prefix product * suffix product，即
        i左边的所有元素乘积 * i右边的所有元素乘积：
            ans[i] = dp1[i-1] * dp2[i+1]
        当然开头和结尾需要单独处理，因为它们在最左和最右
        """
        for i in range(1, n):
            dp1[i] = nums[i] * dp1[i-1]
        for i in range(n-2, -1, -1):
            dp2[i] = nums[i] * dp2[i+1]

        ans[0] = dp2[1]
        for i in range(1, n-1):
            ans[i] = dp1[i-1] * dp2[i+1]
        ans[n-1] = dp1[n-2]
        return ans

    # more efficient one
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        left = right = 1  # 分别记录在遍历时当前的prefix product和suffix product
        """
        我们可以在遍历时边计算prefix/suffix product边给ans[i]赋值，即一共两次遍历：
            第一次遍时用left记录prefix product，并同时更新ans[i] = prefix product
        """
        for i in range(n):
            ans[i] = left       # 先更新ans[i]，即不含nums[i]的prefix product: left
            left *= nums[i]     # 再更新left为下一个元素做准备
        for i in range(n-1, -1, -1):  # 同理，从右往左记录suffix product，并同时更新ans[i]
            ans[i] *= right  # 现在ans[i]已经是prefix product了，乘上suffix product即为要的答案
            right *= nums[i]
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    sol = Solution()
    print(sol.productExceptSelf(nums))

