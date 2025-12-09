from collections import *
from typing import *


"""
面经中看到的题：找到二叉搜索树中小于（等于）m 的最大值

重点是得搜索完，直到搜索到leaf为止（当前节点是None），因为找到第一个 <m 的node后，右子树种可能还会有更大的但还是小于m的节点！
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1. <= m
def floor_in_bst(root: TreeNode, m: int):
    """
    返回 BST 中小于等于 m 的最大值。
    若不存在，返回 None。
    """
    ans = None
    node = root

    while node:
        if node.val == m:       # 刚好等于，直接返回
            return node.val
        elif node.val < m:      # 比 m 小，是候选，往右找更大
            ans = node.val
            node = node.right
        else:                   # 比 m 大，只能往左找
            node = node.left

    return ans


# 2. < m
def predecessor_in_bst(root: TreeNode, m: int):
    """
    返回 BST 中严格小于 m 的最大值。
    若不存在，返回 None。
    """
    ans = None
    node = root

    while node:
        if node.val < m:         # 只要严格小于 m，就是候选
            ans = node.val
            node = node.right    # 看右子树里有没有更大但仍 < m 的
        else:
            # node.val >= m，太大或刚好等于，往左缩小
            node = node.left

    return ans








