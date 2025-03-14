# 103
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # self try
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        同level order traversal，只是加了个reverse，在True和False之间交替来代表方向
        """
        ans = []
        if not root:
            return ans
        q = [root]
        reverse = False
        while q:
            level_len = len(q)
            level = []
            for _ in range(level_len):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if reverse:
                level = level[::-1]
            ans.append(level)
            reverse = not reverse
        return ans


if __name__ == '__main__':
    sol = Solution()
