from typing import *


class Solution:
    """
    把string转成list做会方便很多，操作按题意即可。
    """
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l, r = l + 1, r - 1

        s = list(s)  # 转成list
        n = len(s)
        i = 0
        while i + 2 * k < n:  # 当前有2k个字母则一直反转前k个
            reverse(i, i + k - 1)
            i += 2 * k
        # 当剩余的字母个数n - i不足k时，全部反转
        if n - i < k:
            reverse(i, n - 1)
        else:  # 否则，反转前k个
            reverse(i, i + k - 1)
        return ''.join(s)



