# 173
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(d) space, where d is the depth, utilize stack
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        """
        inorder：左 -> 中间 -> 右
        用一个stack，初始化时把最左边的一列push进stack里
        其实是参照了inorder的顺序，先left再中再右，一开始左边一列在stack
        第一个pop出来的就是最小的那个node(按递归思想想，其实这个node是看作中间node，其左子树为空)，即BST左下角的那个node
        每次pop出node，按inorder的顺序接下来应该是这个node的右子树的inorder traversal
        即按递归思想应该inorder(node.right),我们就还是和之前操作一样，以当前node.right为root
        一直循环压入左节点即可，这样整体来看顺序符合inorder
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        root = node.right
        while root:
            self.stack.append(root)
            root = root.left
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# self try: 记录了所有节点，不efficient！
class BSTIterator1:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = []
        self.idx = -1
        self.inorder(root)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.nodes.append(root)  # 其实只要val，不需要node
        self.inorder(root.right)

    def next(self) -> int:
        self.idx += 1
        return self.nodes[self.idx].val

    def hasNext(self) -> bool:
        return self.idx + 1 < len(self.nodes)


if __name__ == '__main__':
    pass
