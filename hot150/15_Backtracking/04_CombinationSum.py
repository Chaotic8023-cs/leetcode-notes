# 39
from typing import *


class Solution:
    def __init__(self):
        self.ans = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.backtrack([], candidates, target)
        return self.ans

    def is_valid(self, partial, target):
        return sum(partial) == target

    def get_poss(self, partial, candidates, target):
        if len(partial) == 0:
            return candidates
        else:
            """
            can have repeats, but at least 1 of same elements need to have different frequency
            which means no same combination: [2,2,3] is same as [2,3,2]!
            所以用一种和combination很像的写法，这里选大于等于前面用过的，因为加了等于，所以可以复选
            但是同时保证了没有给相同combination！
            而且，其实candidate不用递增也能正常work！
            """

            return [i for i in candidates if i >= partial[-1] and i + sum(partial) <= target]

    def backtrack(self, partial, candidates, target):
        if self.is_valid(partial, target):
            self.ans.append(partial[:])
        else:
            for i in self.get_poss(partial, candidates, target):
                partial.append(i)
                self.backtrack(partial, candidates, target)
                partial.pop()


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    sol = Solution()
    print(sol.combinationSum(candidates, target))
