from typing import *
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
普通层序遍历然后结果中奇数层反转即可
"""
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 普通层序遍历
        q = deque([root])
        ans = []
        if root is None:
            return ans
        while q:
            lvl = []
            for _ in range(len(q)):
                curr = q.popleft()
                lvl.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            ans.append(lvl)
        # 反转奇数层
        for i in range(len(ans)):
            if i % 2 == 1:
                ans[i] = ans[i][::-1]
        return ans



