# 290
from typing import *


class Solution:
    # 和Isomorphic Strings一样，就多一个len检查
    # 如果pattern长度和string split后长度不一样即False
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = {}
        mapping_rev = {}
        ss = s.split()
        if len(pattern) != len(ss):
            return False
        for i in range(len(pattern)):
            if (pattern[i] in mapping and mapping[pattern[i]] != ss[i]) or (
                    ss[i] in mapping_rev and mapping_rev[ss[i]] != pattern[i]):
                return False
            else:
                mapping[pattern[i]] = ss[i]
                mapping_rev[ss[i]] = pattern[i]
        return True


if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat fish"
    sol = Solution()
    print(sol.wordPattern(pattern, s))
