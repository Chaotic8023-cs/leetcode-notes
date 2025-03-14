# 637
from typing import *
from utils.pprintdp import pprintdp


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        我们可以通过len(q)来直接看每层有多少个node，省去了记录depth
        在每次一直pop掉这层所有的node并同时把下层的push进queue
        """
        ans = []
        q = [root]
        while q:
            vals, n = 0, len(q)
            for _ in range(n):
                node = q.pop(0)
                vals += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(vals/n)
        return ans

    # self try
    def averageOfLevels1(self, root: Optional[TreeNode]) -> List[float]:
        d = {}
        q = [(root, 0)]
        while q:
            node, lv = q.pop(0)
            if lv not in d:
                d[lv] = [node.val]
            else:
                d[lv].append(node.val)
            if node.left:
                q.append((node.left, lv+1))
            if node.right:
                q.append((node.right, lv+1))
        ans = []
        for k, v in d.items():
            ans.append(sum(v) / len(v))
        return ans


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(sol.averageOfLevels(root))

