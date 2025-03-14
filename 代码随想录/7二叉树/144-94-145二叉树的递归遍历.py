from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
二叉树前中后序遍历的递归实现
"""
class Solution:
    """
    前序：中左右
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(curr, ans):
            if not curr:
                return
            ans.append(curr.val)
            traverse(curr.left, ans)
            traverse(curr.right, ans)

        ans = []
        traverse(root, ans)
        return ans

    """
    中序：左中右
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(curr, ans):
            if not curr:
                return
            traverse(curr.left, ans)
            ans.append(curr.val)
            traverse(curr.right, ans)

        ans = []
        traverse(root, ans)
        return ans

    """
    后序：左右中
    """
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(curr, ans):
            if not curr:
                return
            traverse(curr.left, ans)
            traverse(curr.right, ans)
            ans.append(curr.val)

        ans = []
        traverse(root, ans)
        return ans










