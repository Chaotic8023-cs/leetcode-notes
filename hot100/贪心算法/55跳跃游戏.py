from typing import *


"""
我们不考虑每次该跳几步，而是只看当前最远能跳多远，遍历每个下标，只要当前下标在当前最远能跳到的下标之前，就证明当前位置可以达到。
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        n = len(nums)
        curr_max = 0
        while i <= curr_max:
            curr_max = max(curr_max, i + nums[i])  # 每个位置都更新最远能跳到的距离
            if curr_max >= n - 1:  # 如果能到最后一个下标则说明总有一种方法能跳到
                return True
            i += 1
        return False

    """
    for循环也可以，不用看
    """
    def canJump1(self, nums: List[int]) -> bool:
        n = len(nums)
        curr_max = nums[0]
        for i in range(1, n):
            if i <= curr_max:
                curr_max = max(curr_max, i + nums[i])
            else:  # 当前下标超出目前能跳到的最远下标
                return False
        return True




