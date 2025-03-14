from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
前序遍历：直接翻转当前节点的左右子树，然后再递归翻转即可
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        # 翻转当前节点
        root.left, root.right = root.right, root.left
        # 再翻转左右子树
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root





