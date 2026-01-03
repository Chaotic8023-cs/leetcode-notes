from typing import *


class Solution:
    """
    纯模拟：用来额extra space，先提取出来所有单词，再反转，最后中间加上空格
    """
    def reverseWords(self, s: str) -> str:
        n = len(s)
        i = 0
        arr = []
        while i < n:
            while i < n and s[i] == ' ':
                i += 1
            start = i
            while i < n and s[i] != ' ':
                i += 1
            if start < i:
                arr.append(s[start:i])
        return ' '.join(arr[::-1])

    """
    双指针（快慢指针）：O(1) 要修改的位置，快指针遍历字符串，如果遇到不是空格的就写到i的地方。
    同时我们给每个单词中间加上空格，即当i不是0的情况下（也就是不是第一个单词space. 思路和移除元素相同，慢指针i指向下一个），
    在写下一个单词前先加一个空格。最后i前面的i个字符就是处理好的，所以先变成正常的字符串，然后再split，反转，最后加空格。
    （当然也可以整个arr[:i]先反转，再变成正常字符串，最后再split，每个单词反转，再合起来）
    """
    def reverseWords1(self, s: str) -> str:
        i, j = 0, 0  # 慢，快指针
        n = len(s)
        arr = list(s)  # 改成list好使用双指针
        while j < n:
            if arr[j] != ' ':
                if i > 0:  # 如果慢指针在中间位置，即不是第一个单词，则先补一个空格
                    arr[i] = ' '
                    i += 1
                while j < n and arr[j] != ' ':
                    arr[i] = arr[j]
                    i, j = i + 1, j + 1
            else:
                j += 1
        # 此时arr中i之前的就是处理好的（所有单词，且中间填好空格）
        ans = ''.join(arr[:i])  # 先变成正常字符串
        return ' '.join(ans.split()[::-1])  # 再依据空格split变成单词，反转顺序，再添加空格
    
    # 该用双指针对每个word进行反转
    def reverseWords2(self, s: str) -> str:
        def reverse(s, i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i, j = i + 1, j - 1
        
        s = list(s)
        n = len(s)
        i, j = 0, 0
        while j < n:
            if s[j] == ' ':
                j += 1
            else:
                if i > 0:
                    s[i] = ' '
                    i += 1
                while j < n and s[j] != ' ':
                    s[i] = s[j]
                    i, j = i + 1, j + 1
        # 改用双指针对每个单词进行反转
        s = s[:i]
        i, j = 0, 0
        while j < len(s):
            while j < len(s) and s[j] != ' ':
                j += 1
            reverse(s, i, j - 1)
            i = j + 1
            j += 1
        return ''.join(s)[::-1]


if __name__ == '__main__':
    sol = Solution()
    s = "the sky is blue"
    print(sol.reverseWords(s))
