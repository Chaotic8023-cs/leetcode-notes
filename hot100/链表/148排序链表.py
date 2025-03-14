from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
链表的归并排序 (Merge Sort)
"""
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(head1, head2):
            if head1 is None or head2 is None:
                return head1 or head2
            if head1.val < head2.val:
                head1.next = merge(head1.next, head2)
                return head1
            else:
                head2.next = merge(head1, head2.next)
                return head2

        """
        在两个节点的情况，普通的快慢指针slow会是第二个节点，但我们要分成两半，所以要用一格prev指针来记录slow前一个节点，这样就能成两半：
            1. 前一半：[head, prev]
            2. 后一半：[prev.next,]
        这样就不会在节点数==2的时候其中一半一直是2另一半是0，出现无限循环！
        """
        # base case: 0个或1个节点时不需要排序，直接返回
        if head is None or head.next is None:
            return head
        # 用快慢指针找到中间节点，将链表分成两半
        prev = head
        slow, fast = head, head
        while fast and fast.next:
            prev = slow
            slow, fast = slow.next, fast.next.next
        h1, h2 = head, prev.next  # 分成两半
        prev.next = None  # 将前后两部分断开
        # 分治
        h1_sorted, h2_sorted = self.sortList(h1), self.sortList(h2)
        return merge(h1_sorted, h2_sorted)







