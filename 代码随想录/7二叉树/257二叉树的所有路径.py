from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    先序遍历：先序遍历二叉树，递归时更新目前的path，只有遇到左右子树都为空的情况才把当前的path加入到ans中
    """
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def preorder(root, path, ans):
            if not root:
                return  # 其实是回溯
            if not root.left and not root.right:  # 只有左右子树都为空才算一条路径
                ans.append(path + str(root.val))
            # 递归时更新已经走过的路径
            preorder(root.left, path + f"{root.val}->", ans)
            preorder(root.right, path + f"{root.val}->", ans)

        ans = []
        preorder(root, "", ans)
        return ans



