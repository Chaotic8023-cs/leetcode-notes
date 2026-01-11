from typing import *
from collections import deque

"""
用两个queue实现stack：q_out临时中转用，即每次需要pop的时候，把q_in前面的元素临时存到q_out，这样q_in剩的就是“栈顶”了。
优化：pop在临时转移后，可以交换q_in和q_out，这样方便操作，且语意一致。
"""
class MyStack:

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
    

"""
用一个queue就能实现栈：既然两个q互相转移元素顺序不变，那么q自己也可以给自己转移：
push：直接加入
pop：循环(size-1)次，把除了末尾的元素都popleft出来再从尾部append进去，此时头部就是原来q的末尾元素，直接popleft即可
top：调用pop，然后再加入到q中即可

复杂度：
push: O(1)
pop: O(n)（把前 n-1 个元素旋到队尾）
top: 通过 pop()+push() 实现，因此也是 O(n)
empty: O(1)
"""
class MyStack1:

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
常用变种：在push的时候就进行旋转，这样pop和top就是O(1)，即将pop和top的复杂度转到了push，一种经典的权衡。
复杂度：
push: O(n)
pop: O(1)（直接 popleft()）
top: O(1)（直接看队首元素）
empty: O(1)

为什么每次push时旋转不会有问题？
因为保证了invariant：队列的队首始终是当前栈顶（最新 pushed 的元素）。
例子：push 1、2、3
1.
    - push后：[1]
    - 旋转后：[1]
2.
    - push后：[1, 2]
    - 旋转后：[2, 1]
3.
    - push后：[2, 1, 3]
    - 旋转后：[3, 2, 1]
可以发现，队列内始终保证了元素顺序是“栈头”到“栈底”！
"""
class MyStack2:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # 每次push时就旋转
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # 每次push保证了头元素就是“栈顶”，所以可以直接popleft
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]  # 访问q[0]是队列的top操作，合理

    def empty(self) -> bool:
        return not self.q


