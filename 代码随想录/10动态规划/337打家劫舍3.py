from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
打家劫舍树形dp版：
看到这种树形状态转移(就像#968监控二叉树)就用后序遍历！

普通打家劫舍种我们每次要看i-1和i-2，但树中只能看到子节点一层，怎么办呢？
解决办法是每一个节点用一个大小为2的dp数组来记录偷和不偷所能获得的最大金钱，这样当前几点就能运用这个信息进行选择了！
    1. 当前节点不偷：则它的左右子节点可以选择偷或不偷（不一定就非要偷！），所以就是左右子节点偷或不偷中最大的那个之和
    2. 当前节点偷： 则它的左右子节点一定不能偷，所以就是当前节点偷的金钱 + 左右子节点不偷所能获得的最大金钱
"""
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def traverse(root):
            if root is None:  # base case：金钱从0起步
                return 0, 0  # 不偷，偷
            ln, ly = traverse(root.left)
            rn, ry = traverse(root.right)
            not_steal = max(ln, ly) + max(rn, ry)  # 当前节点不偷时，它的子节点可以选择偷也可以选择不偷，而不是必须要偷！
            steal = root.val + ln + rn  # 当前节点偷时，子节点只能不偷
            return not_steal, steal

        return max(traverse(root))





