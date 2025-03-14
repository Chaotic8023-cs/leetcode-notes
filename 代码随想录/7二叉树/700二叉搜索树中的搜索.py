from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    二叉搜索树的搜索：左小右大，即target比当前root小往左走，大往右走
    """
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if val == root.val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right
        return None









