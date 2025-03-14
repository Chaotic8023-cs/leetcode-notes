from typing import *


"""
摩尔投票法：因为一定存在一个多数元素（count > n / 2），那么我们遍历一遍数组，如果两个数不相同则直接抵消，那么最后剩下的一定是最多的那个数。
具体实现方法：初始化curr和count，遍历数组：
    1. 如果count == 0：则curr就设为当前元素，且count = 1
    2. 如果当前有count，则看当前num是否为curr，不是则抵消（count -= 1），是则count += 1
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = 0
        count = 0
        for num in nums:
            if count == 0:
                curr = num
                count = 1
            else:
                count += 1 if num == curr else -1  # 相同+1不同-1（抵消）
        return curr



