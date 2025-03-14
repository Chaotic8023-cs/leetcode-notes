# 17
from typing import *


class Solution:
    def __init__(self):
        self.ans = []
        self.mapping = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
                        '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                        '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits: str) -> List[str]:
        self.backtrack([], digits)
        return self.ans

    def is_valid(self, partial, digits):
        return len(partial) == len(digits) and len(digits) != 0

    def backtrack(self, partial, digits):
        if self.is_valid(partial, digits):
            self.ans.append(''.join(partial))
        else:
            for c in self.get_candidates(partial, digits):
                partial.append(c)
                self.backtrack(partial, digits)
                partial.pop()

    def get_candidates(self, partial, digits):
        if digits:
            return self.mapping[digits[len(partial)]]
        else:
            return []

    # 解法2: 一次遍历，每个数字对应的所有数字与前面所有结果进行组合
    def letterCombinations1(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = [""]
        for i in digits:
            s = d[int(i) - 2]
            ans = [a + b for a in ans for b in s]
        return ans


if __name__ == '__main__':
    digits = "23"
    sol = Solution()
    print(sol.letterCombinations1(digits))
