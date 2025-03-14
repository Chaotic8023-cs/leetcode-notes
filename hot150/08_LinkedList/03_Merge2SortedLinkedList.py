# 21
from typing import *
from utils.pprintdp import pprintdp


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        # 先让head指向最小的头
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        # 用一个pointer指向head
        pointer_head = head
        """
        遍历两个list，进行拼接
        """
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            """
            这里head虽然变了，但pointer_head指向的object还是一开始的head，
            我们只是一直改变一开始的object的next
            """
            head = head.next
        if list1 is not None:
            head.next = list1
        if list2 is not None:
            head.next = list2

        return pointer_head

    # 方法2：用一个新建的Node Head（可以省去很多代码，也是迭代）
    def mergeTwoLists1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2  # 这里相当于哪个不是None就选哪个
        return dummy.next

    # 方法2: 递归
    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None or list2 is None:
            return list1 or list2
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists2(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists2(list1, list2.next)
            return list2


if __name__ == '__main__':
    list1 = ListNode(1, ListNode(2, ListNode(4, None)))
    list2 = ListNode(1, ListNode(3, ListNode(4, None)))
    sol = Solution()
    sol.mergeTwoLists(list1, list2)

