from typing import *


class Solution:
    """
    暴力解法：子串一定小于等于一半的长度，所以我们枚举子串的结束位置（因为开头是固定的0），到中间位置为止，看k个子串是否等于s
    """
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for j in range(1, n // 2 + 1):  # 枚举子串结束位置j
            sub_s = s[:j]
            k = n // len(sub_s)  # 当前子串一共需要k个
            if k * sub_s == s:
                return True
        return False

    """
    巧妙解法：当把s和自己合起来的时候变成ss：
        1. 假设s是由重复子串组成的，那么从index 1开始找s，一定能从小于s的长度的index找到s
        2. 假设s不是由重复子串组成的，那么从index 1开始找s，那么找到s的index一定等于s的长度
    例子：
        1. s = abcabc, ss = abcabcabcabc, 从下标1开始找到的s的index为3，小于len(s)
        2. s = abcd, ss = abcdabcd, 从下标1开始找到的s的index为4，等于len(s)
    所以我们只需要判断是否在ss中找到的s的index小于s的长度即可。
    """
    def repeatedSubstringPattern1(self, s: str) -> bool:
        return (s + s).index(s, 1) < len(s)
    
    # 从下标1开始找的index小于len(s)等效于 s in (s + s)[1:-1]
    def repeatedSubstringPattern2(self, s: str) -> bool:
        return s in (s + s)[1:-1]


