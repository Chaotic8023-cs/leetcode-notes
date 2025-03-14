from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    递归插入：按构造树的方法递归插入即可
    """
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:  # 到插入位置了，返回新节点即可
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

    """
    迭代插入
    """
    def insertIntoBST1(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = prev = root
        while curr:
            prev = curr
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        if not prev:  # root为空的情况
            return TreeNode(val)
        # 根据prev节点的大小选择插入位置
        if val < prev.val:
            prev.left = TreeNode(val)
        else:
            prev.right = TreeNode(val)
        return root





