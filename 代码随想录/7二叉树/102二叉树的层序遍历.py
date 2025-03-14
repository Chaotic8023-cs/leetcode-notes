from collections import deque
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    层序遍历用队列：每次遍历一层的节点，即每次遍历len(q)个，同时加入下一层的节点
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        q = deque([root])
        while q:
            l = []
            for _ in range(len(q)):  # 每次遍历当前一层，同时加入下一层的节点
                curr = q.popleft()
                l.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            ans.append(l)
        return ans







