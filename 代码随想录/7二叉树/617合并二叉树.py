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
            merged = TreeNode(val)  # 构建新节点
            # 递归构建左右子树
            merged.left = traverse(root1.left if root1 else None, root2.left if root2 else None)
            merged.right = traverse(root1.right if root1 else None, root2.right if root2 else None)
            return merged

        return traverse(root1, root2)

    """
    方法2：以root1为基础，直接merge到root1上。这样会直接改变原来的root1，如果题目要求原来的root1和root2都不能动，则使用上面的方法。
    """
    def mergeTrees1(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        # 任一root为空，则直接由另一个root代替
        if root1 is None:
            return root2
        elif root2 is None:
            return root1
        # 此时root1和root2都不是None
        root1.val += root2.val  # 将root2的值merge到root1上
        # 递归构建合并root1的左右子树
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        # 返回合并后的root1
        return root1











