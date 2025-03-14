from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    递归：
    1. base case：当其中一个链表为空时，返回不空的那个链表（即剩余部分）
    2. 每次把小的那个节点的next递归赋值，然后返回它
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None or list2 is None:
            return list1 or list2
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

    """
    遍历：先创建一个dummy头节点，然后每次选小的那个节点设为next，最后再把剩余部分加上
    """
    def mergeTwoLists1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        # 哪个小接哪个
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        # 当至少一个为空时，把另一个剩余的部分接上
        curr.next = list1 or list2
        return dummy.next







