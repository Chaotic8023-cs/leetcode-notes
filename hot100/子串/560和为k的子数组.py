from typing import *
from collections import Counter

class Solution:
    """
    前缀和+哈希表：我们用一个哈希表count来记录不同前缀和出现的次数，初始化时和为0的有1个（为了后面的计算）。
    前缀和公式为：s[i, j] = ps[j] - ps[i - 1] = k，移项后得：ps[j] = k + ps[i - 1]，也就是说如果当前的前缀和ps为p[j]，
    那么前面如果出现了另一个前缀和ps[i - 1] = ps[j] - k的话，那么中间部分的和[i, j]就是k。根据此发现，我们在统计前缀和的个数时，当前
    的前缀和为s（对应ps[j]），就可以知道如果s-k的前缀和（对应ps[i - 1]）出现过，即count[s - k] > 0，那么就说明中间部分的和（对应s[i, j]）
    为k。
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = Counter({0: 1})  # count[s] = n，和为s的子数组右n个
        ans = 0
        s = 0
        for num in nums:
            s += num
            ans += count[s - k]  # 相当于中间部分的和为k的个数，即s[i,j] = k的个数
            count[s] += 1
        return ans


    """
    前缀和朴素版（会超时）：nums[i,j]（左闭右闭）的和就是[0,j]的和减去[0,i-1]的和，所以我们可以在暴力的基础上用前缀和进行快速计算，但是还是超时！
    """
    def subarraySum_naive(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]  # 1-index
        s = 0
        for num in nums:
            s += num
            prefix_sum.append(s)
        ans = 0
        n = len(nums)
        # [i,j]的和，左闭右闭
        for i in range(n):
            for j in range(i, n):
                if prefix_sum[j + 1] - prefix_sum[i] == k:  # 因为是1-index，所以j要加1，但前面的因为要减去[0,i-1]的和，i是loop index所以是0-index，相当于自动减1了
                    ans += 1
        return ans



