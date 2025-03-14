from typing import *


"""
使用一个哈希表：m[value] = index，然后遍历数组，每次遇到一个num，那么我么你想找的就是target-num，又因为我们用value做key，所以就可以通过
m[target - num]看是在哈希表内，是的话就直接能得到它的index
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, num in enumerate(nums):
            if target - num in m:
                return [i, m[target - num]]
            m[num] = i





