# 77
from typing import *


class Solution:
    def __init__(self):
        self.ans = []

    """ n choose k """
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtrack([], k, n)
        return self.ans

    def backtrack(self, partial, k, n):
        if self.is_valid(partial, k):
            self.ans.append(partial[:])
        else:
            for i in self.get_poss(partial, n):
                partial.append(i)
                self.backtrack(partial, k, n)
                partial.pop()

    def get_poss(self, partial, n):
        """
        partial里有的取不到
        如4choose3
        1开头的有：123，124，134
        2开头的有：234 （就不能用1了，因为combination的话相同组成不同顺序也只算一种！）
        3开头的就没有了，因为12都用过了，只剩4了，不够组成一个3个数的combination了！
        """
        if len(partial) == 0:
            return range(1, n+1)
        else:
            return [i for i in range(partial[-1]+1, n+1)]

    def is_valid(self, partial, k):
        return len(partial) == k


if __name__ == '__main__':
    n = 4
    k = 2
    sol = Solution()
    print(sol.combine(n, k))
