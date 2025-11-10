from collections import defaultdict
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
记前缀和版本
"""
class Solution:
    """
    暴力解法：因为路径不一定从整个树的根节点开始，所以我们在每个节点都进行一次深搜，统计起点为那个节点且路径和等于targetSum的路径的个数。
    """
    def pathSum1(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 搜索：以root为开始的路径和的个数
        def traverse(root, s):
            if root is None:
                return 0
            count = 0
            if s + root.val == targetSum:
                count += 1
            count += traverse(root.left, s + root.val)
            count += traverse(root.right, s + root.val)
            return count

        if root is None:
            return 0
        return traverse(root, 0) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

    """
    优化：前缀和，思路同#560和为k的子数组
    用cnt来记录不同prefix sum出现的次数，一开始前缀和为0的个数为1。使用前序遍历，先更新ans，即
    当前前缀和为s，如果前缀和s - targetSum的cnt存在，那么说明中间这段的和就是targetSum。更新
    ans之后，再更新当前前缀和s的cnt，因为我们每次更新ans的时候只要之前已经存在的cnt。
    和#560稍有不同的是，因为二叉树中的路径要求方向必须向下，即目当前的cnt仅在当前子树有效，
    所以从子树回来就要进行回溯，即删除刚才+1的cnt。
    """
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def traverse(root, s):
            if root is None:
                return
            nonlocal cnt, ans
            s += root.val
            # 当前前缀和为s，先更行ans
            ans += cnt[s - targetSum]
            # 再更新当前前缀和s的cnt，并在访问完子树后进行回溯操作
            cnt[s] += 1
            traverse(root.left, s)
            traverse(root.right, s)
            cnt[s] -= 1  # 从子树回来进行回溯
            s -= root.val  # 这里的s如果不回溯也不影响答案，因为s是local变量，之后不会再用到！

        cnt = defaultdict(int)
        cnt[0] = 1
        ans = 0
        traverse(root, 0)
        return ans






