from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
和#124二叉树中的最大路径和类似，本题不再考虑节点值，而是路径长度。
traverse返回的是以root为结尾（包含）的最大（单条）路径上的节点数。
为了方便我们算的是最大路径上的节点个数，所以最后-1
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def traverse(root):
            if root is None:
                return 0
            nonlocal ans
            l = traverse(root.left)
            r = traverse(root.right)
            ans = max(ans, l + r + 1)  # 更新ans时左中右路径连起来算，因为为了方便理解我们统计的是节点个数，所以是左右+当前节点
            return max(l, r) + 1  # 返回的是以当前节点为结尾的“单边”路径上的节点数，就是左右子树中最大的再 + 1

        ans = 0
        traverse(root)
        return ans - 1  # 由于我们为方便统计的是节点数，最后求的是路径，所以是节点数-1




