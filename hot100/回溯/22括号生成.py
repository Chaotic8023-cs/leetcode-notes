from typing import *


"""
回溯：记住下面的括号选择条件就行：
    1. 左括号有剩余则一直能选
    2. 右括号只有当前有需要close的左括号时才能选（左括号数大于右括号数）
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def get_next(state, n, count):
            choice = []
            if n - count['('] > 0:  # 左括号有剩余则一直能选
                choice.append('(')
            if count['('] > count[')']:  # 右括号只有当前有需要close的左括号时才能选，即左括号数大于右括号数
                choice.append(')')
            return choice

        def backtracking(state, ans, n, count):
            if len(state) == 2 * n:
                ans.append(''.join(state))
                return
            for p in get_next(state, n, count):
                state.append(p)
                count[p] += 1
                backtracking(state, ans, n, count)
                count[p] -= 1
                state.pop()

        ans = []
        count = {'(': 0, ')': 0}  # 记录当前已经使用过的左右括号数
        backtracking([], ans, n, count)
        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 3
    print(sol.generateParenthesis(n))





