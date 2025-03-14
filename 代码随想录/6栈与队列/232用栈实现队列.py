from typing import *
from collections import deque



"""
collections.deque: deque是一个为双头插入删除优化的数据结构（用双向链表实现），我们可以把他想象成一个list：
    1. 用作stack时：push -> append, pop -> pop, 即从尾部加入，从尾部删除
    2. 用作queue时，push -> append, pop -> popleft, 即从尾部加入，从头部删除

如何用2个栈实现队列？
用一个in_stack来存push进来的元素，一个out_stack用来存即将pop出去的元素。
    1. 所有push操作就直接append到in_stack即可。
    2. pop操作先看out_stack中有无元素，有的话直接pop，没有的话把in_stack的元素全部push进out_stack然后再pop。相当于我们要取头部
       的元素但stack只能从尾部pop，我们就把所有的元素都pop到另一个stack中，这样元素就颠倒了，最后pop出来的就是头部了。
"""
class MyQueue:

    def __init__(self):
        self.in_stack = deque([])
        self.out_stack = deque([])

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if self.out_stack:
            return self.out_stack.pop()
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self) -> int:
        # 这里只能用stack的操作（不能用deque的index），即stack的peek，是从尾部看，但是我们要peek头部，所以直接pop出一个再加回去
        ans = self.pop()
        self.out_stack.append(ans)  # 因为一定是out_stack pop出来的，所以是给out_stack加回去
        return ans

    def empty(self) -> bool:
        return len(self.in_stack) == 0 and len(self.out_stack) == 0



if __name__ == '__main__':
    q = MyQueue()
    q.push(1)
    q.push(2)
