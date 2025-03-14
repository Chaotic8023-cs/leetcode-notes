from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
双指针：用两个指针prev和curr来每次遍历两个节点，反转nxt的指针。初始时prev指向head的前面，即None，curr指向head，也就是说
我们从head开始一个一个反转
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
        return prev  # 在最后，curr指向链表结尾后面的None，prev指向的就是链表结尾，也就是反转后的head

"""
递归：和递归法一摸一样，只是把while换成递归了
"""
class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(prev, curr):
            if not curr:
                return prev
            nn = curr.next
            curr.next = prev
            return reverse(curr, nn)

        return reverse(None, head)


