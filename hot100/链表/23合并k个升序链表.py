from typing import *
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
最小堆：先把头节点头加入到最小堆中，然后一直取最小的设为curr.next。如果当前pop出来的最小的节点有next，那么就加入到最小堆中。
要注意的是，因为我们无法改变ListNode的定义，所以heap中我们用元组的形式存，把节点值存为第一个元素，这样heapq就会默认用第一个元素作比较。
还需注意的是节点值可能有重复，所以此时heapq会用元组中第二个元素进行比较，所以第二个元素不能直接存node本身（因为ListNode没定义__lt__），
我们就用id()函数即可，它会返回一个对象的唯一的id，不会重复。
"""
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        heap = [(head.val, id(head), head) for head in lists if head is not None]
        heapq.heapify(heap)
        while heap:
            _, _, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next is not None:
                heapq.heappush(heap, (node.next.val, id(node.next), node.next))
        return dummy.next






