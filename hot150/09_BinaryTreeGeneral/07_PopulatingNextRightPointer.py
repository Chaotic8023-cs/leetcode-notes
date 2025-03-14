# 117
from typing import *
from utils.pprintdp import pprintdp

from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # 其实可以用层序遍历，不用加depth信息
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = deque([root])
        while queue:
            pre = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if pre:
                    pre.next = node
                pre = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

    # self try: BFS加了depth信息
    def connect1(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = deque()
        queue.append((root, 0))
        while queue:
            node, d = queue.popleft()
            if queue and queue[0][1] == d:
                node.next = queue[0][0]
            else:
                node.next = None
            if node.left:
                queue.append((node.left, d + 1))
            if node.right:
                queue.append((node.right, d + 1))
        return root

    # O(1)space解
    def connect2(self, root: 'Node') -> 'Node':
        """
        层序遍历，遍历当前层时，把下一层串起来（填充下一层的next指针）
        我们进行层序遍历，用两个指针，在遍历一层的时候，next一直指向下一层的开始，即下一层的第一个node
        用一个prev指针来记录过程中的前一个node，用来帮助我们填充下一层的next指针
        """

        def modify(cur):
            """
            一开始
            """
            nonlocal next, prev  # 指的是外头一层的next和prev，即内层函数modify里面改变next和prev其实改变的是外层connect2里的
            if not cur:
                return
            # next仅在第一次被赋值，即第一个node的left child，它用来遍历完当前层后，跳到下一层的初始位置
            next = next or cur  # 等价于 if next is None: next = cur
            # prev用来保留填充next指针时的前一个node，这样才能把前一个node的cur指针设为当前的node
            if prev:
                prev.next = cur
            prev = cur

        node = root
        while node:
            next = prev = None
            while node:
                modify(node.left)
                modify(node.right)
                node = node.next
            node = next  # 到此说明当前层已遍历完，将node设为下一层的开始（next）
        return root


if __name__ == '__main__':
    sol = Solution()
    root = Node(1, Node(2, Node(4), Node(5)), Node(3, right=Node(7)))
    sol.connect(root)
