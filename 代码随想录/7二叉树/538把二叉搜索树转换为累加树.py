from typing import *
from collections import deque


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
    
class Solution1:
    """
    迭代逆中序遍历法:
    普通中序遍历是左中右，由于我们遍历的顺序想按节点值从大到小，所以反过来，右中左。
    放到迭代中序遍历中则是将对应地方都反过来即可。这样维护一个全局的curr_sum就很自然了。
    """
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        stack = deque()
        curr_sum = 0  # 全局 当前累加值
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.right  # 反过来
            curr = stack.pop()
            curr.val += curr_sum
            curr_sum = curr.val
            curr = curr.left  # 反过来
        return root









