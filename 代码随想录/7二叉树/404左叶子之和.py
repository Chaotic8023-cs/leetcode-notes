from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    后序遍历加上一个flag用来看是否是左子节点：后序遍历二叉树，并且到加上一个flag记录当前节点是左子树还是右子树。只有是叶子节点且属于左子树时，
    才算数值。
    """
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def traverse(root, is_left):
            if not root:
                return 0
            l = traverse(root.left, True)
            r = traverse(root.right, False)
            if root.left is None and root.right is None and is_left:  # 只有左叶子节点算
                return root.val
            return l + r  # 中间的节点不算，所以直接返回左右子树的值

        return traverse(root, False)

    """
    不用flag的后序遍历写法（不用看）：普通后序只加上了一个在中时判断左子树是否为叶子。这样即使是叶子节点也返回0，只有包含左叶子的节点才会把
    left_sum设为左叶子的值！
    """
    def sumOfLeftLeaves1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_sum = self.sumOfLeftLeaves1(root.left)
        # 判断当前节点（左中右的中）的左节点是否为叶子
        if root.left and not root.left.left and not root.left.right:
            left_sum = root.left.val
        right_sum = self.sumOfLeftLeaves1(root.right)
        # 其实判断放到这也行，因为左右子树都遍历完才return一个值，所以还是算后序遍历！
        return left_sum + right_sum  # 中间节点不算，所以直接返回左右子树的结果之和







