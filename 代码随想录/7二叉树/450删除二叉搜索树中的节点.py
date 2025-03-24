from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
递归：记这个
"""
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        # 如果key比root小，则在左子树递归删除
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        # 如果key比root大，则在右子树递归删除
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        # 要删除的就是当前节点root
        else:
            # 情况1：root为leaf，则可以直接删除，即返回None
            if root.left is None and root.right is None:
                return None
            # 情况2：root的左/右子树为空，则可以直接删除，即返回root的右/左子树
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # 情况3：root的左右子树都不为空，则先找到successor，把root的的左子树接到successor的左child上，然后直接返回root.right（相当于把root删掉了）即可。
            else:
                succ = root.right
                while succ.left:
                    succ = succ.left
                succ.left = root.left
                return root.right


class Solution1:
    """
    自己写的递归：找到要删除的节点，如果是叶子就直接删，中间节点的话继续递归找到successor，然后root和successor交换值，最后删除successor。
    这题要注意的就是因为successor是先往右再一直往左，找到这个successor不一定就是叶子，因为successor它本身可能还有右子树，所以要把它的右子树
    接上！

    问题：存在节点值的交换，而不是真正的删除！！！
    """
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:  # 没找到，树不会变
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:  # found key
            if not root.left and not root.right:  # 叶子节点，直接删除即可
                return None
            else:  # 中间节点，找到successor
                return self.delete_internal(root)
        return root

    def delete_internal(self, root):  # root就是要删除的节点，先和successor交换值，再删除successor
        prev = root
        curr = root.right
        while curr and curr.left:
            prev = curr
            curr = curr.left
        # 现在curr就是successor
        if not curr:  # 要删除的节点无右子树，所以直接把左子树接到root上即可
            return root.left
        elif prev is root:  # 要删除的节点右子树的第一个节点没左子树了，所以交换完还得把原来的右子树的第一个节点的右子树接到root上
            root.val, curr.val = curr.val, prev.val
            root.right = curr.right
        else:  # 正常情况，successor找到了，就先交换节点值，再把原来successor的右子树接到successor的parent的左边
            root.val, curr.val = curr.val, root.val
            prev.left = curr.right
        return root












