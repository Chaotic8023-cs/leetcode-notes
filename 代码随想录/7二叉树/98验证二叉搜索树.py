from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    中序遍历：最简单直接的方法就是中序遍历得到数组，如果是有序（递增）的则是二叉树是合格的二叉搜索树。
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(root, ans):
            if not root:
                return
            inorder(root.left, ans)
            ans.append(root.val)
            inorder(root.right, ans)

        nums = []
        inorder(root, nums)
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                return False
        return True

    """
    边遍历边检查：用一个prev指针记录上一个访问的元素，并和当前的元素比较
    """
    def isValidBST1(self, root: Optional[TreeNode]) -> bool:
        def inorder(root):
            nonlocal prev
            if not root:
                return True
            a1 = inorder(root.left)
            if root.val <= prev:  # 用上一个元素和当前的元素比较
                return False
            prev = root.val
            a2 = inorder(root.right)
            return a1 and a2

        prev = -float('inf')
        return inorder(root)






