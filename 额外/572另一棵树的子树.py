from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
更简单的写法（记这个）：
辅助函数same不变，在每个节点都call一次same即可。
"""
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def same(r1, r2):
            if r1 is None and r2 is None:
                return True
            elif r1 is None or r2 is None:
                return False
            return r1.val == r2.val and same(r1.left, r2.left) and same(r1.right, r2.right)

        if root is None:
            return False
        # 当前节点调用same，并递归处理左右子树
        return same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


"""
自己写的：
对root进行遍历，遇到当前节点的值等于subRoot的值，则调用辅助函数same来判断以当前节点为根节点的子树是否和subRoot一样。
注意，原树可能存在重复节点值，所以每遇到一个和subRoot值相等的节点都要判断一次！
"""
class Solution1:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def traverse(root, subRoot):
            if root is None:
                return
            nonlocal ans
            if root.val == subRoot.val:
                ans = ans or same(root, subRoot)  # 原树可能存在重复节点值，所以每遇到一个和subRoot值相等的节点都要判断一次
            traverse(root.left, subRoot)
            traverse(root.right, subRoot)

        def same(r1, r2):
            if r1 is None and r2 is None:
                return True
            elif r1 is None or r2 is None:
                return False
            return r1.val == r2.val and same(r1.left, r2.left) and same(r1.right, r2.right)

        ans = False
        traverse(root, subRoot)
        return ans







