# 105
from typing import *
from utils.pprintdp import pprintdp


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        改用index来操作两个list更efficient
        d是一个记录元素值在inorder list里的index的哈希表，用来快速在inorder里找到root的index
        i和j分别为preorder和inorder的起始index，n表示当前的树的节点个数
        一开始初始位置ij都是0，节点个数为preorder或inorder list的长度
        每次先拿出preorder的第一个作为root，然后通过d找到其在inorder中的index k
        那么left subtree的节点个数 = k-j，即root的index k减去inorder的初始位置j
        right subtree的节点个数为 = n-(k-j)-1 = n-k+j-1，即当前node总数减去左子树的节点数(k-j)再减去root的1个节点
        最后分别算出左子树和右子树的新的起始位置并带入左右子树的节点数，进行递归
        当n=0时，即为空，是base case，返回None即可
        """
        def dfs(i, j, n):
            if n == 0:
                return None
            v = preorder[i]  # root
            k = d[v]  # index of root in the inorder
            # recursively get left/right subtree
            l = dfs(i + 1, j, k - j)
            r = dfs(i + k - j + 1, k + 1, n - k + j - 1)
            return TreeNode(v, l, r)

        d = {v: i for i, v in enumerate(inorder)}
        return dfs(0, 0, len(preorder))

    # self try: list slicing, not efficient
    def buildTree1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        preorder总是node先，所以第一个一定是root，但是后面的左右子树各有多少不知道
        于是我么你可以看inorder，inorder总是先left再root最后right，
        所以我们可以先在inorder里找到root，然后它的左边就是所有左子树，右边就是所有右子树，
        然后就可以递归，用划分出来的左子树的preorder和inorder来构建当前root的左子树；右子树同理。
        当preorder和inorder都为空时，则证明到头了，return None即可
        """
        if not preorder:
            return None
        root_ele = preorder[0]
        tree = TreeNode(root_ele)
        lei = inorder[:inorder.index(root_ele)]  # left elements inorder
        rei = inorder[inorder.index(root_ele) + 1:]  # right elements inorder
        lep = preorder[1:1 + len(lei)]  # left elements preorder
        rep = preorder[1 + len(lei):]  # right elements preorder
        # recursively build left subtree and right subtree
        tree.left = self.buildTree(lep, lei)
        tree.right = self.buildTree(rep, rei)
        return tree


if __name__ == '__main__':
    sol = Solution()
    tree = sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(tree)
