from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
先前序遍历，然后展开：直接进行一次前序遍历得到所有节点，然后在两两连接即可
"""
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def traverse(root):
            if root is None:
                return
            nonlocal preorder
            preorder.append(root)
            traverse(root.left)
            traverse(root.right)

        # 前序遍历得到节点
        preorder = []
        traverse(root)
        """
        两两连接，注意要把当前节点的左指针设为None，因为展开头所有节点只能有右指针。
        遍历中i是除了最后一个节点的所有节点，所以它们左指针都被清楚了，但最后一个节点是
        原树中右下角的节点，一定没有左指针，所以不用清除。
        """
        for i in range(len(preorder) - 1):
            preorder[i].right = preorder[i + 1]
            preorder[i].left = None
        return root
    

"""
边遍历边展开：逆前序遍历
我们发现前序遍历时，要设置的right指针是之后要遍历到的节点，无法获得。
但是，我们可以反着来，即由123456的遍历顺序变为654321，这样就可以“记住之后要遍历的节点”：先遍历6，然后在遍历5的时候，就可以把之前记住的6设为5的right child！
于是解法就是 逆前序遍历（根左右 -> 右左根）！（注意，和普通后序的 左右根 有所不同）。
"""
class Solution1:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def traverse(root):
            if root is None:
                return
            traverse(root.right)
            traverse(root.left)
            nonlocal prev
            root.left = None
            root.right = prev
            prev = root
        
        prev = None
        traverse(root)






