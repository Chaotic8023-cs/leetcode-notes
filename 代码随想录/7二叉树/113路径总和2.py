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
    前序遍历：前序遍历整个二叉树，如果找到一条路径等于目标的path则记录到ans中即可，类似回溯。
    要注意的两点：
        1. 只有到叶子节点才算真正的path！
        2. 不要用append，因为append直接就把原数组改了，用path + [root.val]这种会创建一个新list！
    """
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def traverse(root, curr_sum, targetSum, path, ans):  # curr_sum, path记录不包括当前节点的路径和及路径
            if not root:
                return
            curr_sum += root.val
            if not root.left and not root.right and curr_sum == targetSum:  # 只有到叶子节点才算真正的path！
                ans.append(path + [root.val])
            traverse(root.left, curr_sum, targetSum, path + [root.val], ans)
            traverse(root.right, curr_sum, targetSum, path + [root.val], ans)

        ans = []
        traverse(root, 0, targetSum, [], ans)
        return ans
    
    # 另一种写法，s和path每次都直接更新
    def pathSum1(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def traverse(root, s, path, ans):
            if root is None:
                return
            s += root.val
            path += [root.val]
            traverse(root.left, s, path, ans)
            traverse(root.right, s, path, ans)
            if root.left is None and root.right is None and s == targetSum:
                ans.append(path[:])
            path.pop()  # 由于path是mutable的，所以需要pop；而s是local变量，不需要再减一次
        ans = []
        traverse(root, 0, [], ans)
        return ans

