from typing import *


"""
动态规划：
dp[i]表示偷[0,i]家所能获得的最大利润
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n  # 0-index
        dp[0] = nums[0]  # 只偷第一家那最大的利益就是直接偷
        dp[1] = max(nums[0], nums[1])  # 偷前两家：最大的利益就是偷前两家中价值大的那家
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])  # 偷：dp[i - 2] + nums[i]；不偷：dp[i - 1]
        return dp[n - 1]


"""
补充1：#213打家劫舍2：变成环形数组，即偷第一家就不能偷最后一家，偷最后一家就不能偷第一家。
解法：分情况讨论：1. 第一家偷最后一家不偷；2. 第一家不偷最后一家偷。两个dp数组分别求，最后取max。
"""
class Solution1:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:  # <=3家就最多只能偷一家
            return max(nums)
        # 第一家偷最后一家不偷（去掉最后一家）
        dp1 = [0] * (n - 1)
        dp1[0], dp1[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n - 1):
            dp1[i] = max(dp1[i - 2] + nums[i], dp1[i - 1])  # 去掉最后一家index不变
        # 第一家不偷最后一家偷（去掉第一家）
        dp2 = [0] * (n - 1)
        dp2[0], dp2[1] = nums[1], max(nums[1], nums[2])
        for i in range(2, n - 1):
            dp2[i] = max(dp2[i - 2] + nums[i + 1], dp2[i - 1])  # 去掉第一家dp[i]对应的就是nums[i + 1]，所以访问nums时下标+1
        return max(dp1[n - 2], dp2[n - 2])


"""
补充2：#337打家劫舍3：树形打家劫舍
普通打家劫舍需要访问i-2和i-1的下标，但tree中只能看到子节点，如何解决呢？
每个节点返回两个值：当前节点[偷，不偷]所能获得的最高金额。
这种题一看就是后序遍历，每个root从下面返回上来的值来决定怎么继续往上传：
    1. 偷当前节点：两个子节点只能不偷 -> l_notrob + r_notrob + root.val
    2. 不偷当前节点：两个子节点可以偷也可以不偷，我们取max -> max(l_rob, l_notrob) + max(r_rob, r_notrob)
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution2:
    def rob(self, root: Optional[TreeNode]) -> int:
        def traverse(root):
            if root is None:
                return 0, 0  # 当前节点[偷，不偷]所能获得的最大利润
            l_rob, l_notrob = traverse(root.left)
            r_rob, r_notrob = traverse(root.right)
            return l_notrob + r_notrob + root.val, max(l_rob, l_notrob) + max(r_rob, r_notrob)  # 偷， 不偷

        y, n = traverse(root)
        return max(y, n)  # 最后在根节点偷与不偷中取max








