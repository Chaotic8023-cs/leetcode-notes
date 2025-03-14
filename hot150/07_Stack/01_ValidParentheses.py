# 20
from typing import *

"""
每次遇到closing bracket，需要和最近的opening进行配对
所以用stack，每次匹配成功，把这个opening pop掉，然后继续即可。
"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


class Solution:
    def isValid(self, s: str) -> bool:
        # valid pairs of parentheses
        vp = {'(': ')', '[': ']', '{': '}'}
        stack = Stack()  # storing opening brackets
        for c in s:
            if c in vp:  # if c is one of starting brackets
                stack.push(c)
            else:
                # check if the popped (opening) match the current char (closing)
                if stack.is_empty() or vp[stack.pop()] != c:
                    return False
        # when match done, stack should be empty!
        return True if stack.is_empty() else False


if __name__ == '__main__':
    s = "()[]{}"
    sol = Solution()
    print(sol.isValid(s))
