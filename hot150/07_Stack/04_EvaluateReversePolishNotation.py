# 150
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {'+', '-', '*', '/'}
        """
        我们遍历tokens，遇到数字就push进stack，遇到op则
        pop掉stack的两个数字（注意最先pop掉的是op右边的operand）:
            stack: [..., n1, n2] -> n1 op n2
            代码中是顺序的pop两次，所以先pop掉的的是n2，再pop掉的是n1
        然后通过op计算结果，并push回stack
        """
        for token in tokens:
            if token in op:
                n2 = stack.pop()
                n1 = stack.pop()
                if token == '+':
                    ans = n1 + n2
                elif token == '-':
                    ans = n1 - n2
                elif token == '*':
                    ans = n1 * n2
                else:
                    ans = int(n1 / n2)  # truncate towards 0 -> 用int()
                stack.append(ans)
            else:
                stack.append(int(token))
        return stack.pop()


if __name__ == '__main__':
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    sol = Solution()
    print(sol.evalRPN(tokens))
