from typing import *
from collections import Counter

"""
直接分别创建两个哈希表然后比较是否相等（key-value pairs都一样）
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)  # == compare by value

    # 用字典：两个str长度一样的情况下，只用一个哈希表就行
    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapping = {}
        for c in s:
            mapping[c] = mapping.get(c, 0) + 1
        for c in t:
            mapping[c] = mapping.get(c, 0) - 1
            if mapping[c] < 0:
                return False
        return True

