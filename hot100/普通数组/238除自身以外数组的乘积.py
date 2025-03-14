from typing import *


class Solution:
    """
    原地解法：和下面过的过程一样，只是边遍历边更新ans：
        1. 正序遍历：
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        # 正序遍历：计算前缀乘积
        pprefix = 1
        for i in range(n):
            ans[i] *= pprefix
            pprefix *= nums[i]
        # 倒序遍历：计算后缀乘积
        psuffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= psuffix
            psuffix *= nums[i]
        return ans
    """
    体检计算前缀和后缀乘积即可。
    """
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = 1
        # 记录前缀和后缀乘积
        p_forward, p_backward = [], []
        for num in nums:
            s *= num
            p_forward.append(s)
        s = 1
        for num in nums[::-1]:
            s *= num
            p_backward.append(s)
        p_backward = p_backward[::-1]  # 反转后p_backward[i]表示nums[i:]的乘积，所以方便使用
        ans = []
        for i in range(n):
            if i == 0:
                ans.append(p_backward[1])
            elif i == n - 1:
                ans.append(p_forward[n - 2])
            else:
                ans.append(p_forward[i - 1] * p_backward[i + 1])
        return ans








