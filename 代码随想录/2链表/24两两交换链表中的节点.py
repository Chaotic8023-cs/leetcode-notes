from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
三指针：使用一个dummy，每次看三个节点，即要交换的两个node（j，k）和它们前面的那个node（i）
其实可以只维护两个要交换的node的前面那个节点的指针，但三指针便于理解，直接记三指针的方法（自己写的）
"""
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        i, j, k = dummy, dummy.next, dummy.next.next if dummy.next else None
        while k:
            next_j, next_k = k.next, k.next.next if k.next else None  # 提前存储下一个循环中的j和k指针
            i.next = k
            k.next = j
            j.next = next_j
            i, j, k = j, next_j, next_k
        return dummy.next


if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    sol.swapPairs(head)
    print()

