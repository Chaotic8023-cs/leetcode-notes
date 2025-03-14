# 2
from typing import *
from utils.pprintdp import pprintdp


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # recursion
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add(l1, l2, carry, res):
            if l1 is not None and l2 is not None:
                x = l1.val + l2.val + carry
            elif l1 is not None:
                x = l1.val + carry
            elif l2 is not None:
                x = l2.val + carry
            else:  # l1, l2 both None
                if carry == 0:
                    return None
                # if have carry, return a new Node (the leading digit)
                return ListNode(carry)
            d = x % 10
            c = x // 10
            res.val = d
            res.next = ListNode()
            res.next = add(l1.next if l1 else None
                           , l2.next if l2 else None
                           , c, res.next)
            return res

        return add(l1, l2, 0, ListNode())

    # iterative
    def addTwoNumbers1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        curr = dummy
        while l1 or l2 or carry:
            # 这里需要加括号，因为ternary operator比+的precedence小！
            x = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, d = divmod(x, 10)
            curr.next = ListNode(d)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(9, ListNode(9, ListNode(9, None)))
    l2 = ListNode(9, ListNode(9, None))
    sol = Solution()
    res = sol.addTwoNumbers(l1, l2)
    print()

