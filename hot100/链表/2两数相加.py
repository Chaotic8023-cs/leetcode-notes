from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
直接模拟：先创建个dummy头节点，然后两两遍历，算每一位上的值和carry然后创建一个新节点加到curr的后面；遍历完后把剩余部分加上，最后把carry加上即可。
"""
class Solution:
    # 下面的优化版：只要有一个有剩下的部分则一直加，最后就只用检查是否还有carry
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2:  # 只要有一个有剩下的部分则一直加
            a = carry
            if l1:
                a += l1.val
                l1 = l1.next
            if l2:
                a += l2.val
                l2 = l2.next
            d, carry = a % 10, a // 10
            curr.next = ListNode(val=d)
            curr = curr.next
        if carry:  # 最后只用检查有无carry即可
            curr.next = ListNode(val=carry)
        return dummy.next

    def addTwoNumbers1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        # 两两相加
        while l1 and l2:
            v = (l1.val + l2.val) + carry
            d, carry = v % 10, v // 10
            curr.next = ListNode(val=d)
            curr = curr.next
            l1, l2 = l1.next, l2.next
        # 剩余部分加上
        if l1:
            while l1:
                v = l1.val + carry
                d, carry = v % 10, v // 10
                curr.next = ListNode(val=d)
                curr = curr.next
                l1 = l1.next
        elif l2:
            while l2:
                v = l2.val + carry
                d, carry = v % 10, v // 10
                curr.next = ListNode(val=d)
                curr = curr.next
                l2 = l2.next
        # 检查是否还有carry，有的话也加上
        if carry:
            curr.next = ListNode(val=carry)
        return dummy.next










