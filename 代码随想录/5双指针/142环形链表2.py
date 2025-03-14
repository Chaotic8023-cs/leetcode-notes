from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
二刷：快慢指针，慢走一步快走两步，相遇则有环。相遇后，用两个普通指针p1和p2，分别从head和相遇处出发，最后相遇的节点就是环的入口。
"""
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                p1, p2 = head, slow
                while p1 != p2:
                    p1, p2 = p1.next, p2.next
                return p1
        return None