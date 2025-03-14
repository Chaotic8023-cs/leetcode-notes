from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    前序遍历递归删除：和删除单一节点类似，但逻辑稍微简单一些，对于当前的节点root：
        1. 如果root小于low，说明root的左子树都比low小，所以返回递归修剪后的右子树
        2. 如果root大于high，说明root的右子树都比high大，所以返回递归修剪后的左子树
    要注意是不能直接返回左/右子树，因为它们里面也可能有不符合的节点，所以要递归继续修剪！
    """
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # 中
        if not root:
            return None
        if root.val < low:  # 当前节点小于low了，说明它的左子树也都小于low，所以把修剪后的右子树直接返回（不能直接返回右子树，因为右子树中也可能有要trim的）
            return self.trimBST(root.right, low, high)
        if root.val > high:  # 同理：当前节点大于high了，说明它的右子树也都大于high，所以把修剪后的左子树直接返回
            return self.trimBST(root.left, low, high)
        # 左右：当前root不需要修剪，所以修剪左右子树然后返回
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root






