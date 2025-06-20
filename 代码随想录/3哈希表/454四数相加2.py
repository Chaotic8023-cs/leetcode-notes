from typing import *


class Solution:
    """
    空间换时间：用一个4层的循环时间会爆炸，所以我们分治，即分别统计看a+b和c+d。这题不需要考虑结果是否重复，所以直接统计和即可，不用考虑index
    1. 先遍历AB数组统计所有a+b的和出现的次数，记录在哈希表t1中
    2. 再遍历CD数组，当前的和为c+d，要使得总和为0，那么我们看0-(c+d)在t1中是否出现，如果有则说明当前的cd能和t1中对应的ab相加最终和为0，
       我们就更新count，加上t1中对应的ab出现的次数即可。
    """
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 统计AB两个数组中所有和出现的次数
        t1 = {}
        for num1 in nums1:
            for num2 in nums2:
                sumAB = num1 + num2
                t1[sumAB] = t1.get(sumAB, 0) + 1
        # 再遍历CD数组，如果 0 - sumCD 在t1中出现，当前的cd和AB中对应的和0 - sumCD加起来等于0，更新count即可
        count = 0
        for num3 in nums3:
            for num4 in nums4:
                sumCD = num3 + num4
                if 0 - sumCD in t1:
                    count += t1[0 - sumCD]  # 当前c+d和对应的a+b和为0，count加上a+b出现的次数
        return count


"""
也可以提前把两个都统计好然后遍历，唯一要注意的是，因为求的是不同下标的个数，所以是乘法原理！
上面的方法中对于nums3和nums4的数我们是一个一个遍历的，所以是等效的。
"""
class Solution1:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cnt1, cnt2 = Counter(), Counter()
        for num1 in nums1:
            for num2 in nums2:
                cnt1[num1 + num2] += 1
        for num3 in nums3:
            for num4 in nums4:
                cnt2[num3 + num4] += 1
        ans = 0
        for x, cnt in cnt1.items():
            if 0 - x in cnt2:
                ans += cnt * cnt2[0 - x]  # 乘法原理：cnt1中的个数 * cnt2中的个数
        return ans






