from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    如果head就是要去除的节点，那么得单独处理，为了让头部和其他节点处理方法一样，我们引入一个dummy head
    每次检查当前节点的下一个节点是否要删除，如果要删除就skip一个即可
    """
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        curr = dummy
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next


