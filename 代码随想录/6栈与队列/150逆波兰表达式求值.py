from collections import deque
from typing import *


class Solution:
    """
    stack：通过观察逆波兰表达式会发现，每次遇到op，用到的是它前面的两个数。所以我们对tokens进行遍历，同时把数加入到stack中，
    一遇到op，则从stack中pop出两个数进行计算，再放回到stack中。最后的结果就是stack中仅剩的一个数。
    """
    def evalRPN(self, tokens: List[str]) -> int:
        def cal(a, b, op):
            if op == "+":
                return a + b
            elif op == "-":
                return a - b
            elif op == "*":
                return a * b
            else:
                # //为向下取整，一负一正结果会往小的负数走，例如 8 // -3 = -3。所以这里我们用int()，为向0取整。
                return int(a / b)

        stack = deque()
        op = {"+", "-", "*", "/"}
        for t in tokens:
            if t not in op:
                stack.append(int(t))
            else:
                # 注意：stack中[a, b]应该是 a op b，但是pop出来先是b后是a，所以这里要反着写，第一个是b，第二个是a
                b = stack.pop()
                a = stack.pop()
                stack.append(cal(a, b, t))
        return stack.pop()


if __name__ == '__main__':
    sol = Solution()
    tokens = ["4","13","5","/","+"]
    print(sol.evalRPN(tokens))

