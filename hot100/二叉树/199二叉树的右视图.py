from typing import *
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
层序遍历，ans只加每层的最右边的节点即可
"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return ans
        q = deque([root])
        while q:
            for _ in range(len(q) - 1):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            rightmost = q.popleft()
            ans.append(rightmost.val)
            if rightmost.left:
                q.append(rightmost.left)
            if rightmost.right:
                q.append(rightmost.right)
        return ans





