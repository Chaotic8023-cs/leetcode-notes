# 108
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    每次取中间的元素作为parent，并分别使用left和right子序列递归构建左子树和右子树
    """
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        l, mid_val, r = nums[:mid], nums[mid], nums[mid+1:]
        return TreeNode(mid_val, self.sortedArrayToBST(l), self.sortedArrayToBST(r))