# 86
from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # self try:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode(0, None)
        ge = ListNode(0, None)
        p, q = less, ge
        """
        建立两个dummy，less用来链接小于x的nodes，ge用来链接大于等于x的nodes
        一次遍历list，按val大小接到对应dummy上
        最后把ge接到less后面即可
        """
        while head:
            if head.val < x:
                p.next = head
                p = p.next
            else:
                q.next = head
                q = q.next
            head = head.next
        q.next = None  # 把当前ge的末尾(q)的next设为None，因为它在原链表里可能还接着nodes
        p.next = ge.next  # less的末尾(p)要接ge所以不用提前把next设成None
        return less.next

