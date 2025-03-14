from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
快慢指针：使用两个指针，只用一次遍历就能找到倒数第n个节点，即我们使快指针比慢指针多n个节点，当快指针到末尾时，慢指针就是倒数第n个节点
做题的时候画图理解：我们要删除倒数第n个，那么我们就找它前面那个node，即倒数第n+1个node。我们会发现把快指针往右移动n步，那么最后当
快指针是结尾的时候，慢指针就是倒数第n+1个节点，此时删除它后面的节点即可。
需要注意的是，当n等于链表长度的时候，快指针在初始化的时候就会是链表末尾的右边，即None，此时我们需要删除的是head，所以直接返回head.next即可
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head  # 慢指针
        right = head  # 快指针
        for _ in range(n):
            right = right.next
        if not right:  # right为None，此时n等于链表的长度，即我们要去掉head
            return head.next
        # 正常情况下找到倒数第n个节点的前面一个节点，然后删除它后面的即可
        while right.next:
            left, right = left.next, right.next
        # 现在left就是倒数第n个节点的前面那个节点，此时删除left后面的节点即可
        left.next = left.next.next
        return head

