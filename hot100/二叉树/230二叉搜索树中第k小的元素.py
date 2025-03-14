from collections import deque
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
迭代中序遍历：迭代中序遍历方便统计当前经过的节点个数，所以在遍历中遇到第k个返回就行。
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = deque()
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            # 处理中节点
            curr = stack.pop()
            k -= 1
            if k == 0:  # 找到第k小的元素了（从小到大第k个）
                return curr.val
            curr = curr.right
