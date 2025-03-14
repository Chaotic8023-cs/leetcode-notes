from typing import *


class Solution:
    """
    把string转成list做会方便很多，操作按题意即可。
    """
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(i, j, arr):
            left, right = i, j
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left, right = left + 1, right - 1

        n = len(s)
        arr = list(s)
        start = 0
        while start + 2 * k - 1 <= n:  # 当前有2k个
            reverse(start, start + k - 1, arr)
            start += 2 * k
        #当剩余的长度n - start不足2k时，按题意分情况
        if n - start < k:
            reverse(start, n - 1, arr)
        else:
            reverse(start, start + k - 1, arr)
        return ''.join(arr)



