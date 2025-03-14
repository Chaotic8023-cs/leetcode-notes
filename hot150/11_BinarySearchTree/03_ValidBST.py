# 98
import math
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # self try: inorder的时候顺便检查values是不是递增
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(root):
            if not root:
                return True
            a1 = inorder(root.left)
            nonlocal pre
            if root.val <= pre:  # 如果不是递增则不是BST
                return False
            pre = root.val
            a2 = inorder(root.right)
            return a1 and a2

        pre = -math.inf
        return inorder(root)

    # 稍微优化，一旦False直接return
    def isValidBST1(self, root: Optional[TreeNode]) -> bool:
        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            nonlocal pre
            if root.val <= pre:  # 如果不是递增则不是BST
                return False
            pre = root.val
            return inorder(root.right)

        pre = -math.inf
        return inorder(root)


if __name__ == '__main__':
    sol = Solution()
