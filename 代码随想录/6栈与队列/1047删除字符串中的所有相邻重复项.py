from collections import deque
from typing import *


class Solution:
    """
    stack：遍历字符串，如果当前字符和stack顶部的相同，说明挨着的两个一样，则将stack的顶端的字符pop掉，然后直接掠过当前遍历到的字符（相当于把
    两个一样的字符全删了）。如果和stack顶端的字符不一样，则加入stack中。最后stack中的字母反过来就是ans。
    """
    def removeDuplicates(self, s: str) -> str:
        stack = deque()
        for w in s:
            if not stack or stack[-1] != w:
                stack.append(w)
            else:  # if stack and stack[-1] == w
                stack.pop()
        # 这里其实可以直接 return ''.join(stack)
        ans = ""
        while stack:
            ans += stack.pop()
        return ans[::-1]
