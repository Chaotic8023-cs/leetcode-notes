from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    把判断对称转换为判断左右节点是否相等：新定义一个函数sym，给根节点的左右子节点，先判断左右节点值相等，再递归判断左右节点的两组子树是否相等
    其实是后序遍历，因为先递归判断两组子树是否相同，再返到当前节点判断当前节点的值是否相等。
    """
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def sym(l, r):  # lr为要对比的左右子节点
            if not l and not r:  # lr都没说明对称
                return True
            if not l or not r:  # lr其中有一个没有说明不对称
                return False
            # 如果lr都存在，则需要满足左右子节点值相等，然后递归判断左右子节点的两组子树是否相等（相当于后序遍历）
            return l.val == r.val and sym(l.left, r.right) and sym(l.right, r.left)

        return sym(root.left, root.right)




