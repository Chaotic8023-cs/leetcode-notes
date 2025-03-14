from typing import *


"""
遍历切割的右端点：我们从左往右每次，即一层回溯中我们遍历切割的右端点，即切[start_idx:end]左闭右闭，如果是回文那么就继续进入下一层，
从end + 1开始切，直到把整个字符串切完为止。
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtracking(start_idx, state, ans, s):
            if start_idx == len(s):  # 字符出啊切完了
                ans.append(state[:])
                return
            for end in range(start_idx, len(s)):
                if s[start_idx:end + 1] == s[start_idx:end + 1][::-1]:  # 遍历切割右端点，切[start_idx:end]左闭右闭
                    state.append(s[start_idx:end + 1])
                    backtracking(end + 1, state, ans, s)
                    state.pop()

        ans = []
        backtracking(0, [], ans, s)
        return ans




