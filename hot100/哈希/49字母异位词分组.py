from collections import defaultdict
from typing import *

"""
就是把每个字字符串sort一下然后作为key加入到一个字典中，因为sort了所以所有anagram就会到一起
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            m[key].append(s)
        return list(m.values())


if __name__ == '__main__':
    sol = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(sol.groupAnagrams(strs))






