from typing import *
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
二叉树前中后序遍历的迭代实现
"""
class Solution:
    """
    前序：中左右
    stack每次pop一个先记录val，也就是先中；然后放right再放left，这样就是先左后右。
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        stack = deque([root])
        while stack:
            curr = stack.pop()
            ans.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return ans

    """
    后序：左右中
    前序中的输出结果的顺序为中左右，那么经过以下两步：
        1. 调换入栈顺序，变成先左后右，则出栈顺序就也颠倒了，成先右后左，最终的结果就变为中右左
        2. 将最终的结果中右左反转，就变成了左右中
    即我们要的后序遍历！
    速记：调换入栈顺序并反转最终结果
    """
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        stack = deque([root])
        while stack:
            curr = stack.pop()
            ans.append(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return ans[::-1]

    """
    中序：左中右
    核心思想：用栈保存尚未访问的节点，以便在完成左子树的访问后能够返回到父节点
    1. 遍历左子树：一直往左走，并把途中的节点加入到栈中（保留未访问的节点）
    2. 访问中节点：此时左边没了（left == None），那么stack中pop出一个就为中节点，记录val
    3. 遍历右子树：我们直接设置curr为right，然后重新进入循环。这个循环就相当于递归，curr相当于当前要进行中序遍历的树，一开始为root，那么
       现在我们的中序遍历走完左和中了，所以设置curr为右节点就相当于要（递归）进行右子树的中序遍历了。
    速记：
        一直往左并入栈（左），弹出一个节点（中）并访问，设置curr为right（右）
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = deque()
        curr = root
        """
        循环就相当于一个递归，意义为进行以curr为根节点的中序遍历。
            1. curr：记录当前要进行中序遍历的根节点（左中右的“中”）
            2. stack：存储未来要访问的“中”节点（通过一直往左走并记录途中遇到的节点实现）
        （因为中序遍历本身就是递归，先进行左子树的中序遍历，然后中，最后进行右子树的中序遍历）
        为什么循环条件是or？当curr为None意味着上一个根的左子树的中序遍历已经结束（即刚才进行的是左子树的右子树的中序遍历然后结束了），
        此时该访问“中”了（即上一个根，记录在栈中），所以先弹出之前记录在栈中的“中”节点，然后记录到ans中，最后再进行右子树的中序遍历。
        """
        while stack or curr:
            # 遍历左子树：一直往左
            while curr:
                stack.append(curr)  # 记录未处理的节点
                curr = curr.left
            # 访问中节点
            curr = stack.pop()
            ans.append(curr.val)
            # 遍历右子树：设curr为右子树的根节点
            curr = curr.right  # 设curr为右节点相当于继续进行右子树的中序遍历
        return ans












