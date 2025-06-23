from typing import *
from math import inf
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    中序遍历：二叉搜索树的中序遍历是单调递增的有序数组，所以任意两个节点的差值最小时一定是数组中挨着的两个节点，所以进行中序遍历同时更新ans
    即可。
    """
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def traverse(root):
            if not root:
                return
            nonlocal ans, prev
            traverse(root.left)
            ans = min(ans, abs(root.val - prev))
            prev = root.val
            traverse(root.right)

        ans = float('inf')
        prev = -float('inf')
        traverse(root)
        return ans

    # 迭代中序遍历
    def getMinimumDifference1(self, root: Optional[TreeNode]) -> int:
        prev = -inf
        ans = inf
        stack = deque()
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            ans = min(ans, abs(curr.val - prev))
            prev = curr.val
            curr = curr.right
        return ans






