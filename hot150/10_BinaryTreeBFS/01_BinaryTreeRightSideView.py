# 199
from typing import *
from utils.pprintdp import pprintdp
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # self try
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        BFS遍历树，每层取最后一个
        """
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            n = len(q)
            for _ in range(n-1):  # 其实可以直接 ans.append(q[-1].val)然后把这层全部pop掉
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            rightest = q.popleft()
            ans.append(rightest.val)
            if rightest.left:
                q.append(rightest.left)
            if rightest.right:
                q.append(rightest.right)
        return ans

    # 方法2：dfs，用深度优先，每次先遍历右子树，每层第一个遍历到的右子树的node即为right side view
    def rightSideView1(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, depth):
            if root is None:
                return
            if depth == len(ans):  # depth==len说明是每层第一个遍历到的（右子树）
                ans.append(root.val)
            dfs(root.right, depth+1)
            dfs(root.left, depth+1)

        ans = []
        dfs(root, 0)
        return ans


if __name__ == '__main__':
    sol = Solution()

