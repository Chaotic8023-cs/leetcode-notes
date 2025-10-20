from typing import *
from bisect import bisect_left


"""
bisect_left(arr, v) 返回 v 应该插入的位置的下标，保证插入后列表依然有序。如果 v 已经存在，会插入到它左边（即最左边的合适位置）。

本题求的是：在一个数组中，有多少对 (i, j) 满足 i < j 且 nums[i] > nums[j]，也就是说，对于每个数字，统计它前面有多少个数字比它大。
而 bisect_left(arr, v) 由于返回的是v插入的下标，所以也就是v左边比它小的数有几个；但是本题要找的是左边比它大的数，所以我们取反，存负数即可，
也就是将 “找有多少个prev > x” 转换成了 “找有多少个 -prev < -x”。
于是就有了本题的解法：维护一个已经遍历过的数的有序列表 q，对于每个新数 v，看在 q 里有多少个数比 v 大。

补充：
为什么需要q：因为 bisect_left要求数组有序，所以我们要将已经遍历过的数维护成一个有序数组
"""
class Solution:
    def reversePairs(self, record: List[int]) -> int:
        q = []  # 维护一个有序的遍历过的数
        ans = 0
        # 遍历每个数，统计它左边有几个比它大的，然后插入到q中
        for v in record:
            i = bisect_left(q, -v)
            ans += i
            q.insert(i, -v)  # 优化：q[i:i] = [-v]，这样就没有函数调用，而是只有切片，会变快不少
        return ans

