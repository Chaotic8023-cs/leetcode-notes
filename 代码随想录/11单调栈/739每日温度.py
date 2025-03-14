from collections import deque
from typing import *


class Solution:
    """
    单调栈：从栈顶到栈底具备单调性的栈（deque中尾部为顶部，所以是尾部到头部的单调性）。
    问题类型对应的单调性：
        1. 找元素左边或右右边第一个大于它的元素：单调递增
        2. 找元素左边或右右边第一个小于它的元素：单调递减

    此题是典型的单调栈能解决的问题，因为我们要找右边第一个大的元素，所以我们要用从顶到底单调递增的栈，
    即deque中从尾巴（-1）到头部（0）单调递增的栈。栈里面存的是什么？我们其实是存之前遍历过的温度，如果
    栈是单调递增，即小的温度在顶部，那么我们每次遍历到一个大的温度，那么它就是栈顶这些小温度的右边第一个比
    他们大的温度。

    实现细节：为了方便记录ans，我们栈里存下标而不是元素本身。我们遍历温度数组，如果当前的温度大于栈顶的元素，则一直把栈顶的元素弹出（pop），
    直到当前的温度<=栈顶的元素，即加入栈后仍符合单调递增。同时，每当pop出来一个比当前温度小的，就记录到ans里，即当前温度是pop出来的元素
    右边第一个比它大的元素。
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mStack = deque()  # 从顶到底的单调递增栈
        n = len(temperatures)
        ans = [0] * n
        for i in range(n):
            # 当前的元素i即是栈顶那些小于它的温度的右边第一个比它们大的温度，即我们要找的目标
            while mStack and temperatures[i] > temperatures[mStack[-1]]:
                prev_i = mStack.pop()
                ans[prev_i] = i - prev_i
            mStack.append(i)
        while mStack:  # 此时mstack中剩余的就是没有更高温度的index了，因为初始化为0了都，所以其实不用再赋值0一遍
            ans[mStack.pop()] = 0
        return ans




