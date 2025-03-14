from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    按照普通二叉树算：直接后序遍历：当前二叉树的节点数 = 左子树的节点数 + 右子树的节点数 + 1
    也可以用层序遍历做
    """
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

    """
    利用满二叉树及完全二叉树的性质的性质：完全二叉树只有最后一层不满，所以它中间的某个节点（原树的左半部分）一定是一个满二叉树，所以我们可以
    给上面普通的遍历中加上判断当前root是否为满二叉树，如果是则直接用公式2*k-1算，就省了一些节点的遍历！
    如何判断root为满二叉树？看一直往左走的节点数是否和一直往右走的节点数相等
    """
    def countNodes1(self, root: Optional[TreeNode]) -> int:
        # base case：空节点
        if not root:
            return 0
        # 看当前的root是否为满二叉树，如果是就可以直接用公式算：2^k - 1
        l, r = 0, 0
        curr = root
        while curr:
            l += 1
            curr = curr.left
        curr = root
        while curr:
            r += 1
            curr = curr.right
        if l == r:  # 当前root为满二叉树，直接用公式
            return 2 ** l - 1
        else:  # 当前节点不是满二叉树，则按普通二叉树做
            return self.countNodes1(root.left) + self.countNodes1(root.right) + 1






