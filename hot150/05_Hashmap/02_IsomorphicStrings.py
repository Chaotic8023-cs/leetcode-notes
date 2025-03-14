# 205
from typing import *


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        mapping_rev = {}
        for i in range(len(s)):
            # 如果同一个字母只能最多map到一个字母，则s和t，t和s需同时满足一对一映射关系！
            # 每次看s[i]，如果已经有对应的了但是不是当前的遇到的，即False
            # 若s[i]没有对应关系，则需检查s[i]当前对应的字母有没有已经被其他字母对应过了
            # 即检查s[i]当前对应的字母t[i]在mapping_rev里是不是对应的是s[i]！
            # 如果t[i]已经被s之前的某个字母对应过了，则mapping_rev[t[i]]一定存在，检查其是不是s[i]即可
            if ((s[i] in mapping and mapping[s[i]] != t[i])
                    or (t[i] in mapping_rev and mapping_rev[t[i]] != s[i])):
                return False
            else:
                mapping[s[i]] = t[i]
                mapping_rev[t[i]] = s[i]
        return True


if __name__ == '__main__':
    # s = "paper"
    # t = "title"
    s = "badc"
    t = "baba"
    sol = Solution()
    print(sol.isIsomorphic(s, t))