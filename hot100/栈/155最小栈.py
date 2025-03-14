from typing import *
from collections import *


"""
思路：栈中每个元素存的时候另外带一个目前的最小值，即加入前先从栈顶元素看目前的最小值是多少，然后加入当前元素时带的最小值就是包含该元素后的最小值。
也就是说，栈中最新的最小值就是栈顶元素的最小值，即整个栈的最小值；去掉栈顶元素后，下一个元素所带的最小值就是第二新的最小值，即包含第二个元素即
之前所有元素的最小值。这样就能保证加入或删除后我们还能得到那时侯状态下的最小值。
其实可以用另一个栈存当前的最小值，即一个stack1存val，stack2存每个val对应的最小值（包含对应val即所有之前的元素的最小值，即那个状态下的最小值），
这样就不用stack中元素用元组了。
"""
class MinStack:

    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:  # mstack元素：(当前最小值，当前元素)
        if self.stack:
            curr_min, prev = self.stack[-1]
            curr_min = min(curr_min, val)
            self.stack.append((curr_min, val))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][1]

    def getMin(self) -> int:
        return self.stack[-1][0]






