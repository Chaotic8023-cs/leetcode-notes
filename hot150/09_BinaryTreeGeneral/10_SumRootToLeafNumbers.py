# 129
from typing import *
from utils.pprintdp import pprintdp


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 其实可以不用string转int，直接边遍历边算结果
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, s):
            if not root:
                return 0
            s = s * 10 + root.val  # 每次右边多一位数字，即当前的乘上10加这个数
            if root.left is None and root.right is None:
                return s
            return dfs(root.left, s) + dfs(root.right, s)

        return dfs(root, 0)

    # self try
    def sumNumbers1(self, root: Optional[TreeNode]) -> int:
        def dfs(root, nums):
            if not root:
                return 0
            nums += str(root.val)
            if root.left is None and root.right is None:
                return int(nums)
            return dfs(root.left, nums) + dfs(root.right, nums)

        return dfs(root, "")


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    print(sol.sumNumbers(root))

