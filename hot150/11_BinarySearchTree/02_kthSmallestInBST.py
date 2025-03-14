# 230
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # self try
    def kthSmallest1(self, root: Optional[TreeNode], k: int) -> int:
        """
        inorder的时候计数，return第k个即为kth smallest
        """
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            nonlocal count, ans
            count -= 1
            if count == 0:
                ans = root.val
            inorder(root.right)

        count = k
        ans = 0
        inorder(root)
        return ans

    # inorder还可以用stack来做
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        stack也可以用来做inorder：
        先一直push左子树的nodes，再pop掉一个，即最左下角的node，然后开始访问右子树
        inorder顺序是左中右，我们把stack中的node都看作为中，所以每次先把所有node.left全push进去，等于是先访问左子树
        等这个node pop出来的时候，我们设置cur = node.right，即访问完中，用同样的inorder访问右子树
        """
        stk = []
        cur = root
        while cur or stk:
            while cur:  # reach the leftmost
                stk.append(cur)
                cur = cur.left
            node = stk.pop()
            k -= 1
            if k == 0:
                return node.val
            cur = node.right  # visit right subtree


if __name__ == '__main__':
    sol = Solution()
    bst = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    ans = sol.kthSmallest(bst, 1)
    print(ans)

