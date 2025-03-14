from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    递归：我们知道树的递归遍历其实就是递归，也就是说子树的遍历顺序也符合整个树的顺序。所以，我们每次先找到根节点，然后找到左右子树在中序和后序中
    对应的部分，递归构建树即可。具体步骤如下：
        1. 如何找根节点？因为前序是中左右，所以前序的第一个元素就是根节点。
        2. 如何找左右子树在两种遍历中的部分？我们知道根节点后，因为中序遍历是左中右，我们就可以找到根节点在中序遍历中的下标，于是中序遍历数组
        就能分成左中右三部分。对于前遍历，虽然子树的遍历顺序和中序遍历不同，但因为子树遍历节点数相等，所以我们可以用从中序遍历数组提取出来
        的左右子树部分的长度来划分。
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        mid = preorder[0]  # 前序遍历数组的第一个就是根节点
        curr = TreeNode(mid)
        # 分别找出前序和中序遍历中左右子树对应的部分
        mid_idx_inorder = inorder.index(mid)
        l_inorder = inorder[:mid_idx_inorder]
        r_inorder = inorder[mid_idx_inorder + 1:]
        l_preorder = preorder[1:len(l_inorder) + 1]
        r_preorder = preorder[len(l_inorder) + 1:]
        # 再递归构建左右子树
        curr.left = self.buildTree(l_preorder, l_inorder)
        curr.right = self.buildTree(r_preorder, r_inorder)
        return curr
