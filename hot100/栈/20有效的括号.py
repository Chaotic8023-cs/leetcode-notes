from typing import *
from collections import deque


"""
栈：栈加左括号，遇到右括号则pop看是否匹配，最后还得看栈里是否还有剩余的未匹配的左括号。
"""
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(': ')', '[': ']', '{': '}'}
        stack = deque()
        for c in s:
            if c == '(' or c == '[' or c == '{':  # 栈里加入左括号
                stack.append(c)
            else:
                # stack为空，或栈顶的左括号与当前的右括号不匹配
                if not stack or mapping[stack.pop()] != c:
                    return False
        if stack:  # 最后还有剩余，也说明有未匹配的左括号
            return False
        return True




