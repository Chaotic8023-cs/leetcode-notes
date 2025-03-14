from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    三指针：用三个指针记录当前要翻转的两个节点和前一个节点，循环进行操作即可
    """
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        start = dummy
        while start.next and start.next.next:
            i, j = start.next, start.next.next
            next_head = j.next  # 提前存储下组两个节点中的第一个
            j.next = i  # 翻转当前组
            start.next = j  # start接翻转后的头
            i.next = next_head  # 翻转后的尾接下一组的头
            start = i  # 更新start指针开启下一个循环
        return dummy.next

    """
    直接调用k个一组翻转链表
    """
    def swapPairs1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
            def reverse(head):
                prev, curr = None, head
                while curr:
                    temp = curr.next
                    curr.next = prev
                    prev, curr = curr, temp
                return prev

            dummy = ListNode(next=head)
            start = dummy
            while start:
                # start为当前要翻转的k组的前一个节点，每次从start开始curr右移k次，最后curr就会指向当前k组的最后一个节点
                curr = start
                for _ in range(k):
                    curr = curr.next
                    if curr is None:
                        return dummy.next
                # 翻转当前k组
                next_head = curr.next
                curr.next = None
                curr_end = start.next
                curr_head = reverse(start.next)
                # 拼接
                start.next = curr_head
                curr_end.next = next_head
                # 更新start为下一个要翻转的k组的前一个节点，即当前k组翻转后的尾巴curr_end
                start = curr_end

        return reverseKGroup(head, k=2)




