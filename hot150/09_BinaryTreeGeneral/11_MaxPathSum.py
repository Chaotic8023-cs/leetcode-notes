# 124
from typing import *
from math import inf
from utils.pprintdp import pprintdp


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        按经典树的递归做：
        1. 终止条件（何时终止递归）
        2. 递归处理左右子树
        3. 合并左右子树的计算结果

        因为max sum可能是一条直的（从一个node到另一个node中间不穿过某个parent再下到它的child），
        也可能是弯的（穿过某个parent之后下到它的某个child）,我们在dfs外头记一个变量ans，在递归到每个node时我们比较这两种path的大小。
        因为node.val可能为负，所以我们对于左右子树的最大path sum和0取max，如果是0的话意味着此subtree中不选一个node。

        1. return root.val + max(left, right)
        ->  left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
        首先，dfs返回的是加上root的最大path sum，在回到上一层递归时，我们跟0比较，如果加上刚才的root(即当前node下面的)值大于0，则取这个
        path，如果小于0，我们直接不取，意味着当前node下面这个子树不在我们不选（意思是如果刚加上的这个root的值是负的且绝对值超过了已经积累
        的path sum，我们直接不要了，相当于把已经积累的path切断重置了）。这是greedy的思想（只要是正增长我们就选），
        这样我们就得到了left和right，即左子树和右子树的最大path sum。

        2. ans = max(ans, root.val + left + right)
        得到子树的最大path sum之后，我们更新ans，这行相当于在每个node把直的和弯的情况都考虑了：如过left和right的最大path sum都是大于0的，
        即他们对最终的max是正贡献，则加上root.val后相当于构成了弯的的情况。如果其中一个为0，则相当于直的情况，即一边的子树没选上。
        注意，dfs的return一直加上了root.val，保证了dfs返回的一定是当前子树的一个连贯的path。
        """

        def dfs(root):
            if not root:
                return 0
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            nonlocal ans
            ans = max(ans, root.val + left + right)
            return root.val + max(left, right)

        ans = -inf
        dfs(root)
        return ans


if __name__ == '__main__':
    sol = Solution()
