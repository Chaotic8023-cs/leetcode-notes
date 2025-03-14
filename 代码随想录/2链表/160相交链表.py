from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
双指针：先进行一次遍历计算两个链表的长度，同时看末尾节点是否相同，相同才有交点，最后再让长的链表先走（lA-lB）步使得两个指针在剩余长度相等的
位置同时起步，最后就能遍历找到第一个相交的节点（指针相等而非值相等，因为前面不相交的部分值也可能相同！）
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 一次遍历计算长度，同时令curr到末尾节点就停，这样还能比较两个链表末尾节点是否相等来判断是否相交
        lA, lB = 1, 1
        currA, currB = headA, headB
        while currA.next:
            lA += 1
            currA = currA.next
        while currB.next:
            lB += 1
            currB = currB.next
        if currA.val != currB.val:  # 两个链表末尾节点值不想等，所以没有相交
            return None
        # 让长的链表指针先走，使得两个链表的指针在剩余长度相等的情况下同时起步
        currA, currB = headA, headB
        if lA >= lB:
            for _ in range(lA - lB):
                currA = currA.next
        else:
            for _ in range(lB - lA):
                currB = currB.next
        # 此时同时起步，找到值相等的第一个节点即相交位置
        while currA != currB:  # 注意，是指针相等不是值相等！我们要找的是第一个被两个指针同时指向的节点
            currA, currB = currA.next, currB.next
        return currA



