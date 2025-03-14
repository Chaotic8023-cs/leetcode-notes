# 918
from typing import *


class Solution:
    # 分开算max和min subarray sum，不efficient
    def maxSubarraySumCircular1(self, nums: List[int]) -> int:
        """
        分两种情况：
        1. max subarray没有wrap around，则为一般的kadane

        2. max subarray wrap around了，则为array的sum减去min subarray的sum，原因如下：
        wrap的情况下，中间skip掉的那部分（即整个array中除了max subarray剩下的部分）一定是min subarray
        我们可以用proof by contradiction：
        假设我们的array是 [A A A B C C C D A A A A A]
        其中max subarray是A的部分，即从array中的A到结尾然后wrap到开头3个A
        剩下的部分[B C C C D]，假设它不是min subarray，则说明我们可以（从两头）去掉一个正数使得剩下的这个subarray的sum更小
        即[C C C D]或[B C C C]拥有更小的sum。这样就contradiction了，因为max subarray可以加上这个去掉的正数变得更大
        即[A A A A A A A A B]或[D A A A A A A A A]才是真正的max subarray
        所以原array中去掉wrap around的max subarray剩下的就是min subarray，我们可以用普通kadane把max换min来求出

        当然还有一个edge case，即原array中全是负数，那么wrap around的情况下，sum减去min subarray sum为0，
        因为此时min subarray sum就是整个array。这个情况下返回最大的那个负数即为max subarray sum（直接返回普通kadane的结果即可）
        """
        max_sum = cur_max = nums[0]
        for x in nums[1:]:
            cur_max = max(cur_max, 0) + x
            max_sum = max(max_sum, cur_max)

        min_sum = cur_min = nums[0]
        for x in nums[1:]:
            cur_min = min(cur_min, 0) + x
            min_sum = min(min_sum, cur_min)

        # 如果array里全是负数，则sum_arr - min_sum为0不对，应返回array里最大的那个负数，即max_sum
        if max_sum < 0:
            return max_sum
        # 正常情况下两种情况，一种是不wrap的subarray，即一般的kadane；第二种是wrap around了，即sun_arr-min_sum
        return max(max_sum, sum(nums)-min_sum)

    # O(1) space: 就是一次遍历，同时算array sum和max/min subarray sum
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        sum_arr = max_sum = cur_max = min_sum = cur_min = nums[0]
        for x in nums[1:]:
            sum_arr += x  # array sum
            # max subarray sum
            cur_max = max(cur_max, 0) + x
            max_sum = max(max_sum, cur_max)
            # min subarray sum
            cur_min = min(cur_min, 0) + x
            min_sum = min(min_sum, cur_min)
        # 如果array里全是负数，则sum_arr - min_sum为0不对，应返回array里最大的那个负数，即max_sum
        if max_sum < 0:
            return max_sum
        # 正常情况下两种情况，一种是不wrap的subarray，即一般的kadane；第二种是wrap around了，即sun_arr-min_sum
        return max(max_sum, sum_arr - min_sum)


if __name__ == '__main__':
    sol = Solution()

