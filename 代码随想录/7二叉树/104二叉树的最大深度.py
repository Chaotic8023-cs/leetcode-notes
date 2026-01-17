from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    递归：当前节点的最大深度等于左右子树中的最大深度+1，相当于后序遍历
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(root):
            if root is None:
                return 0
            l = traverse(root.left)
            r = traverse(root.right)
            return max(l, r) + 1

        return traverse(root)

