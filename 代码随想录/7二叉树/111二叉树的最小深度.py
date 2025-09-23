from typing import *
from math import inf
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    递归：和104二叉树的最大深度类似，但是这里要注意的是最小深度如果只把max改成min的话在某些情况下会出问题，比如根节点只有右子树，
    这时在根节点min会返回0，但其实左子树为空，不能算作一条路径。所以在选择左右子树的深度时，只有都>1的条件下才能用min(a, b) + 1！
    写法相当于后序，先统计左右子树的深度，再网上累加
    """ 
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(root):
            if root is None:
                return 0
            l = traverse(root.left)
            r = traverse(root.right)
            # 当有一侧没有子树时，选择有子树的另一侧
            if l == 0:
                return r + 1
            elif r == 0:
                return l + 1
            return min(l, r) + 1

        return traverse(root)

    # 方法2:层序遍历，遇到的第一个叶节点就是最小的深度
    def minDepth1(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ans = 0  # 用来记录当前深度
        if root is None:
            return ans
        while q:
            ans += 1
            for _ in range(len(q)):
                curr = q.popleft()
                # 遇到的第一个叶节点就是最小深度
                if curr.left is None and curr.right is None:
                    return ans
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return ans

    # 如果想不出来上面的普通递归，那就直接暴力遍历，遇到一个叶子节点就更新一次ans
    def minDepth2(self, root: Optional[TreeNode]) -> int:
        def traverse(root, d):
            if root is None:
                return
            nonlocal ans
            traverse(root.left, d + 1)
            if root.left is None and root.right is None:
                ans = min(ans, d)
            traverse(root.right, d + 1)

        ans = inf
        if root is None:
            return 0
        traverse(root, 0)
        return ans + 1





