from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
快慢指针：
1. 快慢指针相遇则有环
2. 相遇后，用两个慢指针，一个指向head一个指向相遇处，两个慢指针每次走一步，再相遇时就是环的入口
"""
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                i, j = head, slow
                while i != j:
                    i, j = i.next, j.next
                return i
        return None









