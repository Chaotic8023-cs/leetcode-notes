from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    运用BST的性质：我们从上往下搜索：
        1. 如果pq都比root小，则LCA一定在左子树
        2. 如果pq都比root大，则LCA一定在右子树
    我们返回第一个p和q分别在左右子树的节点，也就是LCA
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if root.val < p.val and root.val < q.val:  # 如果pq都比root小，则LCA一定在左子树，往左找
                root = root.right
            elif root.val > p.val and root.val > q.val:  # 如果pq都比root大，则LCA一定在右子树，往右找
                root = root.left
            else:  # 返回第一个找到的p和q分别在左右子树的节点，也就是pq的LCA
                return root

    """
    运用BST的性质：递归写法
    """
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root.val > p.val and root.val > q.val:
            left = self.lowestCommonAncestor(root.left, p, q)
            if left:
                return left
        elif root.val < p.val and root.val < q.val:
            right = self.lowestCommonAncestor(root.right, p, q)
            if right:
                return right
        else:  # pq分别位于左右子树，及当前的root就是LCA
            return root

    """
    当成普通二叉树做：#236
    """
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse(root):
            if root is None:
                return None
            if root == p or root == q:
                return root
            l = traverse(root.left)
            r = traverse(root.right)
            if l is not None and r is not None:
                return root
            return l or r

        return traverse(root)








