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
    


class Solution1:
    """
    最简单易记的版本：
    traverse返回：
        1. 在没找到LCA之前：以root为根节点的子树中找到的p或q（没找到就是None）
        2. 在找到LCA后：返回LCA
    此代码也恰好解决了p或q本身就是LCA的情况。
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse(root):
            if root is None:
                return None
            # 如果当前节点就是p/q，那么就直接返回找到的p/q（不用再往下找了）
            if root == p or root == q:
                return root
            l = traverse(root.left)
            r = traverse(root.right)
            # 如果pq分别在左右子树中找到，则当前root为LCA，直接返回LCA
            if l is not None and r is not None:
                return root
            # 在没找到LCA前：返回左右子树中找到p或q；在找到LCA后，返回的就是LCA
            return l or r

        return traverse(root)






