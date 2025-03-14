from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    后序遍历：根普通构从数组建二叉树的思想一样，只是这里把数组换成两个二叉树了。我们同时遍历两个二叉树，并根据两个二叉树的当前节点构建
    新树的节点，并递归构构建子节点。
    """
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(root1, root2):
            if not root1 and not root2:  # 终止条件：只有两个树的节点都为空才停
                return None
            # 构建新树的当前节点
            val = 0
            if root1:
                val += root1.val
            if root2:
                val += root2.val
            merged = TreeNode(val)
            # 递归构建左右子树
            merged.left = traverse(root1.left if root1 else None, root2.left if root2 else None)
            merged.right = traverse(root1.right if root1 else None, root2.right if root2 else None)
            return merged

        return traverse(root1, root2)











