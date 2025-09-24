from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
先序遍历：先序遍历二叉树，递归时更新目前的path，只有遇到叶节点才把当前的path加入到ans中
"""
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def traverse(root, path, ans):
            if root is None:  # 应对某些节点只有一边有子树
                return
            if root.left is None and root.right is None:  # 只有叶节点才算一条合法的path
                ans.append(path + str(root.val))
                return
            traverse(root.left, path + f"{root.val}->", ans)
            traverse(root.right, path + f"{root.val}->", ans)

        ans = []
        traverse(root, "", ans)
        return ans
    
# 另一种写法：最后用 "->" 来join，path只记录节点
class Solution1:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def traverse(root, path, ans):
            if root is None:
                return
            if root.left is None and root.right is None:
                ans.append("->".join(path + [str(root.val)]))
                return
            traverse(root.left, path + [str(root.val)], ans)
            traverse(root.right, path + [str(root.val)], ans)

        ans = []
        traverse(root, [], ans)
        return ans



