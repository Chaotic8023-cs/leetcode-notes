from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
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

    """
    后序遍历（自己写的），每个节点返回是否已经见过p和q，和找到的lca（没找到就是None）。
    其实返回值可以是单一的节点，但是“过于精简”，见下面的解法。
    还是记住上面那个更好，更简洁易懂。
    """
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse(root, p, q):
            if root is None:
                return False, False, None
            lp, lq, llca = traverse(root.left, p, q)  # 左子树是否出现过p，q；在左子树中是否已经找到了lca
            rp, rq, rlca = traverse(root.right, p, q)  # 右子树是否出现过p，q；在右子树中是否已经找到了lca
            # 根据当前节点及其子树来确定是否已经见过了p和q了。在返回前先更新hasP和hasQ确保了pq其中一个是另一个的祖先的情况，即其中一个就是最近公共祖先
            seenP = lp or rp or root == p
            seenQ = lq or rq or root == q
            # 如果已经在一个子树中找到了lca，则优先直接返回那个找到的lca
            if llca or rlca:
                return True, True, llca or rlca
            # 如果lca当前还没找到，但当前节点已经包含了p和q了，所以当前节点就是lca
            if seenP and seenQ:
                return True, True, root
            # 默认情况就是lca没找到，继续向上传递目前hasP和hasQ的状态
            return seenP, seenQ, None

        return traverse(root, p, q)[2]






