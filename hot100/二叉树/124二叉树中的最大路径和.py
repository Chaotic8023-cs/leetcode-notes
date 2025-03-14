from typing import *
from math import inf


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    """
    后序遍历+动态规划思想：我们定义traverse(root)为终点为root的最大路径和（注意是终点，即路径为单条的意思，前面只能来自左边或右边），
    用后序遍历遍历二叉树，每次到一个节点就把root和左右两侧的最大单条路径合起来，看有没有更大。需要注意的就是这个traverse的定义，一定是
    终点为root，所以每次能把左中右连起来。同时，根据定义，traverse的返回值也必须满足它的定义，以便它的父节点能把左右两边的路径和连起来，
    所以返回的是lr中最大的那个路径和加上当前节点的数值。
    """
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def traverse(root):
            if not root:
                return 0
            # l/r表示从树底开始，终点到l/r（包括l/r）的最大路径和，可以为0（即不包含终点l/r，说明全是负数）
            l = traverse(root.left)
            r = traverse(root.right)
            nonlocal ans
            # 更新ans时加上root，看左中右这条路径是否更大。如果l=0，则路径是中右，如果r为0，则路径是左中，如果lr都为0，则路径只右当前节点
            ans = max(ans, l + root.val + r)
            """
            因为traverse(root)表示的是终点为root（包含）的最大路径（单条，即不能从左边上来经过root再往右边去），
            所以要选左右两边最大的加上root。如果此时最大的路径和都是负数了，那么就直接不选当前root，所以直接返回0。
            """
            return max(0, max(l, r) + root.val)

        ans = -inf  # 不能一开始就是0，因为有可能最大路径和为负数！（比如只有一个节点，值为-3）
        traverse(root)
        return ans






