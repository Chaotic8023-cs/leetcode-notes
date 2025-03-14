from typing import *


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


"""
O(N)额外空间：用一个哈希表记录旧节点到新节点的映射。进行两次遍历：
    1. 先遍历一遍旧链表，复制一份不含random指针的新链表，并构建old2new
    2. 再遍历一遍旧链表，用old2new获取旧节点的random指针指向的旧节点所对应的新节点，并赋给新节点的random指针
即可复制完成
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        old2new = {}  # 旧节点到新节点的映射
        # 先遍历一遍旧链表，复制一份不含random指针的新链表，并构建old2new
        curr_old, curr_new = head, dummy
        while curr_old:
            new_node = Node(curr_old.val)
            curr_new.next = new_node
            old2new[curr_old] = new_node
            curr_old, curr_new = curr_old.next, curr_new.next
        # 再遍历一遍旧链表，用old2new获取旧节点的random指针指向的旧节点所对应的新节点，并赋给新节点的random指针
        curr_old, curr_new = head, dummy.next
        while curr_old:
            new_random = None
            if curr_old.random:
                new_random = old2new[curr_old.random]  # curr_old.random指向的是某个旧节点，此时用这个旧节点通过old2new获取对应的新节点
            curr_new.random = new_random
            curr_old, curr_new = curr_old.next, curr_new.next
        return dummy.next















