from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    按题意直接递归即可（前序）。
    """
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        mid = max(nums)
        mid_idx = nums.index(mid)  # 也可以一次得到mid和它的index：mid_idx, mid = max(enumerate(nums), key=lambda x: x[1])
        curr = TreeNode(mid)
        curr.left = self.constructMaximumBinaryTree(nums[:mid_idx])
        curr.right = self.constructMaximumBinaryTree(nums[mid_idx + 1:])
        return curr




