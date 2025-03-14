# 82
from typing import *
from utils.pprintdp import pprintdp


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = pre = ListNode(next=head)
        cur = head
        """
        更efficient的解法:
        弄一个dummy,pre指向dummmy，cur指向head
        对于每个cur，当其next的值和它相等时，cur一直向右移动
        移动完后我们判断pre.next是不是cur，如果是则说明cur没有移动过即没有重复，这是pre和cur都向右移动一格更新
        如果不是，说明cur有重复，责令pre直接连接到cur.next,因为这是cur是重复的nodes中的最后一个，最后还是要更新cur到下一个
        """
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur = cur.next
            # after while, the cur should be at the last node of the duplicated nodes
            if pre.next == cur:  # cur does not have duplicates
                pre = cur
            else:  # cur have duplicate
                pre.next = cur.next
            # cur moves right one position
            cur = cur.next
        return dummy.next

    # self try
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0, head)
        prev = dummy
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:  # has duplicates
                # 连续跳过cur右边的重复node
                while cur.next and cur.val == cur.next.val:
                    cur.next = cur.next.next
                # 使prev链接cur.next来删除cur，并更新cur
                prev.next = cur.next
                cur = cur.next
            else:
                cur = cur.next
                prev = prev.next
        return dummy.next


if __name__ == '__main__':
    sol = Solution()

