# 530
from math import inf
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# self try
class Solution:
    def getMinimumDifference1(self, root: Optional[TreeNode]) -> int:
        """
        先中序遍历得到sorted array，再两两比对
        """

        def inorder(root):
            if not root:
                return []
            l1 = inorder(root.left)
            l2 = inorder(root.right)
            return l1 + [root.val] + l2

        sorted_vals = inorder(root)
        min_val = inf
        for i in range(len(sorted_vals) - 1):
            min_val = min(min_val, abs(sorted_vals[i] - sorted_vals[i + 1]))
        return min_val

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        可以中序遍历的时候边遍历边记录两两node的差，用一个pre来记录前一个node
        """

        def inorder(root):
            if not root:
                return
            nonlocal pre, ans
            inorder(root.left)
            ans = min(ans, abs(root.val - pre))
            pre = root.val
            inorder(root.right)

        pre = -inf
        ans = inf
        inorder(root)
        return ans


if __name__ == '__main__':
    sol = Solution()
