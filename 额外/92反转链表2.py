from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
一次遍历：找到要反转的部分的头，提前记录要反转部分头节点的前一个节点，然后使用普通反转链表方法进行反转，反转后prev就是新头，curr就是新头的下一个节点（也就是要反转部分的后面的链表头），
最后使用指针进行拼接即可。

例子：

1 -> 2 -> 3 -> 4 -> 5, left = 2, right = 4
1. 遍历找到要反转部分的头和前一个节点，并用两个指针pq做记录：
    dummy -> 1 -> 2 -> 3 -> 4 -> 5
        prev = 1, curr = 2
        p = 1, q = 2
2. 标准反转链表（使用prev和curr指针）： 
    反转前：dummy -> 1 -> 2 -> 3 -> 4 -> 5, prev = 1, curr = 2
    反转后 dummy -> 1 <- 2 <- 3 <- 4 -> 5, prev = 4, curr = 5 (此时1的next还是2，但是不影响)
3. 进行拼接：
    3.1 p为前半部分的尾节点，prev为要反转部分反转后的新头：p.next = prev
        p: 1
        prev: 4
    3.2 q为要反转部分反转后的新尾，curr为后半部分的头节点：q.next = curr
        q: 2
        curr: 5
    得到： dummy -> 1 -> 4 -> 3 -> 2 -> 5
"""
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 如果要反转的部分只有一个节点
        if left == right:
            return head
        dummy = ListNode(next=head)
        # 找到要反转部分的头节点（curr）和前一个节点（prev）
        prev, curr = dummy, dummy
        for _ in range(left):
            prev = curr
            curr = curr.next
        """
        在反转前，记录：
            p：反转前要反转部分头节点的前一个节点
            q：反转前要反转部分的头节点，即反转后的尾节点
        """
        p, q = prev, curr
        # 使用普通反转链表的方法反转这部分
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        """
        此时各指针：
            1. prev：指向已经反转后的头（即反转前要反转的部分的尾节点）
            2. curr：指向反转前要反转部分的尾节点的后面一个节点（即要反转的部分之后的所有节点的头）
            3. p：指向要反转前要反转部分的头节点的前一个节点，即要反转部分的前面的所有节点的尾吧
            4. q：指向要反转部分反转后的尾节点（因为反转前指向的是要反转部分的头节点）
            
        进行拼接：
            1. p.next = prev
                要反转部分前一个节点p 接 反转后的新头prev
            2. q.next = curr
                反转后的尾q 接 要反转部分后面那些节点的头节点curr
        """
        p.next = prev
        q.next = curr
        # 最后返回dummy.next即可
        return dummy.next


"""
简化版
"""
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 找到起始点
        dummy = ListNode(next=head)
        prev, curr = dummy, head
        for _ in range(left - 1):
            prev, curr = prev.next, curr.next
        # 存一下要反转部分的前一个节点（prev）和反转后变成tail的curr指针
        i, j = prev, curr
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        # 拼接
        i.next = prev
        j.next = curr
        return dummy.next