from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
每次取中间的元素作为中节点，然后递归构建即可
"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])
        return node


"""
指针形式，无数组切片
"""
class Solution1:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildTree(l, r):  # 都是闭区间
            if l > r:  # 因为是闭区间，等于的情况说明还有一个元素可用，想象三个数的情况：[0,1,2]
                return None
            mid = (l + r) >> 1
            root = TreeNode(nums[mid])
            root.left = buildTree(l, mid - 1)
            root.right = buildTree(mid + 1, r)
            return root

        return buildTree(0, len(nums) - 1)

