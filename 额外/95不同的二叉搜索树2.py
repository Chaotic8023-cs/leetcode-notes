from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
深搜递归：
generate(i, j)返回[i,j]能生成的所有二叉搜索树
跟96题只返回数量的思路一样，还是先枚举根节点，然后再看左右子树，具体的思路为：
    对于每个根节点（[i,j]），左右子树能生成的不同二叉搜索树能通过递归得到，然后我们把所有可能的左右子树组合放到当前跟节点下，就能生成当前
    根节点的所有可能的树。那么最后[i,j]能生成的所有树就是所有可能的根节点，从i到j，所能生成的所有树合起来。
"""
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # 返回[i, j]能生成的所有可能的二叉搜索树的一个list（左闭右闭！）
        def generate(i, j):
            if i > j:  # i > j时只有一种可能，即空树
                return [None]
            trees = []
            # 此时枚举不同的根节点，对于每个根节点它的左右子树的所有可能的情况可以递归获得，然后枚举所有可能的左右子树的组合（笛卡尔积），和当前根节点构成一个树，加入到ans中
            for root in range(i, j + 1):  # 根节点可能是[i,j]中的任何一个
                # 注意，generate的参数是左闭右闭，所以当根节点是root时，左边就是[i, root - 1]，右边就是[root + 1, j]
                l_trees = generate(i, root - 1)
                r_trees = generate(root + 1, j)
                for lt in l_trees:
                    for rt in r_trees:
                        trees.append(TreeNode(root, lt, rt))
            return trees

        return generate(1, n)







