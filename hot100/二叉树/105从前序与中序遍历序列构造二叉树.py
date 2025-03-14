from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
preorder: 中左右
inorder：左中右
preorder的第一个元素就是中节点，通过这个中节点我们就能从inorder中找到左右子树对应元素的子数组，之后就能从preorder中也提取同样部分，
最后递归构建二叉树即可。
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        # preorder的第一个元素就是中节点
        mid =  preorder[0]
        root = TreeNode(mid)
        # 通过这个中节点把inorder的左子树和右子树对应的元素分出来，然后通过得到的左右子树元素多少在从preorder里提取同样的部分
        mid_idx = inorder.index(mid)
        inorder_l = inorder[:mid_idx]
        inorder_r = inorder[mid_idx + 1:]
        preorder_l = preorder[1:len(inorder_l) + 1]
        preorder_r = preorder[1 + len(inorder_l):]
        # 最后递归构建二叉树即可
        root.left = self.buildTree(preorder_l, inorder_l)
        root.right = self.buildTree(preorder_r, inorder_r)
        return root






