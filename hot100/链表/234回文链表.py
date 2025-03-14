from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    O(n)空间：直接遍历获得所有节点的值，然后看是不是回文
    """
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        elements = []
        while head:
            elements.append(head.val)
            head = head.next
        return elements == elements[::-1]

    """
    O(1)额外空间：先用快慢指针找到中间节点，再反转后半部分，最后同时遍历前半部分和反转后的后半部分看是否相等（即回文）    
    """
    def isPalindrome1(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            prev, curr = None, head
            while curr:
                temp = curr.next
                curr.next = prev
                prev, curr = curr, temp
            return prev

        slow, fast = head, head
        prev = head
        while fast and fast.next:
            prev = slow
            slow, fast = slow.next, fast.next.next
        tail = reverse(prev.next)
        prev.next = None
        while head and tail:
            if head.val != tail.val:
                return False
            head, tail = head.next, tail.next
        return True

    """
    isPalindrome1优化版：直接不用prev，直接找中间节点，这样所有链表不论奇偶节点数都可以直接把slow进行反转，然后进行比较（虽然前半部分的指针还连着
    后半部分的第一个，但不影响比较!）
    """
    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        # 1 2 2 1
        # 1 2 3 2 1
        def reverse(head):
            prev, curr = None, head
            while curr:
                temp = curr.next
                curr.next = prev
                prev, curr = curr, temp
            return prev

        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        h1, h2 = head, reverse(slow)
        while h1 and h2:
            if h1.val != h2.val:
                return False
            h1, h2 = h1.next, h2.next
        return True




