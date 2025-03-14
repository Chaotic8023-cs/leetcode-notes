from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    用后序遍历计算高度，自下向上，同时看是否平衡：为了不在每个节点都算一遍高度并比较，我们在统计高度的同时就看左右子树是否平衡，
    如果一个子树不平衡了，那么整个树也就不平衡了。所以我们算高度时看左右子树是否平衡，如果平衡就正常返回高度，如果不平衡直接返回-1，
    这样在上层就可以检查子树是否平衡了。
    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            l = height(root.left)
            r = height(root.right)
            # 如果子树不平衡直接返回-1（l == -1 or r == -1），如果当前节点不平衡也直接返回-1（abs(l - r) > 1）
            if l == -1 or r == -1 or abs(l - r) > 1:
                return -1
            else:
                return max(l, r) + 1  # 一个节点的高度是左右子树中最高的那个+1

        return height(root) != -1  # 如果从root能正常算出高度（不为-1），则说明所有子树都平衡






