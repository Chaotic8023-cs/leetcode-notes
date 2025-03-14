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
        1. 如何找根节点？因为后序是左右中，所以后序的最后一个元素就是根节点。
        2. 如何找左右子树在两种遍历中的部分？我们知道根节点后，因为中序遍历是左中右，我们就可以找到根节点在中序遍历中的下标，于是中序遍历数组
        就能分成左中右三部分。对于后序遍历，虽然子树的遍历顺序和中序遍历不同，但因为子树遍历节点数相等，所以我们可以用从中序遍历数组提取出来
        的左右子树部分的长度来划分。
    """
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        mid = postorder[-1]  # 后序遍历数组的最后一个就是根节点
        curr = TreeNode(mid)
        # 分别找出中序和后序遍历中左右子树对应的部分
        mid_idx_inorder = inorder.index(mid)
        l_inorder = inorder[:mid_idx_inorder]
        r_inorder = inorder[mid_idx_inorder + 1:]
        l_postorder = postorder[:len(l_inorder)]
        r_postorder = postorder[len(l_inorder):len(postorder)-1]
        # 再递归构建左右子树
        curr.left = self.buildTree(l_inorder, l_postorder)
        curr.right = self.buildTree(r_inorder, r_postorder)
        return curr








