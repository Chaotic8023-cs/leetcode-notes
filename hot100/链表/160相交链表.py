from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
思路：
1.遍历一遍两个链表，得到两个链表的长度，同时比较最后一个节点指针是否相同，如过不同说明没有相交
2. 如果有相交，令长的一个链表的指针从头先走使得剩余长度相等，然后两个指针一起走直到遇到相交的地方（指针相等）
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 获取长度
        i, j = headA, headB
        sizeA, sizeB = 1, 1
        while i.next:
            sizeA += 1
            i = i.next
        while j.next:
            sizeB += 1
            j = j.next
        # 如果最后要给节点不同，则两个链表不相交
        if i != j:
            return None
        # 找到交点：让长的链表指针先走使得两个链表剩余长度相等，再一起走找到交点
        i, j = headA, headB
        if sizeA > sizeB:
            for _ in range(sizeA - sizeB):
                i = i.next
        else:
            for _ in range(sizeB - sizeA):
                j = j.next
        while i and j and i != j:
            i, j = i.next, j.next
        return i













