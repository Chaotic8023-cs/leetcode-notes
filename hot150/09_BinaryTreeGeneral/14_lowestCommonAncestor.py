# 236
from typing import *
from utils.pprintdp import pprintdp


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    # simple recursion!
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (p, q, None):  # 找到p或q后直接返回找到的p或q
            return root
        # left和right要么是找到的p或q，要么是在更深层递归返回的LCA
        # 如果其中一个是LCA的话，说明p和q都在这边的子树中已经找到，此时另一个一定是None
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:  # p和q分别在左右子树中，即当前的root就是LCA
            return root  # 这个最终答案会一直回溯到root，此时root的left或right其中一个就是这个最终答案，最后会被正确返回
        """
        如果只有在左或右子树找到了p或q，则继续往递归的上层传递找到的p或q
        这个同时解决了p和q在同一子树的情况：假设先找到的是p，q在p的下面，
        此时函数会直接返回p而不会继续往下递归，等回到root的时候，right(右子树)
        一定为None，因为q在左子树,此时最终返回的是第一个找到的p，符合LCA的定义！
        """
        return left or right


    # self try: 先dfs找p和q并一路记录parents，再在两个parents中找到第一个intersection，即LCA，相比简单递归过于复杂不用记!
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, p, q, parent):
            """
            一直记录node的parent，直到p和q的parent都记录上了(即p和q都在树中找到了)
            """
            if not root:
                return
            if p in parent and q in parent:
                return
            if root.left:
                parent[root.left] = root
            if root.right:
                parent[root.right] = root
            dfs(root.left, p, q, parent)
            dfs(root.right, p, q, parent)

        # 先dfs，找p和q并记录parents
        parent = {root: None}
        dfs(root, p, q, parent)
        # 分别把p和q的parents从树的下到上插入到array中
        parents_p = [p]
        parents_q = [q]
        par_p = parent[p]
        par_q = parent[q]
        while par_p:
            parents_p.append(par_p)
            par_p = parent[par_p]
        while par_q:
            parents_q.append(par_q)
            par_q = parent[par_q]
        # 因为LCA再往上parents都是相同的，所以我们用双指针从p和q的parents array结尾开始往前找，返回从相同变为不同的index上的那个node
        ip = len(parents_p) - 1
        iq = len(parents_q) - 1
        while parents_p[ip] == parents_q[iq] and ip >= 0 and iq >= 0:
            ip -= 1
            iq -= 1
        return parents_p[ip + 1]


if __name__ == '__main__':
    sol = Solution()
    q = TreeNode(4)
    p = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), q))
    root = TreeNode(3, p, TreeNode(1, TreeNode(0), TreeNode(8)))
    res = sol.lowestCommonAncestor(root, p, q)
    print(res)
