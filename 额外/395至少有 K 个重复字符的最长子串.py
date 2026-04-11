from typing import *



"""
分治：非法字符分割

若字符 c 在字符串中出现次数 < k
则任何包含 c 的子串都不可能合法
用 c 将字符串分割，递归求解每一段
"""
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:  # base case
            return 0
        for c, cnt in Counter(s).items():
            if cnt < k:  # 找到不合法字符（即总数都小于k）
                # 对当前合法的子段递归计算
                return max(self.longestSubstring(sub, k) for sub in s.split(c))
        return len(s)
