from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    一看到满足xxx的路径，就想前序！前序不返回值，而是遇到一个满足的节点直接更新（全局的）ans。
    前序遍历：直接前序遍历二叉树，找到一个叶子节点时判断当前的路径和是否等于目标即可。要注意的就是只有是叶子节点才算是一条路径！
    """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(root, curr_sum, targetSum):  # curr_sum记录不包含当前节点root的路径和
            if not root:
                return
            curr_sum += root.val
            nonlocal ans
            if not root.left and not root.right and curr_sum == targetSum:  # 叶子节点才算路径
                ans = True
            traverse(root.left, curr_sum, targetSum)
            traverse(root.right, curr_sum, targetSum)

        ans = False
        traverse(root, 0, targetSum)
        return ans

    """
    普通遍历也行，没必要使用nonlocal：前中后序都行（if s + root.val == targetSum这个判断放到两个traverse前面，中间和后面都行！）
    """
    def hasPathSum1(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(root, s):
            if root is None:
                return False
            if s + root.val == targetSum and root.left is None and root.right is None:  # 叶子节点才算路径
                return True
            l = traverse(root.left, s + root.val)
            r = traverse(root.right, s + root.val)
            return l or r

        return traverse(root, 0)





