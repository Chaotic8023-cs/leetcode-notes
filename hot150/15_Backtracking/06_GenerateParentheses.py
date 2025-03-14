# 22
from typing import *
from collections import Counter


class Solution:
    def __init__(self):
        self.ans = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.backtrack([], n)
        return self.ans

    def is_goal(self, partial, n):
        return len(partial) == 2*n

    def get_poss(self, partial, n):
        # empty, only '('
        if len(partial) == 0:
            return ['(']
        freq = Counter(partial)
        # starting parenthesis used up, only ')'
        if freq['('] == n:
            return [')']
        avail = []
        # as long as '(' is not used up, then it's possible, no mater the previous one
        if freq['('] < n:
            avail.append('(')
        # as long as there are still starting parentheses needs to be closed
        # ')' is possible, no mater the previous one
        if freq['('] > freq[')']:
            avail.append(')')
        return avail

    def backtrack(self, partial, n):
        if self.is_goal(partial, n):
            self.ans.append(''.join(partial[:]))
        else:
            for i in self.get_poss(partial, n):
                partial.append(i)
                self.backtrack(partial, n)
                partial.pop()


if __name__ == '__main__':
    n = 3
    sol = Solution()
    print(sol.generateParenthesis(3))
