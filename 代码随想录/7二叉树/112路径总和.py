from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    一看到满足xxx的路径，就想前序！前序不返回值，而是遇到一个满足的节点直接更新（全局的）ans。
    前序遍历：直接前序遍历二叉树，找到一个叶子节点时判断当前的路径和是否等于目标即可。要注意的就是只有是叶子节点才算是一条路径！
    """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(root, curr_sum, targetSum):  # curr_sum记录不包含当前节点root的路径和
            if not root:
                return
            curr_sum += root.val
            nonlocal ans
            if not root.left and not root.right and curr_sum == targetSum:  # 叶子节点才算路径
                ans = True
            traverse(root.left, curr_sum, targetSum)
            traverse(root.right, curr_sum, targetSum)

        ans = False
        traverse(root, 0, targetSum)
        return ans

    """
    后序遍历也可以，不用记，其实中序也行
    """
    def hasPathSum1(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(root, curr_sum, target_sum):
            if not root:
                return False
            curr_sum += root.val
            l = traverse(root.left, curr_sum, target_sum)
            r = traverse(root.right, curr_sum, target_sum)
            if not root.left and not root.right and curr_sum == targetSum:
                return True
            return l or r

        return traverse(root, 0, targetSum)





