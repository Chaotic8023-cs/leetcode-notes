from typing import *


"""
基础回溯：每层的candidates是当前数字对应的所有字母。因为每层对应单独的一个数字，且我们要按顺序选，所以这里我们用idx来表示当前到第几个数字了。
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtracking(idx, state, ans, digits, mapping):
            if idx == len(digits):
                ans.append(''.join(state))
                return
            for c in mapping[int(digits[idx])]:
                state.append(c)
                backtracking(idx + 1, state, ans, digits, mapping)
                state.pop()

        ans = []
        if len(digits) == 0:
            return ans
        mapping = {
            2: list("abc"),
            3: list("def"),
            4: list("ghi"),
            5: list("jkl"),
            6: list("mno"),
            7: list("pqrs"),
            8: list("tuv"),
            9: list("wxyz")
        }
        backtracking(0, [], ans, digits, mapping)
        return ans









