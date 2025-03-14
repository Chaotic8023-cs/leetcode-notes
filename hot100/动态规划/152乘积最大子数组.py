from typing import *


"""
动态规划：
dp_max[i]：表示以i结尾的子数组的最大乘积
dp_min[i]：表示以i结尾的子数组的最小乘积
为什么还要个dp_min呢？例如[5,6,−3,4,−3]，因为可以负负得正，所以最大子数组乘积就是所有乘起来，如果用#53最大子数组和的方式做，就会忽略负负得正。
递推公式：
    1. dp_max[i] = max(nums[i], dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i])
        1> nums[i]：即子数组长度为1，它本身，思想同#53，如果前面是负贡献，则不选前面
        2> dp_max[i - 1] * nums[i]：nums[i]可能为为正数，所以乘上以i-1结尾的最大乘积后可能回变得更大
        3> dp_min[i - 1] * nums[i]：nums[i]可能为负数，所以乘上i-1结尾的最小乘积后可能负负得正变得更大
    2. dp_min[i] = min(nums[i], dp_min[i - 1] * nums[i], dp_max[i - 1] * nums[i])
        1> nums[i]：同理
        2> dp_min[i - 1] * nums[i]：nums[i]可能为为正数，所以乘上以i-1结尾的最小乘积后可能回变得更小
        3> dp_max[i - 1] * nums[i]：nums[i]可能为负数，所以乘上i-1结尾的最大乘积后可能变得更小
初始化：都初始化dp数组下标0为nums[0]即可
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp_max = [0] * n
        dp_min = [0] * n
        dp_max[0] = dp_min[0] = nums[0]
        for i in range(1, n):
            dp_max[i] = max(nums[i], dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i])
            dp_min[i] = min(nums[i], dp_min[i - 1] * nums[i], dp_max[i - 1] * nums[i])
        return max(dp_max)



if __name__ == '__main__':
    sol = Solution()
    nums = [-2,3,-4]
    print(sol.maxProduct(nums))


