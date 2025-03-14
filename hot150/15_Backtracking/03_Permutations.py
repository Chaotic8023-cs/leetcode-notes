# 46
from typing import *


class Solution:
    def __init__(self):
        self.ans = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtrack([], nums)
        return self.ans

    def backtrack(self, partial, nums):
        if self.is_valid(partial, nums):
            self.ans.append(partial[:])
        else:
            for i in self.get_poss(partial, nums):
                partial.append(i)
                self.backtrack(partial, nums)
                partial.pop()

    def get_poss(self, partial, nums):
        """
        permutation里组合一样顺序不同也算单独的一种，
        所以就不用考虑前面用过的数字了，只要不在partial里的都行！
        """
        return [i for i in nums if i not in partial]

    def is_valid(self, partial, nums):
        return len(partial) == len(nums)


if __name__ == '__main__':
    nums = [1, 2, 3]
    sol = Solution()
    print(sol.permute(nums))
