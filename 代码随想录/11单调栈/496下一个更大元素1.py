from collections import deque
from typing import *


class Solution:
    """
    和739每日温度一个思路，单调递增栈解决。此题直接存元素即可，因为最后需要的是元素而不是下标。
    """
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mStack = deque()  # 此题直接求的是元素本身，所以直接存元素即可
        mapping = {}  # 存nums2中每个元素右边的第一个比它大的元素，因为最后只要找的是nums2的子集（nums1），所以建立mapping以便快速查找
        # 先遍历nums2把nums2中每个元素右边的第一个最大的找到
        for num in nums2:
            while mStack and num > mStack[-1]:
                mapping[mStack.pop()] = num
            mStack.append(num)
        while mStack:
            mapping[mStack.pop()] = -1
        # 再根据mapping快速找到nums2的子集nums1中元素对应的答案
        return [mapping[x] for x in nums1]
