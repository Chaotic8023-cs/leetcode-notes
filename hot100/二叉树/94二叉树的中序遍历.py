from collections import deque
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
细节见代码随想录
"""
class Solution:
    """
    递归
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root):
            if root is None:
                return
            nonlocal ans
            traverse(root.left)
            ans.append(root.val)
            traverse(root.right)

        ans = []
        traverse(root)
        return ans

    """
    迭代
    """
    def inorderTraversal_it(self, root: Optional[TreeNode]) -> List[int]:
        stack = deque()
        curr = root  # curr表示中节点
        ans = []
        while stack or curr:
            # 遍历左子树：一直往左
            while curr:
                stack.append(curr)  # 记录未处理的节点
                curr = curr.left
            # 访问中节点
            curr = stack.pop()
            ans.append(curr.val)
            # 遍历右子树：设curr为右子树的根节点
            curr = curr.right  # 设curr为右节点相当于继续进行右子树的中序遍历
        return ans







