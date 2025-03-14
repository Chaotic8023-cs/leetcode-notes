# 114
from typing import *
from utils.pprintdp import pprintdp


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(1) Space
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        递归思想解决：
        因为顺序是preorder，所以左子树一定出现在右子树前，
        右子树第一个node的前一个node一定是当前root的predecessor
        所以我们先把当前root的右子树接到当前root的predecessor的右下，
        然后把当前root的左子树(包含了在predecessor右下接着的原右子树)挪到右子树位置上作为右子树
        当然代码实现是先将predecessor的right设为root的right，然后把root的right设为root的left，最后root.left=Node即可
        例如下图：
                1                        1
            2       5           ->          2
          3   4   6   7                  3      4
                                                  5
                                               6     7
        最后再recursively解决root.right
        其实就相当于做了等价变换，此时root下面变换好一次的树(root.right)按照preorder的话等价于原来的root的左右子树进行preorder！
        所以我们又可以把root.right(例子中的2)看做root，重新进行上述操作，只要当前的root有左子树就变换一次，直到最后全部变换完成.
        """
        while root:
            if root.left:
                # find predecessor
                pre = root.left
                while pre.right:
                    pre = pre.right
                pre.right = root.right
                root.right = root.left
                root.left = None
            root = root.right

    # self try
    def flatten1(self, root: Optional[TreeNode]) -> None:
        """
        就是先一遍preorder记录所有node的指针，然后再连起来，O(n) space
        """
        nodes = []

        def preorder(node):
            if not node:
                return
            nodes.append(node)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        dummy = TreeNode()
        h = dummy
        for node in nodes:
            node.left = None
            h.right = node
            h = node
        return dummy.right


if __name__ == '__main__':
    sol = Solution()
