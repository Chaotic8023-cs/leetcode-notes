from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
先前序遍历，然后展开：直接进行一次前序遍历得到所有节点，然后在两两连接即可
"""
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def traverse(root):
            if root is None:
                return
            nonlocal preorder
            preorder.append(root)
            traverse(root.left)
            traverse(root.right)

        # 前序遍历得到节点
        preorder = []
        traverse(root)
        """
        两两连接，注意要把当前节点的左指针设为None，因为展开头所有节点只能有右指针。
        遍历中i是除了最后一个节点的所有节点，所以它们左指针都被清楚了，但最后一个节点是
        原树中右下角的节点，一定没有左指针，所以不用清除。
        """
        for i in range(len(preorder) - 1):
            preorder[i].right = preorder[i + 1]
            preorder[i].left = None
        return root






