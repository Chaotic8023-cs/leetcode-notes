from typing import *
from collections import deque


"""
用一个queue就能实现栈：既然两个q互相转移元素顺序不变，那么q自己也可以给自己转移：
push：直接加入
pop：循环(size-1)次，把除了末尾的元素都popleft出来再从尾部append进去，此时头部就是原来q的末尾元素，直接popleft即可
top：调用pop，然后再加入到q中即可
"""
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        x = self.pop()
        self.push(x)
        return x
        
    def empty(self) -> bool:
        return len(self.q) == 0


"""
用两个queue实现stack，这里和用两个stack实现queue不一样，因为就算把元素从一个queue移到另一个queue中，顺序还是不变的。
所以这里q2完全相当于临时储存，或者说是q1的备份。
下面是我自己写的，其实也可以有别的写法：

push：存到q1和q2中有元素的那个
pop：把有元素的那个q一直popleft到另一个q中，直到剩最后一个，刚好就是尾部，直接popleft返回。此时另一个q中顺序不变。
top：直接调用pop，然后再加入回去，注意此时哪个q有元素就加回到哪个q中，因为pop会把元素全都加到另一个q中！
"""
class MyStack1:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        if self.q1:
            self.q1.append(x)
        else:
            self.q2.append(x)

    def pop(self) -> int:
        if self.q1:
            while len(self.q1) > 1:
                self.q2.append(self.q1.popleft())
            return self.q1.popleft()
        else:
            while len(self.q2) > 1:
                self.q1.append(self.q2.popleft())
            return self.q2.popleft()

    def top(self) -> int:
        ans = self.pop()
        if self.q1:
            self.q1.append(ans)
        else:
            self.q2.append(ans)
        return ans

    def empty(self) -> bool:
        return len(self.q1) == 0 and len(self.q2) == 0
    

# 优化版：明确命名区分in和out
class MyStack2:

    def __init__(self):
        self.q_in = deque()  # q_in一直存所有的元素
        self.q_out = deque()  # q_out为临时中转用

    def push(self, x: int) -> None:
        self.q_in.append(x)

    def pop(self) -> int:
        for _ in range(len(self.q_in) - 1):
            self.q_out.append(self.q_in.popleft())
        self.q_in, self.q_out = self.q_out, self.q_in  # 此时q_in剩的那个就是要pop掉的元素，于是做交换，保证q_in一直存所有的元素
        return self.q_out.popleft()

    def top(self) -> int:
        x = self.pop()
        self.q_in.append(x)
        return x
    
    def empty(self) -> bool:
        return len(self.q_in) == 0 and len(self.q_out) == 0

