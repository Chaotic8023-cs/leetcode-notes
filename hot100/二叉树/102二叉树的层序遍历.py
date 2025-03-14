from typing import *
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
用一个queue，每次遍历当前层的节点个数次，且同时加入下一层的节点。
"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        q = deque([root])
        while q:
            curr_level = []
            for _ in range(len(q)):  # 每次遍历当前层的节点个数次，且同时加入下一层的节点
                node = q.popleft()
                curr_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(curr_level)
        return ans








