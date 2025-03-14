# 169
from typing import *

"""
摩尔投票法:
major，count代表当前的majority和（抵消过）的票数。
遍历数组，若遇到和major相同的则票数加1，不同的则减去1（抵消），
若当前count为0，说明major的所有的票被抵消完了，则需更新major。

因为题目中说input一定存在majority，所以不用第二次遍历去检查
major的count是否大于n/2.
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major, count = 0, 0
        for num in nums:
            if count == 0:
                major = num
                count += 1
            else:
                count += 1 if num == major else -1
        return major


if __name__ == '__main__':
    nums = [2, 2, 1, 1, 1, 2, 2]
    sol = Solution()
    print(sol.majorityElement(nums))
