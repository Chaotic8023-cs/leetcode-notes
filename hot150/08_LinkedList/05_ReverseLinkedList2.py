# 92
from typing import *
from utils.pprintdp import pprintdp


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next is None or left == right:
            return head
        dummy = ListNode(0, head)
        pre = dummy
        for _ in range(left-1):
            pre = pre.next
        """
        首先通过遍历，记录left左边的node和left本身为p和q两个指针，这两个指针不变，为reverse之后做准备
        然后对于left到right的每一个node，我们把它的next指针变更为指向前一个node
        最后，我们用一开始记录的p和q指针，来进行相应的对接，即原来left左边的node接right，left接原来right右边的node
        """
        p, q = pre, pre.next  # fixed pinter for later use
        """
        q,p为固定指针用来保存初始的left和其前一个node
        p一直指向初始的left的左边一个node
        q一直指向left

        pre,cur作为变化的'滑动'指针来反转left到right中所有node的next指针
        """
        cur = q
        for _ in range(right-left+1):
            t = cur.next
            cur.next = pre
            pre, cur = cur, t
        p.next = pre  # p接原right
        q.next = cur  # q接原right后面的那个node
        return dummy.next

    # def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    #     if head.next is None or left == right:
    #         return head
    #     dummy = ListNode(0, head)
    #     pre = dummy
    #     for _ in range(left-1):
    #         pre = pre.next
    #     p, q = pre, pre.next
    #     """
    #     只是自己试着重写一个，这里直接从left右边一个node开始变更next指针，而不是上面从left本身开始，
    #     因为最终left本身要指向原来right的右边一个node，所以一开始left自己的next指针可以不用动
    #     """
    #     pp, cur = q, q.next
    #     for _ in range(right-left):
    #         t = cur.next
    #         cur.next = pp
    #         pp, cur = cur, t
    #     p.next = pp
    #     q.next = cur
    #     return dummy.next


if __name__ == '__main__':
    sol = Solution()

