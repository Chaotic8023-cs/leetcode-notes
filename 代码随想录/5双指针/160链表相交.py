from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
二刷：双指针，先遍历一遍两个链表，统计长度，并看最后一个节点的指针是否相同，如果指向相同的最后一个节点则说明有相交。
有相交的情况下，让长的那个链表的指针先走长度差步，使得两个指针的剩余节点数相等，然后一同出发，直到两个指针指向相同的节点
为止，此节点就是相交的入口。注意比较的是指针而不是节点值！
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        i, j = headA, headB
        sizeA, sizeB = 1, 1
        while i.next:
            sizeA += 1
            i = i.next
        while j.next:
            sizeB += 1
            j = j.next
        if not i == j:  # 不相交
            return None
        i, j = headA, headB
        if sizeA > sizeB:
            for _ in range(sizeA - sizeB):
                i = i.next
        else:
            for _ in range(sizeB - sizeA):
                j = j.next
        while i != j:
            i, j = i.next, j.next
        return i
