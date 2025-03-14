# 102
from typing import *
from utils.pprintdp import pprintdp


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        用BFS，每次先获取当前层的节点个数，即len(queue)，
        然后一次pop掉一层的nodes，并同时把子节点加入到queue中
        """
        if not root:
            return []
        ans = []
        q = [root]
        while q:
            level_length = len(q)
            level = []
            for _ in range(level_length):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)
        return ans





if __name__ == '__main__':
    sol = Solution()

