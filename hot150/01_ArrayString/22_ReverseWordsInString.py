# 151
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        n = len(s)
        i = n-1
        while i >= 0:
            """
            第一个while跳过空格，即i会成第一个不是空格的word的末尾
            第二个while跳过一个单词，即i会成这个word前的第一个空格
            我们判断有没有到头，到头就停下，然后最后返回去掉结尾空格s：
                1. 第一个word前有空格，则第一个while过后，end和i都为-1
                2. 第一个word前没空格，则上一循环里第一个word会加入到ans，
                i会变成-1，最外层的while就进不来了直接结束
            """
            while i >= 0 and s[i] == ' ':
                i -= 1
            end = i
            while i >= 0 and s[i] != ' ':
                i -= 1
            if i < end:
                ans += s[i+1:end+1] + ' '
        return ans[:-1]

    def reverseWords1(self, s: str) -> str:
        return ' '.join(reversed(s.split()))


if __name__ == '__main__':
    s = " hello  world    "
    sol = Solution()
    print(sol.reverseWords(s))

