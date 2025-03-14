# 138
from typing import *


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # O(n) space
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old2new_mapping = {}
        dummy = Node(0)
        curOld = head
        cur = dummy
        """
        先将旧链表每个node复制一个新的，并链接好next，同时
        记录一个旧node到新node的mapping
        再遍历旧的链表，连接好random指针：
            old2new_mapping: 
                旧node -> 新node
            我们通过旧node的random指针能获得指向的旧node
                旧node.random -> 旧node'
            再通过old2new_mapping即可获得对应的新node
                old2new_mapping[旧node'] -> 新node'
            最后把当前新node的random指向新node'即可
        """
        # 第一遍遍历链接next
        while curOld:
            cur.next = Node(curOld.val)
            cur = cur.next
            old2new_mapping[curOld] = cur
            curOld = curOld.next
        curOld = head
        cur = dummy.next
        # 第二遍遍历链接random
        while curOld:
            cur.random = old2new_mapping.get(curOld.random, None)
            cur = cur.next
            curOld = curOld.next
        return dummy.next


    # O(1) space: 拼接+拆分
    def copyRandomList1(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        """
        step1：交叉拼接，即把复制的新node插入到每个旧node之后
            旧->新->旧->新->旧->新
        step2：连接好新node的random指针
        在O(n)space的方法中我们通过建立旧node和新node的mapping，在本方法中这个mapping
        其实就是每个旧node的next就是新node，所以
            对于每个旧node n，它的复制的新node就是n.next。旧node n的random若是n'
            则n'对应的新复制的node就是n'.next。
            即：旧对应：n -> n', 新对应：n.next -> n'.next
            所以我们就可以链接当前新node(n.next)的random指针：n.next.random = n.random.next
        step3：将交叉链表分开，即新旧分开
            我们先记住复制node的开头以便最后return，即ans = head.next
            然后我们遍历每个node（按顺序，旧新都遍历）
            将每个node的next指针更新为间隔一个的node，即旧node的next都会指向
            旧node，复制node的next都会指向复制node的next
            example：
                old1 -> new1 -> old2 -> new2 -> old3 -> new3
            =>  old1 -> old2 -> old3
                new1 -> new2 -> new3
                先遍历到old1，next指针指向间隔一个的old2；
                然后遍历到new1，next指针指向间隔一个的new2；
                以此类推，唯一要注意的就是遍历到末尾的new3时，
                已经没有next了，注意要check一下！
        """
        # 交叉拼接
        cur = head
        while cur:
            new = Node(cur.val, cur.next)
            cur.next = new
            cur = new.next
        # 连好新node的random指针
        cur = head
        while cur:
            if cur.random:
                # 新.random = 旧.random.next
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 拆分交叉的链表
        ans = head.next
        cur = head
        while cur:
            nxt = cur.next
            if nxt:  # 到末尾的new node了，没有next了
                cur.next = nxt.next
            cur = nxt
        return ans


if __name__ == '__main__':
    sol = Solution()
