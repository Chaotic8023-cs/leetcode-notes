# 49
from typing import *
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        agroups = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            agroups[key].append(s)
        return list(agroups.values())


if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    sol = Solution()
    print(sol.groupAnagrams(strs))
