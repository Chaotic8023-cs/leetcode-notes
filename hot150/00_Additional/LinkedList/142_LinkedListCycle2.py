# 142
from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
快慢指针找链表循环入口位置：https://zhuanlan.zhihu.com/p/454262200
同类型：Hashmap: 07 (#202)
"""
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # fast catch up with slow, loop exists
                # introduce a third pointer, when it meets slow, it will be the loop starting point
                third = head
                while third.val != slow.val:
                    third = third.next
                    slow = slow.next
                return slow
        return None


if __name__ == '__main__':
    sol = Solution()
