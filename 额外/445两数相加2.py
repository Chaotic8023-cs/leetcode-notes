from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
其实就是 #2两数相加 把链表换成正序的了，我们只需要反转一下再做即可
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev, curr = None, head
            while curr:
                temp = curr.next
                curr.next = prev
                prev, curr = curr, temp
            return prev

        l1 = reverse(l1)
        l2 = reverse(l2)
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0
            a = d1 + d2 + carry
            d, carry = a % 10, a // 10
            curr.next = ListNode(d)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            curr.next = ListNode(carry)
        return reverse(dummy.next)  # 注意：最后也要反转一次，因为要的是正序的结果！



