# 206
from typing import *
from utils.pprintdp import pprintdp


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        start = head
        pre, cur = head, head.next
        while cur:
            t = cur.next
            cur.next = pre
            pre, cur = cur, t
        start.next = None
        return pre

    def reverseList1(self, head: ListNode) -> ListNode:  # 递归反转链表
        if head is None or head.next is None:
            return head
        """
            画图能帮助理解
            非tail recursive：ans是已经反转好的tail，这时head的next是原来它的下一个，即ans中的最后一个node，
            所以head.next.next = head即把反转好的部分(ans)的结尾指向head，然后把head的next指针设为None，这样就
            相当于把当前的head加入到已反转部分的尾部
        """
        ans = self.reverseList(head.next)  # 反转好的tail，这时head指向ans的尾部node
        # 下面两行相当于把当前的head移到已更新好的链表末尾
        head.next.next = head  # 让已反转好的部分的尾部指向head
        head.next = None  # 并把当前head的结尾更新为None
        return ans




if __name__ == '__main__':
    sol = Solution()

