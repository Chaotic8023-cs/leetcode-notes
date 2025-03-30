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
自己写的纯模拟，不用看。　
"""
class Solution1:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 普通反转链表，但是不光返回反转后的头，还返回反转后的尾（原来的头）
        def reverse(head):
            original_head = head  # 反转后的尾，即原来的头
            prev, curr = None, head
            while curr:
                temp = curr.next
                curr.next = prev
                prev, curr = curr, temp
            return prev, original_head

        # left == right即指向同一个节点，不需要反转，直接返回
        if left == right:
            return head
        # 找到prev和start，即要反转的前一个节点（prev）和要反转的开头节点（start）
        prev, start = None, head
        for _ in range(left - 1):
            prev = start
            start = start.next
        # 从start开始往后遍历找到要反转的末尾节点（end）
        end = start
        for _ in range(right - left):
            end = end.next
        # 反转前保存end后面的尾巴（tail）
        tail = end.next
        end.next = None
        # 使用reverse进行反转，得到反转后的头和尾
        new_start, new_end = reverse(start)
        # 如果prev不是None，即left不是head的话，将原来的前面的节点尾巴（prev）与反转后的头相接
        if prev:
            prev.next = new_start
        # 将反转后的尾巴和原来的尾部节点相接
        new_end.next = tail
        # 最后如果left不是head（即开始反转的地方不是原来的head）就返回原来的head，否则返回反转后的头部
        return head if prev else new_start