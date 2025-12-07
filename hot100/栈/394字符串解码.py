from collections import deque
from typing import *


"""
栈：
方法：遇到数字加数字，遇到字母加字母（加入以当前字母为开头的整个子字母字符串，即单词）；左括号[直接跳过
     重点是：每遇到一个右括号，则一直从stack pop单词，合起来，直到遇到第一个数字k，那么就把当前合并的单词乘上这个k，再放回stack中。
     最后，stack中会仅剩1个或多个单词，把他们合并起来即可。
     
     注意顺序：因为我们要的顺序是栈底到栈顶，所以我们每次pop的时候取反，最后再把整体合并的取反，才是最终的结果。例如：
     尾[ab, cd, efg]顶 -> 先pop并反转：gfe, dc, ba -> 整个反转：abcdefg
"""
class Solution:
    # stack统一存string，通过每个string的第一个char来区分int和string（不用isinstance！）
    def decodeString(self, s: str) -> str:
        n = len(s)
        stack = deque()
        i = 0
        while i < n:
            if s[i].isdigit():
                start = i
                i += 1
                while i < n and s[i].isdigit():
                    i += 1
                stack.append(s[start:i])
            elif s[i].isalpha():
                start = i
                i += 1
                while i < n and s[i].isalpha():
                    i += 1
                stack.append(s[start:i])
            elif s[i] == '[':
                i += 1
            else:
                curr = ""
                while stack[-1][0].isalpha():  # 检查当前字符串第一个char，看是字母还是数字
                    curr += stack.pop()[::-1]
                k = int(stack.pop())
                stack.append(k * curr[::-1])
                i += 1
        ans = ""
        while stack:
            ans += stack.pop()[::-1]
        return ans[::-1]
    
    # 双指针，用 j 代替 start
    def decodeString1(self, s: str) -> str:
        n = len(s)
        stack = deque()
        i = 0
        while i < n:
            if s[i].isdigit():
                j = i + 1
                while j < n and s[j].isdigit():
                    j += 1
                stack.append(s[i:j])
                i = j
            elif s[i].isalpha():
                j = i + 1
                while j < n and s[j].isalpha():
                    j += 1
                stack.append(s[i:j])
                i = j
            elif s[i] == '[':
                i += 1
            else:
                curr = ''
                while stack and stack[-1][0].isalpha():
                    curr += stack.pop()[::-1]
                k = int(stack.pop())
                stack.append(k * curr[::-1])
                i += 1
        ans = ''
        while stack:
            ans += stack.pop()[::-1]
        return ans[::-1]


if __name__ == '__main__':
    sol = Solution()
    s = "3[a2[c]]"
    print(sol.decodeString(s))


