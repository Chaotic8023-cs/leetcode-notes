from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
后序遍历：traverse返回3个值：见过p，见过q，找到的lca
通过左右子树的发现来更新结果，并继续往上层传递结果
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse(root):
            if root is None:
                return False, False, None  # 见过p，见过q，找到的lca
            lp, lq, llca = traverse(root.left)
            rp, rq, rlca = traverse(root.right)
            # 根据当前节点root即左右子树的结果，看看有没有见过p和q
            seenP = lp or rp or root == p
            seenQ = lq or rq or root == q
            if llca or rlca:  # 已经找到lca，则继续往上传
                return True, True, llca or rlca
            elif seenP and seenQ:  # p和q都见过了，那么当前节点root就是lca
                return True, True, root
            else:  # 没见过pq或只见了其中一个，那么就继续往上传当前的结果
                return seenP, seenQ, None

        return traverse(root)[2]






