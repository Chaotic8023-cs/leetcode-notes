# 106
from typing import *
from utils.pprintdp import pprintdp


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        道理同#105，只是root变成了postorder的最后有一个，然后postorder的前面显示left subtree再是right subtree
        """
        def dfs(i, j, n):
            if n == 0:
                return None
            v = postorder[j+n-1]
            k = d[v]
            l = dfs(i, j, k-i)
            # 右子树节点数 = 总数n - 左子树节点个数(k-i) - root的一个节点
            # 右子树的起始index = 当前postorder起始位置j + 左子树节点数(k-i)
            r = dfs(k+1, j+k-i, n-k+i-1)
            return TreeNode(v, l, r)

        d = {v: i for i, v in enumerate(inorder)}
        return dfs(0, 0, len(inorder))


if __name__ == '__main__':
    sol = Solution()

