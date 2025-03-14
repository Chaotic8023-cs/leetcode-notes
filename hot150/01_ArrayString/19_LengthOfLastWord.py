# 58
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        i = n-1
        """
        反着遍历：第一个while先过滤掉空格（找到last word的end），
        然后第二个while再找到这个last word的start，两头一减即
        是其长度
        """
        while s[i] == ' ':
            i -= 1
        end = i
        while i >= 0 and s[i] != ' ':
            i -= 1
        return end-i


if __name__ == '__main__':
    s = "   fly me   to   the moon  "
    sol = Solution()
    print(sol.lengthOfLastWord(s))

