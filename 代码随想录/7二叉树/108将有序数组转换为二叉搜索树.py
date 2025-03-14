from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    直接递归构建二叉树即可，每次取中见的元素作为root
    """
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        mid = len(nums) // 2  # 左闭右开/左闭右闭均可以
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root

    """
    双指针版
    """
    def sortedArrayToBST1(self, nums: List[int]) -> Optional[TreeNode]:
        def traverse(nums, left, right):  # 左闭右开
            if left == right:
                return None
            mid = (left + right) >> 1
            root = TreeNode(nums[mid])
            root.left = traverse(nums, left, mid)
            root.right = traverse(nums, mid + 1, right)
            return root

        return traverse(nums, 0, len(nums))











