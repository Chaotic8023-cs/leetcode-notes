from typing import *


"""
创建一个nums1的哈希表，再对nums2中的每个数字看在nums1中出没出现过。
也可以直接用python的set取交集即可。
"""
class Solution:
    # 用字典
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ht = {}
        for num in nums1:
            ht[num] = ht.get(num, 0) + 1
        ans = []
        for num in nums2:
            if num in ht:
                ans.append(num)
                del ht[num]  # 如果出现过我们就删除，这样之后遇到重复的就不用再检查一遍
        return ans

    def intersection1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))  # 两个set的交集


