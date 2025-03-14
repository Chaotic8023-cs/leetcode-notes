# 155
from typing import *
from utils.pprintdp import pprintdp


class MinStack:
    def __init__(self):
        self.stack = []
        """
        用第二个stack记录min，即stackMin的top就是
        当前stack的min
        """
        self.stackMin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.stackMin:
            self.stackMin.append(min(self.stackMin[-1], val))
        else:
            self.stackMin.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.stackMin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackMin[-1]


if __name__ == '__main__':
    obj = MinStack()

