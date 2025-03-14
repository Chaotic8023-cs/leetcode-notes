from typing import *
from math import inf


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    递归：和104二叉树的最大深度类似，但是这里要注意的是最小深度如果只把max改成min的话在某些情况下会出问题，比如根节点只有右子树，
    这时在根节点min会返回0，但其实左子树为空，不能算作一条路径。所以在选择左右子树的深度时，只有都>1的条件下才能用min(a, b) + 1！
    写法相当于后序，先统计左右子树的深度，再网上累加
    """
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        a = self.minDepth(root.left)
        b = self.minDepth(root.right)
        # 当有一侧没有子树时，选择有子树的另一侧
        if a == 0:
            return b + 1
        elif b == 0:
            return a + 1
        else:
            return min(a, b) + 1

    # 如果想不出来上面的普通递归，那就直接暴力遍历，遇到一个叶子节点就更新一次ans
    def minDepth1(self, root: Optional[TreeNode]) -> int:
        def traverse(root, d):
            if root is None:
                return
            nonlocal ans
            traverse(root.left, d + 1)
            if root.left is None and root.right is None:
                ans = min(ans, d)
            traverse(root.right, d + 1)

        ans = inf
        if root is None:
            return 0
        traverse(root, 0)
        return ans + 1





