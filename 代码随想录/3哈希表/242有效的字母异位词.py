from typing import *
from collections import Counter

"""
直接分别创建两个哈希表然后比较是否相等（key-value pairs都一样）
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)  # == compare by value

    # 用字典
    def isAnagram1(self, s: str, t: str) -> bool:
        ht_s, ht_t = {}, {}
        for cs in s:
            ht_s[cs] = ht_s.get(cs, 0) + 1
        for ct in t:
            ht_t[ct] = ht_t.get(ct, 0) + 1
        return ht_s == ht_t

