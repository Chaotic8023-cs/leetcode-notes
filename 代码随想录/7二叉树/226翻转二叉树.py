from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
用二叉树的遍历解决。注意，中序遍历会有问题，可以自己画一下就知道了。
其实中序也能写，就是逻辑比较绕，记的时候就记前序或者后序即可，或pythonic写法也行.

速记：
1. 前序：
    swap(l, r)
    invertTree(l)
    invertTree(r)

2. 后序：
    invertTree(l)
    invertTree(r)
    swap(l, r)

3. pythonic：
    l, r = invertTree(r), invertTree(l)
"""
class Solution:
    """
    前序遍历：从上到下交换左右子树
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # 直接交换当前节点的左右子树（中左右，先序）
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    """
    后序遍历：从下到上交换左右子树
    """
    def invertTree1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # 先翻转左右子树（左右中，后序）
        self.invertTree1(root.left)
        self.invertTree1(root.right)
        # 再交换换翻转好的左右子树
        root.left, root.right = root.right, root.left
        return root

    """
    后序遍历：比较绕，不要记！
    先翻转左子树，翻转好后到中了交换左右子树，交换前左子树已经翻转好了，右子树还没遍历到所以没动，交换完了左子树变成了没翻转的右子树，
    所以递归还要继续翻转左子树！
    """
    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # 先翻转左子树（左中右，中序）
        self.invertTree2(root.left)
        # 再交换翻转好的左子树，和没翻转的右子树
        root.left, root.right = root.right, root.left
        # 此时没翻转的右子树跑到左边了，所以还处理左边
        self.invertTree2(root.left)
        return root


    """
    Pythonic的写法：直接交换左右子树。这种写法是从下到上交换，即先换最底下的，递归回来的时候换中间的，最后换上面的.
    注意，写成两行不行：
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(root.left)
        因为root.left被修改成right之后，在修改right的时候用到的left就已经被覆盖了，原来的丢失了！
        所以用pythonic的写法就是写到一行，这样赋值是同时进行的就不会出现覆盖的情况。
    """
    def invertTree3(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree3(root.right), self.invertTree3(root.left)
        return root


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(4, TreeNode(7, TreeNode(9), TreeNode(6)), TreeNode(2, TreeNode(3), TreeNode(1)))
    print(sol.invertTree(root))
    print()


