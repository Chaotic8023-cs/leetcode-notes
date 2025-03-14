from typing import *


class Solution:
    """
    二刷：双指针，先用快慢指针去除多余空格，然后整个反转，最后把每个单词反转即可。
    """
    def reverseWords(self, s: str) -> str:
        arr = list(s)
        i, j = 0, 0  # 慢，快指针
        n = len(s)
        while j < n:
            if arr[j] != ' ':
                if i > 0:
                    arr[i] = ' '
                    i += 1
                while j < n and arr[j] != ' ':
                    arr[i] = arr[j]
                    i, j = i + 1, j + 1
            else:
                j += 1
        arr = arr[:i]
        s = ''.join(arr[::-1])
        return ' '.join(w[::-1] for w in s.split())

