# 222
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 二分查找，O(log^2(n)), depth计算是O(log(n)), 然后二分查找一共O(log(n))次，所以最终是O(log^2(n))，即log(n)的平方
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        先统计左子树和右子树的高度
        若左子树高度等于右子树高度，则左子树一定是完全二叉树，其节点个数等于2^d-1,加上当前的root就是2^d，然后再递归加上右子树
        若左子树高度大于右子树，则右子树一定是完全二叉树(比左子树少最后一层)，同第一种情况，2^d然后递归加上左子树的节点个数
        """

        def depth(root):
            d = 0
            while root:
                d += 1
                root = root.left
            return d

        if root is None:
            return 0
        left, right = depth(root.left), depth(root.right)
        if left == right:  # root.left is a full binary tree
            return 2 ** left + self.countNodes(root.right)
        return 2 ** right + self.countNodes(root.left)

    # self try: just dfs, O(n) time, not good, require less than O(n)!
    def countNodes1(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            return 1 + dfs(root.left) + dfs(root.right)

        return dfs(root)


if __name__ == '__main__':
    sol = Solution()
