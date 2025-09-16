from typing import *
from math import inf


class Solution:
    """
    滑动窗口（也是特殊的双指针）：遍历right，并在curr_sum >= target的条件下尽可能的左移left

    暴力解法中外循环对应初始位置，内循环对应结束位置，为了用一个循环，我们遍历结束位置。
    遍历right，并更新当前的和curr_sum，同时在curr_sum满足条件的时候右移，即尽可能的减少元素，
    当不能减少时，当前的窗口就是end为right的最小子数组。此时我们就可以right右移一位继续遍历，因为右移一位后
    当前的curr_sum会变大，一定满足条件，所以left不断右移是在寻找新right的最小子数组。
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, 0
        ans = float('inf')
        curr_sum = 0
        while right < n:  # 根据end遍历
            curr_sum += nums[right]  # 更新当前的sum，加入end一个元素
            while curr_sum >= target:  # 在curr_sum满足条件的情况下尽可能的缩小窗口（右移left）
                ans = min(ans, right - left + 1)
                curr_sum -= nums[left]
                left += 1
            right += 1
        return ans if ans != float('inf') else 0
    
    # 使用i，j，更直观的双指针
    def minSubArrayLen1(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = inf
        i, j = 0, 0
        curr_sum = 0
        while j < n:
            curr_sum += nums[j]
            while curr_sum >= target:
                ans = min(ans, j - i + 1)
                curr_sum -= nums[i]
                i += 1
            j += 1
        return ans if ans < inf else 0


if __name__ == '__main__':
    sol = Solution()
    target = 7
    nums = [8, 3, 1, 2, 4, 3]
    print(sol.minSubArrayLen(target, nums))
