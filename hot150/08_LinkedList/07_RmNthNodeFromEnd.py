# 19
from typing import *
from utils.pprintdp import pprintdp


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # 快慢指针, 遍历一次!!! O(1) space
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        slow = fast = dummy  # start from dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return dummy.next

    # 两次遍历
    def removeNthFromEnd1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count length
        length = 0
        cur = head
        while cur is not None:
            cur = cur.next
            length += 1
        idx = length - n
        if idx == 0:  # if removing the head
            return head.next
        # find the node to remove
        p = head
        for _ in range(idx-1):
            p = p.next
        # p is the previous node of the node to be removed, just make the next pointer skip it
        p.next = p.next.next
        return head

    # remove nth node from end in one pass: 空间复杂度不好！！！
    def removeNthFromEnd1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptrs = []
        cur = head
        l = 0
        """
        一次遍历，遍历的时候记录所有node的pointer
        """
        while cur is not None:
            l += 1
            ptrs.append(cur)  # record a pointer to the current node
            cur = cur.next  # cur changed, but the pointers in the ptrs list remain unchanged!
        idx = l-n
        if idx == 0:
            return head.next
        ptrs[idx-1].next = ptrs[idx-1].next.next
        return head






if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    # head = ListNode(1, None)
    sol = Solution()
    sol.removeNthFromEnd(head, 2)

