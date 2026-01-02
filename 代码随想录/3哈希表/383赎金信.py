from typing import *


class Solution:
    """
    先用哈希表t统计magazine中字母出现的次数，在遍历ransomNote，如果其中的字母没出现过，或是t中对应的字母的次数用完了，就返回False
    注意：哈希表可以用数组替换，index用ord(c) - ord('a')，这样更快因为不需要维护红黑树或哈希表
    """
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
       t = {}
       for s in magazine:
           t[s] = t.get(s, 0) + 1

       for s in ransomNote:
            if s not in t:
                return False
            t[s] -= 1
            if t[s] == -1:
                return False
       return True
    
    # 简单版：直接看在不在，然后看个数够不够
    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        target = Counter(ransomNote)
        mag = Counter(magazine)
        for c in target:
            if c not in mag or mag[c] < target[c]:
                return False
        return True

