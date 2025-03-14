from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
 思路：快慢指针，fast每次走两步，slow每次走一步，如果fast slow相遇，则证明有环。
 如何找到环的入口：head和相遇点同时出发两个指针，都是每次走一步，相遇的时候即为环的入口
 https://programmercarl.com/0142.%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8II.html#%E6%80%9D%E8%B7%AF
"""
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:  # 快慢指针相遇则说明有环
                # 找环的入口，即从头和相遇位置各出发一个普通指针，一次走一步，相遇处即为环的入口
                p1, p2 = head, slow
                while p1 != p2:
                    p1, p2 = p1.next, p2.next
                return p1
        return None  # 快指针走到结尾了还没和慢指针相遇，说明无环（同时解决了直接解决了0个或1个元素的情况，while直接不会运行）



