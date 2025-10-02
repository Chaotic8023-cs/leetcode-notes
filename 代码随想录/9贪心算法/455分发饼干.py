from typing import *


class Solution:
    """
    自己做的思路：先都排序，然后双指针，饼干和胃口从小的开始，能分配就分配，分配不了饼干大小（j）就就+1
    """
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        m, n = len(g), len(s)
        g.sort()
        s.sort()
        i, j = 0, 0
        while i < m and j < n:
            if s[j] >= g[i]:
                i, j = i + 1, j + 1
            else:
                j += 1
        return i  # i最后就是分发了几块饼干






