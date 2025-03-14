# 61
from typing import *
from utils.pprintdp import pprintdp


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 其实在求出等效的k后可以用快慢指针来找到切断点!
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        """
        先求出链表长度然后就可以求出最小的等效k
        最后就可以用快慢指针来找到切断点，把链表拼接一下即可
        """
        cur = head
        l = 0  # length of the list
        while cur:
            l += 1
            cur = cur.next
        if l < 2:  # 没有node或只有一个node就不用rotate了
            return head
        k %= l
        if k == 0:  # 等价于不rotate
            return head
        dummy = ListNode(0, head)
        slow = fast = dummy
        for _ in range(k):
            fast = fast.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        # 现在slow就是断点的前一个node，fast是结尾
        new_head = slow.next
        slow.next = None
        fast.next = head
        return new_head

    # 自己的尝试，记录了每个node的指针，空间复杂度O(N)不太好
    def rotateRight1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        cur = head
        ptrs = []
        while cur:
            ptrs.append(cur)
            cur = cur.next
        k %= len(ptrs)
        if k == 0:  # 等价于不rotate
            return head
        p, q = ptrs[len(ptrs) - k - 1], ptrs[len(ptrs) - k]  # 切断点的前一个和后一个
        end = ptrs[-1]
        end.next = head
        p.next = None
        return q


if __name__ == '__main__':
    sol = Solution()
