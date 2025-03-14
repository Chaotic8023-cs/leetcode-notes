# 112
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 简洁版
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, sum):
            if not root:
                return False
            sum += root.val
            if root.left is None and root.right is None and sum == targetSum:
                return True
            return dfs(root.left, sum) or dfs(root.right, sum)

        return dfs(root, 0)

    # self try
    def hasPathSum1(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, sum):
            if not root:  # empty root
                return False
            if root.left is None and root.right is None:  # reach a leaf
                return sum + root.val == targetSum
            # 其实r1和r2可以直接省略，见上面的简介版解
            r1 = r2 = False
            if root.left:
                r1 = dfs(root.left, sum + root.val)
            if root.right:
                r2 = dfs(root.right, sum + root.val)
            return r1 or r2

        return dfs(root, 0)


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1, TreeNode(2))
    print(sol.hasPathSum(root, 1))
