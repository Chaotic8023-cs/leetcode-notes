from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
快慢指针：让快指针先走n步，这样最后慢指针就会指向要删除的节点的前一个节点，此时删除它后面那个即可。
要注意的是，我们需要考虑删除头节点的情况，即n就是节点个数。此时slow就是head没动，且fast走到头出去了变成None了，
只有同时满足这两个条件才是删除头节点！（因为只有slow是head的话，[1,2]，n=1也能满足，此时slow是head但fast不是None，fast指向2）
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        # 让快指针先走n步
        for _ in range(n):
            fast = fast.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next
        # 此时slow就是要删除的节点的前一个节点
        if fast is None:  # 特殊情况：n == 节点数，即要删除的是头节点，此时fast是None
            return head.next
        # 删除倒数第n个节点
        slow.next = slow.next.next
        return head



