# 101
from typing import *
from utils.pprintdp import pprintdp


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
我们先不看root，我们发现，两个tree如果是对称的话，
那么首先这两个tree的root value相等，其次
tree1.left和tree2.right对称，同时tree1.right
和tree2.left对称。
所以我们就可以递归写，每次给两个树，判断它们的root value
即它们的subtree的对称性。对于单独的root怎么办，我们直接
pass两个root的左右subtree到上述function中即可。
甚至我们可以直接pass相同的两个root进去也行，只是对于root来说
会判断左右对称和右左对阵，重复判断了一次。
"""


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSym(tree1, tree2):
            if tree1 is None and tree2 is None:
                return True
            if tree1 is None or tree2 is None or tree1.val != tree2.val:
                return False
            return (tree1.val == tree2.val and
                    (isSym(tree1.left, tree2.right)
                     and isSym(tree1.right, tree2.left)))
        # return isSym(root, root)  # 直接两个root也行
        return isSym(root.left, root.right)


if __name__ == '__main__':
    sol = Solution()
