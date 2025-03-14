from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val

"""
二刷：快慢指针，先让fast走n步，然后快慢一起走，当快指是最后一个节点时，慢指针就是倒数第n个节点的前一个节点，此时删除slow后面的一个节点即可。
注意，如果fast先走n步后为None了，即说明n等于链表的长度，则需要去除head，直接返回head.next即可。
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        if not fast:  # n == size, remove head
            return head.next
        while fast.next:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return head
