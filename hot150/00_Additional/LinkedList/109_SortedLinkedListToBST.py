# 109
from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    直接把链表弄成list再用divide and conquer变成BST即可
    """
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def buildBST(start, end, nums):
            if start > end:  # 自己画个array[1,2,3,4]动手算一次就可以知道条件
                return None
            mid = (start+end) // 2
            return TreeNode(nums[mid], buildBST(start, mid-1, nums), buildBST(mid+1, end, nums))
        
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        return buildBST(0, len(nums)-1, nums)

    def sortedListToBST1(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Base case: empty or only 1 element
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        # find mid
        prev = None
        slow, fast = head, head.next
        while fast and fast.next:
            prev = slow  # 记录slow的前一个node，后面用来拆分链表：left，mid，right
            slow, fast = slow.next, fast.next.next
        # now slow is at mid
        # 拆分出链表左半部分
        tail = slow.next
        slow.next = None
        """
        拆分出链表右半部分：
        1. 如果有prev，则把当前的slow去掉，即prev.next=None
        2. 如果没prev，则说明slow就是head，则拆分出来的链表左半部分应该为None，我们把head设为None即可
        """
        if prev:
            prev.next = None
        else:
            head = None
        # 递归构建左子树（用链表左半部分，即head）和右子树（用链表右半部分，即tail）
        return TreeNode(slow.val, self.sortedListToBST(head), self.sortedListToBST(tail))