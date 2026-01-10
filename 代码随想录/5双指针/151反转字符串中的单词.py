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

    # 完全in-place的写法：1. 去除多余空格 2. 全部反转 3. 每个单词反转
    def reverseWords1(self, s: str) -> str:
        def reverse(s, i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i, j = i + 1, j - 1

        s = list(s)
        n = len(s)
        i, j = 0, 0
        while j < n:
            if s[j] != ' ':
                if i > 0:
                    s[i] = ' '
                    i += 1
                while j < n and s[j] != ' ':
                    s[i] = s[j]
                    i, j = i + 1, j + 1
            else:
                j += 1
        s = s[:i]
        n = len(s)
        # 整个反转
        reverse(s, 0, n - 1)
        i, j = 0, 0
        while j < n:
            while j < n and s[j] != ' ':
                j += 1
            reverse(s, i, j - 1)  # 此时j是空格，反转当前单词
            j += 1
            i = j
        return ''.join(s)
    
    # 旧版写法，很容易出bug，不建议记！
    def reverseWords2(self, s: str) -> str:
        s = list(s)
        n = len(s)
        i, j = 0, 0
        while j < n:
            while j < n and s[j] == ' ':
                j += 1
            if j >= n:  # 容易出错：如果s最后也是空格，那么j走完了，下面的i设置一个空格就不应该再运行一次！！！
                break
            if i > 0:
                s[i] = ' '
                i += 1
            while j < n and s[j] != ' ':
                s[i] = s[j]
                i, j = i + 1, j + 1
        s = s[:i]
        s = ''.join(s).split()[::-1]
        return ' '.join(s)

