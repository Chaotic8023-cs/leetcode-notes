from typing import *
from math import inf


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
中序遍历：
中序遍历二叉搜索树就是排序号的数组，我们边遍历边比较前一个元素（用prev记录）和当前元素，如果当前元素不比前一个大则直接return False即可
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(root):
            if root is None:
                return True
            nonlocal prev
            l = traverse(root.left)
            if root.val <= prev:
                return False
            prev = root.val
            r = traverse(root.right)
            return l and r

        prev = -inf  # 一开始“if root.val <= prev:”不能为True，所以设置成-inf
        return traverse(root)






