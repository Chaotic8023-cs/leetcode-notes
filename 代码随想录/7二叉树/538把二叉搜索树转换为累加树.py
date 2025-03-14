from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    交换左右的中序遍历：用一个全局变量curr_sum记录当前的累计和，然后遵循右中左遍历（统计比每个节点大的节点值之和），一直更新即可。
    """
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(root):
            if not root:
                return
            traverse(root.right)
            nonlocal curr_sum
            curr_sum += root.val
            root.val = curr_sum  # curr_sum就是右子树的节点值的和，即大于等于当前节点的所有节点之和
            traverse(root.left)

        curr_sum = 0
        traverse(root)
        return root

    """
    其实用双指针也行（prev）：即用一个prev来记录上一个节点的累加后的值即可。
    """
    def convertBST1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(root):
            if not root:
                return
            nonlocal prev
            traverse(root.right)
            root.val = root.val + prev
            prev = root.val
            traverse(root.left)

        prev = 0
        traverse(root)
        return root









