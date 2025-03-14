from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
前序遍历：定义一个函数sym来判断两个树是否对称
"""
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def sym(r1, r2):
            if r1 is None and r2 is None:  # 对称情况的base case，两个树需要同时为空
                return True
            if r1 is None or r2 is None or r1.val != r2.val:  # 不对称的情况
                return False
            # 左左对右右，左右对右左
            return sym(r1.left, r2.right) and sym(r1.right, r2.left)

        return sym(root.left, root.right)



