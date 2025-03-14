# 148
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Merge Sort
    1. 使用龟兔赛跑算法（快慢指针）找到链表中间元素
    2. 把链表divide成两部分
    3. recursively sort这两部分
    4. merge sort好的两个两个链表
    """
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base Case: empty or only 1 element, already sorted
        if head is None or head.next is None:
            return head
        # find mid: 龟兔赛跑算法，用快慢指针，快指针到末尾时慢指针就在中间
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        # now slow at the mid of the list
        # divide the list into 2 half
        t = slow.next  # head of the second half
        slow.next = None
        l1, l2 = self.sortList(head), self.sortList(t)
        # merge 2 sorted linked list
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next


