from typing import *



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



"""
O(1)空间做法：
1. 快慢指针找到中点
2. 分离前后两段，将后面的按规则拼接到前段即可

如果节点个数是奇数：
    1 -> 2 -> 3 -> 4 -> 5
    前段：123
    后段：45
如果节点个数是偶数
    1 -> 2 -> 3 -> 4 -> 5 -> 6
    前段：1234
    后段：56
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse(head):
            prev, curr = None, head
            while curr:
                temp = curr.next
                curr.next = prev
                prev, curr = curr, temp
            return prev
        
        # 1. 快慢指针找到中点
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
         
        # 2. 分离前后两段, 将后半段按照规则拼接到前半段
        l1, l2 = head, reverse(slow.next)
        slow.next = None 
        while l2:
            tmp1, tmp2 = l1.next, l2.next
            l1.next = l2
            l2.next = tmp1
            l1, l2 = tmp1, tmp2
        return head


"""
笨办法：将链表的每个节点放到一个list中，然后使用双指针拼接即可
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
        i, j = 0, len(arr) - 1
        dummy = ListNode()
        curr = dummy
        while i < j:
            curr.next = arr[i]
            curr = curr.next
            i += 1
            curr.next = arr[j]
            curr = curr.next
            j -= 1
        if i == j:  # 奇数个节点时，中间的节点就是i == j，需要加上作为最后一个节点
            curr.next = arr[i]
            curr = curr.next
        curr.next = None  # 要设置最后一个节点的尾巴为None，因为还指向原链表的某个节点，造成环，测试脚本就会就会造成exceed memory limit！
        return dummy.next
