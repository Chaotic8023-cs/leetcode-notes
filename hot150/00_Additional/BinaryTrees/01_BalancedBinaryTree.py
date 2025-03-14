# 110
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            hl, hr = dfs(node.left), dfs(node.right)
            if hl == -1 or hr == -1 or abs(hl - hr) > 1:
                return -1
            return max(hl, hr) + 1

        return dfs(root) != -1

tree = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, None, None), None), None),
                TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, None))))

sol = Solution()
sol.isBalanced(tree)
print()


